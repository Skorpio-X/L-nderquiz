"""Globals constants."""

import pygame
import os
import gettext


en = gettext.translation('quiz', localedir='locale', languages=['en'])
en.install()

pygame.init()
pygame.font.init()

BLACK = (0, 0, 0)
RED = (210, 73, 0)
BLUE = (30, 70, 170)
GREEN = (0, 90, 0)
WHITE = (255, 255, 255)
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

START_SCREEN = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])


def load_image(folder, name):
    """Load opaque images.

    Parameters:
        folder (str): Folder that contains images.
        name (str): Name of the image.
    """
    image = pygame.image.load(os.path.join(folder, name)).convert()
    return image


def load_flags():
    """Load the flag images and insert them into a dict."""
    path = os.path.join('graphics', 'flags')
    flags = {}
    for _, _, filenames in os.walk(path):
        for filename in filenames:
            print(filename)
            if filename.endswith('.png'):
                flags[filename[:-4]] = load_image(path, filename)
    return flags

# Load images
# europe_map = load(
#     'graphics/europakarte.png'
#     ).convert()

# Unittest works with this path.
# europe_map = load(
#     join('..', 'graphics', "europakarte.png")
#     ).convert()

ASIA_MAP = load_image('graphics', "asienkarte.png")
ASIA_MAP2 = load_image('graphics', "asienkarte2.png")
EUROPE_MAP = load_image('graphics', "europakarte.png")
AFRICA_MAP = load_image('graphics', "afrikakarteB.png")
AFRICA_MAP2 = load_image('graphics', "afrikakarte3.png")
NORTHAMERICA_MAP = load_image('graphics', "nordamerikakarte.png")
NORTHAMERICA_MAP2 = load_image('graphics', "nordamerikakarte2.png")
SOUTHAMERICA_MAP = load_image('graphics', "suedamerikakarte.png")
SOUTHAMERICA_MAP2 = load_image('graphics', "suedamerikakarte2.png")
AUSTRALIAOCEANIA_MAP = load_image('graphics', "australienozeanien.png")
AUSTRALIAOCEANIA_MAP2 = load_image('graphics', "australienozeanien2.png")

FONT = pygame.font.Font(os.path.join('graphics', "GenBasB.ttf"), 30)
# font = pygame.font.Font("C:/WINDOWS/Fonts/ARIAL.TTF", 25)

win_sound = pygame.mixer.Sound(os.path.join("sound", "win3.wav"))
fail_sound = pygame.mixer.Sound(os.path.join("sound", "fail3.wav"))

flags_euro = load_flags()
# print(len(flags_euro))
# print([name for name in flags_euro])
