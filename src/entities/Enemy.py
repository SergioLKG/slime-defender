from src.entities.Entity import Entity
import pygame


class Enemy(Entity):
    def __init__(self, vida, ataque, velocidad, velocidad_ataque, rango, x, y, size=30, element="Agua"):
        super().__init__(vida, x, y, size, element)

        self.ataque = ataque
        self.velocidad = velocidad
        self.velocidad_ataque = velocidad_ataque
        self.rango = rango

    def draw_healthbar(self, screen):  # Barra de vida
        barra_vida_rect = pygame.Rect(self.rect.x, self.rect.y - 10, self.barra_vida_ancho, self.barra_vida_alto)
        pygame.draw.rect(screen, (255, 0, 0), barra_vida_rect, 0)
        vida_actual_rect = pygame.Rect(self.rect.x, self.rect.y - 10,
                                       max(0, int(self.barra_vida_ancho * (self.vida / 100))), self.barra_vida_alto)
        pygame.draw.rect(screen, self.barra_vida_color, vida_actual_rect, 0)

    def atacar(self, objetivo):
        if objetivo is not isinstance(Enemy):
            if self.esta_en_rango(objetivo):
                objetivo.recibir_dano(self.ataque)

    def esta_en_rango(self, objetivo):
        distancia = abs(objetivo.rect.x - self.rect.x)
        return distancia <= self.rango

    def recibir_dano(self, cantidad, elemento_enemigo="neutro"):
        super().recibir_dano()

    def morir(self):
        print("A muerto un enemigo!")
        self.kill()

    def update(self):
        self.rect.x -= self.velocidad
