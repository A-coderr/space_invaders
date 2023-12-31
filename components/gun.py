import pygame

class Gun():
    #Initializing the gun#
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('./assets/gun.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.move_left = False
        self.move_right = False

    #Show the gun on the screen#
    def show(self):
        self.screen.blit(self.image, self.rect)

    #Gun refresh#
    def update_gun(self):
        if self.move_left and self.rect.left > 0:
            self.center -= 1.5

        if self.move_right and self.rect.right < self.screen_rect.right:
            self.center += 1.5
        
        self.rect.centerx = self.center