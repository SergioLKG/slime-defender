import pygame.sprite

from src.entities.Enemy import Enemy


class Gota(Enemy):

    def __init__(self, x, y, objetivo):
        vida = 20
        ataque = 5
        velocidad = 1
        velocidad_ataque = 1
        rango = 50
        size = (50, 50)
        super().__init__(x, y, size, objetivo, vida, ataque, velocidad, velocidad_ataque, rango, element="agua")

        self.image = self.load_image("assets/sprites/entities/enemies", "gota_standar.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)


    def morir(self):
        print("Ha muerto una Gota.")
        self.kill()
