"""class Actor
        A visible, moveable word that participates in the game. The responsibility of Actor is to keep track of the word being held
        the position, and velocity in 2d space. It is 'alive' while it is on the screen and when it is 'dead' or off the screen it
        report this back so that the Word class can keep track of the different words that have been used. 

    Stereotype:
        Information Holder

    Attributes:
        _word (string): The word given by the Word class that is being represented moving accross the string
        _position (Point): The actor's position in 2d space.
        _velocity (Point): The actor's speed and direction.
    

"""