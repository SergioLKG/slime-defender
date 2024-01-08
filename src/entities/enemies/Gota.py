from src.entities.Enemy import Enemy


class Gota(Enemy):
    def __init__(self, x, y):
        vida = 20
        ataque = 5
        velocidad = 3
        velocidad_ataque = 1
        rango = 50
        size = 30

        super().__init__(vida, ataque, velocidad, velocidad_ataque, rango, x, y, size)

    def recibir_dano(self, cantidad, elemento_enemigo="Neutro"):
        super().recibir_dano(cantidad, elemento_enemigo)

    def morir(self):
        print("Ha muerto una Gota.")
        # Puedes agregar acciones específicas para la Gota después de morir, como soltar recompensas

    def update(self):
        super().update()
        # Puedes agregar acciones específicas para la Gota durante la actualización (si es necesario)
