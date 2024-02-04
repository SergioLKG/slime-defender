import pygame.sprite

from src.entities.Entity import *
from src.effects.Effect import Effect


class Player(Entity):

    def __init__(self, x, y, size=(80, 80), vida=100, ataque=5, velocidad_ataque=2, rango=200, element="neutro",
                 effects=None):
        super().__init__(x, y, size, element)
        if effects is None:
            effects = []

        self.player_path = "assets/sprites/entities/player"
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

        self.focusing = False
        self.attacking = False

        # Healthbar
        self.barra_vida_color = (60, 160, 60)
        self.barra_vida_inactiva = (20, 80, 20)
        self.barra_vida_ancho = self.rect.width
        self.barra_vida_alto = self.rect.height * 0.20

        # Cosmetics
        self.focusing_sprite = self.load_image(f"{self.player_path}/animations", "focusing.png")
        self.attacking_sprite = self.load_image(f"{self.player_path}/animations", "attacking.png")
        self.attack_animation_duration = 300  # Duración en milisegundos anim ataque
        self.attack_animation_start_time = 0  # Inicializado en 0

    def draw_healthbar(self, screen):  # Barra de vida
        vida_proporcion = self.vida / self.vida_maxima

        ancho_vida_proporcional = self.barra_vida_ancho * vida_proporcion

        top = self.rect.top - 10 - self.height // 2
        left = self.rect.left - self.width // 2

        barra_vida_rect = pygame.Rect(left, top, self.barra_vida_ancho, self.barra_vida_alto)
        vida_actual_rect = pygame.Rect(left, top, ancho_vida_proporcional, self.barra_vida_alto)
        vida_maxima_rect = pygame.Rect(left, top, self.barra_vida_ancho, self.barra_vida_alto)

        pygame.draw.rect(screen, self.barra_vida_inactiva, barra_vida_rect)  # Fondo barra
        pygame.draw.rect(screen, self.barra_vida_color, vida_actual_rect)  # Barra de vida
        pygame.draw.rect(screen, (50, 50, 50), vida_maxima_rect, 2)  # Marco barra máxima

        # Contador numerico vida
        txt_size = 20
        texto_puntuacion = pygame.font.Font(None, txt_size).render(str(int(self.vida)), True, (255, 255, 255))
        screen.blit(texto_puntuacion,
                    (barra_vida_rect.x - texto_puntuacion.get_width() // 2 + barra_vida_rect.width // 2,
                     barra_vida_rect.y - texto_puntuacion.get_height() // 2 + barra_vida_rect.height // 2))

    def load_sprite(self):
        try:
            if self.element == 'neutro':
                return self.load_image(f"{self.player_path}", "slime_neutro.png")
            if self.element == 'fuego':
                return self.load_image(f"{self.player_path}", "slime_fire.png")
            if self.element == 'agua':
                return self.load_image(f"{self.player_path}", "slime_water.png")
            if self.element == 'rayo':
                return self.load_image("assets/sprites/entities/player", "slime_thunder.png")
            if self.element == 'hielo':
                return self.load_image("assets/sprites/entities/player", "slime_ice.png")
            if self.element == 'plant':
                return self.load_image("assets/sprites/entities/player", "slime_plant.png")
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
        self.focusing = False

        for enemigo in self.enemies:
            if self.esta_en_rango(enemigo):
                self.focusing = True
                if enemigo.alive() and self.esta_en_rango(enemigo):
                    if self.puede_atacar():
                        self.attacking = True
                        self.attack_animation_start_time = pygame.time.get_ticks()  # Guardar el tiempo de inicio
                        enemigo.recibir_dano(self.calc_dmg())
                        porcent = (self.robo_vida / 100)
                        self.vida = max(0, self.vida + int(
                            enemigo.tabla_tipos(self.calc_dmg(), enemigo.element) * porcent))
                        self.tiempo_ultimo_ataque = pygame.time.get_ticks()

        # Después del bucle, actualiza el estado de self.attacking para que dure el tiempo deseado
        current_time = pygame.time.get_ticks()
        if self.attacking and (current_time - self.attack_animation_start_time) >= self.attack_animation_duration:
            self.attacking = False

    def recibir_dano(self, cantidad, elemento_enemigo="neutro"):
        if self.vida > 0:
            self.vida = max(0, int(self.vida - self.tabla_tipos(cantidad, elemento_enemigo)))
            # print(f"{self} recibe daño")
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

        current_time = pygame.time.get_ticks()

        if self.attacking and (current_time - self.attack_animation_start_time) < self.attack_animation_duration:
            screen.blit(self.attacking_sprite,
                        (self.rect.x - (self.image.get_width() // 2), self.rect.y - self.image.get_width() // 2))
        elif self.focusing:
            screen.blit(self.focusing_sprite,
                        (self.rect.x - (self.image.get_width() // 2), self.rect.y - self.image.get_width() // 2))

    def update(self):
        if self.vida <= 0:
            self.morir()
        if self.vida > self.vida_maxima:
            self.vida = self.vida_maxima
        self.atacar()
