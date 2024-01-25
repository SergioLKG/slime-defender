from src.entities.Player import Player
from src.util.Effect import Effect


class RoboVida(Effect):

    def __init__(self, tier):
        self.tier = tier
        self.hpsum = 50
        name = "hp_steal"
        categoria = "slime"
        precio = self.calc_precio(100)  # Poner precio minimo
        super().__init__(name, precio, tier, categoria)

    def cargar(self, player: Player):
        if self.tier > 3:
            player.vida_maxima += (self.hpsum * (self.tier * 1.20))
        player.vida_maxima += (self.hpsum * self.tier)

    def calc_precio(self, precio):
        return super().calc_precio(precio)
        # Por si se quiere cambiar el calculo de precio
        # para hacerlo más caro o más barato según el tier
