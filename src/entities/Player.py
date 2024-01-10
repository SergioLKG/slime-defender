from src.entities.Entity import Entity
import pygame
import math


class Player(Entity):

    def __init__(self, x, y,size=50,vida=100,ataque=5,velocidad_ataque=5,rango=10, element="Neutro"):
        super().__init__(vida, x, y, size, element)

        self.image = self.load_image()
        self.rango = rango
        self.ataque = ataque
        self.velocidad_ataque = velocidad_ataque
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.tiempo_ultimo_ataque = 0

    def load_image(self):
        if self.element == "Neutro":
            return pygame.image.load("../../assets/sprites/entities/player/neutro_sprite.png").convert_alpha()
        elif self.element == "Fuego":
            return pygame.image.load("../assets/sprites/fuego_sprite.png").convert_alpha()
        elif self.element == "Agua":
            return pygame.image.load("../assets/sprites/agua_sprite.png").convert_alpha()
        elif self.element == "Hielo":
            return pygame.image.load("../assets/sprites/hielo_sprite.png").convert_alpha()
        elif self.element == "Tierra":
            return pygame.image.load("../assets/sprites/tierra_sprite.png").convert_alpha()

    def morir(self):
        print("¡El jugador ha muerto!")

    def puede_atacar(self):
        tiempo_actual = pygame.time.get_ticks()
        tiempo_transcurrido_desde_ataque = tiempo_actual - self.tiempo_ultimo_ataque
        return tiempo_transcurrido_desde_ataque >= 1000 / self.velocidad_ataque

    def esta_en_rango(self, enemigo):
        distancia = abs(enemigo.rect.x - self.rect.x)
        return distancia <= self.rango

    def atacar(self, enemigos):
        if self.puede_atacar():
            for enemigo in enemigos:
                if self.esta_en_rango(enemigo):
                    enemigo.recibir_dano(self.ataque)
                    self.tiempo_ultimo_ataque = pygame.time.get_ticks()
