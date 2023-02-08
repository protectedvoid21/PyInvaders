from Enemy import Enemy


class EnemyWave:
    def __init__(self):
        self.enemy_list = [Enemy(i * 50, 100) for i in range(10)]
        
    def update(self):
        for enemy in self.enemy_list:
            enemy.update()
            
    def draw(self, surface):
        for enemy in self.enemy_list:
            enemy.draw(surface)
