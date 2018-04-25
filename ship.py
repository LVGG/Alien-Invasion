# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 11:08:11 2018

@author: Ghost
"""

import pygame

class Ship():
    
    def __init__(self, ai_settings,screen):
        """init ship and set the start position"""
        self.screen = screen
        
        # load ship image and get the square
        self.image = pygame.image.load('image/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #put every ship on the center of the screen's bottom
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
  
        # Movment sign
        self.moving_right = False
        self.moving_left = False
        self.moving_speed = 1.5
        
    def blitme(self):
        """ draw the ship at pointed position"""
        self.screen.blit(self.image, self.rect)
        
    def update(self):
        """ Adjust the position of the ship according to the movement sign"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.moving_speed + 0.5
        elif self.moving_left and self.rect.left > self.screen_rect.left:
            self.rect.centerx -= self.moving_speed
            
            
        