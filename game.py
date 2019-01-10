import sys
import tkinter
import tkinter.messagebox

import pygame
from Settings import Settings
from bullet import Bulleta
from ship import Ship
from pygame.sprite import Group
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings=Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()
    pygame.display.set_caption("打人啦");
    #game loop
    gf.init_alien(ai_settings,screen,aliens)
    while True:
        gf.check_events(ship)
        ship.update()
        if ship.fire:
            gf.fire_bullet(ai_settings, screen, ship, bullets)
            ship.fire = False
        bullets.update()
        gf.update_aliens(aliens)
        gf.update_bullets(bullets)
        gf.check_kill(bullets,aliens,ai_settings)
        gf.update_screen(ai_settings,screen,ship,bullets,aliens)
run_game()