from src.entities.Player import Player
from src.util.Effect import Effect


class RoboVida(Effect):

    def __init__(self, tier):
        self.tier = tier
        self.porcent = 1
        name = "hp_steal"
        categoria = "slime"
        precio = self.calc_precio(500)  # Poner precio minimo
        super().__init__(name, precio, tier, categoria)

    def cargar(self, player: Player):
        player.robo_vida = self.calculate()

    def calculate(self):
        if self.tier == 0:
            self.porcent = 0
        if self.tier > 3:
            return int((self.porcent * (self.tier * 3)))
        return int((self.porcent * (self.tier * 2.2)))

    def calc_precio(self, precio):
        return super().calc_precio(precio)
        # Por si se quiere cambiar el calculo de precio
        # para hacerlo más caro o más barato según el tier
