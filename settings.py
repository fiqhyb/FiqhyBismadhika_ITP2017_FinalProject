class Setting():
    def __init__(self):
        ######################################
        #___display and background setting___#
        ######################################
        self.screen_width  = 1300
        self.screen_height = 700
        self.bg_speed      = 2 #determines how fast the background is moving
        self.bg_colour     = 60,60,250 #sets the score rect colour
        self.text_colour   = 20,20,20 #sets the score text colour

        #################################
        #___chara and bullet settings___#
        #################################
        self.chara_invincibility = 1000#sets how long the chara goes invincible
        self.chara_speed_factor  = 1#chara moving speed
        self.lives_limit   = 3#amount of lives the chara has
        self.bullet_speed  = 2
        self.bullet_width  = 12
        self.bullet_height = 4
        self.bullet_colour = 250,230,0

        ######################
        #___enemy settings___#
        ######################
        self.enemy_speed_factor = 0.25#enemy's moving speed
        self.enemy_xpos         = 900#sets the enemy's x position
        self.blink_time         = 5#determines how long the enemy's blink after hit

        #####################################
        #___fireball and tornado settings___#
        #####################################
        self.ebullet_time = 500#sets the delay of the fireball
        self.ebullet_ypos = 90
        self.ebullet_xpos = 50
        self.tornado_allowed = 1#limit tornado in game
        self.tornado_ypos    = 450

        ########################
        #___scaling settings___#
        ########################
        self.speedup_scale = 1.1#amount of scaling to speed up several attributes
        self.hit_scale     = 1.5#scale to increase the hit score

        #loop if the buildup reached the needed amount to scale up
        self.scale_buildup  = 0#first amount if score is zero
        self.buildup_amount = 1
        self.start_scale    = 50#determines the needed amount for the build up

        #initialize attributes that needed to be changed throughout the game
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.tornado_speed   = 1
        self.ebullet_speed   = 2
        self.hit_score   = 10#amount of score earned when the player hits the enemy

    #function to scale up the game
    def increase_difficulty(self):
        self.ebullet_speed  *= self.speedup_scale
        self.tornado_speed  *= self.speedup_scale
        #change hit_score by multiplying hit_score and hit_scale
        self.hit_score = int(self.hit_score * self.hit_scale)