# Author: Skorpio
# License: MIT...

__version__ = "1.0.0"

import sys
from collections import namedtuple

import pygame

import data.game_class as gc
import data.globs as gl
from data.lists.europe_list import europe_list
from data.lists.africa_list import africa_list
from data.lists.asia_list import asia_list
from data.lists.southamerica_list import southamerica_list
from data.lists.northamerica_list import northamerica_list
from data.lists.australiaoceania_list import australiaoceania_list


ContTup = namedtuple('ContinentTuple', 'continent map list')
continents = {
    "Africa": ContTup(gc.Africa, gl.africa_map, africa_list),
    "Europe": ContTup(gc.Europe, gl.europe_map, europe_list),
    "Asia": ContTup(gc.Asia, gl.asia_map, asia_list),
    "SouthAmerica": ContTup(gc.SouthAmerica, gl.southamerica_map, southamerica_list),
    "NorthAmerica": ContTup(gc.NorthAmerica, gl.northamerica_map, northamerica_list),
    "AustraliaOceania": ContTup(gc.AustraliaOceania, gl.australiaoceania_map,
                                australiaoceania_list),
    "AfricaCountries": ContTup(gc.AfricaCountries, gl.africa_map2, africa_list),
    "EuropeCountries": ContTup(gc.EuropeCountries, gl.europe_map, europe_list),
    "AsiaCountries": ContTup(gc.AsiaCountries, gl.asia_map2, asia_list),
    "SouthAmericaCountries": ContTup(gc.SouthAmericaCountries, gl.southamerica_map2,
                                     southamerica_list),
    "NorthAmericaCountries": ContTup(gc.NorthAmericaCountries, gl.northamerica_map2,
                                     northamerica_list),
    "AustraliaOceaniaCountries": ContTup(
        gc.AustraliaOceaniaCountries, gl.australiaoceania_map2, australiaoceania_list),
    }


def get_windowsize(map_image):
    rect = map_image.get_rect()
    return rect.width, rect.height


def change_scene(game):
    cont_tup = continents[game.scene]
    game = cont_tup.continent(cont_tup.map, cont_tup.list)
    windowwidth, windowheight = get_windowsize(cont_tup.map)
    screen = pygame.display.set_mode([windowwidth, windowheight])
    return game, screen


def main():
    pygame.init()
    windowwidth, windowheight = get_windowsize(gl.europe_map)
    screen = pygame.display.set_mode([windowwidth, windowheight])
    
    fps = 30
    
    fpsclock = pygame.time.Clock()
    pygame.mouse.set_visible(True)
    game = gc.TitleMain()
    while not game.done:
        if game.scene is None:
            game.process_events()
            game.run_logic()
            game.display_frame(screen)
        elif game.scene == "TitleMain":
            game = gc.TitleMain()
        elif game.scene == "TitleCountries":
            game = gc.TitleCountries()
        elif game.scene == "TitleCapitals":
            game = gc.TitleCapitals()
        else:
            game, screen = change_scene(game)

        fpsclock.tick(fps)
#     print(game.marker_list)  # Used to create the capital marks.
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
