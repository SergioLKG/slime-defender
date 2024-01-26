import pygame

from src import game_logic
from src.entities.Enemy import Enemy


class Boss(Enemy):

    def __init__(self, x, y, size, enemies, vida, ataque, velocidad, velocidad_ataque, rango, aquafragments):
        super().__init__(x, y, size, enemies, vida, ataque, velocidad, velocidad_ataque, rango, aquafragments)

        # Healthbar
        self.barra_vida_color = (180, 60, 60)
        self.barra_vida_inactiva = (40, 20, 20)

    def draw_healthbar(self, screen):  # Barra de vida
        barra_vida_ancho = (screen.get_width() // 2 - 40)
        barra_vida_alto = 50
        vida_proporcion = self.vida / self.vida_maxima

        ancho_vida_proporcional = self.barra_vida_ancho * vida_proporcion

        barra_vida_rect = pygame.Rect(self.rect.x, self.rect.y - 20, self.barra_vida_ancho, self.barra_vida_alto)

        vida_actual_rect = pygame.Rect(self.rect.x, self.rect.y - 20, ancho_vida_proporcional, self.barra_vida_alto)

        # Dibuja la barra de vida
        pygame.draw.rect(screen, self.barra_vida_inactiva, barra_vida_rect)  # Fondo barra
        pygame.draw.rect(screen, self.barra_vida_color, vida_actual_rect)  # Barra de vida

        txt_size = 16
        texto_puntuacion = pygame.font.Font(None, txt_size).render(str(f"{self.vida} / {self.vida_maxima}"), True,
                                                                   (255, 255, 255))
        screen.blit(texto_puntuacion,
                    (barra_vida_rect.x - texto_puntuacion.get_width() // 2 + barra_vida_rect.width // 2,
                     barra_vida_rect.y - texto_puntuacion.get_height() // 2 + barra_vida_rect.height // 2))

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
        if self.vida > 0:
            self.vida = max(0, self.vida - self.tabla_tipos(cantidad, elemento_enemigo))
            print(f"{self} recibe daño")
        else:
            self.morir()

    def morir(self):
        print(f"Ha muerto {self}")
        game_logic.aquafragments += self.aquafragments
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
