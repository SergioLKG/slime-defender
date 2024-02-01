# gameconf.py
import pygame
import pygame as p


# Settings ->

def importconfigs():
    volumeconf()
    screenconf()


# <- Settings

# SCREEEN ->
width = 800
height = 600
resolution = (width, height)  # Tamaño pantalla

# GRAPHICS
hardware_acceleratio = pygame.HWACCEL
double_buffer = pygame.DOUBLEBUF
fullscreen = pygame.FULLSCREEN


def screenconf():
    p.display.set_mode(resolution, double_buffer)  # Tamaño pantalla


# <- SCREEN

# VOLUME ->
master = 100  # Master vol
effects = 100  # Effects vol
music = 100  # Music vol

volumes = [100, 100, 100]  # [master, effects, music]


def volumeconf():
    master_channel = p.mixer.Channel(0)  # Channel 0 Master
    effects_channel = p.mixer.Channel(1)  # Channel 1 Effects
    music_channel = p.mixer.Channel(2)  # Channel 2 Music
    master_channel.set_volume(master / 100.0)
    music_channel.set_volume(music / 100.0)
    effects_channel.set_volume(effects / 100.0)


# <- VOLUME


# Returns and def
def __master__():
    return master


def __effects__():
    return effects


def __music__():
    return music


def __volumes__():
    return volumes


def __widthscreen__():
    return width


def __heightcreen__():
    return height


def __resolutionscreen__():
    return resolution


def __sizescreen__():
    return p.display.set_mode(__resolutionscreen__())
