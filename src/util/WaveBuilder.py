from src.util.Wave import Wave


class WaveBuilder:
    @staticmethod
    def build_wave(screen, allies, wave_config):
        num_enemies = wave_config.get("num_enemies", 4)
        enemy_cooldown = wave_config.get("enemy_cooldown", 2000)
        enemy_types = wave_config.get("enemy_types", None)
        return Wave(screen, allies, num_enemies, enemy_cooldown, enemy_types)
