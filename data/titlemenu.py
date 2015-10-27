# coding=utf-8

import pygame
from .pygbutton import PygButton
from . import globs as gl


class Title:
    
    def __init__(self):
        self.image = pygame.Surface((640, 480))
        self.game_map = self.image
        self.done = False
        self.next_scene = None
        self.scene = None

    def run_logic(self):
        pass


class TitleMain(Title):

    def __init__(self):
        super().__init__()
        self.button_länder = PygButton((50, 100, 200, 30), 'Länderquiz')
        self.button_hauptstädte = PygButton((50, 150, 200, 30),
                                            'Hauptstadtquiz')
        self.button_quit = PygButton((50, 400, 200, 30), 'Beenden')

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.scene = 'Europe'
            if 'click' in self.button_länder.handleEvent(event):
                self.scene = "TitleCountries"
            if 'click' in self.button_hauptstädte.handleEvent(event):
                self.scene = "TitleCapitals"
            if 'click' in self.button_quit.handleEvent(event):
                self.done = True

    def display_frame(self, screen):
        screen.fill(gl.WHITE)
        start_text = gl.FONT.render("Geographie-Quiz", True, gl.BLACK)
        screen.blit(start_text, [100, 20])
        self.button_länder.draw(screen)
        self.button_hauptstädte.draw(screen)
        self.button_quit.draw(screen)
        pygame.display.flip()


class TitleCountries(Title):
    """The title menu for country quizzes."""

    def __init__(self):
        super().__init__()
        self.button_europe = PygButton((50, 100, 200, 30), 'Europas Länder')
        self.button_africa = PygButton((50, 150, 200, 30), 'Afrikas Länder')
        self.button_asia = PygButton((50, 200, 200, 30), 'Asiens Länder')
        self.button_southamerica = PygButton(
            (50, 250, 200, 30), 'Südamerikas Länder')
        self.button_northamerica = PygButton(
            (50, 300, 200, 30), 'Nordamerikas Länder')
        self.button_australiaoceania = PygButton(
            (50, 350, 260, 30), 'Australiens u. Ozeaniens Länder')
        self.button_main = PygButton((50, 400, 200, 30), 'Hauptmenü')
        self.button_quit = PygButton((50, 450, 200, 30), 'Beenden')

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.scene = "TitleMain"
                if event.key == pygame.K_LEFT:
                    self.scene = 'Europe'
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

    def display_frame(self, screen):
        screen.fill(gl.WHITE)
        start_text = (gl.FONT.render("Länder-Quiz", True, gl.BLACK))
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


class TitleCapitals(Title):
    """The title menu for capital quizzes."""

    def __init__(self):
        super().__init__()
        self.button_europe = PygButton(
            (50, 100, 200, 30), 'Europas Hauptstädte')
        self.button_africa = PygButton(
            (50, 150, 200, 30), 'Afrikas Hauptstädte')
        self.button_asia = PygButton(
            (50, 200, 200, 30), 'Asiens Hauptstädte')
        self.button_southamerica = PygButton(
            (50, 250, 200, 30), 'Südamerikas Hauptstädte')
        self.button_northamerica = PygButton(
            (50, 300, 200, 30), 'Nordamerikas Hauptstädte')
        self.button_australiaoceania = PygButton(
            (50, 350, 260, 30), 'Australiens u. Ozeaniens Hauptstädte')
        self.button_main = PygButton(
            (50, 400, 200, 30), 'Hauptmenü')
        self.button_quit = PygButton(
            (50, 450, 200, 30), 'Beenden')

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.scene = "TitleMain"
                if event.key == pygame.K_LEFT:
                    self.scene = 'Europe'
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

    def display_frame(self, screen):
        screen.fill(gl.WHITE)
        start_text = (gl.FONT.render("Hauptstädte-Quiz", True, gl.BLACK))
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