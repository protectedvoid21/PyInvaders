from Enemy import Enemy


class EnemyWave:
    def __init__(self):
        self.enemy_list = [Enemy(i * 50, 100) for i in range(2)]
        
    def update(self, delta_time):
        for enemy in self.enemy_list:
            enemy.update(delta_time)
            
    def draw(self, surface):
        for enemy in self.enemy_list:
            enemy.draw(surface)
