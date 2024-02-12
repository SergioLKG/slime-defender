# game_logic.py
import math

import src.controls.mouse as mouseconf
import src.util.gameconf as conf
from src.entities.Group import Group
from src.ui import EffectsMenu, MouseEffects
from src.util.WaveBuilder import WaveBuilder
from src.util.users import *


def load_image(directorio):
    try:
        return pygame.image.load(directorio)
    except FileNotFoundError:
        return pygame.image.load("assets/debug.png")


# Globals
shop_coins: int = 0  # Monedas de la tienda
coin_img = load_image(directorio="assets/ui/general/coin.png")
aquafragments: int = 0  # Monedas en partida
wave_number: int = 1  # Wave actual
current_wave = None
multiplier = 1  # Aumento en el número de enemigos por cada wave

# Mouse Variables
mouse_pressed_last_frame = False  # Ultimo ckick
tier_dmg_buff = 0
tier_cd_buff = 0
mouse_dmg = 5
mouse_cooldown = 5000


def calc_mouse_buff(n: [0 - 1]):
    global tier_dmg_buff, tier_cd_buff, mouse_dmg, mouse_cooldown
    limite_dmg = 100
    limite_cd = 20
    if n == 0:  # dmg buff
        if tier_dmg_buff != limite_dmg:
            mouse_dmg = math.ceil(0.75 * (1.1 ** tier_dmg_buff))
            tier_dmg_buff += 1
        else:
            print("Error")
    elif n == 1:  # cd buff
        if tier_cd_buff != limite_cd:
            mouse_cooldown = math.ceil(37 * math.log(1.2 * (1.4 ** tier_cd_buff), 2))
            tier_cd_buff += 1
        else:
            print("Error")
    else:
        print("Error")


last_click = -5000


def calculate_num_enemies():
    global multiplier
    if wave_number % 20 == 0:
        multiplier += 1
    num_enemies = math.ceil((5 * (wave_number / 2)) / multiplier)

    return num_enemies


def start_game():
    global current_wave
    global shop_coins
    global aquafragments
    global wave_number
    ##############################
    # PYGAME CONFIG
    pygame.display.set_caption("Slime Defender: Aqua phobia")  # App Name
    pygame.display.set_icon(pygame.image.load("assets/icon.png"))
    conf.importconfigs()  # Import configs
    width = conf.width
    height = conf.height
    screen = conf.__sizescreen__()  # Screen declaration
    custom_cursor = mouseconf.Cursor()

    # MOUSE
    pygame.mouse.set_visible(0)  # Mouse Disable (Usando Custom -> controls\mouse.py)

    clock = pygame.time.Clock()

    # IMGS
    bg_img = cargar_fondo(screen, "assets/bg/fondo_atardecer.png")  # Fondo
    bg_night = cargar_fondo(screen, "assets/bg/fondo_noche.png")  # Fondo noche
    bg_day = cargar_fondo(screen, "assets/bg/fondo_noche.png")  # Fondo día
    game_over_img = load_image("assets/ui/general/gameover.png")  # Game Over
    go_next = load_image("assets/ui/general/go_next.png")  # Botón next
    go_back = load_image("assets/ui/general/home.png")  # Botón back

    # Entities                               Menos el 20% del height
    player = Player((width // 2), (height // 2 + (height * 0.22)), (90, 90))
    player.vida = player.vida_maxima  # Curamos al player para que empiece con toda la vida

    allies = Group(screen)
    allies.add(player)

    new_wave_config = {
        "num_enemies": calculate_num_enemies(),
        "enemy_cooldown": 2000,
        "enemy_types": None
    }
    current_wave = WaveBuilder.build_wave(screen, allies, new_wave_config)
    allies.set_enemies(current_wave.get_enemies())

    # Interfaz
    interfaz_bg = pygame.transform.scale(pygame.image.load("assets/ui/general/general_bg.png"),
                                         size=((width // 2) - 60, height)).convert_alpha()  # Contenedor de la interfaz
    interfaz_rect = interfaz_bg.get_rect()
    padding = 5  # px
    interfaz_rect.inflate_ip(-padding * 2, -padding * 2)  # Ajustar para el padding
    EffectsMenu.load_ef_menu_img()
    MouseEffects.load_ef_menu_img()

    # START GAME
    # user: Usuario = GameMenu.getUser() # User info

    # GAME OVER
    def game_over():
        if not player.alive():
            go_back_img = pygame.transform.scale(go_back, (80, 80)).convert_alpha()
            aux = pygame.transform.scale(game_over_img, (400, 250)).convert_alpha()
            screen.blit(aux, (
                (screen.get_width() // 2) - (aux.get_width() // 2),
                (screen.get_height() // 2) - (aux.get_height() // 2) - (go_back_img.get_height() // 2)))
            screen.blit(go_back_img,
                        ((screen.get_width() // 2) - (go_back_img.get_width() // 2),
                         screen.get_height() // 2 + (aux.get_height() // 2)))

            mouse_pos = pygame.mouse.get_pos()
            mouse_press = pygame.mouse.get_pressed()[0]

            if mouse_press:
                if go_back_img.get_rect().collidepoint(mouse_pos):
                    quit(True)

    # LOGICA
    def game_logic():
        handle_mouse_click()

    def handle_mouse_click():
        global last_click
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()[0]

        if mouse_pressed:
            current_time = pygame.time.get_ticks()
            elapsed_time = current_time - last_click

            if elapsed_time >= mouse_cooldown:
                for enemie in current_wave.get_enemies():
                    if enemie.rect.collidepoint(mouse_pos):
                        enemie.recibir_dano(mouse_dmg)
                        last_click = current_time
                        # print(f"Last hit: {last_click}")
                        break

    def cd_mouse_bar():
        global mouse_cooldown, last_click

        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - last_click

        if elapsed_time <= mouse_cooldown:
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]

            remaining_time = mouse_cooldown - elapsed_time
            percentage_complete = remaining_time / mouse_cooldown

            bg_bar = pygame.Rect(x, y + 32, custom_cursor.rect.width, 5)
            active_bar_width = int(custom_cursor.rect.width * percentage_complete)
            active_bar = pygame.Rect(x, y + 32, active_bar_width, 5)

            pygame.draw.rect(screen, (50, 50, 50), bg_bar)
            pygame.draw.rect(screen, (180, 180, 120), active_bar)

    def interface():
        global current_wave, wave_number, aquafragments

        # Detectar clic en los botones
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()[0]

        screen.blit(interfaz_bg, interfaz_rect)  # Interfaz background

        screen.blit(pygame.transform.scale(coin_img, (30, 30)).convert_alpha(), (width // 2 - 44, 33))

        # Puntuación
        screen.blit(pygame.font.Font(None, 24).render(str(aquafragments), True,
                                                      (0, 0, 0)), (width // 2 - 10, 42))
        # Wave
        screen.blit(pygame.font.Font(None, 24).render("Wave " + str(wave_number), True,
                                                      (20, 0, 0)), (width - 90, 35))
        EffectsMenu.draw_eff_menu(screen, interfaz_rect, player)
        MouseEffects.draw_eff_menu(screen, interfaz_rect)

        go_back_img = pygame.transform.scale(go_back, (45, 45)).convert_alpha()
        go_back_rect = pygame.Rect((screen.get_width() // 2 - 40) - 60, screen.get_height() * 0.75 - 40, 80, 80)

        screen.blit(go_back_img, ((interfaz_rect.left + 20), interfaz_rect.top + 30))  # go_back

        if go_back_rect.collidepoint(mouse_pos):  # Verifica si el clic fue en go_back
            # Ir al menú
            return True

        # WAVE COMPLETE
        if current_wave.is_completed():

            go_next_img = pygame.transform.scale(go_next, (80, 80)).convert_alpha()

            screen.blit(go_next_img, ((screen.get_width() - go_next_img.get_width() - 30),
                                      screen.get_height() - go_next_img.get_height() - 20))  # go_next

            go_next_rect = pygame.Rect(screen.get_width() - go_next_img.get_width() - 30,
                                       screen.get_height() - go_next_img.get_height() - 20, 80, 80)

            font = pygame.font.Font(None, 24).render(str("Wave Complete"), 1, (20, 250, 20))
            screen.blit(font, (go_next_rect.left - 20,
                               go_next_rect.top - 20))

            if mouse_click:  # Verificar si es un clic completo
                if go_next_rect.collidepoint(mouse_pos):  # Verifica si el clic fue en go_next
                    wave_number += 1
                    wave_config = {
                        "num_enemies": calculate_num_enemies(),
                        "enemy_cooldown": 2000,
                        "enemy_types": None
                    }
                    current_wave = WaveBuilder.build_wave(screen, allies, wave_config)
                    allies.set_enemies(current_wave.get_enemies())
                    return True  # Salir del bucle y comenzar la siguiente wave

            # Actualizar el estado del botón del ratón del ciclo anterior
            game_logic.mouse_pressed_last_frame = mouse_click

    # Bucle del JUEGO
    running = True
    while running:
        running = not handle_events()  # Eventos registrados del programa
        screen.fill((255, 255, 255))  # Color del fondo
        screen.blit(bg_img, (0, 0))

        # Dibujar y actualizar sprites
        allies.draw(screen)  # Player, estructuras aliadas etc
        allies.update()
        if not current_wave.is_completed():
            current_wave.draw()  # Enemies Wave
            current_wave.update()

        # Interfaz
        interface()  # Toda la interfaz
        if not player.alive():
            game_over()

        # ---- LOGICA
        game_logic()
        # ---- LOGICA

        # Cursor
        cd_mouse_bar()
        custom_cursor.update()  # Cursor pointer
        custom_cursor.draw()
        pygame.display.update()  # Actualizar pantalla, mejor rendimiento que .flip()
        clock.tick(60)  # Felocidad de fotogramas


def cargar_fondo(screen, path):
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
