# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 14:38:53 2018

@author: Ghost
"""

import sys
import pygame
from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """ Response key """
    """ Change the movment sign according the key events"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # Creat a bullet and add it to the group bullets
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
        
        

def check_keyup_events(event, ship):
    """ Response keyup """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
        
        
        
def check_events(ai_settings,screen, ship, bullets):
    """ Respone key and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
                
            
def update_screen(ai_settings, screen, ship, bullets):
    """ update the image on the screen and switch to the new screen"""
    
    #   Redraw the screen at each cycle
    screen.fill(ai_settings.bg_color)
    
    for bullet in bullets.sprites():
        bullet.draw_bullet()
        
    #   Built the ship on the screen
    ship.blitme()
    
    # Let the recently painted screen be visible
    pygame.display.flip()
    
    
