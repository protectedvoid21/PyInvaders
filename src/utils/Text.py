import pygame


class Text:
    def __init__(self, text, size, position, color):
        self.font = pygame.font.Font('Retro Gaming.ttf', size)
        self.img = self.font.render(text, True, color)
        self.color = color
        self.x_pos = position[0]
        self.y_pos = position[1]
        
    def set_text(self, text):
        self.img = self.font.render(text, True, self.color)

    def draw(self, surface):
        surface.blit(self.img, (self.x_pos, self.y_pos))
