import pygame

from Bullet import Bullet


class Player(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, max_y):
        super().__init__()
        self.image = pygame.image.load('player.png')
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 3, self.image.get_height() * 3))
        self.rect = self.image.get_rect()
        self.rect.center = (start_x, start_y)
        self.max_right = max_y

        self.shoot_cooldown = 2
        self.actual_cooldown = 0
        self.bullets = []

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        
        for bullet in self.bullets:
            bullet.update()

        if pressed_keys[pygame.K_SPACE]:
            if self.actual_cooldown == 0:
                self.actual_cooldown = self.shoot_cooldown
                self.bullets.append(Bullet(self.rect.x, self.rect.y, True))
            #add cooldown

        if self.rect.left > 0:
            if pressed_keys[pygame.K_a]:
                self.rect.move_ip(-5, 0)
        if self.rect.left < self.max_right:
            if pressed_keys[pygame.K_d]:
                self.rect.move_ip(5, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

        for bullet in self.bullets:
            bullet.draw(surface)
