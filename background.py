import pygame
from pygame.sprite import Sprite

class Background(Sprite):
    def __init__(self,x,y,ai_settings,screen):
        Sprite.__init__(self)
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load("bg.jpeg").convert()#background image when game is active
        self.title = pygame.image.load("title.jpg").convert()#image for the title screen
        #get the image and screen rect
        self.rect  = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        #assigning rect as simple variables
        self.rect.left,self.rect.top = x,y
        #get speed from settings module
        self.speed = ai_settings.bg_speed

    def update(self):
        #if the image's right rect equals to screen's left rect it will set the left rect of image to the screen width
        if self.rect.right <= self.screen_rect.left:
            self.rect.left = self.ai_settings.screen_width
        #if not it will move towards the left
        else:
            self.rect.left -= self.speed
    #display the in game background function
    def blitme(self):
        self.screen.blit(self.image, self.rect)
    #display the title background function
    def blitme2(self):
        self.screen.blit(self.title,self.rect)