import random

import pygame

from . import globs as gl


class FlagQuiz:

    def __init__(self, countries, next_scene):
        self.countries = countries
        self.width, self.height = 800, 600
        self.done = False
        self.scene = None
        self.next_scene = next_scene
        self.active_question = None
        self.active_pos = None
        self.counter = 0
        self.usr_input = ""
        self.score = 0
        self.incorrect_answer = False
        self.last_pos = None
        self.game_over = False
        random.shuffle(self.flags)
        self.wrong_answer = None
        self.backspace_pressed = False
        self.backspace_timer = 20

    def reset(self):
        self.done = False
        self.scene = None
        self.active_question = None
        self.active_pos = None
        self.counter = 0
        self.usr_input = ""
        self.score = 0
        self.incorrect_answer = False
        self.last_pos = None
        self.game_over = False
        self.wrong_answer = None

    def process_events(self, event):
        """Handle events.

        Parameters:
            event: pygame.Event
        """
        if event.type == pygame.QUIT:
            self.done = True

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
            if (event.key == pygame.K_KP_ENTER or
                event.key == pygame.K_RETURN):
                self.next_flag()
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

    def display_frame(self, screen):
        """Render everything.

        Parameters:
            screen: pygame.Surface. The game display.
        """
        screen.fill(gl.WHITE)
        # Blit next flag.
        # Blit points.
        # Blit usr_input.
