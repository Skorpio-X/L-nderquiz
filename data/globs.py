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


def load_flags(path):
    """Load the images and insert them into a dict.

    Load all files from different flag directories.
    """
    images = {}
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith('.png'):
                country_name = filename[:-4]
                with open(os.path.join(dirpath, filename), 'rb') as file:
                    img = pygame.image.load(file).convert()
                    images[country_name] = scale(img)

    return images


def scale(img):
    """Scale images to 380 px height.

    Parameters:
        img (pygame.Surface): The image to be scaled.
    """
    width, height = img.get_size()
    percent = 100 / 380 * height
    mult = 100 / percent
    return pygame.transform.smoothscale(img, (int(width * mult),
                                              int(height * mult)))


ASIA_MAP = load_image('graphics', 'asienkarte.png')
ASIA_MAP2 = load_image('graphics', 'asienkarte2.png')
EUROPE_MAP = load_image('graphics', 'europakarte.png')
AFRICA_MAP = load_image('graphics', 'afrikakarteB.png')
AFRICA_MAP2 = load_image('graphics', 'afrikakarte3.png')
NORTHAMERICA_MAP = load_image('graphics', 'nordamerikakarte.png')
NORTHAMERICA_MAP2 = load_image('graphics', 'nordamerikakarte2.png')
SOUTHAMERICA_MAP = load_image('graphics', 'suedamerikakarte.png')
SOUTHAMERICA_MAP2 = load_image('graphics', 'suedamerikakarte2.png')
AUSTRALIAOCEANIA_MAP = load_image('graphics', 'australienozeanien.png')
AUSTRALIAOCEANIA_MAP2 = load_image('graphics', 'australienozeanien2.png')

FONT = pygame.font.Font(os.path.join('graphics', 'GenBasB.ttf'), 30)
# font = pygame.font.Font('C:/WINDOWS/Fonts/ARIAL.TTF', 25)

win_sound = pygame.mixer.Sound(os.path.join('sound', 'win3.wav'))
fail_sound = pygame.mixer.Sound(os.path.join('sound', 'fail3.wav'))

FLAGS_EUROPE = load_flags(os.path.join('graphics', 'flags', 'europe'))
FLAGS_AFRICA = load_flags(os.path.join('graphics', 'flags', 'africa'))
FLAGS_ASIA = load_flags(os.path.join('graphics', 'flags', 'asia'))
FLAGS_SOUTHAMERICA = load_flags(os.path.join('graphics', 'flags', 'south_america'))
FLAGS_NORTHAMERICA = load_flags(os.path.join('graphics', 'flags', 'north_america'))
FLAGS_AUSTRALIAOCEANIA = load_flags(os.path.join('graphics', 'flags', 'australia_oceania'))
