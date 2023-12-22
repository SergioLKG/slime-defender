# main.py
import pygame # 2.5.2v
from src import game_logic

def main():
    pygame.init()
    game_logic.start_game()

if __name__ == "__main__":
    main()
