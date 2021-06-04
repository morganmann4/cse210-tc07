import sys
from game import constants
from asciimatics.widgets import Frame
from game.active_actors import Active_Actors
from game.score import Score
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
        self._active_actors = Active_Actors()
        self._actor = Actor()
        self._score = Score()

    def clear_screen(self):
        self._screen.clear_buffer(7, 0, 0)
        self._screen.print_at("-" * constants.MAX_X, 0, 0, 7)
        self._screen.print_at("-" * constants.MAX_X, 0, constants.MAX_Y, 7)

    def draw_actor(self, actor):
        '''renders a word on the screen'''
        text = actor.get_actors()
        position = self._actor.position
        x = position.get_x()
        y = position.get_y()
        self._screen.print_at(text, x, y, 7)


    def draw_actors(self):
        '''renders all the words in the list on the screen'''
        actors = self._active_actors.actor_list()
        for actor in actors:
            draw_actor(actors)
        

    def flush_buffer(self):
        """Renders the screen.

        Args:
            self (OutputService): An instance of OutputService.
        """ 
        self._screen.refresh() 
    
    

    
        
