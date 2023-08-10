from typing import Any
import pygame
from pygame.sprite import Group

class Bullet(pygame.sprite.Sprite):

    #Creating a bullet in gun's position#
    def __init__(self, screen, gun):
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 2, 12)
        self.color = 237, 28, 35
        self.speed = 1
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    #Bullet movements to the top#
    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    #Drawing bullet on the screen#
    def show(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        