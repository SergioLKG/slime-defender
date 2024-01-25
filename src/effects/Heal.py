from src.entities.Player import Player
from src.util.Effect import Effect


class Heal(Effect):

    def __init__(self):
        tier = 99999
        name = "heal_dev"
        categoria = "dev"
        precio = 0
        super().__init__(name, precio, tier, categoria)

    def cargar(self, player: Player):
        player.vida = player.vida_maxima
