# coding=utf-8

"""Title menu scenes."""

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
        for y_pos, txt, scne in zip(range(100, 451, 50), button_texts, scenes):
            if txt == 'Beenden' and isinstance(self, TitleMain):
                y_pos = 400
            self.buttons.append((PygButton((50, y_pos, 200, 30), txt), scne))

    def run_logic(self):
        pass

    def display_frame(self, screen):
        screen.fill(gl.WHITE)
        screen.blit(self.start_text, [100, 20])
        for button, _ in self.buttons:
            button.draw(screen)

    def process_events(self, event):
        if event.type == pygame.QUIT:
            self.done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.scene = "TitleMain"
            if event.key == pygame.K_LEFT:
                self.scene = 'Europe'

        for button, scene in self.buttons:
            if 'click' in button.handleEvent(event):
                self.scene = scene
            if self.scene == 'done':
                self.done = True


class TitleMain(Title):
    """Main menu."""

    def __init__(self):
        button_texts = ['Länderquiz', 'Hauptstadtquiz', 'Beenden']
        scenes = ["TitleCountries", "TitleCapitals", "done"]
        super().__init__(button_texts, scenes, "Geographie-Quiz")


class TitleCountries(Title):
    """The title menu for country quizzes."""

    def __init__(self):
        button_texts = [
            'Europas Länder', 'Afrikas Länder', 'Asiens Länder',
            'Südamerikas Länder', 'Nordamerikas Länder',
            'Australiens u. Ozeaniens Länder', 'Hauptmenü', 'Beenden'
            ]
        scenes = [
            "EuropeCountries", "AfricaCountries", "AsiaCountries",
            "SouthAmericaCountries", "NorthAmericaCountries",
            "AustraliaOceaniaCountries", "TitleMain", "done"
            ]
        super().__init__(button_texts, scenes, "Länder-Quiz")


class TitleCapitals(Title):
    """The title menu for capital quizzes."""

    def __init__(self):
        button_texts = [
            'Europas Hauptstädte', 'Afrikas Hauptstädte', 'Asiens Hauptstädte',
            'Südamerikas Hauptstädte', 'Nordamerikas Hauptstädte',
            'Australiens u. Ozeaniens Hauptstädte', 'Hauptmenü', 'Beenden'
            ]
        scenes = [
            "Europe", "Africa", "Asia", "SouthAmerica", "NorthAmerica",
            "AustraliaOceania", "TitleMain", "done"
            ]
        super().__init__(button_texts, scenes, "Hauptstädte-Quizz")
