import pygame
from src.entities.Entity import *


class Player(Entity):

    def __init__(self, x, y, size=50, vida=100, ataque=5, velocidad_ataque=2, rango=10, element="neutro",
                 effects: [] = None, coins=None):
        super().__init__(x, y, size, element)
        self.image = self.load_image("assets", "debug.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        # Misc
        self.coins = coins

        # Atributos
        self.vida = vida
        self.rango = rango
        self.ataque = ataque
        self.velocidad_ataque = velocidad_ataque
        self.tiempo_ultimo_ataque = 0
        self.effects = effects  # Lista de efectos activos

    def load_sprite(self):
        if self.element == 'neutral':
            self.load_image("debug.png", "assets")  # TODO cambiar png a slime_neutral
        if self.element == 'fuego':
            self.load_image("slime_fuego.png", "assets")
        if self.element == 'agua':
            self.load_image("slime_agua.png", "assets")
        if self.element == 'tierra':
            self.load_image("slime_tierra.png", "assets")
        if self.element == 'hielo':
            self.load_image("slime_hielo.png", "assets")

    def draw_healthbar(self, screen):  # Barra de vida
        barra_vida_rect = pygame.Rect(self.rect.x, self.rect.y - 10, self.barra_vida_ancho, self.barra_vida_alto)
        pygame.draw.rect(screen, (255, 0, 0), barra_vida_rect, 0)
        vida_actual_rect = pygame.Rect(self.rect.x, self.rect.y - 10,
                                       max(0, int(self.barra_vida_ancho * (self.vida / 100))), self.barra_vida_alto)
        pygame.draw.rect(screen, self.barra_vida_color, vida_actual_rect, 0)

    def morir(self):
        print("Un jugador ha muerto!")
        self.kill()

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
