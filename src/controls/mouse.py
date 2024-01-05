# mouse.py
import pygame

cursor_path = "assets/ui/cursor.png"


class Cursor:
    def __init__(self):
        self.spr = pygame.transform.scale(pygame.image.load(cursor_path), (24, 24))
        self.root = pygame.display.get_surface()
        self.x = 0
        self.y = 0
        self.rect = pygame.rect.Rect(self.x, self.y, 24, 24)

    def draw(self):
        self.root.blit(self.spr, (self.x, self.y))

    def update(self):
        self.x = pygame.mouse.get_pos()[0] - 6
        self.y = pygame.mouse.get_pos()[1]
        self.rect = pygame.rect.Rect(self.x, self.y, 24, 24)
