import pygame.font

from src.utils.Text import Text


class TextManager:
    def __init__(self):
        pygame.font.init()

        self.score_label = Text('Score : 0', 30, (10, 10), 'white')
        self.live_label = Text('Lives : 3', 30, (620, 10), 'white')
        self.game_over_label = Text('Game over!', 50, (300, 300), 'white')

    def draw(self, surface):
        self.score_label.draw(surface)
        self.live_label.draw(surface)
