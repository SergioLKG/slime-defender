from src.effects.BuffAttack import BuffAttack
from src.effects.BuffVida import BuffVida
import pygame

from src.effects.RoboVida import RoboVida


def draw_eff_menu(screen, interfaz_rect, aquafragments, player):
    # --------------------- EFFECTS ---------------------
    effects_cat = pygame.Rect(interfaz_rect.left, interfaz_rect.top + 50, interfaz_rect.width, 300)
    pygame.draw.rect(screen, (200, 100, 100), effects_cat)
    margin_left_ef = 30
    # ########### BuffVida ###########
    tier_actual_buff_vida = 0
    for effect in player.effects:
        if isinstance(effect, BuffVida):
            tier_actual_buff_vida = effect.tier

    precio_buff_vida = BuffVida(tier_actual_buff_vida + 1).precio
    color_bv_btn = (100, 255, 100)
    if aquafragments < precio_buff_vida:
        color_bv_btn = (220, 50, 50)

    boton_buff_vida_rect = pygame.Rect(interfaz_rect.left + margin_left_ef, interfaz_rect.top + 50, 160, 40)
    pygame.draw.rect(screen, color_bv_btn, boton_buff_vida_rect)  # Color verde para el botón

    texto_boton_buff_vida = pygame.font.Font(None, 24).render(f"+Health | {precio_buff_vida}AF", True,
                                                              (0, 0, 0))
    info_txt_buff_dano = pygame.font.Font(None, 20).render(
        f" +{int(BuffVida(tier_actual_buff_vida + 1).calculate())} HP",
        True,
        (0, 0, 0))

    screen.blit(info_txt_buff_dano, (boton_buff_vida_rect.left + 160, boton_buff_vida_rect.top + 12))
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

    boton_buff_dano_rect = pygame.Rect(interfaz_rect.left + margin_left_ef, interfaz_rect.top + 100, 160, 40)
    pygame.draw.rect(screen, color_ba_btn, boton_buff_dano_rect)

    texto_boton_buff_dano = pygame.font.Font(None, 24).render(f"+Attack | {precio_buff_dano} AF", True,
                                                              (0, 0, 0))
    info_txt_buff_dano = pygame.font.Font(None, 20).render(
        f" +{int(BuffAttack(tier_actual_buff_dano + 1).calculate())} ATK",
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

    color_rv_btn = (100, 255, 100)
    if aquafragments < precio_robo_vida:
        color_rv_btn = (220, 50, 50)

    boton_robo_vida_rect = pygame.Rect(interfaz_rect.left + margin_left_ef, interfaz_rect.top + 150, 160, 40)
    pygame.draw.rect(screen, color_rv_btn, boton_robo_vida_rect)

    texto_boton_robo_vida = pygame.font.Font(None, 24).render(f"+LifeSteal | {precio_robo_vida} AF",
                                                              True,
                                                              (0, 0, 0))

    info_txt_roba_vida = pygame.font.Font(None, 20).render(
        f" +{int(RoboVida(tier_actual_robo_vida + 1).calculate())} %",
        True,
        (0, 0, 0))

    screen.blit(texto_boton_robo_vida, (boton_robo_vida_rect.left + 10, boton_robo_vida_rect.top + 10))
    screen.blit(info_txt_roba_vida, (boton_robo_vida_rect.left + 160, boton_robo_vida_rect.top + 12))
    # #################################

    # Puntuación
    screen.blit(pygame.font.Font(None, 24).render("AquaFragments: " + str(aquafragments), True,
                                                  (0, 0, 0)), (interfaz_rect.left + 30, interfaz_rect.top + 20))

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
        elif boton_robo_vida_rect.collidepoint(mouse_pos):
            if aquafragments >= precio_robo_vida:  # Costo del BuffVida
                player.add_effect(RoboVida(tier_actual_robo_vida + 1))
                player.cargar_effects()
                aquafragments -= precio_robo_vida
        # --------------------- EFFECTS END ---------------------
