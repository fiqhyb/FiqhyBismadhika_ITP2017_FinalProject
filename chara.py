import pygame

class Chara():
    #initialize the chara
    def __init__(self,ai_settings,screen):
        self.screen      = screen
        self.ai_settings = ai_settings

        #load images and get the image rect
        self.image  = pygame.image.load("chara.png").convert_alpha()#opaque image
        self.imaget = pygame.image.load("chartransparent.png").convert_alpha()#transparent image
        self.rect   = self.image.get_rect()
        # get the display screen's rect for positioning purpose
        self.screen_rect = self.screen.get_rect()

        #posotions the chara to the center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        #converts the chara x and y into float numbers to move the chara
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        #movement flags, are set to false initially
        self.moving_right = False
        self.moving_left  = False
        self.moving_up    = False
        self.moving_down  = False
        #controls the chara invincibility
        self.collision_immune = False
        self.chara_invincible = 0#the starting value to conrol the duration
        #get the lives limit from settings module and sets it as lives remaining
        self.lives_left = ai_settings.lives_limit

    #function to reposition the chara after restarting
    def center_chara(self):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def update(self):
        if self.collision_immune:#check chara's collsion
            self.chara_invincible += 1#attribute will be added by one value
            #if the chara invincible duration equals the setting's value of invincibility
            if self.chara_invincible == self.ai_settings.chara_invincibility:
                self.collision_immune = False#change to flag to False
                self.chara_invincible = 0#reset value to 0
        #make the chara moves to certain directions if several conditions are true
        #limits the chara movement inside the screen using the screen's and chara's rectangle
        #determines the movement speed by getting the value from the settings module
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.centery -= self.ai_settings.chara_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.chara_speed_factor
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.chara_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.centerx -= self.ai_settings.chara_speed_factor
        #updates the value of the rectangle while moving
        self.rect.center = (self.centerx,self.centery)

    #make the object appear on screen
    def blitme(self):
        #check conditions to load transparent image if immunity is true
        if self.collision_immune:
            self.screen.blit(self.imaget,self.rect)
        else:
            self.screen.blit(self.image, self.rect)