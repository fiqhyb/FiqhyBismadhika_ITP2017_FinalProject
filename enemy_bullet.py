import pygame
from pygame.sprite import Sprite

class Fire(Sprite):
    # initialize the fireball and make it a sprite
    def __init__(self,ai_settings,screen,enemy):
        super(Fire,self).__init__()
        self.screen = screen

        # load images and get the image rect
        self.image = pygame.image.load("fireball.png").convert_alpha()
        self.rect  = self.image.get_rect()
        # get the enemy's rect and added by addition of x and y from settings to positions where the fireball comes out
        self.rect.y = enemy.rect.y + ai_settings.ebullet_ypos
        self.rect.x = enemy.rect.x + ai_settings.ebullet_xpos

        self.x = float(self.rect.x)#converts the x position into float number to move the bullet
        # get the attributes from settings module
        self.speed = ai_settings.ebullet_speed

    def update(self):
        self.x -= self.speed
        #updates the value of the rectangle while moving
        self.rect.x = self.x

    # make the object appear on screen
    def draw_ebullet(self):
        self.screen.blit(self.image, self.rect)