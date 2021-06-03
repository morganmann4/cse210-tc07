class Active_Actors:
    """ Morgan, this class is the 'correcting' class that we had talked about as a group. after getting into the psuedo code a bit
    I thought this might be a bit more accurate of a name for this class since we are going to keep the list of active actors here
    """

    
    """A class that holds a list of all the current words on the board. It is the job of this class to check user inputs to see if they
    match any of the current words on the board. 

    Stereotype:
        Information Holder
    
    Attributes:
        _active_words(list[Actor]): list of active Actor objects on the screen
    
    Base function ideas:
        new_word(Actor): takes in a new Actor object that is the new word being added to the screen and puts it in the _active_words list.
        attempt(string): takes in string from the director class and checks it against the _active_words list to see if it is a current active word (returns True for correct and False for incorrect). If correct it also needs to use the kill_word function in Actor and remove it from the active word list
    """