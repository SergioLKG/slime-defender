import pygame

from src.entities.Entity import Entity


class Enemy(Entity):
    def __init__(self, x, y, size, objetivo, vida, ataque, velocidad, velocidad_ataque, rango, element="agua"):
        super().__init__(x, y, size, element)

        self.objetivo = objetivo
        self.vida = vida
        self.ataque = ataque
        self.velocidad = velocidad
        self.velocidad_ataque = velocidad_ataque
        self.rango = rango
        self.tiempo_ultimo_ataque = 0

        # Healthbar
        self.barra_vida_color = (160, 60, 60)
        self.barra_vida_inactiva = (80, 20, 20)
        self.barra_vida_ancho = self.rect.width * 1
        self.barra_vida_alto = self.rect.height * 0.20

    def draw_healthbar(self, screen):  # Barra de vida
        vida_maxima = int(self.vida)
        vida_actual = min(0, vida_maxima)

        vida_actual_rect = pygame.Rect(self.rect.x - self.rect.width // 2, self.rect.y - (self.rect.height - 10),
                                       vida_maxima - vida_actual - (self.rect.width // 4), self.barra_vida_alto)

        barra_vida_rect = pygame.Rect(self.rect.x - self.rect.width // 2, self.rect.y - (self.rect.height - 10),
                                      self.barra_vida_ancho,
                                      self.barra_vida_alto)
        pygame.draw.rect(screen, self.barra_vida_inactiva, barra_vida_rect, 0)

        pygame.draw.rect(screen, self.barra_vida_color, vida_actual_rect, 0)
        # Dibujar el número de puntuación dentro de la barra de vida
        txtSize = 18
        texto_puntuacion = pygame.font.Font(None, txtSize).render(str(self.vida), True, (255, 255, 255))
        screen.blit(texto_puntuacion,
                    (self.rect.x - txtSize // 2,
                     self.rect.y - (self.rect.height - (txtSize - self.barra_vida_alto // 2))))

    def atacar(self):
        if self.puede_atacar():
            if self.esta_en_rango():
                print(f"{self} golpea a {self.objetivo}")
                self.tiempo_ultimo_ataque = 0
                self.objetivo.recibir_dano(self.calc_dmg())

    def calc_dmg(self):
        dmg = self.ataque
        # Añadir powerups etc
        return dmg

    def puede_atacar(self):
        if self.esta_en_rango():
            tiempo_actual = pygame.time.get_ticks()
            tiempo_transcurrido_desde_ataque = tiempo_actual - self.tiempo_ultimo_ataque
            return tiempo_transcurrido_desde_ataque >= 100000 / (self.velocidad_ataque * 10)

    def esta_en_rango(self):
        distancia = abs(self.objetivo.rect.x - self.rect.x)
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
        if not self.objetivo.alive():  # Si player NO esta vivo
            # TODDO dance (por ejemplo)
            pass

        if self.esta_en_rango():
            self.atacar()
        else:
            self.rect.x -= self.velocidad  # moverse a la izquierda
