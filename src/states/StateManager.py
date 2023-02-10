import sys

import pygame

from src.utils.GameTime import GameTime
from src.states.MenuState import MenuState


class StateManager:
    def __init__(self):
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 600
        self.screen = pygame.display.set_mode([self.SCREEN_WIDTH, self.SCREEN_HEIGHT])

        self.game_time = GameTime(60)

        pygame.display.set_caption('PyInvaders')

        self.current_state = None
        self.change_state(MenuState())
        
    def change_state(self, new_state):
        new_state.inject(self, self.screen)
        self.current_state = new_state

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.game_time.update()

            self.current_state.update()
            self.current_state.draw()

            pygame.display.update()
