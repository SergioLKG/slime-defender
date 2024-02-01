from src.entities.Player import Player
from src.effects.Effect import Effect


class BuffVida(Effect):

    def __init__(self, tier):
        self.tier = tier
        self.hpsum = 20
        name = "buff_hp"
        categoria = "slime"
        precio = self.calc_precio(400)  # Poner precio minimo
        super().__init__(name, precio, tier, categoria)

    def cargar(self, player: Player):
        player.vida_maxima += self.calculate()

    def calculate(self):
        if self.tier > 3:
            return self.hpsum * (self.tier * 1.20)
        return self.hpsum * self.tier

    def calc_precio(self, precio):
        return super().calc_precio(precio)
        # Por si se quiere cambiar el calculo de precio
        # para hacerlo más caro o más barato según el tier
