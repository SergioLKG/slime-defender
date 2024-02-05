import math

from src import game_logic
from src.entities.Enemy import Enemy


class GotaMuscle(Enemy):

    def __init__(self, x, y, objetivo):
        vida = 50
        ataque = 20
        velocidad = 0.6
        velocidad_ataque = 0.3
        size = (100, 100)
        rango = (size[0] // 2 + 50)
        super().__init__(x, y, size, objetivo, vida, ataque, velocidad, velocidad_ataque, rango, element="agua")

        self.vida = self.calc_vida()
        self.vida_maxima = self.vida
        self.ataque = self.calc_atk()

        self.image = self.load_image("assets/sprites/entities/enemies", "gota_muscle.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def calc_vida(self):
        vida_final = self.calc_vida_anterior()
        return vida_final

    def calc_atk(self):
        ataque_final = self.calc_ataque_anterior()
        return ataque_final

    def calc_vida_anterior(self):
        vida_anterior = math.ceil(self.vida_maxima)
        for i in range(game_logic.wave_number):
            vida_anterior += math.ceil((2.5 * (1.1 ** game_logic.wave_number)))
        return vida_anterior

    def calc_ataque_anterior(self):
        ataque_anterior = math.ceil(self.ataque)
        for i in range(game_logic.wave_number):
            ataque_anterior += math.ceil(4 * (1.1 ** game_logic.wave_number))
        return ataque_anterior
