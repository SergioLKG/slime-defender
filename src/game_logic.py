# game_logic.py

import src.controls.mouse as mouseconf
import src.entities.Group
import src.util.gameconf as conf
from src.entities.enemies.Gota import Gota
from src.util.WaveBuilder import WaveBuilder
from src.util.users import *


def start_game():
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
    shop_coins: int = 0  # Monedas de la tienda

    clock = pygame.time.Clock()
    click_timer = 0

    # Entities                               Menos el 20% del height
    player = Player((width // 2 - 40), (height // 2 - 40 + (height * 0.22)), (80, 80))
    allies = src.entities.Group.Group(screen)
    allies.add(player)

    # Waves
    wave_config = {"num_enemies": 4, "enemy_cooldown": 2000, "enemy_type": [Gota]}
    current_wave = WaveBuilder.build_wave(screen, allies, wave_config)
    allies.set_enemies(current_wave.get_enemies())

    # LOGICA
    def game_logic():
        if current_wave.is_completed():
            # Ganaste o lo que sea
            screen.blit(
                (pygame.font.Font(None, 74).render(str("¡Enhorabuena ganaste!"), 1, (255, 255, 255), (0, 0, 0))),
                (screen.get_width() // 2, screen.get_height() // 2))

    #  Bucle del JUEGO
    running = True
    while running:
        running = not handle_events()  # Eventos registrados del programa
        screen.fill((255, 255, 255))  # Color del fondo
        cargar_bg(screen, "assets/bg/fondo_atardecer.png")  # Fondo
        # ---- LOGICA
        game_logic()
        # ---- LOGICA
        # Dibujar y actualizar sprites
        allies.draw(screen)  # Player, estructuras aliadas etc
        allies.update()
        current_wave.draw()  # Enemies Wave
        current_wave.update()
        custom_cursor.update()  # Cursor pointer
        custom_cursor.draw()

        pygame.display.flip()  # Actualizar pantalla
        clock.tick(60)  # Felocidad de fotogramas


def cargar_bg(screen, path):
    try:
        bg_img = pygame.image.load(path)
        bg_img = pygame.transform.scale(bg_img, (screen.get_width(), screen.get_height()))
        screen.blit(bg_img, (0, 0))
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
