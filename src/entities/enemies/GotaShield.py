from src import game_logic
from src.entities.Enemy import Enemy


class GotaShield(Enemy):

    def __init__(self, x, y, objetivo):
        vida = 80
        ataque = 1
        velocidad = 0.6
        velocidad_ataque = 0.8
        size = (60, 60)
        rango = (size[0] // 2 + 50)
        super().__init__(x, y, size, objetivo, vida, ataque, velocidad, velocidad_ataque, rango, element="agua")

        self.vida_base = self.calc_vida()
        self.ataque_base = self.calc_atk()
        self.vida_maxima = self.vida

        self.image = self.load_image("assets/sprites/entities/enemies", "gota_shield.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def calc_vida(self):
        aux = self.vida
        if game_logic.wave_number <= 1:
            aux = self.vida_base
        vida_final = aux + (4 * (1.1 ** game_logic.wave_number))
        return int(vida_final)

    def calc_atk(self):
        aux = self.ataque
        if game_logic.wave_number <= 1:
            aux = self.ataque_base
        ataque_final = aux + ((1.1 ** game_logic.wave_number) / 5)
        return int(ataque_final)
