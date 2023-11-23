import pygame


class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.bg_image = pygame.image.load('core_files/images/background_image.jpg')

        self.ship_speed = 1.5
        self.ship_limit = 3
        self.ship_image = pygame.image.load('core_files/images/ship.bmp')

        self.bullet_speed = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 255, 255)
        self.bullets_allowed = 3

        self.alien_speed = 0.5
        self.fleet_drop_speed = 5
        self.fleet_direction = 1
        self.alien_image = pygame.image.load('core_files/images/alien.bmp')

        self.speedup_scale = 1.5
        self.score_scale = 1.5
        self.initialize_dynamic_settings()
        filepath = 'game_files/'
        self.filename = f"{filepath}high_score.txt"

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 0.5
        self.alien_points = 50

        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
