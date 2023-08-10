import pygame
import sys

#Events handling#
def events(gun):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            
            elif event.type == pygame.KEYDOWN:
                 #Left#
                 if event.key == pygame.K_a:
                      gun.move_left = True
                 #Right#
                 if event.key == pygame.K_d:
                      gun.move_right = True
            elif event.type == pygame.KEYUP:
                 #Left#
                 if event.key == pygame.K_a:
                      gun.move_left = False
                 #Right#
                 if event.key == pygame.K_d:
                      gun.move_right = False
                 