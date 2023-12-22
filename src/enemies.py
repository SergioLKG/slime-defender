# enemies.py
class WaterEnemy:
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage

    def attack_player(self, player):
        player.take_damage(self.damage)
