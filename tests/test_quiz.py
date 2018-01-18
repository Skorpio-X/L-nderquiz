# coding=utf-8

# Can be run from parent directory with $ python -m unittest tests.test_quiz

import unittest
# import sys
import pygame
pygame.init()
# import os
# This is not needed if run from parent directory.
# sys.path.append('../')
# sys.path.append('../data')
# sys.path.append('../graphics')
# sys.path.append('graphics/')
# sys.path.append('graphics')
# sys.path.append('Länderquiz_Projekt/graphics/')
# import graphics
# print(sys.path)
# print(os.path)
# euro_map = pygame.image.load('../graphics/europakarte.png')  # Works
# print(euro_map)

import länderquiz as lq
import data.globs as gl
from data import game_class
from data.lists import (AUSTRALIAOCEANIA_LIST, SOUTHAMERICA_LIST, ASIA_LIST,
                        NORTHAMERICA_LIST, EUROPE_LIST, AFRICA_LIST)


class TestCheckText(unittest.TestCase):

    # TODO: Find a better way to test the inputs. Maybe refactor `check_input`.
    def test_check_text(self):
        """Check user inputs for the capital quiz."""
        game = game_class.Game(gl.EUROPE_MAP, AFRICA_LIST, 1, 'Africa')
        n = [i for i, country in enumerate(game.country_list)
             if country[2] == 'Burkina Faso'][0]
        print(n)
        game.counter = n
        print(game.country_list[game.counter][2])
        game.usr_input = 'ouagadougou'
        self.assertEqual(game.check_input(), True)


# TODO: 'Vereinigte Staaten von Amerika' fails the test
#       because the name is a tuple, but the game works.
class TestFlags(unittest.TestCase):

    def test_flag_names(self):
        """Check if the flag names match the names in the country list."""
        country_lists = (AUSTRALIAOCEANIA_LIST, SOUTHAMERICA_LIST, ASIA_LIST,
                         NORTHAMERICA_LIST, EUROPE_LIST, AFRICA_LIST)
        flag_dicts = (gl.FLAGS_AUSTRALIAOCEANIA, gl.FLAGS_SOUTHAMERICA,
                      gl.FLAGS_ASIA, gl.FLAGS_NORTHAMERICA, gl.FLAGS_EUROPE,
                      gl.FLAGS_AFRICA)

        for list_, dict_ in zip(country_lists, flag_dicts):
            for country in list_:
                country_name = country[2]
                with self.subTest(cntry=country_name, dicti=dict_):
                    self.assertIn(
                        country_name, dict_.keys(),
                        '{} not found'.format(country_name))

if __name__ == '__main__':
    unittest.main()
