import pdb

import pygame


class Sounds:
    def __init__(self):
        self.bg_music = "core_files/sounds/background.mp3"
        self.shoot = "core_files/sounds/shoot.ogg"
        self.collision = "core_files/sounds/collision.ogg"
        self.fleet = "core_files/sounds/new_fleet.ogg"
        self.ship_hit = "core_files/sounds/ship_hit.ogg"
        self.game_over = "core_files/sounds/game_over.ogg"

    def play_bg_music(self):
        pygame.mixer.music.load(self.bg_music)
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(-1)

    def pause_bg_music(self):
        pygame.mixer.music.pause()

    def shoot_sound(self):
        s_shoot = pygame.mixer.Sound(self.shoot)
        s_shoot.play()

    def collision_sound(self):
        s_collision = pygame.mixer.Sound(self.collision)
        s_collision.play()

    def fleet_sound(self):
        s_fleet = pygame.mixer.Sound(self.fleet)
        s_fleet.play(maxtime=3000)

    def ship_hit_sound(self):
        s_ship_hit = pygame.mixer.Sound(self.ship_hit)
        s_ship_hit.play()

    def game_over_sound(self):
        s_game_over = pygame.mixer.Sound(self.game_over)
        s_game_over.play()