import sys
import pygame
from bullet import Bullet
from enemy_bullet import Fire
from tornado import Tornado

########################################################
#___function of sprites to be called in check events___#
########################################################
def wind(settings,screen,tornados):
    #check the range of tornados in Group
    if len(tornados) < settings.tornado_allowed:
        new_tor = Tornado(settings,screen)#create an instance of tornado
        tornados.add(new_tor)#add the instance to the Group and to the game
        #load and play sound if tornado is added to the Group
        st = pygame.mixer.Sound("wind.wav")
        st.play()

def fireball(settings,screen,enemy,ebullets):
    new_fire = Fire(settings,screen,enemy)#create an instance of fireball
    ebullets.add(new_fire)#add the instance to the Group and to the game
    # load and play sound if fireball is added to the Group
    sf = pygame.mixer.Sound("fireball.wav")
    sf.play()

def fire_bullet(settings, screen, chara, bullets):
    new_bullet = Bullet(settings, screen, chara)#create an instance of bullet
    bullets.add(new_bullet)#add the instance to the Group and to the game
    # load and play sound if bullet is added to the Group
    so = pygame.mixer.Sound("pop.wav")
    so.play()

############################################
#___function of keyup and keydown events___#
############################################
def check_keydown_events(event, settings,screen, chara,bullets):
    # when the spacebar is pressed, calls the function of fire_bullet
    if event.key == pygame.K_SPACE:
        fire_bullet(settings,screen,chara,bullets)
    #change booleans in chara module if a certain key is pressed
    if event.key == pygame.K_d:
        chara.moving_right = True
    elif event.key == pygame.K_a:
        chara.moving_left = True
    elif event.key == pygame.K_w:
        chara.moving_up = True
    elif event.key == pygame.K_s:
        chara.moving_down = True

def check_keyup_events(event, chara):
    # change booleans in chara module if a certain key is released
    if event.key == pygame.K_d:
        chara.moving_right = False
    elif event.key == pygame.K_a:
        chara.moving_left = False
    elif event.key == pygame.K_w:
        chara.moving_up = False
    elif event.key == pygame.K_s:
        chara.moving_down = False

#######################################################
#___function of check events and check play buttons___#
#######################################################
def check_events(settings, screen,stat, chara, bullets,enemy,ebullets,tornados,play_button):
    #if fire is True calls the function fireball and wind
    if enemy.fire:
        fireball(settings, screen, enemy, ebullets)
        wind(settings,screen,tornados)
    for event in pygame.event.get():#loop to access events detected by pygame
        #to enable system quit and close the program
        if event.type == pygame.QUIT:
            sys.exit()
        #calls the check play button function if mouse is clicked
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()#get the mouse x and y coordinate
            check_play_button(stat, play_button, mouse_x, mouse_y, bullets, ebullets, tornados,chara,enemy)
        #enable the keydown and keyup events only when the game is active
        if stat.game_active:
            if event.type == pygame.KEYDOWN:
                check_keydown_events(event,settings,screen,chara,bullets)
            elif event.type == pygame.KEYUP:
                check_keyup_events(event,chara)

def play_button(stat,play_button):
    #automatically draw the play button if game is not active
    if not stat.game_active:
        play_button.draw_button()

def check_play_button(stat,play_button,mouse_x,mouse_y,bullets,ebullets,tornados,chara,enemy):
    #sets the collidepoint between play button's rect and mouse click position
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and stat.game_active == False:
        pygame.mouse.set_visible(False)#make the cursor invisible
        stat.reset_stats()#calls the reset_stats function in game stat module
        stat.game_active = True#makes the game active
        #empty Group from instances
        bullets.empty()
        ebullets.empty()
        tornados.empty()

        chara.center_chara()#reposition character to the center of the screen
        enemy.replace()#replace postion of the enemy to the designated value in enemy module

#####################################################
#___needed functions to update the module in game___#
#####################################################
def check_col(chara,enemy):
    #check collisions between the player and the enemy
    collision = pygame.sprite.collide_rect(chara, enemy)
    if chara.collision_immune == False and collision:
        pygame.mixer.Sound("glass.ogg").play()#play sounds
        chara.collision_immune = True#sets the player invincible after collision
        chara.lives_left -= 1#removes one life if collided

def update_tornados(chara,tornados):
    thit = pygame.sprite.spritecollide(chara, tornados, False)
    if chara.collision_immune == False and thit:
        pygame.mixer.Sound("glass.ogg").play()
        chara.collision_immune = True
        chara.lives_left -= 1
    #remove instance if tornado goes outside the screen
    for tornado in tornados.copy():
        if tornado.rect.right < 0:
            tornados.remove(tornado)
    tornados.update()#calls update function

def update_ebullets(chara,ebullets):
    ehit = pygame.sprite.spritecollide(chara, ebullets, False)
    if chara.collision_immune == False and ehit:
        pygame.mixer.Sound("glass.ogg").play()
        chara.collision_immune = True
        chara.lives_left -= 1
    for ebullet in ebullets.copy():
        if ebullet.rect.right < 0:
            ebullets.remove(ebullet)
    ebullets.update()

def update_bullets(chara,enemy,bullets,stats,ai_settings,sb):
    hit = pygame.sprite.spritecollide(enemy, bullets, True)
    for bullet in bullets.copy():
        if bullet.rect.left > chara.screen_rect.right:
            bullets.remove(bullet)
    bullets.update()
    #make the enemy blinks everytime it get shot by the payer
    if enemy.got_hit == False and hit:
        enemy.got_hit = True
        sb.prep_score()#calls the prep_score function in scoreboard module
        stats.score += ai_settings.hit_score#add score when shot
        ai_settings.scale_buildup += ai_settings.buildup_amount#add the buildup amount
        #check if the buildup is the same value as the initialized amount to scale up
        if ai_settings.scale_buildup == ai_settings.start_scale:
            ai_settings.scale_buildup = 0#reset the buildup to 0
            ai_settings.increase_difficulty()#calls the function and scale up the game

#calls the update function in chara and enemy module
def update_sprites(chara,enemies):
    chara.update()
    enemies.update()

#updates the screen and displays every sprites
def update_screen(chara,enemy,bullets,ebullets,tornados,sb):
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    for ebullet in ebullets.sprites():
        ebullet.draw_ebullet()
    for tornado in tornados.sprites():
        tornado.draw_tornado()
    enemy.blitme()
    chara.blitme()
    sb.show_score()