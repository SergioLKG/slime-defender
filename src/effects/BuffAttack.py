from src.entities.Player import Player
from src.effects.Effect import Effect


class BuffAttack(Effect):

    def __init__(self, tier):
        self.tier = tier
        self.dmgsum = 25  # Ataque añadido
        name = "buff_attack"
        categoria = "slime"
        precio = self.calc_precio(500)  # Poner precio minimo
        super().__init__(name, precio, tier, categoria)

    def cargar(self, player: Player):
        player.ataque += self.calculate()

    def calculate(self):
        if self.tier > 3:
            return self.dmgsum * (self.tier * 1.20)
        return self.dmgsum * self.tier

    def calc_precio(self, precio):
        return super().calc_precio(precio)
        # Por si se quiere cambiar el calculo de precio
        # para hacerlo más caro o más barato según el tier
