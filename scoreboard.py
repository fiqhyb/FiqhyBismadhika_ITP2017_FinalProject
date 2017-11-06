import pygame.font

class Scoreboard():
    def __init__(self,ai_settings,screen,stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        #get value from settings module
        self.text_colour = ai_settings.text_colour
        self.font = pygame.font.SysFont(None,48)
        #calls prep_score function
        self.prep_score()

    def prep_score(self):
        #to round the score which the player earn during the game
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        #create the score image
        self.score_image = self.font.render(score_str,True,self.text_colour,self.ai_settings.bg_colour)
        #get the rectangle of image score and set the positions
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right
        self.screen_rect.top = self.screen_rect.top

    #displays the score rectangle
    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)