
###########################
#         IMPORTS         #
###########################

# Try importing Kalman filter
try: 
    print('Searching for class Kalman in file Kalman.py...')
    from Kalman import Kalman
    kalman_implemented = True
except ModuleNotFoundError:
    kalman_implemented = False
    print('No implementation of class Kalman found, running simulation without it.')
    
# Imports
import pygame as pg
from random import random
import numpy as np


###########################
#    CLASS DEFINITIONS    #
###########################

class Projectile():

    def __init__(self, 
                 background,           # Display surface
                 y_target,             # y coordinate of target (known)
                 proj_left=800,        # Initial left edge of projectile rectangle
                 proj_top=700,         # Initial top edge of projectile rectangle
                 proj_width=16,        # Projectile width in pixels
                 proj_height=16,       # Projectile height in pixels
                 vy = -1.0,            # Vertical velocity (constant)
                 ax = 0.02,            # Absolute value of acceleration in pix/it^2
                 kalman = None):       # Kalman filter
        
        # Set background and create projectile rectangle
        self.background = background
        self.rect = pg.Rect(proj_left,proj_top,proj_width,proj_height)
        
        # Set position, velocity, acceleration and time variables
        self.x_p = self.rect.centerx
        self.y_p = self.rect.centery
        self.vy_p = vy            
        self.vx_p = 0.0           # Initial x velocity of projectile is zero
        self.vx_p_desired = 0.0   # Initial desired projectile x velocity is zero
        self.ax_p = ax            # Projectile acceleration
        
        self.x_t = self.x_p       # Start assuming that target has same x coordinate as projectile
        self.y_t = y_target       # Set target y coordinate (known)
        self.vx_t = 0             # Start assuming that target has zero x velocity. 
        self.t_impact = (self.y_t - self.y_p)/self.vy_p  # Time (#iterations) to impact 
        
        self.kalm = kalman        # Kalman filter, if implemented

        
    def move(self,x_target_meas):
        """ 
        "Desired" x velocity for projectile is calculated using following logic:
        We assume that estimates for target postition and velocity are available (x_t and vx_t)
        We want to achieve x_p = x_t at t_impact, and use equation x = x0 + v*t on both sides.
        
            x_p + vx_p*t_impact = x_t + vx_t*t_impact
            vx_p = (x_t - x_p) / t_impact + vx_t
        
        """
        # Get new estimate of target's current position and speed
        if self.kalm:
            self.x_t,self.vx_t = self.kalm.estimate_current_position_and_velocity(x_target_meas)
        else:
            self.vx_t = x_target_meas - self.x_t  # v = dx / dt, dt = 1
            self.x_t = x_target_meas              
        
        # Update t_impact
        self.t_impact = (self.y_t - self.y_p) / self.vy_p
        
        # Update desired x velocity
        if self.t_impact:
            self.vx_p_desired = (self.x_t - self.x_p) / self.t_impact + self.vx_t
                    
        # Change x velocity (constant acceleration, positive or negative)
        if self.vx_p < self.vx_p_desired:
            self.vx_p += self.ax_p
        else:
            self.vx_p -= self.ax_p

        # Move in both directions
        self.x_p += self.vx_p
        self.y_p += self.vy_p  # Move with constant speed in y direction
        
        # Update rectangle position
        self.rect.centerx = int(self.x_p)
        self.rect.centery = int(self.y_p)
                

class Target():

    def __init__(self, 
                 background,                   # Display surface
                 y_target_bottom,              # y coordinate for bottom of target
                 target_left_margin = 200,     # Margin within which target starts
                 target_width = 16,            # 
                 target_height = 16,           #
                 vx_mean = 0.4,                # Mean x velocity of target 
                 dvx = 0.6,                    # Range of possible x velocities
                 dax = 0.003):                 # Range of possible x accelerations
        
        # Create target rectangle
        self.background = background
        target_left = target_left_margin*random()            # Randomized starting position        
        target_top = y_target_bottom - target_height
        self.rect = pg.Rect(target_left, target_top, target_width, target_height)
        
        # Initialize position, speed and acceleration
        self.x = self.rect.centerx
        self.y = self.rect.centery
        self.vx = vx_mean + dvx*random()    # Random initial velocity
        self.ax = dax*random()              # Random acceleration
        
    def move(self):
        self.vx += self.ax        # Update velocity
        self.x += self.vx         # Update position
        self.rect.centerx = int(self.x)

    def noisy_x_pos(self, noise_scale=150):
        return self.rect.x + np.random.normal(0,noise_scale)


#############################
#    GAME SETUP AND LOOP    #
#############################    

# Parameters
background_width = 1600
background_height = 800
y_target_bottom = 66

max_fps = 300

# Set up game loop
pg.init()                                                                 # Initialize pygame modules
background = pg.display.set_mode((background_width,background_height))    # Initialize display surface
surf = pg.surfarray.pixels3d(background)                                  # Create array that references pixels in surface    
clock = pg.time.Clock()                                                   # Create clock for regulating fps

# Initialize counters
kalman_score = 0
reg_score = 0
iters = 0

# Main game loop
while True:
    target = Target(background, y_target_bottom)
    missile = Projectile(background,y_target_bottom)
    if kalman_implemented:
        k_miss = Projectile(background,y_target_bottom,kalman=Kalman()) 

    # Initialize array indicating position
    noisy_draw = np.zeros((background_width,20))

    # Set trial loop flag and increment # of trials
    trial = True
    iters += 1

    while trial:
        # Regulate fps, program will never run at more than 300 frames per second
        clock.tick(max_fps)    
        
        # Check if program should quit
        for e in pg.event.get():
            if e.type == pg.QUIT:
                pg.quit()
                exit()
        
        # Set background and noisy position "strip"
        background.fill(0x448844)
        surf[:,0:20,0] = noisy_draw

        # Get latest (noisy) target position
        last_x_pos = target.noisy_x_pos()

        # Move target and missile(s)
        target.move()
        missile.move(last_x_pos)
        if kalman_implemented:
            k_miss.move(last_x_pos) 

        # Draw target and missile(s)
        pg.draw.rect(background, (255, 200, 255), target.rect)
        pg.draw.rect(background, (255, 200, 0), missile.rect)
        if kalman_implemented:
            pg.draw.rect(background, (0, 200, 255), k_miss.rect) 

        # Update noisy position strip
        if last_x_pos >= 0:                                           # Ignore negative positions
            noisy_draw[int(last_x_pos):int(last_x_pos)+20,:] = 255    # Set last position as brightest
        noisy_draw -= 5                                               # Fade all positions
        np.clip(noisy_draw, 0, 255, noisy_draw)                       # Keep values within range [0,255]

        # Check if missile(s) hit
        coll = missile.rect.colliderect(target.rect)
        if coll: reg_score += 1
            
        if kalman_implemented:
            k_coll = k_miss.rect.colliderect(target.rect) #kommenter inn denne linjen naar Kalman er implementert#
            if k_coll: kalman_score += 1

        # End trial if missile(s) hit, or missile is sufficiently high up
        oob = missile.rect.y < 20
        if oob or coll or (kalman_implemented and k_coll): 
            trial = False

        # Update the display surface to the screen
        pg.display.flip()
    
    # Print hit rates
    print('Hit rate after ' + str(iters) + ' iterations:')
    print('Without filter: '  + str(round((reg_score/iters)*100,1)) + ' %')
    if kalman_implemented:
        print('With filter:    ' + str(round((kalman_score/iters)*100,1)) + ' %')
    