from src import game_logic
from src.effects.BuffAttack import BuffAttack
from src.effects.BuffVida import BuffVida
import pygame

from src.effects.RoboVida import RoboVida

# img_buff_vida = load_image()
# img_buff_dano = load_image()
# img_robo_vida = load_image()
# img_marco_ef = load_image()
img_boton_on = None
img_boton_off = None


def load_image(nombre, size):
    try:
        return pygame.transform.scale(pygame.image.load(f"assets/ui/general/{nombre}"),
                                      size=size).convert_alpha()
    except FileNotFoundError:
        return pygame.transform.scale(pygame.image.load("assets/debug.png"), size=size).convert_alpha()


def load_ef_menu_img():
    global img_boton_on, img_boton_off
    # img_buff_vida = load_image()
    # img_buff_dano = load_image()
    # img_robo_vida = load_image()
    img_boton_on = load_image("btn_bg.png", (160, 40))
    img_boton_off = load_image("btn_bg_disable.png", (160, 40))
    # img_marco_ef = load_image()


def draw_eff_menu(screen, interfaz_rect, player):
    global img_boton_off, img_boton_on
    aquafragments = game_logic.aquafragments

    top = interfaz_rect.top + 70
    left = interfaz_rect.left + 20
    # -------------------- TITLE -----------------------
    bg_eff = pygame.Rect(left, top + 10, interfaz_rect.w - 30, 200)  # TODO Meter trasparencia.
    pygame.draw.rect(screen, (160, 140, 120), bg_eff)
    screen.blit(pygame.font.Font(None, 30).render(f"Slime Buffs", True, (0, 0, 0)), (left + 10, top + 20))
    # --------------------- EFFECTS ---------------------
    margin_left_ef = 25
    # ########### BuffVida ###########
    tier_actual_buff_vida = 0
    for effect in player.effects:
        if isinstance(effect, BuffVida):
            tier_actual_buff_vida = effect.tier

    precio_buff_vida = BuffVida(tier_actual_buff_vida).precio

    screen.blit(img_boton_on, (left + margin_left_ef, top + 50))
    if aquafragments < precio_buff_vida:
        screen.blit(img_boton_off, (left + margin_left_ef, top + 50))

    texto_boton_buff_vida = pygame.font.Font(None, 24).render(f" + Health", True,
                                                              (0, 0, 0))
    info_txt_buff_vida = pygame.font.Font(None, 20).render(
        f"{precio_buff_vida} AF | +{(BuffVida(tier_actual_buff_vida).calculate(player.vida_maxima))} HP", True,
        (0, 0, 0))

    boton_buff_vida_rect = pygame.Rect(left + margin_left_ef, top + 50, 160, 40)

    screen.blit(info_txt_buff_vida, (boton_buff_vida_rect.left + 165, boton_buff_vida_rect.top + 15))
    screen.blit(texto_boton_buff_vida, (boton_buff_vida_rect.left + 35, boton_buff_vida_rect.top + 13))
    # #################################

    # ########### BuffAttack ###########
    tier_actual_buff_dano = 0
    for effect in player.effects:
        if isinstance(effect, BuffAttack):
            tier_actual_buff_dano = effect.tier

    precio_buff_dano = BuffAttack(tier_actual_buff_dano).precio

    screen.blit(img_boton_on, (left + margin_left_ef, top + 100))
    if aquafragments < precio_buff_dano:
        screen.blit(img_boton_off, (left + margin_left_ef, top + 100))

    boton_buff_dano_rect = pygame.Rect(left + margin_left_ef, top + 100, 160, 40)

    texto_boton_buff_dano = pygame.font.Font(None, 24).render(f" + Attack ", True,
                                                              (0, 0, 0))
    info_txt_buff_dano = pygame.font.Font(None, 20).render(
        f" {precio_buff_dano} AF | +{(BuffAttack(tier_actual_buff_dano).calculate(player.ataque))} ATK",
        True,
        (0, 0, 0))

    screen.blit(info_txt_buff_dano, (boton_buff_dano_rect.left + 165, boton_buff_dano_rect.top + 15))
    screen.blit(texto_boton_buff_dano, (boton_buff_dano_rect.left + 35, boton_buff_dano_rect.top + 13))
    # #################################

    # ########### RoboVida ###########
    tier_actual_robo_vida = 0
    for effect in player.effects:
        if isinstance(effect, RoboVida):
            tier_actual_robo_vida = effect.tier

    precio_robo_vida = RoboVida(tier_actual_robo_vida).precio

    screen.blit(img_boton_on, (left + margin_left_ef, top + 150))
    if aquafragments < precio_robo_vida:
        screen.blit(img_boton_off, (left + margin_left_ef, top + 150))

    boton_robo_vida_rect = pygame.Rect(left + margin_left_ef, top + 150, 160, 40)

    texto_boton_robo_vida = pygame.font.Font(None, 24).render(f" + LifeSteal ",
                                                              True,
                                                              (0, 0, 0))

    info_txt_roba_vida = pygame.font.Font(None, 20).render(
        f" {precio_robo_vida} AF | +{(RoboVida(tier_actual_robo_vida).calculate(player.robo_vida))} %",
        True,
        (0, 0, 0))

    screen.blit(texto_boton_robo_vida, (boton_robo_vida_rect.left + 35, boton_robo_vida_rect.top + 13))
    screen.blit(info_txt_roba_vida, (boton_robo_vida_rect.left + 165, boton_robo_vida_rect.top + 15))
    # #################################

    # Detectar clic en botones
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()[0]

    if not game_logic.mouse_pressed_last_frame and mouse_pressed:  # Verificar si es un clic completo
        if boton_buff_vida_rect.collidepoint(mouse_pos):
            if aquafragments >= precio_buff_vida:  # Costo del BuffVida
                player.add_effect(BuffVida(tier_actual_buff_vida + 1))
                player.cargar_effect(BuffVida)
                game_logic.aquafragments -= precio_buff_vida
        elif boton_buff_dano_rect.collidepoint(mouse_pos):
            if aquafragments >= precio_buff_dano:  # Costo del BuffVida
                player.add_effect(BuffAttack(tier_actual_buff_dano + 1))
                player.cargar_effect(BuffAttack)
                game_logic.aquafragments -= precio_buff_dano
        elif boton_robo_vida_rect.collidepoint(mouse_pos):
            if aquafragments >= precio_robo_vida:  # Costo del BuffVida
                player.add_effect(RoboVida(tier_actual_robo_vida + 1))
                player.cargar_effect(BuffAttack)
                game_logic.aquafragments -= precio_robo_vida

    # Actualizar el estado del botón del ratón del ciclo anterior
    game_logic.mouse_pressed_last_frame = mouse_pressed
