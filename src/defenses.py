# defenses.py
class Defense:
    def __init__(self, name, cost, damage):
        self.name = name # Nombre elemento Hielo, Fuego, Roca...
        self.cost = cost
        self.damage = damage

    def deploy(self, enemies):
        #Logica para los enemigos.
        pass
