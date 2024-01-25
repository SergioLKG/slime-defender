from src.entities.Entity import Entity


class Effect:

    # Categorias: Miscelanea(misc), Armas(weapon), Armaduras(armor), Mouse(mouse), Slime(slime)
    def __init__(self, name, precio, tier, categoria):
        self.name = name
        self.tier = tier
        self.categoria = categoria
        self.precio: int = self.calc_precio(precio)

    def calc_precio(self, precio):
        tier = self.tier
        if tier <= 1:
            return int(precio)
        if tier >= 6:
            return int(precio * (tier * 0.65))
        if tier >= 12:  # No creo que ninguna llegue aquí xd
            return int(precio * (tier * 0.60))
        return int(precio * (tier * 0.75))

    def cargar(self, entity: Entity):
        # Effecto que quieres cargar en Player
        pass
