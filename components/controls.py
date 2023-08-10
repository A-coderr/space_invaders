import pygame
import sys
from components.bullet import Bullet

#Events handling#
def events(screen, gun, bullets):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            
            elif event.type == pygame.KEYDOWN:
                 #Left#
                 if event.key == pygame.K_a:
                      gun.move_left = True
                 #Right#
                 elif event.key == pygame.K_d:
                      gun.move_right = True
                 #Bullet#
                 elif event.key == pygame.K_SPACE:
                      new_bullet = Bullet(screen, gun)
                      bullets.add(new_bullet)
              
            elif event.type == pygame.KEYUP:
                 #Left#
                 if event.key == pygame.K_a:
                      gun.move_left = False
                 #Right#
                 elif event.key == pygame.K_d:
                      gun.move_right = False

#Screen refresh#
def update(bg_color, screen, gun, bullets):
        screen.fill(bg_color)
        for bullet in bullets.sprites():
             bullet.show()
        gun.show()
        pygame.display.flip()

#Updates bullet position#
def update_bullets(bullets):
        bullets.update()
        for bullet in bullets.copy():
              if bullet.rect.bottom <= 0:
                    bullets.remove(bullet)

        print(len(bullets))

                 