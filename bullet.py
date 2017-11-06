import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    # initialize the bullet and make it a sprite
    def __init__(self,ai_settings,screen,chara):
        super(Bullet,self).__init__()
        self.screen = screen

        # create a rectangle as a bullet and get it's rectangle
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        # get the chara's rect to positions where the bullet comes out
        self.rect.centery = chara.rect.centery
        self.rect.right   = chara.rect.right

        self.x = float(self.rect.x)#converts the x position into float number to move the bullet
        #get the attributes from settings module
        self.colour = ai_settings.bullet_colour
        self.speed  = ai_settings.bullet_speed

    def update(self):
        self.x += self.speed
        #updates the value of the rectangle while moving
        self.rect.x = self.x

    # make the object appear on screen
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.colour, self.rect)