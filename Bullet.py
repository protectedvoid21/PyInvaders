import pygame.sprite


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos, is_friendly):
        super().__init__()
        self.rect = pygame.Rect(x_pos, y_pos, 3, 15)
        self.is_friendly = is_friendly
        self.speed = -5 if is_friendly else 5

    def update(self):
        self.rect.move_ip(0, self.speed)

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), self.rect)
