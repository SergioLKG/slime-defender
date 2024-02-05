import math

from src.entities.Player import Player
from src.effects.Effect import Effect


class RoboVida(Effect):

    def __init__(self, tier):
        self.tier = tier
        name = "lp_steal"
        categoria = "slime"
        precio = self.calc_precio()  # Poner precio minimo
        super().__init__(name, precio, tier, categoria)

    def cargar(self, player: Player):
        player.robo_vida = self.calculate(player.robo_vida)
        print("robo de vida", player.robo_vida)

    def calculate(self, lpsteal):
        calc_steal = math.ceil(lpsteal + (1.005 ** (self.tier + 1)))
        return calc_steal
