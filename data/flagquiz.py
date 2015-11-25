import random

import pygame

from . import globs as gl
from .game_class import BaseGame


class FlagQuiz(BaseGame):

    def __init__(self, flags, country_list, next_scene):
        self.flags = flags
        self.country_list = country_list
        self.width, self.height = 800, 600
        self.game_map = pygame.Surface((self.width, self.height))
        self.done = False
        self.scene = None
        self.next_scene = next_scene
        self.counter = 0
        self.usr_input = ""
        self.score = 0
        self.incorrect_answer = False
        self.game_over = False
        random.shuffle(self.country_list)
        self.wrong_answer = None
        self.backspace_pressed = False
        self.backspace_timer = 20
        self.quiz_type = 2  # The country name index.

    # def process_events(self, event):
    #     """Handle events.
    #
    #     Parameters:
    #         event: pygame.Event
    #     """
    #     if event.type == pygame.QUIT:
    #         self.done = True
    #
    #     elif event.type == pygame.KEYDOWN:
    #         if event.key == pygame.K_ESCAPE:
    #             self.scene = "TitleMain"
    #         if event.unicode.isalnum():  # unicode
    #             self.usr_input += event.unicode
    #         if event.key == pygame.K_SPACE:
    #             self.usr_input += " "
    #         if event.key == pygame.K_SLASH:
    #             self.usr_input += "-"
    #         if event.key == pygame.K_PERIOD:
    #             self.usr_input += "."
    #         if event.key == pygame.K_COMMA:
    #             self.usr_input += ","
    #         if event.key == 92:
    #             self.usr_input += "'"
    #         if event.key == pygame.K_RIGHT:
    #             self.scene = self.next_scene
    #         if (event.key == pygame.K_KP_ENTER or
    #             event.key == pygame.K_RETURN):
    #             self.next_country()
    #         if event.key == pygame.K_BACKSPACE:
    #             self.backspace_timer = 20
    #             self.usr_input = self.usr_input[:-1]
    #             self.backspace_pressed = True
    #         # Skip country. Debugging.
    #         if event.key == pygame.K_0:
    #             if not self.game_over:
    #                 self.counter += 1
    #                 self.usr_input = ""
    #     elif event.type == pygame.KEYUP:
    #         if event.key == pygame.K_BACKSPACE:
    #             self.backspace_pressed = False

    # def run_logic(self):
    #     if self.backspace_pressed:
    #         self.backspace_timer -= 1
    #         self.del_letters()
    #     # Check if game is over.
    #     if len(self.country_list) == self.counter:
    #         self.game_over = True

    def display_frame(self, screen):
        """Render everything.

        Parameters:
            screen: pygame.Surface. The game display.
        """
        screen.fill((230, 230, 230))
        # Blit next flag.
        if not self.incorrect_answer and not self.game_over:
            current_flag = self.flags[self.country_list[self.counter][2]]
            screen.blit(current_flag, (20, 20))
            self.render_question(screen)
        else:
            current_flag = self.flags[self.country_list[self.counter - 1][2]]
            screen.blit(current_flag, (20, 20))
        # Blit points.
        self.render_score(screen)
        active = self.get_active()
        self.render_incorrect_answer(screen, active)
        # Blit usr_input.
        self.render_game_over(screen)

    # def del_letters(self):
    #     """When backspace is pressed continuously delete letters."""
    #     if self.backspace_timer <= 0:
    #         self.usr_input = self.usr_input[:-1]
    #         self.backspace_timer = 2

    # def next_country(self):
    #     """Switch to next country."""
    #     if not self.game_over and not self.incorrect_answer:
    #         if self.check_input():
    #             self.score += 1
    #         else:
    #             self.incorrect_answer = True
    #             self.wrong_answer = self.usr_input
    #         self.counter += 1
    #     elif self.incorrect_answer:
    #         self.incorrect_answer = False
    #     self.usr_input = ""

    # def check_input(self):
    #     """Checks if active name equals name."""
    #     # Is either a tuple or a string.
    #     correct_answer = self.country_list[self.counter][self.quiz_type]
    #     try:
    #         if self.usr_input.lower() == _(correct_answer).lower():
    #             gl.win_sound.play()
    #             return True
    #     # correct_answer was a tuple.
    #     except AttributeError:
    #         correct_answer = (_(answ).lower() for answ in correct_answer)
    #         if self.usr_input.lower() in correct_answer:
    #             gl.win_sound.play()
    #             return True
    #     gl.fail_sound.play()
    #     return False

    # def check_input(self):
    #     """Checks if active name equals name."""
    #     # Is either a tuple or a string.
    #     correct_answer = self.country_list[self.counter][self.quiz_type]
    #     try:
    #         correct = self.usr_input.lower() == _(correct_answer).lower()
    #     # correct_answer was a tuple.
    #     except AttributeError:
    #         correct_answer = {_(answ).lower() for answ in correct_answer}
    #         correct = self.usr_input.lower() in correct_answer
    #     if correct:
    #         gl.win_sound.play()
    #         return True
    #     else:
    #         gl.fail_sound.play()
    #         return False

    # def check_input(self):
    #     """Checks if active name equals name."""
    #     # Is either a tuple or a string.
    #     correct_answer = self.country_list[self.counter][self.quiz_type]
    #     if isinstance(correct_answer, tuple):
    #         correct_answer = (_(answ).lower() for answ in correct_answer)
    #         correct = self.usr_input.lower() in correct_answer
    #     else:
    #         correct = self.usr_input.lower() == _(correct_answer).lower()
    #     if correct:
    #         gl.win_sound.play()
    #         return True
    #     else:
    #         gl.fail_sound.play()
    #         return False

    def render_question(self, screen):
        txt = _('Welches Land hat diese Flagge?')
        country = gl.FONT.render(txt, True, gl.BLUE)
        answer = gl.FONT.render(self.usr_input, True, gl.BLUE)

        screen.blit(country, (10, self.height + 2))
        screen.blit(answer, (10, self.height + 32))

    def render_score(self, screen):
        percent = self.calc_percent()

        txt = "{0}/{1}".format(self.score, self.counter)
        txt2 = "{} %".format(int(percent))

        score_txt = gl.FONT.render(_('Pkte'), True, gl.BLUE)
        score_txt2 = gl.FONT.render(txt, True, gl.BLUE)
        perc_txt = gl.FONT.render(txt2, True, gl.BLUE)

        screen.blit(score_txt, (self.width - 20, 10))
        screen.blit(score_txt2, (self.width - 20, 45))
        screen.blit(perc_txt, (self.width - 20, 80))

    def render_incorrect_answer(self, screen, active):
        if not self.game_over and self.incorrect_answer:
            given_answer = _('Ihre Antwort war {}.').format(self.wrong_answer)
            correct = _('Die korrekte Antwort lautet {}.').format(active)

            text = gl.FONT.render(given_answer, True, gl.RED)
            text2 = gl.FONT.render(correct, True, gl.RED)

            screen.blit(text, (10, self.height + 2))
            screen.blit(text2, (10, self.height + 32))

    # def render_game_over(self, screen):
    #     if self.game_over:
    #         txt = _('Spiel beendet - Pfeiltaste rechts für das nächste Quiz,')
    #         txt2 = _('ESC um ins Hauptmenü zu gelangen.')
    #
    #         game_over_txt = gl.FONT.render(txt, True, gl.BLUE)
    #         game_over_txt2 = gl.FONT.render(txt2, True, gl.BLUE)
    #
    #         screen.blit(game_over_txt, (10, self.height + 2))
    #         screen.blit(game_over_txt2, (10, self.height + 32))

    # def calc_percent(self):
    #     try:
    #         percent = round(100 / self.counter * self.score, 2)
    #     except ZeroDivisionError:
    #         percent = 0
    #     return percent

    # def get_active(self):
    #     active = self.country_list[self.counter - 1][self.quiz_type]
    #     if isinstance(active, tuple):
    #         active = active[0]
    #     return _(active)
