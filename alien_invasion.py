# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 10:25:52 2018

@author: Ghost
"""

import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    # init game and creat a screen objection
    pygame.init()
    
    ai_settings = Settings()
    screen = pygame.display.set_mode(
            (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # Creat a ship
    ship = Ship(ai_settings,screen)
    bullets = Group()
    
    #start the game main function
    while True:
        # Monitor the key events and mouse events
        gf.check_events(ai_settings, screen, ship, bullets)
        # Update the date(Position, action, etc)
        ship.update()
        bullets.update()
        # Delete bullets disappear
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        
        gf.update_screen(ai_settings,screen, ship,bullets)

        
"""" Run the game now!!!!!!!!!!!!!!!"""

run_game()