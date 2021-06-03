import sys
from game import constants
from asciimatics.widgets import Frame

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