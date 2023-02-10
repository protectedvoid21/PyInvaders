import random

import pygame.sprite

from src.utils.GameTime import GameTime


class Enemy(pygame.sprite.Sprite):
    def __init__(self, image_index, x_position, y_position, enemy_wave, shoot_func):
        super().__init__()
        self.enemy_wave = enemy_wave
        
        self.sprites = []
        
        self.image = pygame.image.load(f'images/enemy{image_index}_1.png')
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.sprites.append(self.image)
        
        second_image = pygame.image.load(f'images/enemy{image_index}_2.png')
        second_image = pygame.transform.scale(second_image, (30, 30))
        self.sprites.append(second_image)
        
        self.animation_index = 0
        self.animation_speed = 0.2
        self.animation_act_time = self.animation_speed
        self.death_image = pygame.transform.scale(pygame.image.load("images/enemy_death.png"), (30, 30))
        
        self.rect = self.image.get_rect()
        self.rect.center = (x_position, y_position)
        self.x_position = x_position
        self.y_position = y_position
        
        self.shoot_sound = pygame.mixer.Sound('sounds/enemy_shoot.wav')
        self.death_sound = pygame.mixer.Sound('sounds/enemy_death.wav')

        self.speed = 15
        self.shoot_func = shoot_func
        self.shoot_cooldown = 2
        self.actual_cooldown = self.actual_cooldown = (random.random() * 2 - 1) + self.shoot_cooldown
        self.death_length = 0.4
        self.is_dying = False

    def change_direction(self):
        self.speed *= -1
        self.rect.y += 20

    def die(self):
        self.is_dying = True
        self.image = self.death_image
        self.death_sound.play()

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
            return
        
        self.actual_cooldown -= GameTime.delta_time
        self.animation_act_time -= GameTime.delta_time
        
        if self.animation_act_time <= 0:
            self.animation_act_time = self.animation_speed
            self.animation_index += 1
            if self.animation_index == len(self.sprites):
                self.animation_index = 0
            
            self.image = self.sprites[self.animation_index]
        
        if self.actual_cooldown <= 0:
            self.shoot()

    def shoot(self):
        self.shoot_func((self.rect.centerx, self.rect.centery), False)
        self.actual_cooldown = (random.random() * 2 - 1) + self.shoot_cooldown
        self.shoot_sound.play()

    def draw(self, surface):
        surface.blit(self.image, self.rect)
