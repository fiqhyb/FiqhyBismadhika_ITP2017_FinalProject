import pygame
from  chara import Chara
from settings import Setting
import game_functions as gf
from pygame.sprite import Group
from pbutton import Button
from enemy import Enemy
from background import Background
from game_stat import GameStats
from scoreboard import Scoreboard

score = 0#variable is used to store the highest score
###################################
#___function to run the program___#
###################################
def run_game():
    global score#enable the "score" variable to be called from inside the function
    pygame.init()#initialize pygame module as the run_game function is started
    settings    = Setting()#import settings and make an instance of setting
    #import the screen width and height from settings module
    screen      = pygame. display.set_mode((settings.screen_width,settings.screen_height))

    #make an empty group to hold all sprites in game
    bullets     = Group()
    ebullets    = Group()
    tornados    = Group()

    #####################################################################
    #__import each modules and make an instance of each related module__#
    #####################################################################
    stats   = GameStats(settings)
    chara   = Chara(settings,screen)
    enemy   = Enemy(settings,screen)
    #first background's x and y position is set 0, thus appear before the second background
    bg1 = Background(0,0,settings,screen)
    #second background's x position is set next to the first background
    bg2 = Background(1300,0,settings,screen)
    bgt = Background(0,0,settings,screen)#instance of the title screen background
    sb  = Scoreboard(settings,screen,stats)#instance of the scoreboard
    #make an instance of the play button, the "PLAY" string is used for the button to be clicked
    #while the "High score" is used to display the high score and calls the global variable of "score"
    play_button = Button(screen, "PLAY", "High Score : " + str(score))#instance of the play button

    ########################################
    #___caption,music file, and booleans___#
    ########################################
    pygame.display.set_caption("Cuphead")#set the programs caption while running
    pygame.mixer.music.load("panic.mp3")#load the music in mp3 format
    pygame.mixer.music.set_volume(0.5)#sets the music volume
    music = 0#acts as the boolean of the music player
    title = 1#sets boolean of the title screen

    ##########################################################
    #____function to display the title screen of the game____#
    ##########################################################
    def main_menu():
        #the title screen is dispalyed right after running the game and when the game is not active
        if title == 1 and stats.game_active == False:
            bgt.blitme2()#displays the background title image
        #check list of events in the game function and perform tasks depending on the type of event which occured
        gf.check_events(settings,screen,stats,chara,bullets,enemy,ebullets,tornados,play_button)
        gf.play_button(stats,play_button)#displays the play button if the game is not active yet

    ##############################################################################
    #___contains event loop and code which manages the game and performs tasks___#
    ##############################################################################
    while True:
        main_menu()#calls the main_menu function

        #performs condition checking after the play button is pressed
        if stats.game_active:
            title = 0#disable the title screen
            if music == 0:
                pygame.mixer.music.play()#plays the music
                music = 1#change music from 0 to 1 to plays the music after the game is set to active

            #displays the first and second background on screen
            screen.blit(bg1.image,bg1.rect)
            screen.blit(bg2.image,bg2.rect)

            gf.check_col(chara, enemy)  # check the collision of chara and enemy

            #updates every module that needed to keep being updated while the game is running
            gf.update_sprites(chara,enemy)
            gf.update_bullets(chara,enemy,bullets,stats,settings,sb)
            gf.update_ebullets(chara,ebullets)
            gf.update_tornados(chara,tornados)
            gf.update_screen(chara,enemy,bullets,ebullets,tornados,sb)

            #update background to move
            bg1.update()#update the first background
            bg2.update()#update the scond background

            ################################################
            #_____conditions while the game is running_____#
            ################### #############################
            #set new high score if the last game score is higher than the current high score
            if stats.score > score and chara.lives_left == 0:
                # rounds up the new high score to the nearest ten and separate it with a comma
                score = "{:,}".format(int(round(stats.score, -1)))

            #to restart the game everytime the player runs out of lives
            if chara.lives_left == 0:
                pygame.mouse.set_visible(True)#set the mouse cursor to be visible
                run_game()#restart the game

        pygame.display.flip()#make the most recently drawn screen be visible

run_game()#calls the run_game function and starts the program