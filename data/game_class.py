import random
import pygbutton

from .globs import *
#import data.lists
from data.lists.europe_list import europe_list
from data.lists.africa_list import africa_list
from data.lists.asia_list import asia_list
from data.lists.southamerica_list import southamerica_list

##from .europe_list import *
##from .africa_list import *
##from .asia_list import *
##from .southamerica_list import *

def check_text_input(active_name, name):
    if active_name.lower() == name.lower():
        return True
    else:
        return False

class Game():
    done = False
    timer = 0
    scene = None
    gamemap = None
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
##    marker_list = []
##    marker_count = 0

    def __init__(self, background, country_list):
        self.background = background
        pygame.display.set_caption('Länderquiz')
        random.shuffle(country_list)
        self.country_list = country_list

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
##                sys.exit()

##            if event.type == pygame.MOUSEBUTTONDOWN:
##                # locate cities on the map
##                print(pygame.mouse.get_pos())
##                mouse_pos = pygame.mouse.get_pos()
##                city = input("Hauptstadt: ")
##                self.marker_list.append([mouse_pos, city])
##                self.marker_count += 1
     
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.scene = "Title"
                if event.unicode.isalnum(): # unicode
                    self.name += event.unicode
                if event.key == pygame.K_SPACE:
                    self.name += " "
                if event.key == pygame.K_MINUS or event.key == pygame.K_SLASH:
                    self.name += "-"
##                if event.key == pygame.K_QUOTE:
##                    self.name += "'"
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
                            self.name = ""
                        
                if event.key == pygame.K_BACKSPACE:
                    self.name = self.name[:-1]

            elif event.type == pygame.KEYUP:
                if (event.key == pygame.K_KP_ENTER or
                    event.key == pygame.K_RETURN):
                    self.enter = False

    def run_logic(self):
        #self.timer += 1
        # Next country
        if self.enter and len(self.country_list) > self.counter:
            self.counter += 1
            self.enter = False
        if len(self.country_list) == self.counter:
            self.game_over = True
            
        #--Automatic country changer
##        if self.timer % 3 == 0 and len(self.country_list) - 1 > self.counter:
##            self.counter += 1
##            print(self.country_list[self.counter][1])

        if not self.game_over:
            # city name
            self.active_question = self.country_list[self.counter][1]
            # city position 
            self.active_position = self.country_list[self.counter][0] 
            self.last_position = self.country_list[self.counter - 1][0]
        if len(self.country_list) == self.counter:
            self.last_position = self.active_position

        
        
    def display_frame(self, screen):
        screen.blit(self.gamemap, [0, 0])
##        pygame.draw.circle(screen, RED, pygame.mouse.get_pos(), 1)
        
        # active question indicator
        if not self.game_over:
            if len(self.country_list) >= self.counter:
                pygame.draw.circle(screen, BLUE, self.active_position, 4)
                pygame.draw.line(screen, BLUE, self.active_position,
                                 [self.active_position[0] + 10,
                                  self.active_position[1] - 10], 4)
                pygame.draw.line(screen, BLUE, [self.active_position[0] + 10,
                                  self.active_position[1] - 10],
                                 [self.active_position[0] + 50,
                                  self.active_position[1] - 10], 4)
                name_text = font.render(self.name, True, BLUE)
                screen.blit(name_text, [self.active_position[0] + 10,
                                  self.active_position[1] - 40])

        if self.incorrect_answer and len(self.country_list) >= self.counter:
            inc_name_text = font.render(self.country_list[self.counter - 1][1], True, RED)
            screen.blit(inc_name_text, [self.last_position[0] + 10,
                        self.last_position[1] - 22])
            inc_text = font.render(
                "Die korrekte Antwort lautet "+
                self.country_list[self.counter - 1][1],
                True, RED)
            screen.blit(inc_text, [10, self.gamemap.get_height() - 30])
##        if self.incorrect_answer == False:
##            inc_name_text = font.render(self.country_list[self.counter - 1][1], True, GREEN)
##            screen.blit(inc_name_text, [self.last_position[0] + 10,
##                              self.last_position[1] - 32])
           #--string formatting tests 
##        score_txt = font.render(str(self.score) + " richtige von " + str(len(self.country_list)) +
##                                str(round(100 / len(self.country_list) * self.score, 2)) +
##                                "% korrekt", True, BLACK)
##        score_txt = font.render("%d richtige Antworten von %d.  %d Prozent korrekt" % (self.score, len(self.country_list), round(100 / len(self.country_list) * self.score, 3)),
##                                True, BLACK)

        score_txt = (
            font.render(
                "{0} richtige Antworten von {1}. {2} Prozent korrekt".format(
                    self.score, self.counter,
                    round(100 / (self.counter + 0.0000001) * self.score, 2
                    )), True, BLACK
            )
        )
        screen.blit(score_txt,[20, 20])
        if self.game_over:
            game_over_txt = (
                font.render(
                    "Spiel beendet - Pfeiltaste links für das nächste Quiz",
                    True, BLACK
                )
            )
            game_over_txt2 = (font.render("ESC um ins Hauptmenü zu gelangen",
                                         True, BLACK))
            screen.blit(game_over_txt,[20, 50])
            screen.blit(game_over_txt2,[20, 80])
            
        pygame.display.flip()

class Europe(Game):
    gamemap = europe_map
    scene = None
    next_scene = "Africa"

    def __init__(self, background, country_list):
        Game.__init__(self, background, country_list)

class Africa(Game):
    gamemap = africa_map
    scene = None
    next_scene = "Asia"

    def __init__(self, background, country_list):
        Game.__init__(self, background, country_list)

class Asia(Game):
    gamemap = asia_map
    scene = None
    next_scene = "SouthAmerica"

    def __init__(self, background, country_list):
        Game.__init__(self, background, country_list)

class SouthAmerica(Game):
    gamemap = southamerica_map
    scene = None
    next_scene = "Europe"

    def __init__(self, background, country_list):
        Game.__init__(self, background, country_list)

class Title():
    done = False
    next_scene = "Europe"
    scene = None
    button_europe = pygbutton.PygButton((50, 100, 200, 30),
                                        'Europas Hauptstädte')
    button_africa = pygbutton.PygButton((50, 150, 200, 30),
                                        'Afrikas Hauptstädte')    
    button_asia = pygbutton.PygButton((50, 200, 200, 30),
                                        'Asiens Hauptstädte')
    button_southamerica = pygbutton.PygButton((50, 250, 200, 30),
                                        'Südamerikas Hauptstädte')
    button_quit = pygbutton.PygButton((50, 300, 200, 30),
                                            'Beenden')

    def __init__(self):
        self.image = pygame.Surface((600, 400))

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True

            elif event.type == pygame.KEYDOWN:
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
            if 'click' in self.button_quit.handleEvent(event):
                self.done = True
##                sys.exit()

    def run_logic(self):
        pass

    def display_frame(self, screen):
        screen.fill(WHITE)
        start_text = (font.render("Hauptstädte-Quiz",
                                  True, BLACK))
        screen.blit(start_text, [100, 20])
        self.button_europe.draw(screen)
        self.button_africa.draw(screen)
        self.button_asia.draw(screen)
        self.button_southamerica.draw(screen)
        self.button_quit.draw(screen)
        pygame.display.flip()
        
