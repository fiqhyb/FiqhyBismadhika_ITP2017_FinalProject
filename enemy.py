import pygame

class Enemy():
    # initialize the enemy
    def __init__(self,ai_settings,screen):
        self.screen      = screen
        self.ai_settings = ai_settings

        # load images and get the image rect
        self.image  = pygame.image.load("drag_mor.png").convert_alpha()#normal image
        self.imaget = pygame.image.load("dragtransparent.png").convert_alpha()#blink image
        self.rect   = self.image.get_rect()
        # get the display screen's rect to change enemy movement direction
        self.screen_rect = self.screen.get_rect()

        self.x = ai_settings.enemy_xpos# get the x position from settings module
        self.y = float(self.rect.y)#convert y into float to move the enemy automatically

        #movement flags
        self.down = True
        self.up   = False
        #respond flags
        self.got_hit = False#controls the blinking when shot
        self.blink   = 0#the starting value to conrol the duration
        self.fire      = False#controls fireball shooting
        self.time_fire = 0#the starting value to conrol the duration

    # function to reposition the enemy after restarting
    def replace(self):
        self.y = float(self.rect.y)

    def update(self):
        # time_fire keeps adding itself by 1 until it reached the set value in settings module
        if self.time_fire >= 0:
            self.time_fire += 1
            if self.time_fire == self.ai_settings.ebullet_time:#change fire flag to True
                self.fire = True
            # immidiately set fire flag back to false and time_fire to 0 when the set value adds by 1
            if self.time_fire == self.ai_settings.ebullet_time+1:
                self.fire = False
                self.time_fire = 0
        #check got_hit flag
        if self.got_hit:
            self.blink += 1
            #add blink time by 1 value until it's equals to blink time in settings module
            if self.blink == self.ai_settings.blink_time:
                self.got_hit = False#set flag to False
                self.blink = 0#return to 0 value

        #checks the rectangle to changes the movement flag
        if self.rect.bottom == self.screen_rect.bottom:
            self.down = False
            self.up   = True
        if self.rect.top == self.screen_rect.top:
            self.down = True
            self.up   = False
        # changes direction evrytime the rectangle reaches top or bottom of the screen
        if self.down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.ai_settings.enemy_speed_factor
        if self.up and self.rect.top > 0:
            self.y -= self.ai_settings.enemy_speed_factor
        #updates the value of the rectangle while moving
        self.rect.x = self.x
        self.rect.y = self.y

    # make the object appear on screen
    def blitme(self):
        # check conditions to load blink image if got hit is true
        if self.got_hit:
            self.screen.blit(self.imaget,self.rect)
        else:
            self.screen.blit(self.image, self.rect)