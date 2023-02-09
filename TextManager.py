import pygame.font

from Text import Text


class TextManager:
    def __init__(self):
        pygame.font.init()
        
        self.score_label = Text('Score : 0', 30, 10, 10)
        self.live_label = Text('Lives : 3', 30, 620, 10)
        
    def draw(self, surface):
        self.score_label.draw(surface)
        self.live_label.draw(surface)
        