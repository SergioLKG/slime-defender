import pygame.sprite

from src.entities.Entity import *
from src.util.Effect import Effect


class Player(Entity):

    def __init__(self, x, y, size=(80, 80), vida=100, ataque=5, velocidad_ataque=2, rango=200, element="neutro",
                 effects: [Effect] = None):
        super().__init__(x, y, size, element)
        self.image = self.load_sprite()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        # Atributos
        self.vida = vida
        self.rango = rango
        self.ataque = ataque
        self.velocidad_ataque = velocidad_ataque
        self.tiempo_ultimo_ataque = 0
        self.effects: [Effect] = effects  # Lista de efectos activos

        # Healthbar
        self.barra_vida_color = (60, 160, 60)
        self.barra_vida_inactiva = (20, 80, 20)
        self.barra_vida_ancho = self.rect.width * 1
        self.barra_vida_alto = self.rect.height * 0.20

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

    def draw_healthbar(self, screen):  # Barra de vida (Sobreescribir si es necesario).
        vida_maxima = int(self.vida)
        vida_actual = min(0, vida_maxima)

        vida_actual_rect = pygame.Rect(self.rect.x, self.rect.y - (self.rect.height // 2) + 10,
                                       (vida_maxima - vida_actual) * (self.width / 100), self.barra_vida_alto)

        barra_vida_rect = pygame.Rect(self.rect.x, self.rect.y - (self.rect.height // 2) + 10,
                                      self.barra_vida_ancho,
                                      self.barra_vida_alto)
        pygame.draw.rect(screen, self.barra_vida_inactiva, barra_vida_rect, 0)

        pygame.draw.rect(screen, self.barra_vida_color, vida_actual_rect, 0)
        # Dibujar el número de puntuación dentro de la barra de vida
        txt_size = 20
        texto_puntuacion = pygame.font.Font(None, txt_size).render(str(self.vida), True, (255, 255, 255))
        screen.blit(texto_puntuacion,
                    (barra_vida_rect.x - texto_puntuacion.get_width() // 2 + barra_vida_rect.width // 2,
                     barra_vida_rect.y - texto_puntuacion.get_height() // 2 + barra_vida_rect.height // 2))

    def puede_atacar(self):
        tiempo_actual = pygame.time.get_ticks()
        tiempo_transcurrido_desde_ataque = tiempo_actual - self.tiempo_ultimo_ataque
        return tiempo_transcurrido_desde_ataque >= 12000 / (self.velocidad_ataque * 10)

    def esta_en_rango(self, enemigo):
        distancia = abs(enemigo.rect.x - self.rect.x)
        return distancia <= self.rango

    def atacar(self):
        for enemigo in self.enemies:
            if self.esta_en_rango(enemigo):
                if enemigo.alive() and self.esta_en_rango(enemigo):
                    if self.puede_atacar():
                        print(f"{self} ataca a {enemigo}")
                        enemigo.recibir_dano(self.calc_dmg())
                        self.tiempo_ultimo_ataque = pygame.time.get_ticks()

    def recibir_dano(self, cantidad, elemento_enemigo="neutro"):
        if self.vida > 0:
            self.vida -= self.tabla_tipos(cantidad, elemento_enemigo)
        else:
            self.morir()

    def morir(self):
        print("Un jugador ha muerto!")
        self.kill()

    def calc_dmg(self):
        dmg = self.ataque
        # Añadir powerups etc
        return dmg

    def add_effect(self, effect: Effect):
        self.effects.add(effect)

    def cargar_effects(self):  # Update Effects
        if self.effects is not None:
            for effect in self.effects:
                effect.cargar()

    def draw(self, screen):
        super().draw(screen)
        self.draw_healthbar(screen)

    def update(self):
        self.atacar()
