import random
from .globs import *
from .europe_list import *
from .africa_list import *

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
    #-- Used to mark positions of cities
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
##                #--locate cities on the map
##                print(pygame.mouse.get_pos())
##                mouse_pos = pygame.mouse.get_pos()
##                city = input("Hauptstadt: ")
##                self.marker_list.append([mouse_pos, city])
##                self.marker_count += 1
     
            elif event.type == pygame.KEYDOWN:
                if event.unicode.isalnum(): # unicode
                    self.name += event.unicode
                if event.key == pygame.K_SPACE:
                    self.name += " "
                if event.key == pygame.K_LEFT:
                    self.scene = self.next_scene
                if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
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
                if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                    self.enter = False

    def run_logic(self):
        #self.timer += 1
        #--Next country
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
            self.active_question = self.country_list[self.counter][1] #city name
            self.active_position = self.country_list[self.counter][0] #city position
            self.last_position = self.country_list[self.counter - 1][0]
        if len(self.country_list) == self.counter:
            self.last_position = self.active_position

        
        
    def display_frame(self, screen):
        screen.blit(self.gamemap, [0, 0])
##        pygame.draw.circle(screen, RED, pygame.mouse.get_pos(), 1)
        
        #--Active question indicator
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
                name_text = font.render(self.name.capitalize(), True, BLUE)
                screen.blit(name_text, [self.active_position[0] + 10,
                                  self.active_position[1] - 40])

        if self.incorrect_answer and len(self.country_list) >= self.counter:
            inc_name_text = font.render(str.capitalize(
                self.country_list[self.counter - 1][1]), True, RED)
            screen.blit(inc_name_text, [self.last_position[0] + 10,
                              self.last_position[1] - 22])
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

        score_txt = (font.render("{0} richtige Antworten von {1}. {2} Prozent korrekt".format(
                                 self.score, self.counter,
                                 round(100 / (self.counter - 0.0001) *
                                 self.score, 2)),
                                 True, BLACK))
        screen.blit(score_txt,[20, 20])
        if self.game_over:
            game_over_txt = (font.render("Spiel beendet - Pfeiltaste links für das nächste Quiz",
                                         True, BLACK))
            screen.blit(game_over_txt,[20, 50])
        
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
    next_scene = "Europe"

    def __init__(self, background, country_list):
        Game.__init__(self, background, country_list)
