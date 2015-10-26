# coding=utf-8

# Can be run from parent directory with $ python -m unittest tests.test_quiz

import unittest
import sys
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


class TestWindow(unittest.TestCase):

    def test_get_window_size(self):
        self.assertEqual(lq.get_window_size(gl.AFRICA_MAP), (635, 600))


class TestCheckText(unittest.TestCase):

    def test_check_text(self):
        self.assertEqual(game_class.check_text_input('Burkina Faso', 'burkina faso'), True)


if __name__ == '__main__':
    unittest.main()
