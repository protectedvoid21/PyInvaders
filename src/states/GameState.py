import sys

import pygame

from src.entities.BulletManager import BulletManager
from src.entities.EnemyWave import EnemyWave
from src.entities.Player import Player
from src.entities.Statistics import Statistics
from src.states.State import State
from src.utils.Text import Text


class GameState(State):
    def __init__(self):
        super().__init__()

        self.game_objects = []

        self.running = True

        self.statistics = Statistics()
        
        self.bullet_manager = BulletManager()
        self.player = Player((800 / 2, 600 * 5 / 6), 800, self.bullet_manager.shoot)
        self.enemy_wave = EnemyWave(self.bullet_manager.shoot)
        
        self.bullet_manager.inject(self)

        self.game_objects.append(self.player)
        self.game_objects.append(self.enemy_wave)
        
        self.game_over_label = Text('Game over!', 40, (270, 250), 'red')

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        if not self.running:
            return

        for game_obj in self.game_objects:
            game_obj.update()

        self.bullet_manager.update()
                
    def game_over(self):
        self.running = False
        print('game over')

    def draw(self):
        self.screen.fill((0, 0, 0))

        for game_obj in self.game_objects:
            game_obj.draw(self.screen)

        self.statistics.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        
        if not self.running:
            self.game_over_label.draw(self.screen)
