# game_logic.py
import pygame.draw

import src.controls.mouse as mouseconf
import src.util.gameconf as conf
from src.entities.Group import Group
from src.ui.EffectsMenu import draw_eff_menu
from src.util.WaveBuilder import WaveBuilder
from src.util.users import *

# Globals
shop_coins: int = 0  # Monedas de la tienda
aquafragments: int = 0  # Monedas en partida
wave_number: int = 1  # Wave actual
current_wave = None


def calculate_num_enemies():
    # Ajusta esta lógica según tus necesidades
    base_num_enemies = 4  # Número base de enemigos
    enemies_per_wave = 2  # Aumento en el número de enemigos por cada wave

    num_enemies = base_num_enemies + (wave_number - 1) * enemies_per_wave
    return num_enemies


def start_game():
    global current_wave
    global shop_coins
    global aquafragments
    global wave_number
    ##############################
    # PYGAME CONFIG
    pygame.display.set_caption("Slime Defender: Aqua phobia")  # App Name
    conf.importconfigs()  # Import configs
    width = conf.width
    height = conf.height
    screen = conf.__sizescreen__()  # Screen declaration
    custom_cursor = mouseconf.Cursor()

    # MOUSE
    pygame.mouse.set_visible(0)  # Mouse Disable (Usando Custom -> controls\mouse.py)
    ##############################
    # user: Usuario = user_input.open()

    clock = pygame.time.Clock()

    click_timer = 0
    current_time = pygame.time.get_ticks()
    elapsed_time = current_time - click_timer

    # IMGS
    bg_img = cargar_imagen(screen, "assets/bg/fondo_atardecer.png")  # Fondo

    # Entities                               Menos el 20% del height
    player = Player((width // 2 - 40), (height // 2 - 40 + (height * 0.22)), (80, 80))
    player.cargar_effects()
    player.vida = player.vida_maxima  # Curamos al player para que empiece con toda la vida

    allies = Group(screen)
    allies.add(player)

    # Waves
    wave_config = {
        "num_enemies": calculate_num_enemies(),
        "enemy_cooldown": 2000,
        "enemy_types": None
    }
    current_wave = WaveBuilder.build_wave(screen, allies, wave_config)
    allies.set_enemies(current_wave.get_enemies())

    # Interfaz
    interfaz_rect = pygame.Rect(0, 0, (width // 2) - 40, height)  # Contenedor de la interfaz
    padding = 5  # px
    interfaz_rect.inflate_ip(-padding * 2, -padding * 2)  # Ajustar para el padding

    def interface():
        global wave_number
        global current_wave
        pygame.draw.rect(screen, (200, 100, 100), interfaz_rect)  # Interfaz background

        draw_eff_menu(screen, interfaz_rect, aquafragments, player)

        # GAME OVER
        if current_wave.is_completed():
            font = pygame.font.Font(None, 74).render(str("¡Enhorabuena ganaste!"), 1, (255, 255, 255))
            screen.blit(font, (
                (screen.get_width() // 2) - (font.get_width() // 2),
                (screen.get_height() // 2) - (font.get_height() // 2)))

            go_back = pygame.Rect((screen.get_width() // 2 - 40) - 60, (screen.get_height() * 0.75 - 40), 80, 80)
            go_next = pygame.Rect((screen.get_width() // 2 - 40) + 60, (screen.get_height() * 0.75 - 40), 80, 80)

            pygame.draw.rect(screen, (220, 50, 50), go_back)
            pygame.draw.rect(screen, (50, 220, 50), go_next)

            # Detectar clic en los botones
            mouse_pos = pygame.mouse.get_pos()
            mouse_click = pygame.mouse.get_pressed()

            if go_back.collidepoint(mouse_pos) and mouse_click[0]:
                # Ir al menu
                pass

            if go_next.collidepoint(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed()[0]:  # Botón izquierdo del ratón
                    wave_number += 1
                    new_wave_config = {
                        "num_enemies": calculate_num_enemies(),
                        "enemy_cooldown": 2000,
                        "enemy_types": None
                    }
                    current_wave = WaveBuilder.build_wave(screen, allies, new_wave_config)
                    allies.set_enemies(current_wave.get_enemies())
                    return True  # Salir del bucle y comenzar la siguiente wave

    # LOGICA
    def game_logic():
        pass

    # Bucle del JUEGO
    running = True
    while running:
        running = not handle_events()  # Eventos registrados del programa
        screen.fill((255, 255, 255))  # Color del fondo
        screen.blit(bg_img, (0, 0))

        # ---- LOGICA
        game_logic()
        # ---- LOGICA

        # Dibujar y actualizar sprites
        allies.draw(screen)  # Player, estructuras aliadas etc
        allies.update()
        if not current_wave.is_completed():
            current_wave.draw()  # Enemies Wave
            current_wave.update()

        # Interfaz
        interface()  # Toda la interfaz

        # Cursor
        custom_cursor.update()  # Cursor pointer
        custom_cursor.draw()
        pygame.display.update()  # Actualizar pantalla, mejor rendimiento que .flip()
        clock.tick(60)  # Felocidad de fotogramas


def cargar_imagen(screen, path):
    try:
        bg_img = pygame.image.load(path)
        bg_img = pygame.transform.scale(bg_img, (screen.get_width(), screen.get_height()))
        return bg_img
    except FileNotFoundError:
        print("\n\tArchivo no encontrado")
        exit()


def handle_events():  # Eventes & Updater
    for event in pygame.event.get():
        # EXIT
        if event.type == pygame.QUIT:
            return True  # Salir del bucle  

    return False


if __name__ == "__main__":
    pygame.init()
    start_game()
    pygame.quit()
