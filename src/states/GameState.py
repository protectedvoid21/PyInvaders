import sys

import pygame

from src.entities.BulletManager import BulletManager
from src.entities.EnemyWave import EnemyWave
from src.entities.Player import Player
from src.utils.Statistics import Statistics
import src.states.MenuState
from src.states.State import State
from src.utils.LevelManager import LevelManager
from src.utils.PauseMenu import PauseMenu
from src.utils.Text import Text


class GameState(State):
    def __init__(self):
        super().__init__()

        self.running = True
        
        self.level_manager = LevelManager()
        self.statistics = Statistics()
        
        self.bullet_manager = BulletManager()
        self.player = Player((800 / 2, 600 * 5 / 6), 800, self.bullet_manager.shoot)
        self.enemy_wave = EnemyWave(self.bullet_manager.shoot, self.level_manager)
        
        self.bullet_manager.inject(self)
        
        self.paused = False
        self.pause_menu = PauseMenu(self.resume, self.exit, (250, 150), (300, 400))
        
        self.game_over_label = Text('Game over!', 40, (270, 250), 'red')
        
        self.enemy_wave.spawn(1)

    def update(self):
        if self.enemy_wave.is_clear():
            self.statistics.next_level()
            self.enemy_wave.spawn(self.statistics.level)
        
        if self.paused:
            self.pause_menu.update()
            return
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.paused = True
                
        if not self.running:
            return

        self.player.update()
        self.enemy_wave.update()

        self.bullet_manager.update()
    
        
    def resume(self):
        self.paused = False
        
    def exit(self):
        self.state_manager.change_state(src.states.MenuState.MenuState())
                
    def game_over(self):
        self.running = False

    def draw(self):
        if self.paused:
            self.pause_menu.draw(self.screen)
            return
        
        self.screen.fill((0, 0, 0))

        self.player.draw(self.screen)
        self.enemy_wave.draw(self.screen)

        self.statistics.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        
        if not self.running:
            self.game_over_label.draw(self.screen)
