import pygame.sprite

from src.entities.Entity import *
from src.util.Effect import Effect


class Player(Entity):

    def __init__(self, x, y, size=(80, 80), vida=100, ataque=5, velocidad_ataque=2, rango=200, element="neutro",
                 effects=None):
        super().__init__(x, y, size, element)
        if effects is None:
            effects = []
        self.image = self.load_sprite()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        # Atributos
        self.vida_maxima = vida
        self.vida = vida
        self.rango = rango
        self.ataque = ataque
        self.velocidad_ataque = velocidad_ataque
        self.tiempo_ultimo_ataque = 0
        self.effects: [Effect] = effects  # Lista de efectos activos
        self.robo_vida = 0

        # Healthbar
        self.barra_vida_color = (60, 160, 60)
        self.barra_vida_inactiva = (20, 80, 20)
        self.barra_vida_ancho = self.rect.width
        self.barra_vida_alto = self.rect.height * 0.20

    def draw_healthbar(self, screen):  # Barra de vida
        vida_proporcion = self.vida / self.vida_maxima

        ancho_vida_proporcional = self.barra_vida_ancho * vida_proporcion

        barra_vida_rect = pygame.Rect(self.rect.x, self.rect.y - 20, self.barra_vida_ancho, self.barra_vida_alto)

        vida_actual_rect = pygame.Rect(self.rect.x, self.rect.y - 20, ancho_vida_proporcional, self.barra_vida_alto)

        # Dibuja la barra de vida
        pygame.draw.rect(screen, self.barra_vida_inactiva, barra_vida_rect)  # Fondo barra
        pygame.draw.rect(screen, self.barra_vida_color, vida_actual_rect)  # Barra de vida

        # Contador numerico vida
        txt_size = 20
        texto_puntuacion = pygame.font.Font(None, txt_size).render(str(int(self.vida)), True, (255, 255, 255))
        screen.blit(texto_puntuacion,
                    (barra_vida_rect.x - texto_puntuacion.get_width() // 2 + barra_vida_rect.width // 2,
                     barra_vida_rect.y - texto_puntuacion.get_height() // 2 + barra_vida_rect.height // 2))

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
                        porcent = (self.robo_vida / 100)
                        self.vida += int(max(0, enemigo.tabla_tipos(self.calc_dmg(), enemigo.element) * porcent))
                        self.tiempo_ultimo_ataque = pygame.time.get_ticks()

    def recibir_dano(self, cantidad, elemento_enemigo="neutro"):
        if self.vida > 0:
            self.vida = max(0, self.vida - self.tabla_tipos(cantidad, elemento_enemigo))
            print(f"{self} recibe daño")
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
        x: list = self.effects
        x.append(effect)
        self.effects = x

    def cargar_effects(self):  # Update Effects
        for effect in self.effects:
            if self.effects is not None:
                effect.cargar(self)

    def draw(self, screen):
        super().draw(screen)
        self.draw_healthbar(screen)

    def update(self):
        if self.vida > self.vida_maxima:
            self.vida = self.vida_maxima
        self.atacar()
