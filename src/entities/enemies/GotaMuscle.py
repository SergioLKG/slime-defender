from src.entities.Enemy import Enemy


class GotaMuscle(Enemy):

    def __init__(self, x, y, objetivo):
        vida = 50
        ataque = 20
        velocidad = 0.5
        velocidad_ataque = 0.3
        size = (70, 70)
        rango = (size[0]//2 + 50)
        aquafragments = 200
        super().__init__(x, y, size, objetivo, vida, ataque, velocidad, velocidad_ataque, rango, aquafragments,
                         element="agua")

        self.image = self.load_image("assets/sprites/entities/enemies", "gota_muscle.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
