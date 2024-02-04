import math

import pygame

from src import game_logic
from src.entities.Entity import Entity


def load_img_element(directorio):
    try:
        return pygame.transform.scale(pygame.image.load(directorio),
                                      (20, 20)).convert_alpha()
    except FileNotFoundError:
        return pygame.transform.scale(pygame.image.load("assets/debug.png"), (20, 20)).convert_alpha()


def calc_af():
    wave_num = game_logic.wave_number
    aquafragments = math.ceil(1 * 1.12 ** wave_num)
    return aquafragments


class Enemy(Entity):
    def __init__(self, x, y, size, enemies, vida, ataque, velocidad, velocidad_ataque, rango, element="agua"):
        super().__init__(x, y, size, element)

        # Atributos
        self.vida_maxima = vida
        self.vida = vida
        self.ataque = ataque
        self.velocidad = velocidad
        self.velocidad_ataque = velocidad_ataque
        self.rango = rango
        self.tiempo_ultimo_ataque = 0
        self.enemies = enemies

        self.aquafragments = calc_af()  # Los fragmentos que suelta

        self.element_image = self.cargar_element()

        # Healthbar
        self.barra_vida_color = (160, 60, 60)
        self.barra_vida_inactiva = (80, 20, 20)
        self.barra_vida_ancho = self.rect.width
        self.barra_vida_alto = self.rect.height * 0.20

    def cargar_element(self):
        try:
            if self.element == 'neutro':
                return load_img_element("assets/sprites/elements/element_neutro.png")
            if self.element == 'fuego':
                return load_img_element("assets/sprites/elements/element_fire.png")
            if self.element == 'agua':
                return load_img_element("assets/sprites/elements/element_water.png")
            if self.element == 'rayo':
                return load_img_element("assets/sprites/elements/element_thunder.png")
            if self.element == 'hielo':
                return load_img_element("assets/sprites/elements/element_ice.png")
            if self.element == 'plant':
                return load_img_element("assets/sprites/elements/element_plant.png")
        except FileNotFoundError:
            return load_img_element("assets/debug.png")

    def draw_healthbar(self, screen):  # Barra de vida
        vida_proporcion = self.vida / self.vida_maxima

        ancho_vida_proporcional = self.barra_vida_ancho * vida_proporcion

        barra_vida_rect = pygame.Rect(self.rect.x, self.rect.y - 20, self.barra_vida_ancho, self.barra_vida_alto)
        vida_actual_rect = pygame.Rect(self.rect.x, self.rect.y - 20, ancho_vida_proporcional, self.barra_vida_alto)
        vida_maxima_rect = pygame.Rect(self.rect.x, self.rect.y - 20, self.barra_vida_ancho, self.barra_vida_alto)

        pygame.draw.rect(screen, self.barra_vida_inactiva, barra_vida_rect)  # Fondo barra
        pygame.draw.rect(screen, self.barra_vida_color, vida_actual_rect)  # Barra de vida
        pygame.draw.rect(screen, (50, 50, 50), vida_maxima_rect, 2)  # Marco barra máxima

        # Dibujar numero de la vida actual
        # Contador numerico vida
        txt_size = 15
        texto_puntuacion = pygame.font.Font(None, txt_size).render(str(int(self.vida)), True, (255, 255, 255))
        screen.blit(texto_puntuacion,
                    (barra_vida_rect.x - texto_puntuacion.get_width() // 2 + barra_vida_rect.width // 2,
                     barra_vida_rect.y - texto_puntuacion.get_height() // 2 + barra_vida_rect.height // 2))

        # Element
        screen.blit(self.element_image,
                    ((barra_vida_rect.left + 10) - (barra_vida_rect.width / 2), barra_vida_rect.top - 5))

    def atacar(self, enemigo):
        if self.esta_en_rango(enemigo):
            if enemigo.alive() and self.esta_en_rango(enemigo):
                if self.puede_atacar():
                    # print(f"{self} golpea a {enemigo}")
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
        if self.vida > 0:
            self.vida = max(0, int(self.vida - self.tabla_tipos(cantidad, elemento_enemigo)))
            # print(f"{self} recibe daño")

    def morir(self):
        print(f"Ha muerto {self}")
        game_logic.aquafragments += self.aquafragments
        self.kill()

    def draw(self, screen):
        super().draw(screen)
        self.draw_healthbar(screen)

    def update(self):
        if self.vida <= 0:
            self.morir()
        for enemigo in self.enemies:
            if not enemigo.alive():  # Si player NO esta vivo
                # TODDO dance (por ejemplo)
                pass
            if self.esta_en_rango(enemigo):
                self.atacar(enemigo)
            else:
                if enemigo.alive():
                    self.rect.x -= self.velocidad  # moverse a la izquierda
