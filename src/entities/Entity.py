import os

import pygame


class Entity(pygame.sprite.Sprite):
    def __init__(self, x, y, size=(50, 50), element="neutro"):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.size = size
        self.element = element
        self.image = self.load_image("assets", "debug.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.width = self.rect.width
        self.height = self.rect.height
        self.enemies = None  # Lista de objetivos

    def tabla_tipos(self, cantidad, elemento_enemigo):
        if self.element == "neutro":
            cantidad = cantidad
        elif self.element == elemento_enemigo:
            cantidad //= 2  # Daño a la mitad elemento
        elif elemento_enemigo == "agua" and self.element == "fuego":
            cantidad *= 2  # Daño x2 elemento
        elif elemento_enemigo == "hielo" and self.element == "agua":
            cantidad *= 2  # Daño x2 elemento
        elif elemento_enemigo == "tierra" and self.element == "hielo":
            cantidad *= 2  # Daño x2 elemento
        return cantidad

    def load_image(self, directorio, nombre):
        try:
            return pygame.transform.scale(pygame.image.load(os.path.join(directorio, nombre)),
                                          size=self.size).convert_alpha()
        except FileNotFoundError:
            return pygame.transform.scale(pygame.image.load("assets/debug.png"), size=self.size).convert_alpha()

    def recibir_dano(self, cantidad, elemento_enemigo="neutro"):
        pass  # Clase reemplazable

    def morir(self):
        print("Una entidad ha muerto.")
        self.kill()

    def cambiar_elemento(self, nuevo_elemento):
        self.element = nuevo_elemento

    def get_element(self):
        return self.element

    def draw(self, screen):
        screen.blit(self.image,
                    (self.rect.x - (self.image.get_width() // 2), self.rect.y - self.image.get_width() // 2))

    def set_enemies(self, enemies):
        self.enemies = enemies
