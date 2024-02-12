import math

from src import game_logic
import pygame

# img_cd_mouse = load_image()
# img_dmg_mouse = load_image()
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
    # img_cd_mouse = load_image()
    # img_dmg_mouse = load_image()
    img_boton_on = load_image("btn_bg.png", (160, 40))
    img_boton_off = load_image("btn_bg_disable.png", (160, 40))


def calc_price(tier):  # Calcular los precio
    return math.ceil(((tier + 1) * 1.3 ** tier))


def draw_eff_menu(screen, interfaz_rect):
    global img_boton_off, img_boton_on
    aquafragments = game_logic.aquafragments

    top = interfaz_rect.top + 280
    left = interfaz_rect.left + 20
    # -------------------- TITLE -----------------------
    bg_eff = pygame.Rect(left, top + 10, interfaz_rect.w - 30, 150)  # TODO Meter trasparencia.
    pygame.draw.rect(screen, (155, 145, 145), bg_eff)
    screen.blit(pygame.font.Font(None, 30).render(f"Mouse Buffs", True, (0, 0, 0)), (left + 10, top + 25))
    # --------------------- EFFECTS ---------------------
    margin_left_ef = 25
    # ########### Buff Cooldown ###########
    precio_cd_buff = calc_price(game_logic.tier_cd_buff)

    screen.blit(img_boton_on, (left + margin_left_ef, top + 50))
    if aquafragments < precio_cd_buff:
        screen.blit(img_boton_off, (left + margin_left_ef, top + 50))

    boton_buff_cd_rect = pygame.Rect(left + margin_left_ef, top + 50, 160, 40)

    texto_boton_buff_cd = pygame.font.Font(None, 24).render(f" - CoolDown", True,
                                                            (0, 0, 0))
    info_txt_buff_cd = pygame.font.Font(None, 20).render(
        f"{precio_cd_buff} AF | +{game_logic.mouse_cooldown} CD", True,
        (0, 0, 0))

    screen.blit(texto_boton_buff_cd, (boton_buff_cd_rect.left + 35, boton_buff_cd_rect.top + 13))
    screen.blit(info_txt_buff_cd, (boton_buff_cd_rect.left + 165, boton_buff_cd_rect.top + 15))

    # ########### Buff Damage ###########
    precio_dmg_buff = calc_price(game_logic.tier_dmg_buff)

    screen.blit(img_boton_on, (left + margin_left_ef, top + 100))
    if aquafragments < precio_cd_buff:
        screen.blit(img_boton_off, (left + margin_left_ef, top + 100))

    boton_buff_dmg_rect = pygame.Rect(left + margin_left_ef, top + 100, 160, 40)

    texto_boton_buff_vida = pygame.font.Font(None, 24).render(f" + Damage", True,
                                                              (0, 0, 0))
    info_txt_buff_dano = pygame.font.Font(None, 20).render(
        f"{precio_dmg_buff} AF | +{game_logic.mouse_dmg} DMG", True,
        (0, 0, 0))

    screen.blit(info_txt_buff_dano, (boton_buff_dmg_rect.left + 165, boton_buff_dmg_rect.top + 15))
    screen.blit(texto_boton_buff_vida, (boton_buff_dmg_rect.left + 35, boton_buff_dmg_rect.top + 13))
    ######################################
    # Detectar clic en botones
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()[0]

    if not game_logic.mouse_pressed_last_frame and mouse_pressed:  # Verificar si es un clic completo
        if boton_buff_cd_rect.collidepoint(mouse_pos):
            if aquafragments >= precio_cd_buff:  # Costo del BuffVida
                game_logic.calc_mouse_buff(1)
                game_logic.aquafragments -= precio_cd_buff
        elif boton_buff_dmg_rect.collidepoint(mouse_pos):
            if aquafragments >= precio_dmg_buff:  # Costo del BuffVida
                game_logic.calc_mouse_buff(0)
                game_logic.aquafragments -= precio_dmg_buff

    # Actualizar el estado del botón del ratón del ciclo anterior
    game_logic.mouse_pressed_last_frame = mouse_pressed
