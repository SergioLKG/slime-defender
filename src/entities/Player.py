import pygame.sprite

import src.entities.Enemy
from src.entities.Entity import *


class Player(Entity):

    def __init__(self, x, y, size=(80, 80), vida=100, ataque=5, velocidad_ataque=2, rango=200, element="neutro",
                 effects: [] = None):
        super().__init__(x, y, size, element)
        self.image = self.load_sprite()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.enemies = None

        # Atributos
        self.vida = vida
        self.rango = rango
        self.ataque = ataque
        self.velocidad_ataque = velocidad_ataque
        self.tiempo_ultimo_ataque = 0
        self.effects = effects  # Lista de efectos activos

        # Healthbar
        self.barra_vida_color = (60, 200, 60)
        self.barra_vida_ancho = self.rect.width * 0.80
        self.barra_vida_alto = self.rect.height * 0.16

    def load_sprite(self):
        try:
            if self.element == 'neutro':
                return self.load_image("assets/sprites/entities/player", "slime_neutro.png")
            if self.element == 'fuego':
                return self.load_image("assets/sprites/entities/player", "slime_fuego.png")
            if self.element == 'agua':
                return self.load_image("assets/sprites/entities/player", "slime_agua.png")
            if self.element == 'tierra':
                return self.load_image("assets/sprites/entities/player", "slime_tierra.png")
            if self.element == 'hielo':
                return self.load_image("assets/sprites/entities/player", "slime_hielo.png")
        except FileNotFoundError:
            return self.load_image("assets", "debug.png")

    def draw_healthbar(self, screen):  # Barra de vida
        barra_vida_rect = pygame.Rect(self.rect.x - self.rect.width // 2, self.rect.y - (self.rect.height - 10),
                                      self.barra_vida_ancho,
                                      self.barra_vida_alto)
        pygame.draw.rect(screen, (255, 0, 0), barra_vida_rect, 0)
        vida_actual_rect = pygame.Rect(self.rect.x - self.rect.width // 2, self.rect.y - (self.rect.height - 10),
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

    def atacar(self):
        if self.puede_atacar():
            for enemigo in self.enemies:
                if isinstance(enemigo, src.entities.Enemy.Enemy):
                    if self.esta_en_rango(enemigo):
                        print("Player ataca a ", enemigo)
                        enemigo.recibir_dano(self.calc_dmg())
                        self.tiempo_ultimo_ataque = pygame.time.get_ticks()
                else:
                    print("No atacaré a inocentes.")

    def calc_dmg(self):
        daño = self.ataque
        # Añadir powerups etc
        return daño

    def set_enemies(self, enemies):
        self.enemies = enemies

    def draw(self, screen):
        super().draw(screen)
        self.draw_healthbar(screen)

    def update(self):
        self.atacar()
