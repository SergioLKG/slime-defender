# game_logic.py
import pygame # 2.5.2v
from src import player, enemies, menu

def start_game():
    # PYGAME CONFIG
    pygame.display.set_caption("Slime Defender: Aquaphobia")
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    
    menu.show_menu(screen)
    
    player_slime = player.Player()
    enemy_wave = []
    level = 1

    while True:
        handle_events()

        screen.fill((200, 255, 200))
        render_elements(screen, player_slime, enemy_wave)
        
        pygame.display.flip()
        clock.tick(30)  # Felocidad de fotogramas

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

def render_elements(screen, player, enemies):
    pass
