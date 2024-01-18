from src.entities.Entity import Entity


class Effect:

    # Categorias: Miscelanea(misc), Armas(weapon), Armaduras(armor), Mouse(mouse), Slime(slime)
    def __init__(self, name, precio=0, tier=1, categoria="misc"):
        self.name = name
        self.tier = tier
        self.categoria = categoria
        self.precio = precio

    def calc_precio(self, precio):
        if self.tier <= 1:
            return precio
        if self.tier >= 6:
            return precio * (self.tier * 0.65)
        if self.tier >= 12:  # No creo que ninguna llegue aquí xd
            return precio * (self.tier * 0.60)
        return precio * (self.tier * 0.75)

    def cargar(self, entity: Entity):
        # Effecto que quieres cargar en Player
        pass
