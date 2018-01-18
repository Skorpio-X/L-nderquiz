import pygame

from . import globs as gl
from .game_class import BaseGame


# TODO: Display if the last answer was correct.
class FlagQuiz(BaseGame):

    def __init__(self, flags, country_list, next_scene):
        super().__init__(country_list, next_scene)
        self.flags = flags
        self.game_map = pygame.Surface((self.width, self.height))
        pygame.display.set_caption(_('Vexilologiequiz'))

    def display_frame(self, screen):
        """Render everything.

        Parameters:
            screen: pygame.Surface. The game display.
        """
        screen.fill((230, 230, 230))
        # Blit next flag.
        if not self.incorrect_answer and not self.game_over:
            # current_flag = self.flags[self.country_list[self.counter][2]]

            # Need to check if two country names are available.
            # country = self.flags[self.country_list[self.counter][2]]
            # current_flag = country if not isinstance(country, tuple) else country[0]
            try:
                current_flag = self.flags[self.country_list[self.counter][2]]
            except KeyError:
                current_flag = self.flags[self.country_list[self.counter][2][0]]
            screen.blit(current_flag, (20, 20))
            self.render_question(screen)
        else:
            # current_flag = self.flags[self.country_list[self.counter - 1][2]]
            # Need to check if two country names are available.
            try:
                current_flag = self.flags[self.country_list[self.counter - 1][2]]
            except KeyError:
                current_flag = self.flags[self.country_list[self.counter - 1][2][0]]
            screen.blit(current_flag, (20, 20))
        # Blit points.
        self.render_score(screen)
        active = self.get_active()
        self.render_incorrect_answer(screen, active)
        # Blit usr_input.
        self.render_game_over(screen)

    def render_question(self, screen):
        txt = _('Welches Land benutzt diese Flagge?')
        country = gl.FONT.render(txt, True, gl.BLUE)
        answer = gl.FONT.render(self.usr_input, True, gl.BLUE)

        screen.blit(country, (10, self.height + 2))
        screen.blit(answer, (10, self.height + 32))
