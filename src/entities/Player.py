import pygame

from src.entities.Bullet import Bullet
from src.utils.GameTime import GameTime


class Player(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, max_y):
        super().__init__()
        self.image = pygame.image.load('images/player.png')
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 3, self.image.get_height() * 3))
        self.rect = self.image.get_rect()
        self.rect.center = (start_x, start_y)
        self.max_right = max_y
        
        self.shoot_sound = pygame.mixer.Sound('sounds/player_shoot.wav')
        self.death_sound = pygame.mixer.Sound('sounds/player_death.wav')

        self.shoot_cooldown = 1.0
        self.actual_cooldown = 0.0
        self.bullets = []

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        
        for bullet in self.bullets:
            bullet.update()
            
        if self.actual_cooldown > 0:
            self.actual_cooldown -= GameTime.delta_time

        if pressed_keys[pygame.K_SPACE]:
            if self.actual_cooldown <= 0:
                self.actual_cooldown = self.shoot_cooldown
                self.bullets.append(Bullet(self.rect.centerx, self.rect.centery - 30, True))
                self.shoot_sound.play()

        if self.rect.left > 0:
            if pressed_keys[pygame.K_a]:
                self.rect.move_ip(round(-500 * GameTime.delta_time), 0)
        if self.rect.left < self.max_right:
            if pressed_keys[pygame.K_d]:
                self.rect.move_ip(round(500 * GameTime.delta_time), 0)
                
    def die(self):
        self.death_sound.play()

    def draw(self, surface):
        surface.blit(self.image, self.rect)

        for bullet in self.bullets:
            bullet.draw(surface)
