class GameStats():
    def __init__(self,ai_settings):
        self.ai_settings = ai_settings

        self.reset_stats()#calls reset_stat function
        self.game_active = False#game is set initially to be inactive

        self.score = 0#initial score during the game

    def reset_stats(self):
        #set the remaing lives in chara into the lives limit in settings module
        self.lives_left = self.ai_settings.lives_limit