class Kalman():
    def __init__(self):
        """ Initialize filter """
        self.t_d = 1
        self.pred_p = 0.0
        self.pred_v = 0.0
        self.pred_a = 0.0

        self.alpha = 0.02
        self.beta = 0.000_08
        self.gamma = 0.000_000_3

    def estimate_current_position_and_velocity(self, zn):
        """ Estimate current position and velocity from (noisy) position measurement """

        self.e_p = self.pred_p + self.alpha * (zn - self.pred_p)
        self.e_v = self.pred_v + self.beta * ((zn - self.pred_p) / self.t_d)
        self.e_a = self.pred_a + self.gamma * ((zn - self.pred_p) / ((self.t_d ** 2) * 0.5))

        self.pred_p = self.e_p + self.e_v * self.t_d + self.e_a * ((self.t_d ** 2) * 0.5)
        self.pred_v = self.e_v + self.e_a * self.t_d
        self.pred_a = self.e_a

        return self.e_p, self.e_v



