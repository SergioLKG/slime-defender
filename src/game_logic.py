# game_logic.py
import random

import src.controls.mouse as mouseconf
import src.entities.Group
import src.util.gameconf as conf
from src.entities.enemies.Gota import Gota
from src.util.users import *

# GLOBALS
# ENEMIES
enemy_cooldown = 2000  # en milisegundos (2 segundos)
current_time = pygame.time.get_ticks()
next_enemy_time = current_time + enemy_cooldown
generados = 0


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
    enemies = src.entities.Group.Group(screen)

    # LOGICA
    def game_logic():
        global generados
        if generados < 4:
            global next_enemy_time

            player.set_enemies(enemies)  # Decirle a player quienes son sus enemigos.

            current_time = pygame.time.get_ticks()
            r_height = random.Random.uniform(random.Random(), 0.21, 0.25)  # Altura aleatoria

            # Crear un nuevo enemigo si ha pasado suficiente tiempo desde el último
            if current_time > next_enemy_time:
                enemy = Gota((width + 100), (height // 2 + (height * r_height)), allies)
                enemies.add(enemy)
                generados += 1

                # Actualizar el tiempo para el próximo enemigo
                next_enemy_time = current_time + enemy_cooldown
        elif len(enemies) <= 0:
            txt_size = 47
            ganaste_txt = (pygame.font.Font(None, txt_size)
                           .render("ENHORABUENA HAS GANADO", True, (250, 250, 250), (0, 0, 0)))
            screen.blit(ganaste_txt, (screen.get_width() // 2 - ganaste_txt.get_width() // 2, screen.get_height() // 2))

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
        if len(enemies) > 0:  # Dibuja los enemigos, si hay
            enemies.draw(screen)
            enemies.update()
        custom_cursor.update()
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
