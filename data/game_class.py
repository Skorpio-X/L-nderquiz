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

    def __init__(self, next_scene, game_map, country_list, quiz_type):
        self.done = False
        self.timer = 0
        self.scene = None
        self.game_map = game_map
        self.active_question = None
        self.active_pos = None
        # Use 1 for capital and 2 for country quiz. Used as index of lists.
        self.quiz_type = quiz_type
        self.counter = 0
        self.country_list = []
        self.enter = False
        self.name = ""
        self.next_scene = next_scene
        self.score = 0
        self.incorrect_answer = False
        self.last_pos = None
        self.game_over = False
        # Used to manually mark positions of cities on the map.
    #     marker_list = []
    #     marker_count = 0
        pygame.display.set_caption('Länderquiz')
        random.shuffle(country_list)
        self.country_list = country_list
        self.false_name = None
        self.backspace_pressed = False
        self.backspace_timer = 20

    def process_events(self, event):
        """Handle events.

        Parameters:
            event: pygame.Event
        """
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
        self.check_game_over()
        self.change_question()

    def display_frame(self, screen):
        """Render everything.

        Parameters:
            screen: pygame.Surface
        """
        screen.blit(self.game_map, (0, 0))
        self.render_score(screen)
        self.render_active_question(screen)
        self.render_game_over(screen)
        self.render_incorrect_answer(screen)

    def next_country(self):
        if self.enter and len(self.country_list) > self.counter:
            self.counter += 1
            self.enter = False

    def check_game_over(self):
        if len(self.country_list) == self.counter:
            self.game_over = True

    def change_question(self):
        if not self.game_over:
            # Country/capital name.
            question = self.country_list[self.counter][self.quiz_type]
            self.active_question = question
            # Country/capital position.
            self.active_pos = self.country_list[self.counter][0]
            self.last_pos = self.country_list[self.counter - 1][0]
        if len(self.country_list) == self.counter:
            self.last_pos = self.active_pos

    def del_letters(self):
        """When backspace is pressed continuously delete letters."""
        if self.backspace_timer <= 0:
            self.name = self.name[:-1]
            self.backspace_timer = 2

    def check_input(self):
        """Checks if active name equals name."""
        if self.country_list[self.counter][
                self.quiz_type].lower() == self.name.lower():
            gl.win_sound.play()
            return True
        else:
            gl.fail_sound.play()
            return False

    def render_score(self, screen):
        score = self.calculate_score()
        txt = "{0} richtige Antworten von {1}. {2} Prozent korrekt".format(
            self.score, self.counter, score)
        score_txt = gl.FONT.render(txt, True, gl.BLACK)
        screen.blit(score_txt, (3, 40))

    def calculate_score(self):
        try:
            return round(100 / self.counter * self.score, 2)
        except ZeroDivisionError:
            return 0

    def render_game_over(self, screen):
        if self.game_over:
            txt = "Spiel beendet - Pfeiltaste links für das nächste Quiz"
            game_over_txt = gl.FONT.render(txt, True, gl.GREEN)

            txt = "ESC um ins Hauptmenü zu gelangen"
            game_over_txt2 = gl.FONT.render(txt, True, gl.GREEN)

            screen.blit(game_over_txt, (20, 70))
            screen.blit(game_over_txt2, (20, 100))

    def render_active_question(self, screen):
        """Display pointer to active country/capital.

        Parameters:
            screen: pygame.Surface. The game display.
        """
        # Probably used to locate cities.
        # pygame.draw.circle(screen, gl.RED, pygame.mouse.get_pos(), 1)
        if not self.game_over and len(self.country_list) >= self.counter:
            self.render_active_indicator(screen)

            # For country quiz.
            if self.country_active():
                self.render_country_question(screen)
            # For capital quiz.
            elif self.capital_active():
                self.render_capital_question(screen)

    def capital_active(self):
        counter_greater2 = len(self.country_list[self.counter]) > 2
        return counter_greater2 and self.quiz_type == 1

    def country_active(self):
        counter_greater2 = len(self.country_list[self.counter]) > 2
        return counter_greater2 and self.quiz_type == 2

    @staticmethod
    def render_country_question(screen):
        question_txt = "Nenne den Namen dieses Landes "
        question = gl.FONT.render(question_txt, True, gl.GREEN)
        screen.blit(question, (3, 10))

    def render_capital_question(self, screen):
        active_country = self.country_list[self.counter][2]
        txt = "Nenne die Hauptstadt von {}.".format(active_country)
        country_name = gl.FONT.render(txt, True, gl.GREEN)
        screen.blit(country_name, [3, 10])

    def render_active_indicator(self, screen):
        # pygame.draw.circle(screen, gl.BLUE, self.active_position, 4)
        # Short diagonal part.
        x_pos = self.active_pos[0] + 10
        y_pos = self.active_pos[1] - 10

        pos = (x_pos, y_pos)
        pygame.draw.line(screen, gl.BLUE, self.active_pos, pos, 4)

        end_pos = (self.active_pos[0] + 50, y_pos)
        pygame.draw.line(screen, gl.BLUE, pos, end_pos, 4)

        name_text = gl.FONT.render(self.name, True, gl.BLUE)
        pos = (x_pos, self.active_pos[1] - 40)
        screen.blit(name_text, pos)
        screen.blit(name_text, (3, 70))

    def render_incorrect_answer(self, screen):
        not_done = len(self.country_list) >= self.counter
        if self.incorrect_answer and not_done:
            # Red line positions.
            x_pos = self.last_pos[0] - 10
            y_pos = self.last_pos[1] - 10

            pos = (x_pos, y_pos)
            pygame.draw.line(screen, gl.RED, self.last_pos, pos, 4)

            pos_end = (100, y_pos)
            pygame.draw.line(screen, gl.RED, pos, pos_end, 4)

            active = self.country_list[self.counter - 1][self.quiz_type]
            inc_name_text = gl.FONT.render(active, True, gl.RED)
            screen.blit(inc_name_text, [100, self.last_pos[1] - 40])

            given_answer = "Ihre Antwort war {}".format(self.false_name)
            wrong_answer = gl.FONT.render(given_answer, True, gl.RED)
            screen.blit(wrong_answer, [10, self.game_map.get_height() - 60])

            correct = "Die korrekte Antwort lautet {}".format(active)
            text = gl.FONT.render(correct, True, gl.RED)
            screen.blit(text, [10, self.game_map.get_height() - 30])

# TODO: Persistent objects mean that active question markers don't get reset.
# TODO: You can play each quiz only once.
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
        'NorthAmericaCountries',
        gl.SOUTHAMERICA_MAP2,
        SOUTHAMERICA_LIST, 2),
    'NorthAmericaCountries': Game(
        'AustraliaOceaniaCountries',
        gl.NORTHAMERICA_MAP2,
        NORTHAMERICA_LIST, 2),
    'AustraliaOceaniaCountries': Game(
        'EuropeCountries',
        gl.AUSTRALIAOCEANIA_MAP2,
        AUSTRALIAOCEANIA_LIST, 2),
    }
