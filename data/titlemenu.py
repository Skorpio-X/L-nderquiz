"""Title menu scenes."""

import gettext

import pygame

from .pygbutton import PygButton
from . import globs as gl


class Title:
    """Parent class for menus."""

    def __init__(self, button_texts, scenes, start_text):
        self.image = pygame.Surface((640, 480))
        self.game_map = self.image
        self.done = False
        self.next_scene = None
        self.scene = None
        self.buttons = []
        self.start_text = gl.FONT.render(start_text, True, gl.BLACK)
        for y_pos, txt, scne in zip(range(100, 501, 50), button_texts, scenes):
            if txt == _('Beenden') and isinstance(self, TitleMain):
                y_pos = 400
            self.buttons.append((PygButton((50, y_pos, 260, 30), txt), scne))

    def run_logic(self):
        pass

    def display_frame(self, screen):
        screen.fill(gl.WHITE)
        # Flags as background.
        # offset = 0
        # for i, flag in enumerate(gl.FLAGS_EUROPE.values()):
        #     flag = pygame.transform.scale(flag, (80, 40))
        #     screen.blit(flag, (180 * (i % 4), 80 * offset))
        #     if i % 7 == 6:
        #         offset += 1
        # screen.blit(gl.FLAGS_EUROPE['Türkei'], (300, 100))

        screen.blit(self.start_text, [100, 20])
        for button, _ in self.buttons:
            button.draw(screen)

    def process_events(self, event):
        if event.type == pygame.QUIT:
            self.done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.scene = 'TitleMain'
            if event.key == pygame.K_RIGHT:
                self.scene = 'Europe'
        self.check_button_clicks(event)

    def check_button_clicks(self, event):
        for button, scene in self.buttons:
            if 'click' in button.handle_event(event):
                self.scene = scene
            if self.scene == 'done':
                self.done = True

    def reset(self):
        self.scene = None


class TitleMain(Title):
    """Main menu."""

    def __init__(self):
        button_texts = (
            _('Länderquiz'), _('Hauptstadtquiz'), _('Flaggenquiz'),
            _('Optionen'), _('Beenden')
            )
        scenes = ('TitleCountries', 'TitleCapitals', 'TitleFlags', 'Options',
                  'done')
        super().__init__(button_texts, scenes, _('Geographie-Quiz'))


class TitleCountries(Title):
    """The title menu for country quizzes."""

    def __init__(self):
        button_texts = (
            _('Europas Länder'), _('Afrikas Länder'), _('Asiens Länder'),
            _('Südamerikas Länder'), _('Nordamerikas Länder'),
            _('Australiens/Ozeaniens Länder'), _('Hauptmenü'), _('Beenden')
            )
        scenes = (
            'EuropeCountries', 'AfricaCountries', 'AsiaCountries',
            'SouthAmericaCountries', 'NorthAmericaCountries',
            'AustraliaOceaniaCountries', 'TitleMain', 'done'
            )
        super().__init__(button_texts, scenes, _('Länder-Quiz'))


class TitleCapitals(Title):
    """The title menu for capital quizzes."""

    def __init__(self):
        button_texts = (
            _('Europas Hauptstädte'),
            _('Afrikas Hauptstädte'),
            _('Asiens Hauptstädte'),
            _('Südamerikas Hauptstädte'),
            _('Nordamerikas Hauptstädte'),
            _('Australiens/Ozeaniens Hauptstädte'),
            _('Hauptmenü'),
            _('Beenden')
            )
        scenes = (
            'Europe', 'Africa', 'Asia', 'SouthAmerica', 'NorthAmerica',
            'AustraliaOceania', 'TitleMain', 'done'
            )
        super().__init__(button_texts, scenes, _('Hauptstädte-Quiz'))


class TitleFlags(Title):
    """The title menu for capital quizzes."""

    def __init__(self):
        button_texts = (
            _('Europas Flaggen'),
            _('Afrikas Flaggen'),
            _('Asiens Flaggen'),
            _('Südamerikas Flaggen'),
            _('Nordamerikas Flaggen'),
            _('Australiens/Ozeaniens Flaggen'),
            _('Hauptmenü'),
            _('Beenden')
            )
        scenes = (
            'EuropeFlags', 'AfricaFlags', 'AsiaFlags', 'SouthAmericaFlags',
            'NorthAmericaFlags', 'AustraliaOceaniaFlags', 'TitleMain', 'done'
            )
        super().__init__(button_texts, scenes, _('Flaggenquiz'))


class Options(Title):
    """The options menu."""

    def __init__(self):
        button_texts = ('Deutsch', 'English', _('Hauptmenü'))
        languages = ('Deutsch', 'English', 'TitleMain')
        self.language = 'English'
        super().__init__(button_texts, languages, _('Optionen'))

    def display_frame(self, screen):
        super().display_frame(screen)
        txt = gl.FONT.render(_('Sprache'), True, gl.BLACK)
        screen.blit(txt, (100, 50))
        txt2 = gl.FONT.render(self.language, True, gl.BLACK)
        offset = txt.get_width() + 10
        screen.blit(txt2, (100 + offset, 50))

    def check_button_clicks(self, event):
        for button, scene in self.buttons:
            if 'click' in button.handle_event(event):
                if scene == 'TitleMain':
                    self.scene = scene
                elif scene == 'Deutsch':
                    gettext.install('quiz')
                    self.language = 'Deutsch'
                    self.scene = None
                elif scene == 'English':
                    gl.en.install()
                    self.language = 'English'
                    self.scene = None
