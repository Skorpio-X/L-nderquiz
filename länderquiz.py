# coding=utf-8

"""A geographical quiz about countries and capitals.

Author: Skorpio
License: MIT License
"""

import sys

import pygame

import data.game_class as gc
import data.globs as gl

__version__ = "1.0.2"


def change_scene(game):
    """Change the scene."""
    next_game = gc.scenes[game.scene]
    game.scene = None
    window_width, window_height = next_game.game_map.get_size()
    screen = pygame.display.set_mode([window_width, window_height])
    return next_game, screen


def main():
    """Main game function."""
    pygame.init()
    window_width, window_height = gl.EUROPE_MAP.get_size()
    screen = pygame.display.set_mode([window_width, window_height])

    fps = 30

    fps_clock = pygame.time.Clock()
    pygame.mouse.set_visible(True)
    game = gc.scenes['TitleMain']
    while not game.done:
        if game.scene is None:
            game.process_events()
            game.run_logic()
            game.display_frame(screen)
        else:
            game, screen = change_scene(game)

        fps_clock.tick(fps)
#     print(game.marker_list)  # Used to create the capital marks.
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
