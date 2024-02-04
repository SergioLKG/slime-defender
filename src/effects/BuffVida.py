import math

from src.entities.Player import Player
from src.effects.Effect import Effect


class BuffVida(Effect):

    def __init__(self, tier):
        self.tier = tier
        name = "buff_hp"
        categoria = "slime"
        precio = self.calc_precio()  # Poner precio minimo
        super().__init__(name, precio, tier, categoria)

    def cargar(self, player: Player):
        player.vida_maxima = self.calculate(player.vida_maxima)

    def calculate(self, vida):
        vida_calc = math.ceil(vida + (5 * (1.1 ** (self.tier + 1))))
        return vida_calc
