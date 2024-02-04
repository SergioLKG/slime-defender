from src import game_logic
from src.entities.Enemy import Enemy


class GotaMuscle(Enemy):

    def __init__(self, x, y, objetivo):
        vida = 50
        ataque = 20
        velocidad = 0.6
        velocidad_ataque = 0.3
        size = (70, 70)
        rango = (size[0] // 2 + 50)
        super().__init__(x, y, size, objetivo, vida, ataque, velocidad, velocidad_ataque, rango, element="agua")

        self.vida_anterior = self.calc_vida()
        self.ataque_anterior = self.calc_atk()
        self.vida_maxima = self.vida

        self.image = self.load_image("assets/sprites/entities/enemies", "gota_muscle.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def calc_vida(self):
        vida_final = self.calc_vida_anterior() + (2.5 * (1.1 ** game_logic.wave_number))
        return int(vida_final)

    def calc_atk(self):
        ataque_final = self.ataque + (1.1 ** game_logic.wave_number)
        return int(ataque_final)

    def calc_vida_anterior(self):
        aux = self.vida_maxima
        for i in range(game_logic.wave_number):
            vida_anterior = aux + (2.5 * (1.1 ** game_logic.wave_number))
            aux = vida_anterior
        return aux
