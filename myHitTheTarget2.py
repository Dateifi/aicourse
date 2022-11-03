import math
import pygame as pg


try:
    print('Searching for class Kalman in file Kalman.py...')
    from Kalman import Kalman
    kalman_implemented = True
except ModuleNotFoundError:
    kalman_implemented = False
    print('No implementation of class Kalman found, running simulation without it.')

import random
import numpy as np


class Target():
    def __init__(self, y_t):
        self.y_t = y_t
        self.vx_t = 0.4 + 0.6*random.random()
        self.ax_t = 0.003*random.random()

        target_left = 200*random.random()  # Randomized starting position
        target_top = 50
        self.rect = pg.Rect(target_left, target_top, 16, 16)

        # Initialize position, speed and acceleration
        self.x_t = self.rect.centerx
        self.y_t = self.rect.centery


    def move(self):
        self.vx_t += self.ax_t
        self.x_t += self.vx_t
        self.rect.centerx = int(self.x_t)

    def noisy_x_pos(self, noise_scale=150):
        return self.rect.x + np.random.normal(0,noise_scale)

class Player():
    def __init__(self, y_t, kalman = None):
        self.rect = pg.Rect(800, 700, 16, 16)
        self.x_p = self.rect.centerx
        self.y_p = self.rect.centery
        self.vx_p = 0
        self.vy_p = -1.0
        self.ax_p = 0.02
        self.vx_p_desired = 0
        self.kalm = kalman

        self.x_t = self.x_p
        self.vx_t = 0
        self.y_t = y_t
        self.t_impact = (self.y_t - self.y_p) / self.vy_p

    def move(self, x_target_meas):
        if self.kalm:
            self.x_t, self.vx_t = self.kalm.estimate_current_position_and_velocity(x_target_meas)
        else:
            self.vx_t = x_target_meas - self.x_t
            self.x_t = x_target_meas

        self.t_impact = (self.y_t - self.y_p) / self.vy_p

        if self.t_impact:
            self.vx_p_desired = (self.x_t - self.x_p) / self.t_impact + self.vx_t

        if self.vx_p < self.vx_p_desired:
            self.vx_p += self.ax_p
        else:
            self.vx_p -= self.ax_p

        self.x_p += self.vx_p
        self.y_p += self.vy_p

        self.rect.centerx = int(self.x_p)
        self.rect.centery = int(self.y_p)

pg.init()
kalman_score = 0
reg_score = 0
iters = 0
y_t = 66

while True:
    target = Target(y_t)
    missile = Player(y_t)
    if kalman_implemented:
        k_miss = Player(y_t, kalman=Kalman())
    trial = True
    iters += 1
    coll = 0
    k_coll = 0

    while trial:

        # Get latest (noisy) target position
        last_x_pos = target.noisy_x_pos()

        # Move target and missile(s)
        target.move()
        missile.move(last_x_pos)
        if kalman_implemented:
            k_miss.move(last_x_pos)

        coll = missile.rect.colliderect(target.rect)
        if coll: reg_score += 1

        if kalman_implemented:
            k_coll = k_miss.rect.colliderect(target.rect)  # kommenter inn denne linjen naar Kalman er implementert#
            if k_coll: kalman_score += 1

        # End trial if missile(s) hit, or missile is sufficiently high up
        oob = missile.rect.y < 20
        if oob or (kalman_implemented and k_coll):
            trial = False


    if iters % 100 == 0:
    # Print hit rates
        print('Hit rate after ' + str(iters) + ' iterations:')
        print('Without filter: ' + str(round((reg_score / iters) * 100, 1)) + ' %')
        if kalman_implemented:
            print('With filter:    ' + str(round((kalman_score / iters) * 100, 1)) + ' %')