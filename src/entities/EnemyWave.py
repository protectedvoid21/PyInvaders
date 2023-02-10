import random

import pygame.image

from src.entities.Enemy import Enemy
from src.utils.GameTime import GameTime


class EnemyWave:
    def __init__(self, shoot_func):
        self.enemy_bullets = []
        self.enemy_list = [
            Enemy(random.randint(1, 4), i * 50 + 50, 60, self, shoot_func)
            for i in range(10)]

        self.move_cooldown = 1
        self.actual_cooldown = self.move_cooldown

    def update(self):
        for enemy in self.enemy_list:
            enemy.update()

        for bullet in self.enemy_bullets:
            bullet.update()

        if self.actual_cooldown > 0:
            self.actual_cooldown -= GameTime.delta_time
            return

        self.actual_cooldown = self.move_cooldown

        if len(self.enemy_list) > 0:
            if self.enemy_list[-1].rect.x > 730 or self.enemy_list[0].rect.x < 30:
                self.move_cooldown -= self.move_cooldown * 0.1
                for enemy in self.enemy_list:
                    enemy.change_direction()

        for enemy in self.enemy_list:
            enemy.move()

    def draw(self, surface):
        for enemy in self.enemy_list:
            enemy.draw(surface)

        for bullet in self.enemy_bullets:
            bullet.draw(surface)
