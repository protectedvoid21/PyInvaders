import pygame.sprite


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x_position, y_position):
        super().__init__()
        self.image = pygame.image.load('enemy.png')
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 3, self.image.get_height() * 3))
        self.rect = self.image.get_rect()
        self.rect.center = (x_position, y_position)
        self.x_position = x_position
        self.y_position = y_position
        self.speed = 100
        
    def change_direction(self):
        self.speed *= -1
        
    def update(self, delta_time):
        self.rect.move_ip(round(self.speed * delta_time), 0)
            
    def draw(self, surface):
        surface.blit(self.image, self.rect)