# mouse.py
import pygame

cursor_path = "assets/ui/cursor.png"
onclick_path = "assets/ui/cursor_click.png"


class Cursor:
    def __init__(self):
        self.size = 35
        self.spr = pygame.transform.scale(pygame.image.load(cursor_path), (self.size, self.size))
        self.onclk = pygame.transform.scale(pygame.image.load(onclick_path),
                                            (self.size, self.size))
        self.root = pygame.display.get_surface()
        self.x = 0
        self.y = 0
        self.rect = pygame.rect.Rect(self.x, self.y, self.size, self.size)

    def draw(self):
        if pygame.mouse.get_pressed()[0]:
            self.root.blit(self.onclk, (self.x, self.y))
        else:
            self.root.blit(self.spr, (self.x, self.y))

    def update(self):
        self.x = pygame.mouse.get_pos()[0] - 6
        self.y = pygame.mouse.get_pos()[1]
        self.rect = pygame.rect.Rect(self.x, self.y, self.size, self.size)
