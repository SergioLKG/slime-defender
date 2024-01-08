import pygame


class Entity(pygame.sprite.Sprite):
    def __init__(self, vida, x, y, size=50, element="Neutro"):
        super().__init__()

        self.vida = vida
        self.size = size
        self.element = element
        self.image = self.load_image()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        # Añadir atributos para la barra de vida
        self.barra_vida_color = (0, 255, 0)  # Color verde
        self.barra_vida_ancho = size
        self.barra_vida_alto = 5

    def tabla_tipos(self, cantidad, elemento_enemigo):
        if self.element is "Neutro":
            cantidad = cantidad
        elif self.element == elemento_enemigo:
            cantidad //= 2  # Daño a la mitad elemento
        elif elemento_enemigo is "Agua" and self.element is "Fuego":
            cantidad *= 2  # Daño x2 elemento
        elif elemento_enemigo is "Hielo" and self.element is "Agua":
            cantidad *= 2  # Daño x2 elemento
        elif elemento_enemigo is "Tierra" and self.element is "Hielo":
            cantidad *= 2  # Daño x2 elemento
        return cantidad

    def load_image(self):
        # Cargar la imagen correspondiente al elemento
        # (Implementación específica según tus necesidades)
        image = pygame.Surface((self.size, self.size))
        image.fill((255, 150, 255))  # Color blanco por defecto
        return image

    def recibir_dano(self, cantidad, elemento_enemigo="Neutro"):
        cantidad = self.tabla_tipos(cantidad, elemento_enemigo)
        if self.vida <= 0:
            self.morir()

    def morir(self):
        print("Una entidad ha muerto.")

    def dibujar_barra_vida(self, screen):
        barra_vida_rect = pygame.Rect(self.rect.x, self.rect.y - 10, self.barra_vida_ancho, self.barra_vida_alto)
        pygame.draw.rect(screen, (255, 0, 0), barra_vida_rect, 0)
        vida_actual_rect = pygame.Rect(self.rect.x, self.rect.y - 10,
                                       max(0, int(self.barra_vida_ancho * (self.vida / 100))), self.barra_vida_alto)
        pygame.draw.rect(screen, self.barra_vida_color, vida_actual_rect, 0)

    def atacar(self, objetivo):
        pass

    def cambiar_elemento(self, nuevo_elemento):
        self.element = nuevo_elemento
        self.image = self.load_image()

    def get_element(self):
        return self.element
