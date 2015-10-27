"""Game classes for country and capital quizzes."""

import random

import pygame

from . import globs as gl
from .titlemenu import TitleMain, TitleCountries, TitleCapitals
from data.lists.europe_list import EUROPE_LIST
from data.lists.africa_list import AFRICA_LIST
from data.lists.asia_list import ASIA_LIST
from data.lists.southamerica_list import SOUTHAMERICA_LIST
from data.lists.northamerica_list import NORTHAMERICA_LIST
from data.lists.australiaoceania_list import AUSTRALIAOCEANIA_LIST


class Game:
    """Game class for country and capital quizzes."""

    def __init__(self, next_scene, game_map, country_list, active_idx):
        self.done = False
        self.timer = 0
        self.scene = None
        self.game_map = game_map
        self.active_question = None
        self.active_position = None
        # Use 1 for capital and 2 for country quiz.
        self.active_idx = active_idx
        self.counter = 0
        self.country_list = []
        self.enter = False
        self.name = ""
        self.next_scene = next_scene
        self.score = 0
        self.incorrect_answer = False
        self.last_position = None
        self.game_over = False
        # Used to mark positions of cities
    #     marker_list = []
    #     marker_count = 0
        pygame.display.set_caption('Länderquiz')
        random.shuffle(country_list)
        self.country_list = country_list
        self.false_name = None
        self.backspace_pressed = False
        self.backspace_timer = 20

    def process_events(self):
        """Handle events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True

            # Locate cities on the map by mouse clicking.
            # Used to create the list for the indicators.
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 print(pygame.mouse.get_pos())
#                 mouse_pos = pygame.mouse.get_pos()
#                 city = input("Hauptstadt: ")
#                 self.marker_list.append([mouse_pos, city])
#                 self.marker_count += 1

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.scene = "TitleMain"
                if event.unicode.isalnum():  # unicode
                    self.name += event.unicode
                if event.key == pygame.K_SPACE:
                    self.name += " "
                if event.key == pygame.K_SLASH:
                    self.name += "-"
                if event.key == pygame.K_PERIOD:
                    self.name += "."
                if event.key == pygame.K_COMMA:
                    self.name += ","
                if event.key == 92:
                    self.name += "'"
                if event.key == pygame.K_LEFT:
                    self.scene = self.next_scene
                if (event.key == pygame.K_KP_ENTER or
                        event.key == pygame.K_RETURN):
                    self.enter = True
                    if not self.game_over:
                        if self.check_input():
                            self.score += 1
                            self.name = ""
                            self.incorrect_answer = False
                        else:
                            self.incorrect_answer = True
                            self.false_name = self.name
                            self.name = ""
                if event.key == pygame.K_BACKSPACE:
                    self.backspace_timer = 20
                    self.name = self.name[:-1]
                    self.backspace_pressed = True
            elif event.type == pygame.KEYUP:
                if (event.key == pygame.K_KP_ENTER or
                        event.key == pygame.K_RETURN):
                    self.enter = False
                if event.key == pygame.K_BACKSPACE:
                    self.backspace_pressed = False

    def run_logic(self):
        if self.backspace_pressed:
            self.backspace_timer -= 1
            self.del_letters()
        self.next_country()

        if not self.game_over:
            # country name
            self.active_question = self.country_list[self.counter][
                self.active_idx]
            # country position
            self.active_position = self.country_list[self.counter][0]
            self.last_position = self.country_list[self.counter - 1][0]
        if len(self.country_list) == self.counter:
            self.last_position = self.active_position

    def next_country(self):
        if self.enter and len(self.country_list) > self.counter:
            self.counter += 1
            self.enter = False
        if len(self.country_list) == self.counter:
            self.game_over = True

    def del_letters(self):
        """When backspace is pressed continuously delete letters."""
        if self.backspace_timer <= 0:
            self.name = self.name[:-1]
            self.backspace_timer = 2

    def check_input(self):
        """Checks if active name equals name."""
        if self.country_list[self.counter][
                self.active_idx].lower() == self.name.lower():
            return True
        else:
            return False

    def display_frame(self, screen):
        """Render everything."""
        screen.blit(self.game_map, (0, 0))
        self.render_score(screen)
        self.render_active_question(screen)
        self.render_game_over(screen)
        self.render_incorrect_answer(screen)

    def render_score(self, screen):
        try:
            score = round(100 / self.counter * self.score, 2)
        except ZeroDivisionError:
            score = 0
        score_txt = gl.FONT.render(
            "{0} richtige Antworten von {1}. {2} Prozent korrekt".format(
                self.score, self.counter, score),
            True, gl.BLACK)
        screen.blit(score_txt, [3, 40])

    def render_game_over(self, screen):
        if self.game_over:
            game_over_txt = gl.FONT.render(
                "Spiel beendet - Pfeiltaste links für das nächste Quiz",
                True, gl.GREEN)
            game_over_txt2 = gl.FONT.render(
                "ESC um ins Hauptmenü zu gelangen", True, gl.GREEN)
            screen.blit(game_over_txt, [20, 70])
            screen.blit(game_over_txt2, [20, 100])

    def render_active_question(self, screen):
        """Display pointer to active country/capital."""
        # Probably used to locate cities.
        # pygame.draw.circle(screen, gl.RED, pygame.mouse.get_pos(), 1)
        if not self.game_over:
            if len(self.country_list) >= self.counter:
                # pygame.draw.circle(screen, gl.BLUE, self.active_position, 4)
                pygame.draw.line(
                    screen, gl.BLUE, self.active_position,
                    [self.active_position[0] + 10,
                     self.active_position[1] - 10],
                    4)
                pygame.draw.line(
                    screen, gl.BLUE,
                    [self.active_position[0] + 10,
                     self.active_position[1] - 10],
                    [self.active_position[0] + 50,
                     self.active_position[1] - 10],
                    4)
                name_text = gl.FONT.render(self.name, True, gl.BLUE)
                screen.blit(name_text,
                            [self.active_position[0] + 10,
                             self.active_position[1] - 40])
                screen.blit(name_text, (3, 70))
                # For country quiz.
                if (len(self.country_list[self.counter]) > 2
                        and self.active_idx == 2):
                    question = gl.FONT.render(
                        "Nenne den Namen dieses Landes ", True, gl.GREEN)
                    screen.blit(question, [3, 10])
                # For capital quiz.
                if (len(self.country_list[self.counter]) > 2
                        and self.active_idx == 1):
                    country_name = gl.FONT.render(
                        "Nenne die Hauptstadt von {}.".format(
                            self.country_list[self.counter][2]),
                        True, gl.GREEN)
                    screen.blit(country_name, [3, 10])

    def render_incorrect_answer(self, screen):
        if self.incorrect_answer and len(self.country_list) >= self.counter:
            pygame.draw.line(screen, gl.RED, self.last_position,
                             [self.last_position[0] - 10,
                              self.last_position[1] - 10], 4)
            pygame.draw.line(screen, gl.RED,
                             [100, self.last_position[1] - 10],
                             [self.last_position[0] - 10,
                              self.last_position[1] - 10], 4)
            inc_name_text = gl.FONT.render(
                self.country_list[self.counter-1][self.active_idx],
                True, gl.RED)
            # screen.blit(inc_name_text, [self.last_position[0] -
            #     len(self.country_list[self.counter - 1][2]) * 10,
            #                       self.last_position[1] - 40])
            screen.blit(inc_name_text, [100,
                        self.last_position[1] - 40])
            last_answer = gl.FONT.render(
                "Ihre Antwort war {}".format(self.false_name), True, gl.RED)
            screen.blit(last_answer, [10, self.game_map.get_height() - 60])
            inc_text = gl.FONT.render(
                "Die korrekte Antwort lautet {}".format(
                    self.country_list[self.counter-1][
                        self.active_idx]), True, gl.RED)
            screen.blit(inc_text, [10, self.game_map.get_height() - 30])


scenes = {
    'TitleMain': TitleMain(),
    'TitleCountries': TitleCountries(),
    'TitleCapitals': TitleCapitals(),
    'Europe': Game('Africa', gl.EUROPE_MAP, EUROPE_LIST, 1),
    'Africa': Game('Asia', gl.AFRICA_MAP, AFRICA_LIST, 1),
    'Asia': Game('SouthAmerica', gl.ASIA_MAP, ASIA_LIST, 1),
    'SouthAmerica': Game(
        'NorthAmerica', gl.SOUTHAMERICA_MAP, SOUTHAMERICA_LIST, 1),
    'NorthAmerica': Game(
        'AustraliaOceania', gl.NORTHAMERICA_MAP, NORTHAMERICA_LIST, 1),
    'AustraliaOceania': Game(
        'Europe', gl.AUSTRALIAOCEANIA_MAP, AUSTRALIAOCEANIA_LIST, 1),
    'EuropeCountries': Game(
        'AfricaCountries', gl.EUROPE_MAP, EUROPE_LIST, 2),
    'AfricaCountries': Game(
        'AsiaCountries', gl.AFRICA_MAP2, AFRICA_LIST, 2),
    'AsiaCountries': Game(
        'SouthAmericaCountries', gl.ASIA_MAP2, ASIA_LIST, 2),
    'SouthAmericaCountries': Game(
        'NorthAmericaCountries', gl.SOUTHAMERICA_MAP2, SOUTHAMERICA_LIST, 2),
    'NorthAmericaCountries': Game(
        'AustraliaOceaniaCountries',
        gl.NORTHAMERICA_MAP2, NORTHAMERICA_LIST, 2),
    'AustraliaOceaniaCountries': Game(
        'EuropeCountries', gl.AUSTRALIAOCEANIA_MAP2, AUSTRALIAOCEANIA_LIST, 2),
    }
