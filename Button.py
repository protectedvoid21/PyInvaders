import pygame.sprite

from Text import Text


class Button(pygame.sprite.Sprite):
    def __init__(self, size, position, color, hover_color, text, text_color):
        super().__init__()
        
        self.default_color = color
        self.color = color
        self.hover_color = hover_color
        self.rect = pygame.rect.Rect(position, size)
        self.label = Text(text, 50, position, text_color)
        
    def check_for_hover(self, position):
        if position[0] in range(self.rect.left, self.rect.right) \
                and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False
    
    def update(self, position):
        self.color = self.hover_color if self.check_for_hover(position) else self.default_color
            
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        self.label.draw(surface)
