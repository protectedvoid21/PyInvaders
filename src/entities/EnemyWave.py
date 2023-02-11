import random

from src.entities.Enemy import Enemy
from src.utils.GameTime import GameTime


class EnemyWave:
    def __init__(self, shoot_func, level_manager):
        self.shoot_func = shoot_func
        self.level_manager = level_manager

        self.enemy_list = []

        self.move_cooldown = 1
        self.actual_cooldown = self.move_cooldown
        
    def is_clear(self):
        return len(self.enemy_list) == 0

    def spawn(self, level):
        rows = self.level_manager.get_enemy_rows(level)

        row_index = 0
        for row in rows:
            self.enemy_list.extend(
                Enemy(random.randint(1, 4), 50 * i + row['start_x'], 60 + row_index * 40, self, self.shoot_func)
                for i in range(row['count']))
            row_index += 1

    def update(self):
        if len(self.enemy_list) == 0:
            return

        for enemy in self.enemy_list:
            enemy.update()

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
