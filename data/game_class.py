"""Game classes for country and capital quizzes."""

import random

import pygame

from . import globs as gl


class Game:
    """Game class for country and capital quizzes.

    Attributes:
        usr_input (str): Currently entered name of country/capital.
        quiz_type (int): 1 for capital, 2 for country quiz.
        next_scene (str): Switch to this scene if left arrow pressed.
        counter (int): Index of current active country/capital.
    """

    def __init__(self, next_scene, game_map, country_list, quiz_type):
        self.width, self.height = game_map.get_size()
        self.done = False
        self.scene = None
        self.next_scene = next_scene
        self.game_map = game_map
        self.active_question = None
        self.active_pos = None
        # Use 1 for capital and 2 for country quiz. Used as index of lists.
        self.quiz_type = quiz_type
        self.counter = 0
        self.usr_input = ""
        self.score = 0
        self.incorrect_answer = False
        self.last_pos = None
        self.game_over = False
        # Used to manually mark positions of cities on the map.
    #     marker_list = []
    #     marker_count = 0
        pygame.display.set_caption(_('Länderquiz'))
        random.shuffle(country_list)
        self.country_list = country_list
        self.wrong_answer = None
        self.backspace_pressed = False
        self.backspace_timer = 20
        self.question_offset = 0

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
                self.usr_input += event.unicode
            if event.key == pygame.K_SPACE:
                self.usr_input += " "
            if event.key == pygame.K_SLASH:
                self.usr_input += "-"
            if event.key == pygame.K_PERIOD:
                self.usr_input += "."
            if event.key == pygame.K_COMMA:
                self.usr_input += ","
            if event.key == 92:
                self.usr_input += "'"
            if event.key == pygame.K_RIGHT:
                self.scene = self.next_scene
            # TODO: Add question skipping?
            if (event.key == pygame.K_KP_ENTER or
                event.key == pygame.K_RETURN):
                self.next_country()
            if event.key == pygame.K_BACKSPACE:
                self.backspace_timer = 20
                self.usr_input = self.usr_input[:-1]
                self.backspace_pressed = True
            # Skip country. Debugging.
            if event.key == pygame.K_0:
                if not self.game_over:
                    self.counter += 1
                    self.usr_input = ""
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_BACKSPACE:
                self.backspace_pressed = False

    def run_logic(self):
        if self.backspace_pressed:
            self.backspace_timer -= 1
            self.del_letters()
        # Check if game is over.
        if len(self.country_list) == self.counter:
            self.game_over = True
        self.change_question()

    def display_frame(self, screen):
        """Render everything.

        Parameters:
            screen: pygame.Surface. The game display.
        """
        screen.fill(gl.WHITE)
        screen.blit(self.game_map, (0, 0))
        self.render_score(screen)
        self.render_game_over(screen)
        self.render_incorrect_answer(screen)
        if not self.incorrect_answer:
            self.render_active_question(screen)
        pygame.draw.rect(screen, gl.BLACK, (0, 0, self.width, self.height), 2)

    def next_country(self):
        """Switch to next country."""
        if not self.game_over and not self.incorrect_answer:
            if self.check_input():
                self.score += 1
            else:
                self.incorrect_answer = True
                self.wrong_answer = self.usr_input
            self.counter += 1
        elif self.incorrect_answer:
            self.incorrect_answer = False
        self.usr_input = ""

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
            self.usr_input = self.usr_input[:-1]
            self.backspace_timer = 2

    def check_input(self):
        """Checks if active name equals name."""
        # Is either a tuple or a string.
        correct_answer = self.country_list[self.counter][self.quiz_type]
        try:
            if self.usr_input.lower() == _(correct_answer).lower():
                gl.win_sound.play()
                return True
        # correct_answer was a tuple.
        except AttributeError:
            correct_answer = (_(answ).lower() for answ in correct_answer)
            if self.usr_input.lower() in correct_answer:
                gl.win_sound.play()
                return True
        gl.fail_sound.play()
        return False

    def render_score(self, screen):
        try:
            percent = round(100 / self.counter * self.score, 2)
        except ZeroDivisionError:
            percent = 0

        # TODO: Render this when the game ends.
        # txt = "{0} richtige Antworten von {1}. {2} Prozent korrekt".format(
        #     self.score, self.counter, percent)
        # score_txt = gl.FONT.render(txt, True, gl.BLACK)
        # screen.blit(score_txt, (3, 10))

        score_txt = gl.FONT.render(_('Pkte'), True, gl.BLUE)
        screen.blit(score_txt, (self.width + 9, 10))

        txt = "{0}/{1}".format(self.score, self.counter)
        score_txt = gl.FONT.render(txt, True, gl.BLUE)
        screen.blit(score_txt, (self.width + 9, 45))

        perc_txt = gl.FONT.render("{} %".format(int(percent)), True, gl.BLUE)
        screen.blit(perc_txt, (self.width + 9, 80))

    def render_game_over(self, screen):
        if self.game_over:
            txt = _('Spiel beendet - Pfeiltaste rechts für das nächste Quiz,')
            game_over_txt = gl.FONT.render(txt, True, gl.BLUE)

            txt = _('ESC um ins Hauptmenü zu gelangen.')
            game_over_txt2 = gl.FONT.render(txt, True, gl.BLUE)

            screen.blit(game_over_txt, (3, self.height + 2))
            screen.blit(game_over_txt2, (3, self.height + 32))

    def render_active_question(self, screen):
        """Display pointer to active country/capital.

        Parameters:
            screen: pygame.Surface. The game display.
        """
        # Probably used to locate cities.
        # pygame.draw.circle(screen, gl.RED, pygame.mouse.get_pos(), 1)
        if not self.game_over and len(self.country_list) >= self.counter:
            self.render_active_indicator(screen)

            # Why has counter to be > 2?
            if len(self.country_list[self.counter]) > 2:
                self.render_question(screen, self.quiz_type)

    def render_question(self, screen, quiz_type=1):
        if quiz_type == 1:
            active_country = self.country_list[self.counter][2]
            if isinstance(active_country, tuple):
                active_country = active_country[0]
            txt = _('Nennen Sie die Hauptstadt von')
            txt2 = "{}:".format(_(active_country))
            country = gl.FONT.render(txt2, True, gl.BLUE)
            self.question_offset = country.get_width() + 8
            screen.blit(country, (3, self.height + 32))
        else:
            txt = _('Nennen Sie den Namen dieses Landes: ')
        question = gl.FONT.render(txt, True, gl.BLUE)
        screen.blit(question, (3, self.height + 2))

    def render_active_indicator(self, screen):
        """Render the indicator and current user input name.

        Parameters:
            screen (pygame.Surface): The game screen.
        """
        # pygame.draw.circle(screen, gl.BLUE, self.active_position, 4)
        # Short diagonal part.
        x_pos = self.active_pos[0] + 10
        y_pos = self.active_pos[1] - 10

        pos = (x_pos, y_pos)
        pygame.draw.line(screen, gl.BLUE, self.active_pos, pos, 4)

        end_pos = (self.active_pos[0] + 50, y_pos)
        pygame.draw.line(screen, gl.BLUE, pos, end_pos, 4)

        name_text = gl.FONT.render(self.usr_input, True, gl.BLUE)
        pos = (x_pos, self.active_pos[1] - 40)
        screen.blit(name_text, pos)
        screen.blit(name_text, (3 + self.question_offset, self.height + 32))

    def render_incorrect_answer(self, screen):
        if self.incorrect_answer:
            # Red line positions.
            x_pos = self.last_pos[0] - 10
            y_pos = self.last_pos[1] - 10

            pos = (x_pos, y_pos)
            pygame.draw.line(screen, gl.RED, self.last_pos, pos, 4)

            pos_end = (100, y_pos)
            pygame.draw.line(screen, gl.RED, pos, pos_end, 4)

            active = self.country_list[self.counter - 1][self.quiz_type]
            if isinstance(active, tuple):
                active = active[0]
            active = _(active)
            inc_name_text = gl.FONT.render(active, True, gl.RED)
            screen.blit(inc_name_text, [100, self.last_pos[1] - 40])

            if not self.game_over:
                given_answer = _('Ihre Antwort war {}.').format(
                    self.wrong_answer)
                text = gl.FONT.render(given_answer, True, gl.RED)
                screen.blit(text, [3, self.height + 32])

                correct = _('Die korrekte Antwort lautet {}.').format(active)
                text = gl.FONT.render(correct, True, gl.RED)
                screen.blit(text, [3, self.height + 2])
