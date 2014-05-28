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
    game = TitleMain()
    while not game.done:
        if game.scene == None:
            game.process_events()
            game.run_logic()
            game.display_frame(screen)
        elif game.scene == "TitleMain":
            game = TitleMain()
        elif game.scene == "TitleCountries":
            game = TitleCountries()
        elif game.scene == "TitleCapitals":
            game = TitleCapitals()
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
        elif game.scene == "NorthAmerica":
            game = NorthAmerica(northamerica_map, northamerica_list)
            windowwidth, windowheight = get_windowsize(northamerica_map)
            screen = pygame.display.set_mode([windowwidth, windowheight])
        elif game.scene == "AustraliaOceania":
            game = AustraliaOceania(australiaoceania_map, australiaoceania_list)
            windowwidth, windowheight = get_windowsize(australiaoceania_map)
            screen = pygame.display.set_mode([windowwidth, windowheight])
        elif game.scene == "AfricaCountries":
            game = AfricaCountries(africa_map2, africa_list)
            windowwidth, windowheight = get_windowsize(africa_map2)
            screen = pygame.display.set_mode([windowwidth, windowheight])
        elif game.scene == "EuropeCountries":
            game = EuropeCountries(europe_map, europe_list)
            windowwidth, windowheight = get_windowsize(europe_map)
            screen = pygame.display.set_mode([windowwidth, windowheight])
        elif game.scene == "AsiaCountries":
            game = AsiaCountries(asia_map2, asia_list)
            windowwidth, windowheight = get_windowsize(asia_map2)
            screen = pygame.display.set_mode([windowwidth, windowheight])
        elif game.scene == "SouthAmericaCountries":
            game = SouthAmericaCountries(southamerica_map2, southamerica_list)
            windowwidth = get_windowsize(southamerica_map2)[0]
            windowheight = get_windowsize(southamerica_map2)[1]
            screen = pygame.display.set_mode([windowwidth, windowheight])
        elif game.scene == "NorthAmericaCountries":
            game = NorthAmericaCountries(northamerica_map2, northamerica_list)
            windowwidth, windowheight = get_windowsize(northamerica_map2)
            screen = pygame.display.set_mode([windowwidth, windowheight])
        elif game.scene == "AustraliaOceaniaCountries":
            game = AustraliaOceaniaCountries(australiaoceania_map2, australiaoceania_list)
            windowwidth, windowheight = get_windowsize(australiaoceania_map2)
            screen = pygame.display.set_mode([windowwidth, windowheight])

        FPSCLOCK.tick(FPS)
##    print(game.marker_list)
    pygame.quit()
##    sys.exit()

if __name__ == "__main__":
    main()          
