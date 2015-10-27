"""Globals constants."""

import pygame
import os.path

pygame.init()
pygame.font.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 90, 0)
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600

START_SCREEN = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])

# Load images
# europe_map = pygame.image.load(
#     'graphics/europakarte.png'
#     ).convert()
EUROPE_MAP = pygame.image.load(
    os.path.join('graphics', "europakarte.png")
    ).convert()
# Unittest works with this path.
# europe_map = pygame.image.load(
#     os.path.join('..', 'graphics', "europakarte.png")
#     ).convert()
AFRICA_MAP = pygame.image.load(
    os.path.join('graphics', "afrikakarteB.png")
    ).convert()
AFRICA_MAP2 = pygame.image.load(
    os.path.join('graphics', "afrikakarte3.png")
    ).convert()
ASIA_MAP = pygame.image.load(
    os.path.join('graphics', "asienkarte.png")
    ).convert()
ASIA_MAP2 = pygame.image.load(
    os.path.join('graphics', "asienkarte2.png")
    ).convert()
SOUTHAMERICA_MAP = pygame.image.load(
    os.path.join('graphics', "suedamerikakarte.png")
    ).convert()
SOUTHAMERICA_MAP2 = pygame.image.load(
    os.path.join('graphics', "suedamerikakarte2.png")
    ).convert()
NORTHAMERICA_MAP = pygame.image.load(
    os.path.join('graphics', "nordamerikakarte.png")
    ).convert()
NORTHAMERICA_MAP2 = pygame.image.load(
    os.path.join('graphics', "nordamerikakarte2.png")
    ).convert()
AUSTRALIAOCEANIA_MAP = pygame.image.load(
    os.path.join('graphics', "australienozeanien.png")
    ).convert()
AUSTRALIAOCEANIA_MAP2 = pygame.image.load(
    os.path.join('graphics', "australienozeanien2.png")
    ).convert()

FONT = pygame.font.Font(os.path.join('graphics', "GenBasB.ttf"), 30)
# font = pygame.font.Font("C:/WINDOWS/Fonts/ARIAL.TTF", 25)
