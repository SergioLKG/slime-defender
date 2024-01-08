# game_logic.py
import this

import pygame  # 2.5.2v
import src.util.gameconf as conf
import src.controls.mouse as mouseconf
import src.controls.keys as keysconf


def __init__():
    pass


def start_game():
    ##############################
    # PYGAME CONFIG
    pygame.display.set_caption("Slime Defender: Aqua phobia")  # App Name
    conf.importconfigs()  # Import configs
    screen = conf.__sizescreen__()  # Screen declaration
    custom_cursor = mouseconf.Cursor()

    # MOUSE
    pygame.mouse.set_visible(0)
    ##############################
    # CONSTANTES
    SHOP_COINS: int = 0  # Monedas de la tienda
    INGAME_COINS: int = 0  # AQUAFRAGMENTS

    # VARIABLESS
    slime_size = 50  # Tamaño del slime
    slime_position = [50, conf.height // 2 - slime_size // 2]  # Posición del slime
    slime_health = 100  # Vida Slime
    enemies = []  # Variable de enemigos en pantalla
    max_click_rate = 5  # Maximo de clicks por segundo

    clock = pygame.time.Clock()
    click_timer = 0

    # LOGICA
    def game_logic():

        pass

    #  Bucle del JUEGO
    running = True
    while running:
        running = not handle_events()  # Eventos registrados del programa
        # MOUSE
        mouse_pos = pygame.mouse.get_pos()  # Almacena la posición del mouse (x,y)
        mouse_x = mouse_pos[0]  # Mouse_pos x
        mouse_y = mouse_pos[1]  # Mouse_pos y

        # ---- LOGICA
        game_logic()
        # ---- LOGICA

        screen.fill((200, 255, 200))  # Color del fondo
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


def handle_events():  # Eventes & Updater
    for event in pygame.event.get():

        # KEYBOARD
        keysconf.keycontrols(this, event)

        # EXIT
        if event.type == pygame.QUIT:
            return True  # Salir del bucle
    return False


if __name__ == "__main__":
    pygame.init()
    start_game()
