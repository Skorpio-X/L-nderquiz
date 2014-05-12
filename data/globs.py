import pygame
import os.path

pygame.font.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255, 0, 0)
GREEN = (0, 255, 255)
windowwidth, windowheight = 800, 600

screen = pygame.display.set_mode([windowwidth, windowheight])

# Load images
europe_map = pygame.image.load(os.path.join('graphics',"europakarte.png")).convert()
africa_map = pygame.image.load(os.path.join('graphics',"afrikakarteB.png")).convert()

#font = pygame.font.Font(os.path.join('graphics',"ARIAL.TTF"), 30)
font = pygame.font.Font("C:/WINDOWS/Fonts/ARIAL.TTF", 25)
