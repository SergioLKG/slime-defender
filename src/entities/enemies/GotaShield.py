from src.entities.Enemy import Enemy


class GotaShield(Enemy):

    def __init__(self, x, y, objetivo):
        vida = 20
        ataque = 1
        velocidad = 1
        velocidad_ataque = 1
        size = (50, 50)
        rango = (size[0]//2 + 50)
        aquafragments = 200
        super().__init__(x, y, size, objetivo, vida, ataque, velocidad, velocidad_ataque, rango, aquafragments,
                         element="agua")

        self.image = self.load_image("assets/sprites/entities/enemies", "gota_standar.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
