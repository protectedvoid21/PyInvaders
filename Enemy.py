import pygame.sprite

from GameTime import GameTime


class Enemy(pygame.sprite.Sprite):
    def __init__(self, image, x_position, y_position, enemy_wave):
        super().__init__()
        self.enemy_wave = enemy_wave
        self.image = image
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (x_position, y_position)
        self.x_position = x_position
        self.speed = 15
        self.death_length = 0.5
        self.is_dying = False
        
    def change_direction(self):
        self.speed *= -1
        self.rect.y += 20
        
    def start_dying(self):
        self.is_dying = True
        
    def update(self):
        if self.is_dying:
            self.death_length -= GameTime.delta_time
            if self.death_length <= 0:
                print('dead!')
                self.enemy_wave.enemy_list.remove(self)
                self.kill()
                
        self.x_position += self.speed
        self.rect.x = self.x_position
        
            
    def draw(self, surface):
        surface.blit(self.image, self.rect)