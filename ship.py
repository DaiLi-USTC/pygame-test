import pygame
from bullet import Bullet
class Ship():
    def __init__(self,ai_settings,screen):
        self.screen = screen
        self.ai_settings = ai_settings
        self.image =pygame.image.load('resources/role.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False
        self.fire = False

    def update(self):
        if self.moving_right:
            if self.rect.centerx<self.ai_settings.screen_width:
                self.rect.centerx += 1
        if self.moving_left:
            if self.rect.centerx>0:
                self.rect.centerx -= 1
        if self.fire:
            #fire_bullet(ai_settings, screen, ship, bullets):
            #self.fire = False
            self.a=3

    def blitme(self):
        #build the ship in screen
        self.screen.blit(self.image, self.rect)

