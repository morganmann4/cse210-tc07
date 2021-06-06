from game.actor import Actor
from game.score import Score
from game.words import Words

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

    def __init__(self, words, score):
        self._words_list = words
        self._score = score
        self._active_words = []
        self.prepare_actors_list()
        



    def check_guess(self, guess):
        """ Takes the guess from director and checks the list of words. If the guess is correct it sends the word to score, 
            then sends the word to be killed and calls the replace_word method

        Args: 
            self (ActiveActors): An instance of Active Actors
            guess (string): The players guess
        """

        for i in range (0, len(self._active_words)):
            if guess == self._active_words[i].get_word():
                self._score.add_points(guess)#sends word to score
                #self._active_words[i].kill_word() #sends word to actor to be killed
                self.replace_word(i)
                return True

        return False 





    def replace_word(self, position):
        """Replaces the guessed word with a new word

        Args:
            self (ActiveActors): An instance of Active Actors
            position (integer): the guessed words postition in string
        """
        new_actor = Actor(self._words_list.get_word())
        new_word = new_actor #gets new actor from actor class
        self._active_words[position] = new_word #puts new word in olds words list position

    def prepare_actors_list(self):
        """Creates the list of active words"""
        
        for i in range (5):
            new_actor = Actor(self._words_list.get_word())
            self._active_words.append(new_actor)
            

    def actor_list(self):
        """Gets the list of active words"""
        return self._active_words #returns updated word list



