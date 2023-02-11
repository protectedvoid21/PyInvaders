import sys

import pygame

from src.utils.Button import Button


class PauseMenu:
    def __init__(self, resume_func, exit_func, position, size):
        self.resume_func = resume_func
        self.exit_func = exit_func

        self.background_panel = pygame.Rect(position, size)

        self.resume_button = Button((size[0] * 0.8, size[1] * 0.3),
                                    (position[0] + size[0] * 0.1, position[1] + size[1] * 0.1),
                                    'green', (147, 255, 128), 'Resume', 'white')

        self.exit_button = Button((size[0] * 0.8, size[1] * 0.3),
                                  (position[0] + size[0] * 0.1, position[1] + size[1] * 0.5),
                                  'green', (147, 255, 128), 'Exit', 'white')

    def update(self):
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.resume_button.check_for_hover(mouse_pos):
                    self.resume_func()
                if self.exit_button.check_for_hover(mouse_pos):
                    self.exit_func()

        self.resume_button.update(mouse_pos)
        self.exit_button.update(mouse_pos)

    def draw(self, surface):
        pygame.draw.rect(surface, (30, 30, 30), self.background_panel)
        self.resume_button.draw(surface)
        self.exit_button.draw(surface)
