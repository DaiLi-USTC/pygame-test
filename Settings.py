class Settings(object):

    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (0,0,0)
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 1.5
        self.ebullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_height = 7
        self.bullets_max_number = 5
        self.bullet_color = (255,0,0)
        self.ebullet_color = (0, 255,0)
        self.state_height=48
        self.level = 1
        self.alien_row = 5
        self.alien_line = 3
        self.ebullets_max_number = self.alien_line
        self.alien_speed_factor = 1.0
        self.life = 3

        self.score = 0
        self.enermy_number = 0