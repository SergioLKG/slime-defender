# game_logic.py

import src.controls.mouse as mouseconf
import src.util.gameconf as conf
from src.entities.enemies.Gota import Gota
from src.util.users import *


def __init__():
    pass


# GLOBALS
# ENEMIES
enemy_cooldown = 2000  # en milisegundos (2 segundos)
current_time = pygame.time.get_ticks()
next_enemy_time = current_time + enemy_cooldown


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
    player = Player((width // 2), (height // 2 + (height * 0.2)), (80, 80))
    enemies = pygame.sprite.Group()
    enemy1 = Gota((width + 150), (height // 2 + (height * 0.2)), player)
    enemy2 = Gota((width + 150), (height // 2 + (height * 0.2)), player)
    enemies.add(enemy1, enemy2)

    # LOGICA
    def game_logic():
        global next_enemy_time
        current_time = pygame.time.get_ticks()

        # Crear un nuevo enemigo si ha pasado suficiente tiempo desde el último
        if current_time > next_enemy_time:
            enemy = Gota((width + 150), (height // 2 + (height * 0.2)), player)
            enemies.add(enemy)

            # Actualizar el tiempo para el próximo enemigo
            next_enemy_time = current_time + enemy_cooldown

        # Dibujar y actualizar enemigos
        enemies.draw(screen)
        enemies.update()

    #  Bucle del JUEGO
    running = True
    while running:
        running = not handle_events()  # Eventos registrados del programa
        screen.fill((255, 255, 255))  # Color del fondo
        cargar_bg(screen, "assets/bg/fondo_atardecer.png")  # Fondo
        # ---- LOGICA
        game_logic()
        # ---- LOGICA
        player.draw(screen)
        player.update()
        custom_cursor.update()
        custom_cursor.draw()

        pygame.display.flip()  # Actualizar pantalla
        clock.tick(60)  # Felocidad de fotogramas


def click():  # Lo que ocurre al hacer click
    sumacoins = 5
    ''' 
    if modificador:
        INGAME_COINS += 20
    if modificador2:
        INGAME_COINS += sumacoins * 2
    else:
        INGAME_COINS += sumacoins
    :return:
    '''
    pass


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
