import sys
from game import constants
from asciimatics.widgets import Frame
from game.active_actors import Active_Actors
from game.score import Score
from game.actor import Actor
class Screen_Output:
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
        """Constructor for the Screen, initializes an instance of Screen

        Args:
            self (Screen): An instance of Screen.
        """
        self._screen = screen

    def clear_screen(self, buffer, score):
        """used to clear the contents of the screen
        
        Args:
            self (Screen): An instance of Screen.
        """ 

        self._screen.clear_buffer(7, 0, 0)
        self._screen.print_at("-" * constants.MAX_X, 0, 0, 7)#I think we'll want to input the buffer into this area followed by "---"
        self._screen.print_at("-" * constants.MAX_X, 0, constants.MAX_Y, 7)#I think we'll want to input the score here followed by "---"
        self._screen.print_at(buffer, 0, 0, 7)
        self._screen.print_at(score, 0, constants.MAX_Y, 7)
    def draw_actor(self, actor):
        '''renders a word on the screen

        Args:
            self (Screen): An instance of Screen.
            actor(Actor): An instance of Actor
        '''
        text = actor.get_word()
        position = actor.get_position()
        x = position.get_x()
        y = position.get_y()
        self._screen.print_at(text, x, y, 7)


    def draw_actors(self, active_actors):
        '''renders all the words in the list on the screen'''
        actors = active_actors.actor_list()
        for each_actor in actors:
            self.draw_actor(each_actor)
        

    def flush_buffer(self):
        """Renders the screen.

        Args:
            self (Screen): An instance of Screen.
        """ 
        self._screen.refresh() 
    
    

    
        
