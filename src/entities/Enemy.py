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

    def draw_healthbar(self, screen):  # Barra de vida

        # Definir colores
        verde = (0, 255, 0)
        rojo = (255, 0, 0)

        # Calcular el ancho de la barra de vida según la puntuación
        puntuacion_maxima = 100
        puntuacion_actual = min(0, puntuacion_maxima)
        ancho_barra_actual = (puntuacion_actual / puntuacion_maxima) * (self.rect * 0.80)

        # Dibujar la barra de vida completa en verde
        pygame.draw.rect(screen, verde, (self.x, self.y, self.size[0], self.size[1]))
        # Dibujar la parte de la barra de vida correspondiente a la puntuación en rojo
        pygame.draw.rect(screen, rojo, (self.x, self.y, ancho_barra_actual, self.size[1]))

        # Dibujar el número de puntuación dentro de la barra de vida
        texto_puntuacion = pygame.font.Font(None, 36).render(str(0), True, (255, 255, 255))
        screen.blit(texto_puntuacion, (self.x + self.size(1) // 2 - texto_puntuacion.get_width() // 2, self.y + 0))

    def atacar(self):
        if self.objetivo is not isinstance(self.objetivo, Enemy):
            self.objetivo.recibir_dano(self.ataque)

    def esta_en_rango(self):
        distancia = abs(self.objetivo.rect.x - self.rect.x)
        return distancia <= self.rango

    def recibir_dano(self, cantidad, elemento_enemigo="neutro"):
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
        if not self.objetivo.alive():
            # TODDO dance (por ejemplo)
            pass
        if self.esta_en_rango():
            self.atacar()
        else:
            self.rect.x -= self.velocidad  # moverse a la izquierda
