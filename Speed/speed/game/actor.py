import random
from game import constants
from game.point import Point


class Actor:
    """ A visible, moveable word that participates in the game. The responsibility of Actor is to keep track of the word being held
        the position, and velocity in 2d space. It is 'alive' while it is on the screen and considered to be 'dead' when it is removed
        from the string

        Stereotype:
            Information Holder

        Attributes:
            _word (string): The word given by the Word class that is being represented moving accross the string
            _position (Point): The actor's position in 2d space.
            _velocity (Point): The actor's speed and direction.
        
        Functions:
            kill_word: no more position on the board, no velocity (to be called when word is guessed correctly or word reaches end of screen)
            word_reached_end: call kill_word

    """
    def __init__(self, word):
        """The class constructor.
        
        Args:
            self (Actor): an instance of Actor.
            word (string): a string from the word class to be represented by the actor
            position(Point): a point on the screen where the Actor is 
            velocity (Point): The Actors speed and direction in 2d space
        """
        self._word = word
        self._position = Point(0, random.randint(1, constants.MAX_Y - 1))
        self._velocity = Point(random.randint(1,2), random.randint(-1, 1))

    def get_position(self):
        """Gets the actor's position in 2d space.
        
        Args:
            self (Actor): an instance of Actor.

        Returns:
            Point: The actor's position in 2d space.
        """
        return self._position

    def get_word(self):
        """Gets the actor's textual representation.
        
        Args:
            self (Actor): an instance of Actor.

        Returns:
            string: The actor's textual representation.
        """
        return self._word
    
    def get_velocity(self):
        """Gets the actor's speed and direction.
        
        Args:
            self (Actor): an instance of Actor.

        Returns:
            Point: The actor's speed and direction.
        """
        return self._velocity

    def move_next(self, active_actors):
        """Moves the actor to its next position according to its velocity. Will 
        wrap the position from one side of the screen to the other when it 
        reaches the boundary in either direction.
        
        Args:
            self (Actor): an instance of Actor.
        """
        x1 = self._position.get_x()
        y1 = self._position.get_y()
        x2 = self._velocity.get_x()
        y2 = self._velocity.get_y()
        x = x1 + x2
        self._position.set_x(x) #set new x
        y = y1 + y2
        self._position.set_y(y) #set new y
        
        #check if Actor is nearing edge
        if ((y + y2) >= constants.MAX_Y or (y + y2) <= 0): #if there is a y velocity and it reaches the top or bottom of the screen, bounce back 
            self._velocity.set_y(self._velocity.get_y() * -1)
        if ((x + x2) >= constants.MAX_X): #if word reaches end of the screen "kill" the word
            index = 0
            while index < len(active_actors.actor_list()):
                if active_actors.actor_list()[index]._word == self._word:
                    active_actors.replace_word(index)
                index += 1
        self._position = Point(self.get_position().get_x(), self.get_position().get_y())
    
    # def kill_word(self):
    #     """Makes sure that the word is out of sight (shouldn't really be a necessary function because if we stop referencing the word it will go to garbage anyways)
        
    #     Args:
    #         self (Actor): an instance of Actor.
    #     """
    #     self._word = ""
    #     self._position.set_x(constants.MAX_X + 5)
    #     self._velocity.set_x(0)
    #     self._velocity.set_y(0)
