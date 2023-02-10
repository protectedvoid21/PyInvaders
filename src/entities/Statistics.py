import pygame

from src.utils.Text import Text


class Statistics:
    def __init__(self):
        self.lives = 3
        self.score = 0
        self.level = 1

        self.score_label = Text(f'Score : {self.score}', 30, (10, 10), 'white')
        self.live_label = Text(f'Lives : {self.lives}', 30, (620, 10), 'white')
        self.level_label = Text(f'Level : {self.level}', 30, (320, 10), 'white')
        
    def add_score(self, amount):
        self.score += amount
        self.score_label = Text(f'Score : {self.score}', 30, (10, 10), 'white')
        
    def remove_life(self):
        self.lives -= 1
        self.live_label = Text(f'Lives : {self.lives}', 30, (620, 10), 'white')
    
    def next_level(self):
        self.level += 1
        self.level_label = Text(f'Level : {self.level}', 30, (320, 10), 'white')

    def draw(self, surface):
        self.score_label.draw(surface)
        self.live_label.draw(surface)
        self.level_label.draw(surface)