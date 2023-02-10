import sys

import pygame.mouse

from src.states.GameState import GameState
from src.states.State import State
from src.utils.Button import Button
from src.utils.Text import Text


class MenuState(State):
    def __init__(self):
        super().__init__()
        
        self.title_label = Text('PyInvaders', 60, (170, 20), 'White')

        self.play_button = Button((300, 100), (250, 150), 'green', (147, 255, 128), 'Play', 'black')
        self.options_button = Button((300, 100), (250, 300), 'green', (147, 255, 128), 'Options', 'black')
        self.exit_button = Button((300, 100), (250, 450), 'green', (147, 255, 128), 'Exit', 'black')

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.play_button.check_for_hover(mouse_pos):
                    self.state_manager.change_state(GameState())
                if self.options_button.check_for_hover(mouse_pos):
                    print('clicked options')
                if self.exit_button.check_for_hover(mouse_pos):
                    pygame.quit()
                    sys.exit()

        self.play_button.update(mouse_pos)
        self.options_button.update(mouse_pos)
        self.exit_button.update(mouse_pos)

    def draw(self):
        self.screen.fill((15, 15, 15))
        
        self.title_label.draw(self.screen)
        self.play_button.draw(self.screen)
        self.options_button.draw(self.screen)
        self.exit_button.draw(self.screen)
