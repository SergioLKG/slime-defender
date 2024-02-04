import math

from src.entities.Player import Player
from src.effects.Effect import Effect


class BuffAttack(Effect):

    def __init__(self, tier):
        self.tier = tier
        name = "buff_attack"
        categoria = "slime"
        precio = self.calc_precio()  # Poner precio minimo
        super().__init__(name, precio, tier, categoria)

    def cargar(self, player: Player):
        player.ataque = self.calculate(player.ataque)

    def calculate(self, ataque):
        atk_calc = math.ceil(ataque + (1.3 * (1.1 ** (self.tier + 1))))
        return atk_calc

