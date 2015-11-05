"""Globals constants."""

import pygame
import os.path

pygame.init()
pygame.font.init()

BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 90, 0)
WHITE = (255, 255, 255)
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

START_SCREEN = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])


def load_image(folder, name):
    image = pygame.image.load(os.path.join(folder, name)).convert()
    return image

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
