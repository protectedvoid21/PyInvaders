import pygame


class Text:
    def __init__(self, text, size, x_pos, y_pos):
        self.font = pygame.font.Font('Retro Gaming.ttf', size)
        self.img = self.font.render(text, True, (255, 255, 255))
        self.x_pos = x_pos
        self.y_pos = y_pos
        
    def set_text(self, text):
        self.img = self.font.render(text, True, (255, 255, 255))

    def draw(self, surface):
        surface.blit(self.img, (self.x_pos, self.y_pos))
