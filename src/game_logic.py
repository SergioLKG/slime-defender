# game_logic.py
import src.controls.mouse as mouseconf
import src.util.gameconf as conf
from src.entities.Group import Group
from src.ui import EffectsMenu
from src.util.WaveBuilder import WaveBuilder
from src.util.users import *


def load_image(directorio):
    try:
        return pygame.image.load(directorio)
    except FileNotFoundError:
        return pygame.image.load("assets/debug.png")


# Globals
mouse_pressed_last_frame = False  # Ultimo ckick
shop_coins: int = 0  # Monedas de la tienda
coin_img = load_image(directorio="assets/ui/general/coin.png")
aquafragments: int = 0  # Monedas en partida
wave_number: int = 1  # Wave actual
current_wave = None

# Mouse Variables
mouse_dmg = 5
mouse_cooldown = 2000
click_timer = 0
current_time = pygame.time.get_ticks()
elapsed_time = max(0, current_time - click_timer)


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

    # IMGS
    bg_img = cargar_fondo(screen, "assets/bg/fondo_atardecer.png")  # Fondo
    go_next = load_image("assets/ui/general/go_next.png")  # Botón next
    go_back = load_image("assets/ui/general/go_back.png")  # Botón back

    # Entities                               Menos el 20% del height
    player = Player((width // 2 - 70), (height // 2 - 40 + (height * 0.22)), (90, 90))
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
    interfaz_bg = pygame.transform.scale(pygame.image.load("assets/ui/general/general_bg.png"),
                                         size=((width // 2) - 60, height)).convert_alpha()  # Contenedor de la interfaz
    interfaz_rect = interfaz_bg.get_rect()
    padding = 5  # px
    interfaz_rect.inflate_ip(-padding * 2, -padding * 2)  # Ajustar para el padding
    EffectsMenu.load_ef_menu_img()

    def interface():
        global current_wave, wave_number, aquafragments
        screen.blit(interfaz_bg, interfaz_rect)  # Interfaz background

        screen.blit(pygame.transform.scale(coin_img, (30, 30)).convert_alpha(), (width // 2 - 44, 33))

        # Puntuación
        screen.blit(pygame.font.Font(None, 24).render(str(aquafragments), True,
                                                      (0, 0, 0)), (width // 2 - 10, 42))
        # Wave
        screen.blit(pygame.font.Font(None, 24).render("Wave " + str(wave_number), True,
                                                      (20, 0, 0)), (width - 90, 35))
        EffectsMenu.draw_eff_menu(screen, interfaz_rect, player)

        # GAME OVER
        if current_wave.is_completed():
            font = pygame.font.Font(None, 74).render(str("¡Enhorabuena ganaste!"), 1, (255, 255, 255))
            screen.blit(font, (
                (screen.get_width() // 2) - (font.get_width() // 2),
                (screen.get_height() // 2) - (font.get_height() // 2)))

            go_back_img = pygame.transform.scale(go_back, (80, 80)).convert_alpha()
            go_next_img = pygame.transform.scale(go_next, (80, 80)).convert_alpha()

            screen.blit(go_back_img, ((screen.get_width() // 2 - 40) - 60, screen.get_height() * 0.75 - 40))  # go_back
            screen.blit(go_next_img, ((screen.get_width() // 2 - 40) + 60, screen.get_height() * 0.75 - 40))  # go_next

            go_back_rect = pygame.Rect((screen.get_width() // 2 - 40) - 60, screen.get_height() * 0.75 - 40, 80, 80)
            go_next_rect = pygame.Rect((screen.get_width() // 2 - 40) + 60, screen.get_height() * 0.75 - 40, 80, 80)

            # Detectar clic en los botones
            mouse_pos = pygame.mouse.get_pos()
            mouse_click = pygame.mouse.get_pressed()[0]

            if mouse_click:  # Verificar si es un clic completo
                if go_back_rect.collidepoint(mouse_pos):  # Verifica si el clic fue en go_back
                    # Ir al menú
                    return True

                if go_next_rect.collidepoint(mouse_pos):  # Verifica si el clic fue en go_next
                    wave_number += 1
                    cd = max(1000, wave_config.get("enemy_cooldown") - (wave_number * 50))
                    new_wave_config = {
                        "num_enemies": calculate_num_enemies(),
                        "enemy_cooldown": cd,
                        "enemy_types": None
                    }
                    current_wave = WaveBuilder.build_wave(screen, allies, new_wave_config)
                    allies.set_enemies(current_wave.get_enemies())
                    return True  # Salir del bucle y comenzar la siguiente wave

            # Actualizar el estado del botón del ratón del ciclo anterior
            game_logic.mouse_pressed_last_frame = mouse_click

    # GAME OVER
    def game_over():
        if not player.alive():
            font = pygame.font.Font(None, 74).render(str("HAS PERDIDO"), 1, (230, 30, 230))
            screen.blit(font, (
                (screen.get_width() // 2) - (font.get_width() // 2),
                (screen.get_height() // 2) - (font.get_height() // 2)))

    # LOGICA
    def game_logic():
        global click_timer, current_time, elapsed_time, mouse_cooldown
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()[0]
        if mouse_pressed:
            for enemie in current_wave.get_enemies():
                if enemie.rect.collidepoint(mouse_pos):
                    if elapsed_time <= 0:
                        enemie.recibir_dano(mouse_dmg)
                        click_timer = mouse_cooldown

    def cd_mouse_bar():
        global click_timer, current_time, elapsed_time, mouse_cooldown
        for i in range(1):
            time_now = current_time
            i += 1
        if elapsed_time <= 0:
            x = custom_cursor.rect.left
            y = custom_cursor.rect.top + 10
            bg_bar = pygame.Rect(x, y, custom_cursor.rect.width, 5, )
            active_bar = pygame.Rect(x, y, custom_cursor.rect.width, 5)

            pygame.draw.rect(screen, (50, 50, 50), bg_bar)
            pygame.draw.rect(screen, (100, 100, 100), active_bar)

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
        if not player.alive():
            game_over()

        # Cursor
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
