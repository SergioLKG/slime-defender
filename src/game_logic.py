# game_logic.py
import pygame  # 2.5.2v
import src.util.gameconf as conf
import src.controls.mouse as mouseconf


def start_game():
    # PYGAME CONFIG
    pygame.display.set_caption("Slime Defender: Aqua phobia")  # App Name
    conf.importconfigs()  # Import configs
    screen = conf.__sizescreen__()  # Screen declaration
    custom_cursor = mouseconf.Cursor()

    # CONTROLS

    # MOUSE
    pygame.mouse.set_visible(0)
    mouse_pos = pygame.mouse.get_pos()  # Almacena la posición del mouse (x,y)
    mouse_x = mouse_pos[0]  # Mouse_pos x
    mouse_y = mouse_pos[1]  # Mouse_pos y

    # KEYBOARD

    clock = pygame.time.Clock()

    def game_logic():
        pass

    # Bucle del juego
    running = True
    while running:
        running = not handle_events()  # Eventos registrados del programa


        # ---- LOGICA
        game_logic()
        # ---- LOGICA

        screen.fill((200, 255, 200))  # Color del fondo
        custom_cursor.update()
        custom_cursor.draw()

        pygame.display.flip()  # Actualizar pantalla
        clock.tick(60)  # Felocidad de fotogramas
    pygame.quit()
    quit()


def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True  # Salir del bucle
    return False


if __name__ == "__main__":
    pygame.init()
    start_game()
