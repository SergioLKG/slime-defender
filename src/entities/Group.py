import pygame

import src.entities.Player
import src.entities.Enemy


class Group(pygame.sprite.Group):
    def __init__(self, screen):
        pygame.sprite.Group.__init__(self)
        self.screen = screen

    def draw(self, surface, bgsurf=None, special_flags=0):
        super().draw(surface, bgsurf, special_flags)
        for entity in self.sprites():
            if isinstance(entity, src.entities.Player.Player):
                entity.draw_healthbar(self.screen)
            if isinstance(entity, src.entities.Enemy.Enemy):
                entity.draw_healthbar(self.screen)