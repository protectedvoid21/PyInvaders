from src.entities.Bullet import Bullet


class BulletManager:
    def __init__(self):
        self.statistics = None

        self.player = None
        self.enemy_list = None

        self.game_over_func = None
        self.bullets = []
        
    def inject(self, game_state):
        self.statistics = game_state.statistics
        
        self.player = game_state.player
        self.enemy_list = game_state.enemy_wave.enemy_list
        self.game_over_func = game_state.game_over

    def shoot(self, position, is_friendly):
        self.bullets.append(Bullet(position, is_friendly))

    def update(self):
        for bullet in self.bullets:
            bullet.update()
        
            if bullet.is_friendly:
                for enemy in self.enemy_list:
                    if bullet.rect.colliderect(enemy):
                        self.bullets.remove(bullet)
                        self.statistics.add_score(10)
                        enemy.die()
                        bullet.kill()
                        break

            elif bullet.rect.colliderect(self.player):
                self.statistics.remove_life()
                self.bullets.clear()
                self.player.die()

                if self.statistics.lives == 0:
                    self.game_over_func()
                return

    def draw(self, surface):
        for bullet in self.bullets:
            bullet.draw(surface)