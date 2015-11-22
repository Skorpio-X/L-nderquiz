import sys
# import gettext

import pygame

from . import game_class as gc
from . import globs as gl


def change_scene(game):
    """Create a new instance of the scene and fill it with params.

    Parameters:
        game: game class
    """
    next_params = gc.scenes[game.scene]
    try:
        next_scene = next_params()  # Menu object.
    except TypeError:
        next_scene = next_params[0](*next_params[1:])  # Game w/ params.
    window_width, window_height = next_scene.game_map.get_size()
    screen = pygame.display.set_mode([window_width + 90, window_height + 90])
    return next_scene, screen


def main():
    """Main game function."""
    pygame.init()
    window_width, window_height = gl.EUROPE_MAP.get_size()
    screen = pygame.display.set_mode([window_width, window_height])
    fps_clock = pygame.time.Clock()
    pygame.mouse.set_visible(True)
    game = gc.scenes['TitleMain']()
    fps = 30

    while not game.done:
        if game.scene is None:
            for event in pygame.event.get():
                game.process_events(event)
            game.run_logic()
            game.display_frame(screen)
            pygame.display.flip()
        elif game.scene == 'Deutsch':
            gl.de.install()
            game.scene = None
        elif game.scene == 'English':
            gl.en.install()
            game.scene = None
        else:
            game, screen = change_scene(game)

        fps_clock.tick(fps)
#     print(game.marker_list)  # Used to create the capital marks.
    pygame.quit()
    sys.exit()
