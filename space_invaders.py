import pygame
import components.controls
from components.gun import Gun
from pygame.sprite import Group

def start():
    pygame.init()
    screen = pygame.display.set_mode((800, 900))
    pygame.display.set_caption("Space Invaders")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()

    while True:
        components.controls.events(screen, gun, bullets)
        gun.update_gun()
        components.controls.update(bg_color, screen, gun, bullets)
        components.controls.update_bullets(bullets)


start()