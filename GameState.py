import sys

import pygame

from EnemyWave import EnemyWave
from GameTime import GameTime
from Player import Player
from State import State
from TextManager import TextManager


class GameState(State):
    def __init__(self):
        super().__init__()

        self.game_objects = []

        self.running = True

        self.player = Player(800 / 2, 600 * 5 / 6, 800)
        self.enemy_wave = EnemyWave()

        self.game_objects.append(self.player)
        self.game_objects.append(self.enemy_wave)

        self.score_count = 0
        self.live_count = 3
        self.text_manager = TextManager()

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        for game_obj in self.game_objects:
            game_obj.update()

        for bullet in self.player.bullets:
            for enemy in self.enemy_wave.enemy_list:
                if bullet.rect.colliderect(enemy):
                    self.player.bullets.remove(bullet)
                    self.score_count += 10
                    self.text_manager.score_label.set_text(f'Score : {self.score_count}')
                    enemy.die()
                    bullet.kill()
                    break

        for bullet in self.enemy_wave.enemy_bullets:
            if bullet.rect.colliderect(self.player):
                self.live_count -= 1
                self.text_manager.live_label.set_text(f'Lives : {self.live_count}')
                self.enemy_wave.enemy_bullets.clear()
                self.player.die()

                if self.live_count == 0:
                    self.running = False
                break

    def draw(self):
        self.screen.fill((0, 0, 0))

        for game_obj in self.game_objects:
            game_obj.draw(self.screen)

        self.text_manager.draw(self.screen)
        
        if not self.running:
            self.text_manager.game_over_label.draw(self.screen)
