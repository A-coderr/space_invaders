import pygame
import sys
from components.gun import Gun

def start():
    pygame.init()
    screen = pygame.display.set_mode((800, 900))
    pygame.display.set_caption("Space Invaders")
    bg_color = (0, 0, 0)
    gun = Gun(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(bg_color)
        gun.show()
        pygame.display.flip()

start()