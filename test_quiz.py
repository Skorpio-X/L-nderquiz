# coding=utf-8

import unittest
# import sys
# sys.path.append('../')
# sys.path.append('../data')
# sys.path.append('../graphics')
# print(sys.path)

# import länderquiz as lq
# import data.globs as gl
from data import game_class


# class TestWindow(unittest.TestCase):
#     # pass
#     def test_get_window_size(self):
#         self.assertEqual(lq.get_window_size(gl.africa_map), (635, 600))


class TestCheckText(unittest.TestCase):

    def test_check_text(self):
        self.assertEqual(game_class.check_text_input('Burkina Faso', 'burkina faso'), True)


if __name__ == '__main__':
    unittest.main()
