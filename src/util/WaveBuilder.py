from src import game_logic
from src.entities.enemies.Gota import Gota
from src.entities.enemies.GotaShield import GotaShield
from src.entities.enemies.GotaMuscle import GotaMuscle
from src.entities.enemies.Boss import Boss
from src.util.Wave import Wave


class WaveBuilder:
    @staticmethod
    def build_wave(screen, allies, wave_config):
        num_enemies = wave_config.get("num_enemies", 4)
        enemy_cooldown = wave_config.get("enemy_cooldown", 2000)
        enemy_types = wave_config.get("enemy_types", None)

        if not enemy_types:
            enemy_types = [Gota]
            current_wave = game_logic.wave_number

            if current_wave % 10 == 0:  # Cada 10 rondas
                enemy_types.append(Boss)
                # Restringir a solo un Boss por wave
                num_enemies -= 1

            # Proporciones deseadas (ajusta según tus necesidades)
            gota_count = int(num_enemies * 0.6)
            gota_escudo_count = int(num_enemies * 0.3)
            gota_musculosa_count = num_enemies - gota_count - gota_escudo_count

            # Añadir enemigos a la lista
            enemy_types += [Gota] * gota_count
            enemy_types += [GotaShield] * gota_escudo_count
            enemy_types += [GotaMuscle] * gota_musculosa_count

        return Wave(screen, allies, num_enemies, enemy_cooldown, enemy_types)
