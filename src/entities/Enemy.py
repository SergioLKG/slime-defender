import pygame

import src.entities.Player
from src.entities.Entity import Entity


class Enemy(Entity):
    def __init__(self, x, y, size, enemies, vida, ataque, velocidad, velocidad_ataque, rango, element="agua"):
        super().__init__(x, y, size, element)

        self.enemies = enemies
        self.vida = vida
        self.ataque = ataque
        self.velocidad = velocidad
        self.velocidad_ataque = velocidad_ataque
        self.rango = rango
        self.tiempo_ultimo_ataque = 0

        # Healthbar
        self.barra_vida_color = (160, 60, 60)
        self.barra_vida_inactiva = (80, 20, 20)
        self.barra_vida_ancho = self.rect.width
        self.barra_vida_alto = self.rect.height * 0.20

    def draw_healthbar(self, screen):  # Barra de vida
        vida_maxima = int(self.vida)
        vida_actual = min(0, vida_maxima)

        vida_actual_rect = pygame.Rect(self.rect.x, self.rect.y - (self.rect.height // 2) + 10,
                                       (vida_maxima - vida_actual) * 2.5,
                                       self.barra_vida_alto)

        barra_vida_rect = pygame.Rect(self.rect.x, self.rect.y - (self.rect.height // 2) + 10,
                                      self.barra_vida_ancho,
                                      self.barra_vida_alto)

        pygame.draw.rect(screen, self.barra_vida_inactiva, barra_vida_rect, 0)

        pygame.draw.rect(screen, self.barra_vida_color, vida_actual_rect, 0)
        # Dibujar numero de la vida actual
        # txt_size = 16
        # texto_puntuacion = pygame.font.Font(None, txt_size).render(str(self.vida), True, (255, 255, 255))
        # screen.blit(texto_puntuacion,
        #             (barra_vida_rect.x - texto_puntuacion.get_width() // 2 + barra_vida_rect.width // 2,
        #              barra_vida_rect.y - texto_puntuacion.get_height() // 2 + barra_vida_rect.height // 2))

    def atacar(self, enemigo):
        if self.esta_en_rango(enemigo):
            if enemigo.alive() and self.esta_en_rango(enemigo):
                if self.puede_atacar():
                    print(f"{self} golpea a {enemigo}")
                    enemigo.recibir_dano(self.calc_dmg())
                    self.tiempo_ultimo_ataque = pygame.time.get_ticks()

    def calc_dmg(self):
        dmg = self.ataque
        # Añadir powerups etc
        return dmg

    def puede_atacar(self):
        tiempo_actual = pygame.time.get_ticks()
        tiempo_transcurrido_desde_ataque = tiempo_actual - self.tiempo_ultimo_ataque
        return tiempo_transcurrido_desde_ataque >= 15000 / (self.velocidad_ataque * 10)

    def esta_en_rango(self, objetivo):
        distancia = abs(objetivo.rect.x - self.rect.x)
        return distancia <= self.rango

    def recibir_dano(self, cantidad, elemento_enemigo="neutro"):
        print(f"{self} esta recibiendo daño")
        self.vida -= self.tabla_tipos(cantidad, elemento_enemigo)
        if self.vida <= 0:
            self.morir()

    def morir(self):
        print("A muerto un enemigo!")
        self.kill()

    def draw(self, screen):
        super().draw(screen)
        self.draw_healthbar(screen)

    def update(self):
        for enemigo in self.enemies:
            if not enemigo.alive():  # Si player NO esta vivo
                # TODDO dance (por ejemplo)
                pass
            if self.esta_en_rango(enemigo):
                self.atacar(enemigo)
            else:
                if enemigo.alive():
                    self.rect.x -= self.velocidad  # moverse a la izquierda
