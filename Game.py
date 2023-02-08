import sys

import pygame
import time

from EnemyWave import EnemyWave
from Player import Player


class Game:
    def __init__(self):
        self.game_objects = []

        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 600
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        self.clock = pygame.time.Clock()
        self.prev_time = time.time()
        self.delta_time = 0.0
        self.framerate = 120

        self.player = Player(self.SCREEN_WIDTH / 2, self.SCREEN_HEIGHT * 5 / 6, self.SCREEN_WIDTH)
        self.enemy_wave = EnemyWave()

        self.game_objects.append(self.player)
        self.game_objects.append(self.enemy_wave)

    def loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill((0, 0, 0))

            self.clock.tick(self.framerate)
            print(self.clock.get_fps())
            now = time.time()
            self.delta_time = now - self.prev_time
            self.prev_time = now

            for game_obj in self.game_objects:
                game_obj.update(self.delta_time)
                game_obj.draw(self.screen)

            pygame.display.update()
