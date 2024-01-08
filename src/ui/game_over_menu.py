import pygame
import sys
import time
import json


class GameOverMenu:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.font = pygame.font.Font(None, 36)
        self.recompensas = {"Aquafragments": 100, "Experiencia": 50}  # Ejemplo de recompensas

    def cargar_traducciones(self):
        try:
            with open(f"lang/{self.lang}.json", "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Archivo de traducción no encontrado para el idioma {self.lang}.")
            return {}

    def mostrar_menu(self, screen):
        self.mostrar_recompensas(screen)

        # Esperar unos segundos antes de mostrar el botón "Continuar"
        time.sleep(3)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.gestionar_eventos(event)

            # Dibujar fondo
            screen.fill((0, 0, 0))

            # Dibujar opciones
            continue_text = self.font.render("Continuar", True, (255, 255, 255))
            screen.blit(continue_text, ((self.width - continue_text.get_width()) // 2, 250))

            pygame.display.flip()

    def mostrar_recompensas(self, screen):
        # Dibujar fondo
        screen.fill((0, 0, 0))

        # Dibujar texto de recompensas
        recompensas_text = self.font.render("", True, (255, 255, 255))
        screen.blit(recompensas_text, ((self.width - recompensas_text.get_width()) // 2, 100))

        # Dibujar recompensas obtenidas
        y_position = 150
        for recompensa, cantidad in self.recompensas.items():
            texto_recompensa = f"{recompensa}: {cantidad}"
            recompensa_text = self.font.render(texto_recompensa, True, (255, 255, 255))
            screen.blit(recompensa_text, ((self.width - recompensa_text.get_width()) // 2, y_position))
            y_position += self.font.get_height()

        pygame.display.flip()

    def gestionar_eventos(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Comprobar clic en "Continuar"
            if 250 <= mouse_y <= 250 + self.font.get_height():
                pygame.quit()
                sys.exit()


# Uso del menú de Game Over
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

game_over_menu = GameOverMenu(WIDTH, HEIGHT)
game_over_menu.mostrar_menu(screen)
