import pygame
import sys
from data.game_class import *

def get_windowsize(map_image):
    rect = map_image.get_rect()
    return rect.width, rect.height

def main():
    pygame.init()
    windowwidth, windowheight = get_windowsize(europe_map)
    screen = pygame.display.set_mode([windowwidth, windowheight])
    
    FPS = 30
    
    FPSCLOCK = pygame.time.Clock()
    pygame.mouse.set_visible(True)
    game = Europe(europe_map, europe_list)
    while not game.done:
        if game.scene == None:
            game.process_events()
            game.run_logic()
            game.display_frame(screen)
        elif game.scene == "Africa":
            game = Africa(africa_map, africa_list)
            windowwidth, windowheight = get_windowsize(africa_map)
            screen = pygame.display.set_mode([windowwidth, windowheight])
        elif game.scene == "Europe":
            game = Europe(europe_map, europe_list)
            windowwidth, windowheight = get_windowsize(europe_map)
            screen = pygame.display.set_mode([windowwidth, windowheight])
            
        FPSCLOCK.tick(FPS)
    #print(game.marker_list)
    pygame.quit()

if __name__ == "__main__":
    main()          
