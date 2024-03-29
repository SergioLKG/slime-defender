import pygame

import src.entities.Enemy
import src.entities.Entity
import src.entities.Player


class Group(pygame.sprite.Group):
    def __init__(self, screen):
        pygame.sprite.Group.__init__(self)
        self.screen = screen

    def draw(self, surface, bgsurf=None, special_flags=0):
        for entity in self.sprites():
            entity.draw(surface)

    def set_enemies(self, enemies):
        for entity in self.sprites():
            if isinstance(entity, src.entities.Entity.Entity) or issubclass(entity.__class__,
                                                                            src.entities.Entity.Entity):
                entity.set_enemies(enemies)
