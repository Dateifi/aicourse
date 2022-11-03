import numpy as np




class Kalman():
    def __init__(self):
        self.kf_x_init = np.array([[108.0], [0.7], [0.0015]])  # Initial state estimate   (x, v, a)
        self.kf_P_init = np.diag([3350.0, 0.03, 0.0000008])  # Initial covariance estimate
        self.kf_F = np.array([[1.0, 1.0, 0.5], [0.0, 1.0, 1.0], [0.0, 0.0, 1.0]])  # State transition matrix
        self.kf_H = np.array([[1.0], [0.0], [0.0]]).T  # Observation matrix
        self.kf_R = np.array([[22500]])  # Measurement covariance
        self.kf_Q = 0  # Process noise covariance
        self.kf_K_n = 0  # Kalman gain at time n declaration
        self.kf_x_n__n = 0  # State estimate at time n declaration
        self.kf_P_n__n = 0  # Covariance estimate at time n declaration



        self.kf_x_n_plus1__n = np.dot(self.kf_F, self.kf_x_init)  # State estimate at time n+1 declaration

        self.kf_P_n_plus1__n = np.dot(np.dot(self.kf_F, self.kf_P_init), self.kf_F.T) + self.kf_Q  # Covariance estimate
        # at time n+1 declaration


    def estimate_current_position_and_velocity(self, zn):


        # Kalman gain at time n:
        self.kf_K_n = np.dot(np.dot(self.kf_P_n_plus1__n, self.kf_H.T),
                             np.linalg.inv(np.dot(np.dot(self.kf_H, self.kf_P_n_plus1__n), self.kf_H.T) + self.kf_R))

        # State estimate at time n:
        self.kf_x_n__n = self.kf_x_n_plus1__n + np.dot(self.kf_K_n, zn - np.dot(self.kf_H, self.kf_x_n_plus1__n))

        self.kf_x_n__n[0] -= 0.42


        # Covariance estimate at time n:
        self.kf_P_n__n = np.dot(np.dot(np.eye(3) - np.dot(self.kf_K_n, self.kf_H), self.kf_P_n_plus1__n),
                                (np.eye(3) - np.dot(self.kf_K_n, self.kf_H)).T) + np.dot(np.dot(self.kf_K_n, self.kf_R),
                                                                                       self.kf_K_n.T)


        # State estimate at time n+1:
        self.kf_x_n_plus1__n = np.dot(self.kf_F, self.kf_x_n__n)

        # Covariance estimate at time n+1:
        self.kf_P_n_plus1__n = np.dot(np.dot(self.kf_F, self.kf_P_n__n), self.kf_F.T) + self.kf_Q

        return self.kf_x_n__n[0], self.kf_x_n__n[1]  # Return position and velocity estimates
