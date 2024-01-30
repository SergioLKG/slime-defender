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


def draw_eff_menu(screen, interfaz_rect, aquafragments, player):
    global img_boton_off, img_boton_on
    # --------------------- EFFECTS ---------------------
    margin_left_ef = 30
    # ########### BuffVida ###########
    tier_actual_buff_vida = 0
    for effect in player.effects:
        if isinstance(effect, BuffVida):
            tier_actual_buff_vida = effect.tier

    precio_buff_vida = BuffVida(tier_actual_buff_vida + 1).precio

    screen.blit(img_boton_on, (interfaz_rect.left + margin_left_ef, interfaz_rect.top + 50))
    if aquafragments < precio_buff_vida:
        screen.blit(img_boton_off, (interfaz_rect.left + margin_left_ef, interfaz_rect.top + 50))

    texto_boton_buff_vida = pygame.font.Font(None, 24).render(f"+Health", True,
                                                              (0, 0, 0))
    info_txt_buff_dano = pygame.font.Font(None, 20).render(
        f" {precio_buff_vida} AF | +{int(BuffVida(tier_actual_buff_vida + 1).calculate())} HP",
        True,
        (0, 0, 0))

    boton_buff_vida_rect = pygame.Rect(interfaz_rect.left + margin_left_ef, interfaz_rect.top + 50, 160, 40)

    screen.blit(info_txt_buff_dano, (boton_buff_vida_rect.left + 160, boton_buff_vida_rect.top + 12))
    screen.blit(texto_boton_buff_vida, (boton_buff_vida_rect.left + 10, boton_buff_vida_rect.top + 10))
    # #################################

    # ########### BuffAttack ###########
    tier_actual_buff_dano = 0
    for effect in player.effects:
        if isinstance(effect, BuffAttack):
            tier_actual_buff_dano = effect.tier

    precio_buff_dano = BuffAttack(tier_actual_buff_dano + 1).precio
    screen.blit(img_boton_on, (interfaz_rect.left + margin_left_ef, interfaz_rect.top + 100))
    if aquafragments < precio_buff_vida:
        screen.blit(img_boton_off, (interfaz_rect.left + margin_left_ef, interfaz_rect.top + 100))

    boton_buff_dano_rect = pygame.Rect(interfaz_rect.left + margin_left_ef, interfaz_rect.top + 100, 160, 40)

    texto_boton_buff_dano = pygame.font.Font(None, 24).render(f"+Attack ", True,
                                                              (0, 0, 0))
    info_txt_buff_dano = pygame.font.Font(None, 20).render(
        f" {precio_buff_dano} AF | +{int(BuffAttack(tier_actual_buff_dano + 1).calculate())} ATK",
        True,
        (0, 0, 0))

    screen.blit(info_txt_buff_dano, (boton_buff_dano_rect.left + 160, boton_buff_dano_rect.top + 12))
    screen.blit(texto_boton_buff_dano, (boton_buff_dano_rect.left + 10, boton_buff_dano_rect.top + 10))
    # #################################

    # ########### RoboVida ###########
    tier_actual_robo_vida = 0
    for effect in player.effects:
        if isinstance(effect, RoboVida):
            tier_actual_robo_vida = effect.tier

    precio_robo_vida = RoboVida(tier_actual_robo_vida + 1).precio

    screen.blit(img_boton_on, (interfaz_rect.left + margin_left_ef, interfaz_rect.top + 150))
    if aquafragments < precio_buff_vida:
        screen.blit(img_boton_off, (interfaz_rect.left + margin_left_ef, interfaz_rect.top + 150))

    boton_robo_vida_rect = pygame.Rect(interfaz_rect.left + margin_left_ef, interfaz_rect.top + 150, 160, 40)

    texto_boton_robo_vida = pygame.font.Font(None, 24).render(f"+LifeSteal ",
                                                              True,
                                                              (0, 0, 0))

    info_txt_roba_vida = pygame.font.Font(None, 20).render(
        f" {precio_robo_vida} AF | +{int(RoboVida(tier_actual_robo_vida + 1).calculate())} %",
        True,
        (0, 0, 0))

    screen.blit(texto_boton_robo_vida, (boton_robo_vida_rect.left + 10, boton_robo_vida_rect.top + 10))
    screen.blit(info_txt_roba_vida, (boton_robo_vida_rect.left + 160, boton_robo_vida_rect.top + 12))
    # #################################

    # Detectar clic en botones
    if pygame.mouse.get_pressed()[0] == pygame.MOUSEBUTTONUP:  # Botón izquierdo del ratón
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
        elif boton_robo_vida_rect.collidepoint(mouse_pos):
            if aquafragments >= precio_robo_vida:  # Costo del BuffVida
                player.add_effect(RoboVida(tier_actual_robo_vida + 1))
                player.cargar_effects()
                aquafragments -= precio_robo_vida
        # --------------------- EFFECTS END ---------------------
