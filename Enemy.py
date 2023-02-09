import pygame.sprite

from GameTime import GameTime


class Enemy(pygame.sprite.Sprite):
    def __init__(self, image, x_position, y_position, enemy_wave):
        super().__init__()
        self.enemy_wave = enemy_wave
        self.image = image
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.death_image = pygame.image.load("images/enemy_death.png")
        self.death_image = pygame.transform.scale(self.death_image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (x_position, y_position)
        self.x_position = x_position
        self.speed = 15
        self.death_length = 0.4
        self.is_dying = False

    def change_direction(self):
        self.speed *= -1
        self.rect.y += 20

    def die(self):
        self.is_dying = True
        self.image = self.death_image
        
    def move(self):
        if self.is_dying:
            return
        
        self.x_position += self.speed
        self.rect.x = self.x_position

    def update(self):
        if self.is_dying:
            self.death_length -= GameTime.delta_time
            if self.death_length <= 0:
                self.enemy_wave.enemy_list.remove(self)
                self.kill()

    def draw(self, surface):
        surface.blit(self.image, self.rect)
