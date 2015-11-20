import sys
import gettext


# def _(string):
#     return string

en = gettext.translation('quiz', localedir='locale', languages=['en'])
en.install()
# print(en)
# print(dir(en))
de = gettext.translation('quiz', localedir='locale', languages=['de'])

import pygame

from . import game_class as gc
from . import globs as gl


def change_scene(game):
    """Change the scene.

    Parameters:
        game: game class
    """
    next_game = gc.scenes[game.scene]
    next_game.reset()
    window_width, window_height = next_game.game_map.get_size()
    screen = pygame.display.set_mode([window_width + 90, window_height + 90])
    return next_game, screen


def main():
    """Main game function."""
    pygame.init()
    window_width, window_height = gl.EUROPE_MAP.get_size()
    screen = pygame.display.set_mode([window_width, window_height])
    fps_clock = pygame.time.Clock()
    pygame.mouse.set_visible(True)
    game = gc.scenes['TitleMain']
    fps = 30

    while not game.done:
        if game.scene is None:
            for event in pygame.event.get():
                game.process_events(event)
            game.run_logic()
            game.display_frame(screen)
            pygame.display.flip()
        elif game.scene == 'Deutsch':
            # global _
            # def _(string):
            #     return string
            # gl._ = _
            de.install()
            game.scene = None
        elif game.scene == 'English':
            en.install()
            game.scene = None
        else:
            game, screen = change_scene(game)

        fps_clock.tick(fps)
#     print(game.marker_list)  # Used to create the capital marks.
    pygame.quit()
    sys.exit()
