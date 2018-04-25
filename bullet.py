# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 16:18:32 2018

@author: Ghost
"""

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ A class that manages the bullet of a alien ship"""
    
    def __init__(self, ai_settings, screen, ship):
        """Create a bullet object in the position of the ship"""
        super(Bullet, self).__init__()
        self.screen = screen
        
        # Creat a rect of bullet at (0,0), then set the correct positon
        self.rect = pygame.Rect(0,0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        # To store the bullet position represented by a decimal.
        self.y = float(self.rect.y)
        
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed
        
        
    def update(self):
        """ Move up bullets"""
        # update the decimal represented bullet's position
        self.y -= self.speed_factor
        
        # update the rect's position represented bullet
        self.rect.y = self.y
        
    def draw_bullet(self):
        """ Draw the bullet on screen """
        pygame.draw.rect(self.screen, self.color, self.rect)