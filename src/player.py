# player.py
class Player:
    def __init__(self):
        self.health = 100
        self.tokens = 0

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print("Game Over. Slime derretido :(")

    def heal(self, amount):
        self.health += amount

    def earn_tokens(self, amount):
        self.tokens += amount
