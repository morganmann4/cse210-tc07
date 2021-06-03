import sys
from game import constants
from asciimatics.widgets import Frame
from game.active_actors import Active_Actors

class Screen:
    """Outputs the game state. The responsibility of the class of objects is to draw the game state on the terminal. 
    
    Stereotype: 
        Service Provider

    Attributes:
        _screen (Screen): An Asciimatics screen.

        needs to have a function to clear the screen (will be called at the begining of each new frame)
        needs to have a function to draw words on screen in given places
        ??? Lets talk, we need to have a function to put the buffer at the bottom of the screen and the score at the top
    """

    def __init__(self, screen):
        self._screen = screen
        #self._active_actors = Active_Actors()
        #self._actor = Actor()

    def clear_screen(self):
        pass

    def draw_word(self):
        '''renders a word on the screen'''

    def draw_words(self):
        '''renders all the words in the list on the screen'''

        #for word in words
            #draw_word()
        pass
        
        
