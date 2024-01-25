# game_logic.py
import pygame.draw

import src.controls.mouse as mouseconf
import src.entities.Group
import src.util.gameconf as conf
from src.effects.BuffAttack import BuffAttack
from src.effects.BuffVida import BuffVida
from src.effects.RoboVida import RoboVida
from src.entities.enemies.Gota import Gota
from src.util.WaveBuilder import WaveBuilder
from src.util.users import *

# Globals
shop_coins: int = 0  # Monedas de la tienda
aquafragments: int = 0  # Monedas en partida


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

    clock = pygame.time.Clock()
    click_timer = 0

    # Entities                               Menos el 20% del height
    player = Player((width // 2 - 40), (height // 2 - 40 + (height * 0.22)), (80, 80))
    player.cargar_effects()
    player.vida = player.vida_maxima  # Curamos al player para que empiece con toda la vida

    allies = src.entities.Group.Group(screen)
    allies.add(player)

    # Waves
    wave_config = {"num_enemies": 4, "enemy_cooldown": 2000, "enemy_type": [Gota]}
    current_wave = WaveBuilder.build_wave(screen, allies, wave_config)
    allies.set_enemies(current_wave.get_enemies())

    # Interfaz
    interfaz_rect = pygame.Rect(0, 0, (width // 2) - 40, height)  # Contenedor de la interfaz
    padding = 5  # px
    interfaz_rect.inflate_ip(-padding * 2, -padding * 2)  # Ajustar para el padding

    def interface():
        global aquafragments
        pygame.draw.rect(screen, (200, 100, 100), interfaz_rect)  # Interfaz background

        # --------------------- EFFECTS ---------------------
        # ########### BuffVida ###########
        tier_actual_buff_vida = 0
        for effect in player.effects:
            if isinstance(effect, BuffVida):
                tier_actual_buff_vida = effect.tier

        precio_buff_vida = BuffVida(tier_actual_buff_vida + 1).precio
        color_bv_btn = (100, 255, 100)
        if aquafragments < precio_buff_vida:
            color_bv_btn = (220, 50, 50)

        boton_buff_vida_rect = pygame.Rect(interfaz_rect.left + 20, interfaz_rect.top + 50, 160, 40)
        pygame.draw.rect(screen, color_bv_btn, boton_buff_vida_rect)  # Color verde para el botón

        texto_boton_buff_vida = pygame.font.Font(None, 24).render(f"+Health - {precio_buff_vida} AF", True,
                                                                  (0, 0, 0))
        screen.blit(texto_boton_buff_vida, (boton_buff_vida_rect.left + 10, boton_buff_vida_rect.top + 10))
        # #################################

        # ########### BuffAttack ###########
        tier_actual_buff_dano = 0
        for effect in player.effects:
            if isinstance(effect, BuffAttack):
                tier_actual_buff_dano = effect.tier

        precio_buff_dano = BuffAttack(tier_actual_buff_dano + 1).precio
        color_ba_btn = (100, 255, 100)
        if aquafragments < precio_buff_dano:
            color_ba_btn = (220, 50, 50)

        boton_buff_dano_rect = pygame.Rect(interfaz_rect.left + 20, interfaz_rect.top + 100, 160, 40)
        pygame.draw.rect(screen, color_ba_btn, boton_buff_dano_rect)

        texto_boton_buff_dano = pygame.font.Font(None, 24).render(f"+Attack - {precio_buff_dano} AF", True,
                                                                  (0, 0, 0))
        screen.blit(texto_boton_buff_dano, (boton_buff_dano_rect.left + 10, boton_buff_dano_rect.top + 10))
        # #################################

        # ########### RoboVida ###########
        tier_actual_robo_vida = 0
        for effect in player.effects:
            if isinstance(effect, RoboVida):
                tier_actual_robo_vida = effect.tier

        precio_robo_vida = RoboVida(tier_actual_robo_vida + 1).precio

        color_rv_btn = (100, 255, 100)
        if aquafragments < precio_buff_dano:
            color_rv_btn = (220, 50, 50)

        boton_robo_vida_rect = pygame.Rect(interfaz_rect.left + 20, interfaz_rect.top + 150, 160, 40)
        pygame.draw.rect(screen, color_rv_btn, boton_robo_vida_rect)

        texto_boton_robo_vida = pygame.font.Font(None, 24).render(f"+LifeSteal - {precio_robo_vida} AF",
                                                                  True,
                                                                  (0, 0, 0))
        screen.blit(texto_boton_robo_vida, (boton_robo_vida_rect.left + 10, boton_robo_vida_rect.top + 10))
        # #################################

        # Puntuación
        screen.blit(pygame.font.Font(None, 24).render("AquaFragments: " + str(aquafragments), True,
                                                      (0, 0, 0)), (10, 10))

        # Detectar clic en botones
        if pygame.mouse.get_pressed()[0]:  # Botón izquierdo del ratón
            mouse_pos = pygame.mouse.get_pos()
            if boton_buff_vida_rect.collidepoint(mouse_pos):
                if aquafragments >= precio_buff_vida:  # Costo del BuffVida
                    player.add_effect(BuffVida(tier_actual_buff_vida + 1))
                    player.cargar_effects()
                    aquafragments -= precio_buff_vida
            elif boton_buff_dano_rect.collidepoint(mouse_pos):
                if aquafragments >= precio_buff_dano:  # Costo del BuffVida
                    player.add_effect(BuffAttack(tier_actual_buff_dano + 1))
                    player.cargar_effects()
                    aquafragments -= precio_buff_dano
                pass
            elif boton_robo_vida_rect.collidepoint(mouse_pos):
                if aquafragments >= precio_robo_vida:  # Costo del BuffVida
                    player.add_effect(RoboVida(tier_actual_robo_vida + 1))
                    player.cargar_effects()
                    aquafragments -= precio_robo_vida
                pass
            # --------------------- EFFECTS END ---------------------

        # GAME OVER
        if current_wave.is_completed():
            # Ganaste o lo que sea
            font = pygame.font.Font(None, 74).render(str("¡Enhorabuena ganaste!"), 1, (255, 255, 255))
            screen.blit(font, (
                (screen.get_width() // 2) - (font.get_width() // 2),
                (screen.get_height() // 2) - (font.get_height() // 2)))

    # LOGICA
    def game_logic():
        pass

    # Bucle del JUEGO
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

        # Interfaz
        interface()  # Toda la interfaz

        # Cursor
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
