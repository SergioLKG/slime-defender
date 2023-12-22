# utils.py
import random

from src.enemies import WaterEnemy

def generate_enemy_wave(level):
    enemies = []
    for _ in range(level * 2):
        health = random.randint(5, 20) # Generar la vida aleatoriamente, luego según la vida cambiar sprite/tipo enemigo
        damage = random.randint(1, 5) # Daño aleatorio (debería depender de la vida/nivel del enemigo)
        enemies.append(WaterEnemy(health, damage))
    return enemies

def purchase_defense(player, defense): #Comprar defensas
    if player.tokens >= defense.cost:
        player.tokens -= defense.cost
        return True
    else:
        print("No tienes suficientes tokens para comprar esta defensa.")
        return False
