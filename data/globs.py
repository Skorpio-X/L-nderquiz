import pygame
import os.path

pygame.font.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255, 0, 0)
GREEN = (0, 180, 0)
windowwidth, windowheight = 800, 600

screen = pygame.display.set_mode([windowwidth, windowheight])

# Load images
europe_map = pygame.image.load(
    os.path.join('graphics',"europakarte.png")
    ).convert()
africa_map = pygame.image.load(
    os.path.join('graphics',"afrikakarteB.png")
    ).convert()
asia_map = pygame.image.load(
    os.path.join('graphics',"asienkarte.png")
    ).convert()
southamerica_map = pygame.image.load(
    os.path.join('graphics',"suedamerikakarte.png")
    ).convert()
northamerica_map = pygame.image.load(
    os.path.join('graphics',"nordamerikakarte.png")
    ).convert()
australiaoceania_map = pygame.image.load(
    os.path.join('graphics',"australienozeanien.png")
    ).convert()

font = pygame.font.Font(os.path.join('graphics',"GenBasB.ttf"), 30)
##font = pygame.font.Font("C:/WINDOWS/Fonts/ARIAL.TTF", 25)

