import sys

import pygame

from EnemyWave import EnemyWave
from GameTime import GameTime
from Player import Player


class Game:
    def __init__(self):
        self.game_objects = []

        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 600
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        self.game_time = GameTime(60)

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

            self.game_time.update()

            for game_obj in self.game_objects:
                game_obj.update()
                game_obj.draw(self.screen)
                
            for bullet in self.player.bullets:
                for enemy in self.enemy_wave.enemy_list:
                    if bullet.rect.colliderect(enemy):
                        self.player.bullets.remove(bullet)
                        enemy.start_dying()
                        bullet.kill()

            pygame.display.update()
