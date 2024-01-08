from src.entities.Entity import Entity


class Enemy(Entity):
    def __init__(self, vida, ataque, velocidad, velocidad_ataque, rango, x, y, size=30, element="Agua"):
        super().__init__(vida, x, y, size, element)

        self.ataque = ataque
        self.velocidad = velocidad
        self.velocidad_ataque = velocidad_ataque
        self.rango = rango

    def atacar(self, objetivo):
        if self.esta_en_rango(objetivo):
            objetivo.recibir_dano(self.ataque)

    def esta_en_rango(self, objetivo):
        distancia = abs(objetivo.rect.x - self.rect.x)
        return distancia <= self.rango

    def recibir_dano(self, cantidad, elemento_enemigo="Neutro"):
        super().recibir_dano()

    def morir(self):
        print("A muerto una entidad una entidad: ", self.__class__)
        self.kill()

    def update(self):
        self.rect.x -= self.velocidad
