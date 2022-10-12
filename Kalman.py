import numpy as np

class Kalman():
    def __init__(self):
        self.kf_x_init = np.array([[108.0], [0.7], [0.0015]])
        self.kf_P_init = np.diag([22500.0, 1, 1])
        self.kf_F = np.array([[1.0, 1.0, 0.5], [0.0, 1.0, 1.0], [0.0, 0.0, 1.0]])
        self.kf_H = np.array([[1.0], [0.0], [0.0]]).T
        self.kf_R = np.array([[625]])
        self.kf_Q = 0
        self.kf_K_n = 0
        self.kf_x_n__n = 0
        self.kf_P_n__n = 0

        self.kf_x_n_plus1__n = np.dot(self.kf_F, self.kf_x_init)

        self.kf_P_n_plus1__n = np.dot(np.dot(self.kf_F, self.kf_P_init), self.kf_F.T) + self.kf_Q

    def estimate_current_position_and_velocity(self, zn):

        self.kf_K_n = np.dot(np.dot(self.kf_P_n_plus1__n, self.kf_H.T), np.linalg.inv(np.dot(np.dot(self.kf_H, self.kf_P_n_plus1__n), self.kf_H.T) + self.kf_R))

        self.kf_x_n__n = self.kf_x_n_plus1__n + np.dot(self.kf_K_n, zn - np.dot(self.kf_H, self.kf_x_n_plus1__n))

        self.kf_P_n__n = np.dot(np.dot(np.eye(3) - np.dot(self.kf_K_n, self.kf_H), self.kf_P_n_plus1__n),
                         (np.eye(3) - np.dot(self.kf_K_n, self.kf_H)).T) + np.dot(np.dot(self.kf_K_n, self.kf_R), self.kf_K_n.T)

        self.kf_x_n_plus1__n = np.dot(self.kf_F, self.kf_x_n__n)

        self.kf_P_n_plus1__n = np.dot(np.dot(self.kf_F, self.kf_P_n__n), self.kf_F.T) + self.kf_Q

        return self.kf_x_n__n[0], self.kf_x_n__n[1]



