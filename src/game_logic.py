# game_logic.py
import pygame # 2.5.2v
import util.colors as c
from util.gameconf import *


def start_game():
    # PYGAME CONFIG
    pygame.display.set_caption("Slime Defender: Aquaphobia")
    screen = pygame.display.set_mode(resolution)
    clock = pygame.time.Clock()
    
    enemy_wave = []
    level = 1

    #Bucle del juego
    while True:
        handle_events() # Eventos registrados del programa
        # ---- LOGICA
        
        # ---- LOGICA
        screen.fill((200, 255, 200)) # Color del fondo
        
        pygame.display.flip() # Actualizar pantalla
        clock.tick(30)  # Felocidad de fotogramas

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # la X de salir
            pygame.quit()
            quit()
