import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    def __init__(self, ai_settings, screen, posx, posy):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('resources/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = posx
        self.rect.y = posy

        self.x = float(self.rect.x)
        ai_settings.enermy_number += 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)#哭唧唧
