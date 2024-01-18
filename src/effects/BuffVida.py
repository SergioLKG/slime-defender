from src.util.Effect import Effect
from src.entities.Player import Player


class BuffVida(Effect):

    def __init__(self, name, tier):
        categoria = "slime"
        precio = 400
        super().__init__(name, precio, tier, categoria)
        self.hpsum = 200

    def cargar(self, player: Player):
        player.vida += (self.hpsum * self.tier)
