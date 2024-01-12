import os

import pygame


class Entity(pygame.sprite.Sprite):
    def __init__(self, x, y, size=(50, 50), element="neutro"):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.size = size
        self.element = element
        self.image = self.load_image("assets/entities", "debug.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        # Añadir atributos para la barra de vida
        self.barra_vida_color = (255, 0, 0)  # Color rojo
        self.barra_vida_ancho = size
        self.barra_vida_alto = 5

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
        ruta = os.path.join(directorio, nombre)
        try:
            image = pygame.image.load(ruta)
            image = pygame.transform.scale(image, size=self.size)
            return image.convert_alpha()
        except FileNotFoundError:
            print("Error! no se puede cargar la imagen")

    def recibir_dano(self, cantidad, elemento_enemigo="neutro"):
        pass  # Clase reemplazable

    def morir(self):
        print("Una entidad ha muerto.")
        self.kill()

    def atacar(self, objetivo):
        pass

    def cambiar_elemento(self, nuevo_elemento):
        self.element = nuevo_elemento
        self.image = self.load_image()

    def get_element(self):
        return self.element
