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
    game = Title()
    while not game.done:
        if game.scene == None:
            game.process_events()
            game.run_logic()
            game.display_frame(screen)
        elif game.scene == "Title":
            game = Title()
        elif game.scene == "Africa":
            game = Africa(africa_map, africa_list)
            windowwidth, windowheight = get_windowsize(africa_map)
            screen = pygame.display.set_mode([windowwidth, windowheight])
        elif game.scene == "Europe":
            game = Europe(europe_map, europe_list)
            windowwidth, windowheight = get_windowsize(europe_map)
            screen = pygame.display.set_mode([windowwidth, windowheight])
        elif game.scene == "Asia":
            game = Asia(asia_map, asia_list)
            windowwidth, windowheight = get_windowsize(asia_map)
            screen = pygame.display.set_mode([windowwidth, windowheight])
        elif game.scene == "SouthAmerica":
            game = SouthAmerica(southamerica_map, southamerica_list)
            windowwidth = get_windowsize(southamerica_map)[0]
            windowheight = get_windowsize(southamerica_map)[1]
            screen = pygame.display.set_mode([windowwidth, windowheight])

        FPSCLOCK.tick(FPS)
##    print(game.marker_list)
    pygame.quit()

if __name__ == "__main__":
    main()          
