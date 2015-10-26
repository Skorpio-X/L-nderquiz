# coding=utf-8

# Author: Skorpio
# License: MIT License

"""A geographical quiz game about countries and capitals."""

# print('länderquiz.py imported')
__version__ = "1.0.2"

import sys
from collections import namedtuple

import pygame

import data.game_class as gc
import data.globs as gl
from data.lists.europe_list import EUROPE_LIST
from data.lists.africa_list import africa_list
from data.lists.asia_list import asia_list
from data.lists.southamerica_list import southamerica_list
from data.lists.northamerica_list import northamerica_list
from data.lists.australiaoceania_list import australiaoceania_list


ContTup = namedtuple('ContinentTuple', 'continent map list')
CONTINENTS = {
    "Africa": ContTup(gc.Africa, gl.AFRICA_MAP, africa_list),
    "Europe": ContTup(gc.Europe, gl.EUROPE_MAP, EUROPE_LIST),
    "Asia": ContTup(gc.Asia, gl.ASIA_MAP, asia_list),
    "SouthAmerica": ContTup(
        gc.SouthAmerica,
        gl.SOUTHAMERICA_MAP,
        southamerica_list),
    "NorthAmerica": ContTup(
        gc.NorthAmerica,
        gl.NORTHAMERICA_MAP,
        northamerica_list),
    "AustraliaOceania": ContTup(
        gc.AustraliaOceania,
        gl.AUSTRALIAOCEANIA_MAP,
        australiaoceania_list),
    "AfricaCountries": ContTup(
        gc.AfricaCountries,
        gl.AFRICA_MAP2,
        africa_list),
    "EuropeCountries": ContTup(gc.EuropeCountries, gl.EUROPE_MAP, EUROPE_LIST),
    "AsiaCountries": ContTup(gc.AsiaCountries, gl.ASIA_MAP2, asia_list),
    "SouthAmericaCountries": ContTup(
        gc.SouthAmericaCountries,
        gl.SOUTHAMERICA_MAP2,
        southamerica_list),
    "NorthAmericaCountries": ContTup(
        gc.NorthAmericaCountries,
        gl.NORTHAMERICA_MAP2,
        northamerica_list),
    "AustraliaOceaniaCountries": ContTup(
        gc.AustraliaOceaniaCountries,
        gl.AUSTRALIAOCEANIA_MAP2,
        australiaoceania_list),
    }


def get_window_size(map_image):
    """Return width and height of a map image."""
    rect = map_image.get_rect()
    return rect.width, rect.height


def change_scene(game):
    """Change the scene."""
    cont_tup = CONTINENTS[game.scene]
    game = cont_tup.continent(cont_tup.map, cont_tup.list)
    window_width, window_height = get_window_size(cont_tup.map)
    screen = pygame.display.set_mode([window_width, window_height])
    return game, screen


def main():
    """Main game function."""
    pygame.init()
    window_width, window_height = get_window_size(gl.EUROPE_MAP)
    screen = pygame.display.set_mode([window_width, window_height])

    fps = 30

    fps_clock = pygame.time.Clock()
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

        fps_clock.tick(fps)
#     print(game.marker_list)  # Used to create the capital marks.
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
