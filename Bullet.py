import pygame.sprite

from GameTime import GameTime


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos, is_friendly):
        super().__init__()
        self.rect = pygame.Rect(x_pos, y_pos, 3, 25)
        self.is_friendly = is_friendly
        self.speed = -500 if is_friendly else 250

    def update(self):
        self.rect.move_ip(0, round(self.speed * GameTime.delta_time))

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), self.rect)
