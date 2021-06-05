class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        active_actors(active_actor): An instance of active_actor that keeps track of current words on the screen and can check user input
        actor
        input_service (InputService): The input mechanism.
        keep_playing (boolean): Whether or not the game can continue.
        screen (Screen): The output mechanism.
        score (Score): The current score.
        buffer_list(list[characters]): keeps a list of the current string to give to the screen to be displayed at the bottom... we probably need to make a buffer class so that this can have a set position with it that we can pass to screen when we move to display this
    """
    """
        Game Flow:

    __init__: initialize active actor directory, input_service, keep_playing as true, screen, and score. 

     
    Start the game loop to control the sequence of play. Something like the following from the snake game
        while self._keep_playing:
            self._get_inputs() - gets input of a single letter, adds them to a list of characters to display as buffer on the bottom of the screen (should we make a buffer class and set the position to the bottom of the screen? it might be easier that way)
            self._do_updates() - did they get a word when the pressed enter or did a word reach the end of the screen? Yes- call function in score to add points and input the word, call funciton in active_actors to kill the word on the screen. No- do nothing. clear buffer list if enter was pressed. move each word to its new position
            self._do_outputs() - output Actors in new positions and add the current buffer and the current score to the screen
            sleep(constants.FRAME_LENGTH)

    """
    def __init__(self, input_service, output_service):