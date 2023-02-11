import json
import os
import random


class LevelManager:
    def __init__(self):
        with open('levels.json') as file:
            self.level_data = file.read()
        self.level_data = json.loads(self.level_data)

    def get_enemy_rows(self, level):
        return self.level_data[level - 1]['rows']

