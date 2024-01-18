from src.util.Effect import Effect
from src.entities.Player import Player


class BuffVida(Effect):

    def __init__(self, tier):
        self.tier = tier
        self.hpsum = 50
        name = "buff_hp"
        categoria = "slime"
        precio = self.calc_precio(200)  # Poner precio minimo
        super().__init__(name, precio, tier, categoria)

    def cargar(self, player: Player):
        if self.tier > 3:
            player.vida += (self.hpsum * self.tier * 1.20)
        player.vida += (self.hpsum * self.tier)

    def calc_precio(self, precio):
        return super().calc_precio(precio)
        # Por si se quiere cambiar el calculo de precio
        # para hacerlo más caro o más barato según el tier
