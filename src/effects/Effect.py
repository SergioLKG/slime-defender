import math

from src.entities.Entity import Entity


class Effect:

    # Categorias: Miscelanea(misc), Armas(weapon), Armaduras(armor), Mouse(mouse), Slime(slime)
    def __init__(self, name, precio, tier, categoria):
        self.name = name
        self.tier = tier
        self.categoria = categoria
        self.precio = precio
        self.precio = self.calc_precio()

    def calc_precio(self):
        precio = math.ceil(((self.tier + 1) * 1.3 ** self.tier))
        return precio

    def cargar(self, entity: Entity):
        # Effecto que quieres cargar en Player
        pass
