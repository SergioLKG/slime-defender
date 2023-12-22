# menu.py
import pygame
import os

# Colores
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)

class Slime(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path("slime.png"))  # Ajusta la ruta según la ubicación de tu imagen
        self.rect = self.image.get_rect()
        self.rect.x = 600
        self.rect.y = 250

def show_menu(screen):
    running = True
    slime = Slime()

    while running:
        screen.fill(WHITE)  # Fondo blanco (puedes personalizarlo)
        draw_menu(screen, slime)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                handle_menu_click(event.pos, slime)
    running = True

    while running:
        screen.fill(WHITE)  # Fondo blanco (puedes personalizarlo)
        draw_menu(screen)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                handle_menu_click(event.pos)
                # Agrega más lógica de clic aquí según sea necesario.

def draw_menu(screen):
    draw_aside(screen)

def draw_aside(screen):
    aside_width = 200
    aside_height = 600

    # Aside
    pygame.draw.rect(screen, GRAY, (0, 0, aside_width, aside_height))

    # Botón de Salir/Volver Atrás
    draw_button(screen, BLACK, (10, 10, 40, 40), "Salir")

    # Engranaje de Opciones
    draw_button(screen, BLACK, (aside_width - 50, 10, 40, 40), "Opciones")

    # Menús
    menu_names = ["Jugar", "Tienda", "Inventario"]
    menu_height = aside_height // len(menu_names)

    for i, menu_name in enumerate(menu_names):
        draw_button(screen, BLACK, (10, 60 + i * menu_height, aside_width - 20, menu_height), menu_name)

def draw_button(screen, color, rect, text):
    pygame.draw.rect(screen, color, rect)
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=(rect[0] + rect[2] // 2, rect[1] + rect[3] // 2))
    screen.blit(text_surface, text_rect)

def handle_menu_click(pos):
    # Maneja los clics en el menú.
    # Puedes agregar más lógica aquí según sea necesario.
    pass