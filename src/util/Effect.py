class Effect:

    # Categorias: Miscelanea(misc), Armas(weapon), Armaduras(armor), Mouse(mouse), Slime(slime)
    def __init__(self, tier, precio, categoria="misc"):
        self.categoria = categoria
        self.precio = precio
        self.tier = tier
