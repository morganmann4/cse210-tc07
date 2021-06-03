class Actor(point):
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