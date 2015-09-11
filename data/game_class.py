"""Game classes for country and capital quizzes."""

import random
import pygame
import data.pygbutton as pygbutton

from . import globs as gl


def check_text_input(active_name, name):
    """Checks if active name equals name."""
    if active_name.lower() == name.lower():
        return True
    else:
        return False


class Game:
    done = False
    timer = 0
    scene = None
    game_map = None
    active_question = None
    active_position = None
    counter = 0
    country_list = []
    enter = False
    name = ""
    score = 0
    incorrect_answer = False
    last_position = None
    game_over = False
    # Used to mark positions of cities
#     marker_list = []
#     marker_count = 0

    def __init__(self, background, country_list):
        self.background = background
        pygame.display.set_caption('Länderquiz')
        random.shuffle(country_list)
        self.country_list = country_list
        self.false_name = None
        self.next_scene = None


class GameCapitals(Game):
    """Parent game class for capital quizzes."""

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
                if event.key == pygame.K_SLASH:  # or event.key == pygame.K_MINUS:
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
                        if check_text_input(self.country_list[self.counter][1],
                                            self.name):
                            self.score += 1
                            self.name = ""
                            self.incorrect_answer = False
                        else:
                            self.incorrect_answer = True
                            self.false_name = self.name
                            self.name = ""
                if event.key == pygame.K_BACKSPACE:
                    self.name = self.name[:-1]
            elif event.type == pygame.KEYUP:
                if (event.key == pygame.K_KP_ENTER or
                        event.key == pygame.K_RETURN):
                    self.enter = False

    def run_logic(self):
        """Change questions."""
        # self.timer += 1
        # Next country
        if self.enter and len(self.country_list) > self.counter:
            self.counter += 1
            self.enter = False
        if len(self.country_list) == self.counter:
            self.game_over = True

        # --Automatic country changer
#         if self.timer % 3 == 0 and len(self.country_list) - 1 > self.counter:
#             self.counter += 1
#             print(self.country_list[self.counter][1])

        if not self.game_over:
            # city name
            self.active_question = self.country_list[self.counter][1]
            # city position
            self.active_position = self.country_list[self.counter][0]
            self.last_position = self.country_list[self.counter - 1][0]
        if len(self.country_list) == self.counter:
            self.last_position = self.active_position

    def display_frame(self, screen):
        """Blit everything."""
        screen.blit(self.game_map, [0, 0])
#         pygame.draw.circle(screen, gl.RED, pygame.mouse.get_pos(), 1)

        # active question indicator
        if not self.game_over:
            if len(self.country_list) >= self.counter:
                pygame.draw.circle(screen, gl.BLUE, self.active_position, 4)
                pygame.draw.line(screen, gl.BLUE, self.active_position,
                                 [self.active_position[0] + 10,
                                  self.active_position[1] - 10], 4)
                pygame.draw.line(
                    screen, gl.BLUE,
                    [self.active_position[0] + 10,
                     self.active_position[1] - 10],
                    [self.active_position[0] + 50,
                     self.active_position[1] - 10],
                    4
                    )
                name_text = gl.FONT.render(self.name, True, gl.BLUE)
                screen.blit(name_text,
                            [self.active_position[0] + 10,
                             self.active_position[1] - 40]
                            )
                screen.blit(name_text, (3, 70))
                if len(self.country_list[self.counter]) > 2:
                    country_name = gl.FONT.render(
                        "Nenne die Hauptstadt von {}.".format(
                            self.country_list[self.counter][2]), True, gl.GREEN)
                    screen.blit(country_name, [3, 10])
        # display incorrect answer
        if self.incorrect_answer and len(self.country_list) >= self.counter:

            inc_name_text = gl.FONT.render(
                self.country_list[self.counter - 1][1], True, gl.RED)
            screen.blit(inc_name_text,
                        [self.last_position[0] + 10,
                         self.last_position[1] - 22]
                        )
            last_answer = gl.FONT.render(
                "Ihre Antwort war {}".format(self.false_name), True, gl.RED)
            screen.blit(last_answer, [10, self.game_map.get_height() - 60])
            inc_text = gl.FONT.render(
                "Die korrekte Antwort lautet " +
                self.country_list[self.counter - 1][1],
                True, gl.RED)
            screen.blit(inc_text, [10, self.game_map.get_height() - 30])

        try:
            score = round(100 / self.counter * self.score, 2)
        except ZeroDivisionError:
            score = 0
        score_txt = (
            gl.FONT.render(
                "{0} richtige Antworten von {1}. {2} Prozent korrekt".format(
                    self.score, self.counter, score), True, gl.BLACK))
        screen.blit(score_txt, [3, 40])
        if self.game_over:
            game_over_txt = (
                gl.FONT.render(
                    "Spiel beendet - Pfeiltaste links für das nächste Quiz",
                    True, gl.GREEN
                )
            )
            game_over_txt2 = (gl.FONT.render(
                "ESC um ins Hauptmenü zu gelangen", True, gl.GREEN))
            screen.blit(game_over_txt, [20, 70])
            screen.blit(game_over_txt2, [20, 100])

        pygame.display.flip()


class GameCountries(Game):
    """Parent game class for country quizzes."""

    def process_events(self):
        """Handle events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.scene = "TitleMain"
                if event.unicode.isalnum():  # unicode
                    self.name += event.unicode
                if event.key == pygame.K_SPACE:
                    self.name += " "
                if event.key == pygame.K_SLASH:  # or event.key == pygame.K_MINUS:
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
                        if check_text_input(self.country_list[self.counter][2],
                                            self.name):
                            self.score += 1
                            self.name = ""
                            self.incorrect_answer = False
                        else:
                            self.incorrect_answer = True
                            self.false_name = self.name
                            self.name = ""
                if event.key == pygame.K_BACKSPACE:
                    self.name = self.name[:-1]

            elif event.type == pygame.KEYUP:
                if (event.key == pygame.K_KP_ENTER or
                        event.key == pygame.K_RETURN):
                    self.enter = False

    def run_logic(self):
        """Change questions."""
        # Next country
        if self.enter and len(self.country_list) > self.counter:
            self.counter += 1
            self.enter = False
        if len(self.country_list) == self.counter:
            self.game_over = True

        if not self.game_over:
            # city name
            self.active_question = self.country_list[self.counter][2]
            # city position
            self.active_position = self.country_list[self.counter][0]
            self.last_position = self.country_list[self.counter - 1][0]
        if len(self.country_list) == self.counter:
            self.last_position = self.active_position

    def display_frame(self, screen):
        """Blit everything."""
        screen.blit(self.game_map, [0, 0])

        score_txt = (
            gl.FONT.render(
                "{0} richtige Antworten von {1}. {2} Prozent korrekt".format(
                    self.score, self.counter,
                    round(100 / (self.counter + 0.0000001) * self.score, 2)
                ), True, gl.BLACK
            )
        )
        screen.blit(score_txt, [3, 40])

        # display incorrect answer
        if self.incorrect_answer and len(self.country_list) >= self.counter:
            pygame.draw.line(screen, gl.RED, self.last_position,
                             [self.last_position[0] - 10,
                              self.last_position[1] - 10], 4)
            pygame.draw.line(screen, gl.RED,
                             [100, self.last_position[1] - 10],
                             [self.last_position[0] - 10,
                              self.last_position[1] - 10], 4)
            inc_name_text = gl.FONT.render(
                self.country_list[self.counter - 1][2], True, gl.RED)
#             screen.blit(inc_name_text, [self.last_position[0] -
#                 len(self.country_list[self.counter - 1][2]) * 10,
#                                   self.last_position[1] - 40])
            screen.blit(inc_name_text, [100,
                        self.last_position[1] - 40])
            last_answer = gl.FONT.render(
                "Ihre Antwort war {}".format(self.false_name), True, gl.RED)
            screen.blit(last_answer, [10, self.game_map.get_height() - 60])
            inc_text = gl.FONT.render(
                "Die korrekte Antwort lautet " +
                self.country_list[self.counter - 1][2],
                True, gl.RED)
            screen.blit(inc_text, [10, self.game_map.get_height() - 30])

        if self.game_over:
            game_over_txt = gl.FONT.render(
                "Spiel beendet - Pfeiltaste links für das nächste Quiz",
                True, gl.GREEN)
            game_over_txt2 = gl.FONT.render(
                "ESC um ins Hauptmenü zu gelangen", True, gl.GREEN)
            screen.blit(game_over_txt, [20, 70])
            screen.blit(game_over_txt2, [20, 100])

        # active question indicator
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
                if len(self.country_list[self.counter]) > 2:
                    question = gl.FONT.render(
                        "Nenne den Namen dieses Landes ", True, gl.GREEN)
                    screen.blit(question, [3, 10])

        pygame.display.flip()


class Europe(GameCapitals):
    game_map = gl.EUROPE_MAP
    scene = None
    next_scene = "Africa"

    def __init__(self, background, country_list):
        Game.__init__(self, background, country_list)


class Africa(GameCapitals):
    game_map = gl.AFRICA_MAP
    scene = None
    next_scene = "Asia"

    def __init__(self, background, country_list):
        Game.__init__(self, background, country_list)


class Asia(GameCapitals):
    game_map = gl.ASIA_MAP
    scene = None
    next_scene = "SouthAmerica"

    def __init__(self, background, country_list):
        Game.__init__(self, background, country_list)


class SouthAmerica(GameCapitals):
    game_map = gl.SOUTHAMERICA_MAP
    scene = None
    next_scene = "NorthAmerica"

    def __init__(self, background, country_list):
        Game.__init__(self, background, country_list)


class NorthAmerica(GameCapitals):
    game_map = gl.NORTHAMERICA_MAP
    scene = None
    next_scene = "AustraliaOceania"

    def __init__(self, background, country_list):
        Game.__init__(self, background, country_list)


class AustraliaOceania(GameCapitals):
    game_map = gl.AUSTRALIAOCEANIA_MAP
    scene = None
    next_scene = "Europe"

    def __init__(self, background, country_list):
        Game.__init__(self, background, country_list)


class EuropeCountries(GameCountries):
    game_map = gl.EUROPE_MAP
    scene = None
    next_scene = "AfricaCountries"

    def __init__(self, background, country_list):
        Game.__init__(self, background, country_list)


class AfricaCountries(GameCountries):
    game_map = gl.AFRICA_MAP2
    scene = None
    next_scene = "AsiaCountries"

    def __init__(self, background, country_list):
        Game.__init__(self, background, country_list)


class AsiaCountries(GameCountries):
    game_map = gl.ASIA_MAP2
    scene = None
    next_scene = "SouthAmericaCountries"

    def __init__(self, background, country_list):
        Game.__init__(self, background, country_list)


class SouthAmericaCountries(GameCountries):
    game_map = gl.SOUTHAMERICA_MAP2
    scene = None
    next_scene = "NorthAmericaCountries"

    def __init__(self, background, country_list):
        Game.__init__(self, background, country_list)


class NorthAmericaCountries(GameCountries):
    game_map = gl.NORTHAMERICA_MAP2
    scene = None
    next_scene = "AustraliaOceaniaCountries"

    def __init__(self, background, country_list):
        Game.__init__(self, background, country_list)


class AustraliaOceaniaCountries(GameCountries):
    game_map = gl.AUSTRALIAOCEANIA_MAP2
    scene = None
    next_scene = "EuropeCountries"

    def __init__(self, background, country_list):
        Game.__init__(self, background, country_list)

# class Title():
#     done = False
#     next_scene = "Europe"
#     scene = None


class TitleMain:
    done = False
    next_scene = "Europe"
    scene = None
    button_länder = pygbutton.PygButton((50, 100, 200, 30),
                                        'Länderquiz')
    button_hauptstädte = pygbutton.PygButton((50, 150, 200, 30),
                                             'Hauptstadtquiz')
    button_quit = pygbutton.PygButton((50, 400, 200, 30),
                                      'Beenden')

    def __init__(self):
        self.image = pygame.Surface((640, 480))

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.scene = self.next_scene
            if 'click' in self.button_länder.handleEvent(event):
                self.scene = "TitleCountries"
            if 'click' in self.button_hauptstädte.handleEvent(event):
                self.scene = "TitleCapitals"
            if 'click' in self.button_quit.handleEvent(event):
                self.done = True

    def run_logic(self):
        pass

    def display_frame(self, screen):
        screen.fill(gl.WHITE)
        start_text = gl.FONT.render(
            "Geographie-Quiz", True, gl.BLACK)
        screen.blit(start_text, [100, 20])
        self.button_länder.draw(screen)
        self.button_hauptstädte.draw(screen)
        self.button_quit.draw(screen)
        pygame.display.flip()


class TitleCountries:
    """The title menu for country quizzes."""
    done = False
    next_scene = "Europe"
    scene = None
    button_europe = pygbutton.PygButton(
        (50, 100, 200, 30), 'Europas Länder')
    button_africa = pygbutton.PygButton(
        (50, 150, 200, 30), 'Afrikas Länder')
    button_asia = pygbutton.PygButton(
        (50, 200, 200, 30), 'Asiens Länder')
    button_southamerica = pygbutton.PygButton(
        (50, 250, 200, 30), 'Südamerikas Länder')
    button_northamerica = pygbutton.PygButton(
        (50, 300, 200, 30), 'Nordamerikas Länder')
    button_australiaoceania = pygbutton.PygButton(
        (50, 350, 260, 30), 'Australiens u. Ozeaniens Länder')
    button_main = pygbutton.PygButton(
        (50, 400, 200, 30), 'Hauptmenü')
    button_quit = pygbutton.PygButton(
        (50, 450, 200, 30), 'Beenden')

    def __init__(self):
        self.image = pygame.Surface((640, 480))

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.scene = "TitleMain"
                if event.key == pygame.K_LEFT:
                    self.scene = self.next_scene
            if 'click' in self.button_europe.handleEvent(event):
                self.scene = "EuropeCountries"
            if 'click' in self.button_africa.handleEvent(event):
                self.scene = "AfricaCountries"
            if 'click' in self.button_asia.handleEvent(event):
                self.scene = "AsiaCountries"
            if 'click' in self.button_southamerica.handleEvent(event):
                self.scene = "SouthAmericaCountries"
            if 'click' in self.button_northamerica.handleEvent(event):
                self.scene = "NorthAmericaCountries"
            if 'click' in self.button_australiaoceania.handleEvent(event):
                self.scene = "AustraliaOceaniaCountries"
            if 'click' in self.button_main.handleEvent(event):
                self.scene = "TitleMain"
            if 'click' in self.button_quit.handleEvent(event):
                self.done = True

    def run_logic(self):
        pass

    def display_frame(self, screen):
        screen.fill(gl.WHITE)
        start_text = (gl.FONT.render(
            "Länder-Quiz", True, gl.BLACK))
        screen.blit(start_text, [100, 20])
        self.button_europe.draw(screen)
        self.button_africa.draw(screen)
        self.button_asia.draw(screen)
        self.button_southamerica.draw(screen)
        self.button_northamerica.draw(screen)
        self.button_australiaoceania.draw(screen)
        self.button_main.draw(screen)
        self.button_quit.draw(screen)
        pygame.display.flip()


class TitleCapitals:
    """The title menu for capital quizzes."""
    done = False
    next_scene = "Europe"
    scene = None
    button_europe = pygbutton.PygButton(
        (50, 100, 200, 30), 'Europas Hauptstädte')
    button_africa = pygbutton.PygButton(
        (50, 150, 200, 30), 'Afrikas Hauptstädte')
    button_asia = pygbutton.PygButton(
        (50, 200, 200, 30), 'Asiens Hauptstädte')
    button_southamerica = pygbutton.PygButton(
        (50, 250, 200, 30), 'Südamerikas Hauptstädte')
    button_northamerica = pygbutton.PygButton(
        (50, 300, 200, 30), 'Nordamerikas Hauptstädte')
    button_australiaoceania = pygbutton.PygButton(
        (50, 350, 260, 30), 'Australiens u. Ozeaniens Hauptstädte')
    button_main = pygbutton.PygButton(
        (50, 400, 200, 30), 'Hauptmenü')
    button_quit = pygbutton.PygButton(
        (50, 450, 200, 30), 'Beenden')

    def __init__(self):
        self.image = pygame.Surface((640, 480))

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.scene = "TitleMain"
                if event.key == pygame.K_LEFT:
                    self.scene = self.next_scene
            if 'click' in self.button_europe.handleEvent(event):
                self.scene = "Europe"
            if 'click' in self.button_africa.handleEvent(event):
                self.scene = "Africa"
            if 'click' in self.button_asia.handleEvent(event):
                self.scene = "Asia"
            if 'click' in self.button_southamerica.handleEvent(event):
                self.scene = "SouthAmerica"
            if 'click' in self.button_northamerica.handleEvent(event):
                self.scene = "NorthAmerica"
            if 'click' in self.button_australiaoceania.handleEvent(event):
                self.scene = "AustraliaOceania"
            if 'click' in self.button_main.handleEvent(event):
                self.scene = "TitleMain"
            if 'click' in self.button_quit.handleEvent(event):
                self.done = True

    def run_logic(self):
        pass

    def display_frame(self, screen):
        screen.fill(gl.WHITE)
        start_text = (gl.FONT.render(
            "Hauptstädte-Quiz", True, gl.BLACK))
        screen.blit(start_text, [100, 20])
        self.button_europe.draw(screen)
        self.button_africa.draw(screen)
        self.button_asia.draw(screen)
        self.button_southamerica.draw(screen)
        self.button_northamerica.draw(screen)
        self.button_australiaoceania.draw(screen)
        self.button_main.draw(screen)
        self.button_quit.draw(screen)
        pygame.display.flip()
