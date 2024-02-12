"""           SLIME DEFENDER : Aqua Phobic

Slime Defender is a defend the castle game like, defend your
slime from the hordes of aqua monsters and more, upgrade your
defences and the slime equipment, use the elements for your
resistance or offensive against the enemies and become your
own hero saving the world!"""
# main.py
import pygame  # 2.5.2v

import src.game_logic as gl


def main():
    pygame.init()
    running = True
    while running:
        running = gl.start_game()


if __name__ == "__main__":
    main()
