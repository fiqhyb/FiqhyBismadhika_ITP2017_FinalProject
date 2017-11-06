import pygame.font

class Button():
    def __init__(self, screen, msg,hsc):
        self.screen = screen
        self.screen_rect = screen.get_rect()#get rect of the display screen

        #set width, height, colours, and font
        self.width, self.height = 200,50
        self.button_colour = (255,0,0)
        self.text_colour = (255,255,255)
        self.font = pygame.font.SysFont(None,48)

        #set posotions and size of the rectangle
        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        #calls function
        self.prep_msg(msg)#play button
        self.prep_hsc(hsc)#high score

    def prep_msg(self,msg):
        #create the rectangle and text for the play button
        self.msg_image = self.font.render(msg,True,self.text_colour,self.button_colour)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def prep_hsc(self,hsc):
        #create the rectangle and text for the high score
        self.hsc_image = self.font.render(hsc,True,self.text_colour,self.button_colour)
        self.hsc_image_rect = self.hsc_image.get_rect()
        self.hsc_image_rect.top = self.msg_image_rect.bottom + 20 #give distance from the play button
        self.hsc_image_rect.centerx = self.rect.centerx

    def draw_button(self):
        #displays the play button and high score rectangle
        self.screen.fill(self.button_colour,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)
        self.screen.blit(self.hsc_image,self.hsc_image_rect)