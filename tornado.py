import pygame
from pygame.sprite import Sprite
from random import randint

class Tornado(Sprite):
    # initialize the tornado and make it a sprite
    def __init__(self,ai_settings,screen):
        super(Tornado,self).__init__()
        self.screen = screen

        # load images and get the image rect
        self.image = pygame.image.load("tornado.png").convert_alpha()
        self.rect  = self.image.get_rect()
        # get the x from random integer outside the screen and y from the settings module
        self.rect.x = randint (1300,2000)
        self.rect.y = ai_settings.tornado_ypos

        self.x = float(self.rect.x)#converts the x position into float number to move the bullet
        # get the attributes from settings module
        self.speed = ai_settings.tornado_speed

    def update(self):
        self.x -= self.speed
        #updates the value of the rectangle while moving
        self.rect.x = self.x

    # make the object appear on screen
    def draw_tornado(self):
        self.screen.blit(self.image, self.rect)