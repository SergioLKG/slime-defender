# game_logic.py
import pygame  # 2.5.2v

import src.ui.user_input as user_input
import src.ui.gameover_menu as gameover_menu
import src.ui.game_menu as game_menu
import src.util.gameconf as conf
from src.util.users import *
import src.controls.mouse as mouseconf


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
    pygame.mouse.set_visible(0) # Mouse Disable (Usando Custom -> controls\mouse.py)
    ##############################
    # user: Usuario = user_input.open()
    shop_coins: int = 0 # Monedas de la tienda

    clock = pygame.time.Clock()
    click_timer = 0

    # LOGICA
    def game_logic():
         
        pass

    #  Bucle del JUEGO
    running = True
    while running:
        running = not handle_events()  # Eventos registrados del programa
      
        # ---- LOGICA
        game_logic()
    
        # ---- LOGICA

        screen.fill((200, 255, 200, 0))  # Color del fondo
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
        # EXIT
        if event.type == pygame.QUIT:
            return True  # Salir del bucle  
        
    return False


if __name__ == "__main__":
    pygame.init()
    start_game()
