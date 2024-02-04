import math

from src import game_logic
from src.entities.Enemy import Enemy


class Gota(Enemy):

    def __init__(self, x, y, objetivo):
        vida = 20
        ataque = 5
        velocidad = 0.6
        velocidad_ataque = 1
        size = (50, 50)
        rango = (size[0] // 2 + 50)
        super().__init__(x, y, size, objetivo, vida, ataque, velocidad, velocidad_ataque, rango, element="agua")

        self.vida = self.calc_vida()
        self.vida_maxima = self.vida
        self.ataque = self.calc_atk()

        self.image = self.load_image("assets/sprites/entities/enemies", "gota_standar.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def calc_vida(self):
        vida_final = self.calc_vida_anterior()
        return vida_final

    def calc_atk(self):
        ataque_final = self.ataque + (1.1 ** game_logic.wave_number)
        return int(ataque_final)

    def calc_vida_anterior(self):
        vida_anterior = math.ceil(self.vida_maxima)
        for i in range(game_logic.wave_number):
            vida_anterior += math.ceil((1.1 ** game_logic.wave_number))
        return vida_anterior
