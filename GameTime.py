import time

import pygame.time


class GameTime:
    delta_time = 0.0
    
    def __init__(self, framerate):
        self.framerate = framerate
        self.clock = pygame.time.Clock()
        self.previous_time = time.time()

    def update(self):
        self.clock.tick(self.framerate)
        now = time.time()
        GameTime.delta_time = now - self.previous_time
        self.previous_time = now
        