import random

import pygame

from src.entities.Group import Group
from src.entities.enemies.Gota import Gota


class Wave:
    def __init__(self, screen, allies, num_enemies, enemy_cooldown, enemy_types=None):
        self.screen = screen
        self.allies = allies
        self.num_enemies = num_enemies
        self.enemy_cooldown = enemy_cooldown
        self.enemy_types = enemy_types or [Gota]  # Lista de clases de enemigos

        self.enemies = Group(screen)
        self.next_enemy_time = pygame.time.get_ticks()
        self.generated = 0

    def update(self):
        current_time = pygame.time.get_ticks()

        if self.generated < self.num_enemies:
            if current_time > self.next_enemy_time:
                enemy_type = random.choice(self.enemy_types)
                r_height = random.uniform(0.21, 0.25)
                enemy = enemy_type((self.screen.get_width() + 100),
                                   (self.screen.get_height() // 2 + (self.screen.get_height() * r_height)),
                                   self.allies)
                self.enemies.add(enemy)
                self.generated += 1
                self.next_enemy_time = current_time + self.enemy_cooldown

        self.enemies.update()

    def is_completed(self):
        return len(self.enemies) == 0 and self.generated >= self.num_enemies

    def draw(self):
        self.enemies.draw(self.screen)

    def get_enemies(self):
        return self.enemies

    def get_allies(self):
        return self.allies
