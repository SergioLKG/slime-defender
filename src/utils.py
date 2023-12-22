# utils.py
import random

from src.enemies import WaterEnemy

def generate_enemy_wave(level):
    # Genera una oleada de enemigos basada en el nivel actual del juego.
    # Puedes personalizar esta función según la lógica de tu juego.
    enemies = []
    for _ in range(level * 2):
        health = random.randint(5, 20)
        damage = random.randint(1, 5)
        enemies.append(WaterEnemy(health, damage))
    return enemies

def purchase_defense(player, defense):
    # Realiza la lógica de compra de defensa.
    # Puedes ajustar esto según la economía de tu juego.
    if player.tokens >= defense.cost:
        player.tokens -= defense.cost
        return True
    else:
        print("No tienes suficientes tokens para comprar esta defensa.")
        return False
