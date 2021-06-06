from game.point import Point
class Score:

    """Points earned. The responsibility of Score is to keep track of the player's points. To be output to the screen

    ***Im not sure how this works yet, but I think the number of points should change according to how long the word was. 
    ***In the snake game score inherited from Actor. I don't know if we need to do that again, but I put it in because thats
    ***how the other one worked

    Stereotype:
        Information Holder

    Attributes: 
        _points (integer): The number of points the food is worth.
        needs to have a set position at the top of the screen
    """
    def __init__(self):
        """The class constructor. Invokes the superclass constructor, initializes points to zero, sets the position and updates the text.
        
        Args:
            self (Score): an instance of Score.
        """
        self._points = 0
        self._position = Point(1, 0)
        self._text = f"Score: {self._points}"
    
    def add_points(self, word):
        """Adds a certain amount of points to the running total. The word gets one point for each letter in the word.
        
        Args:
            self (Score): An instance of Score.
            word (string): The word to get points for.
        """
        points = len(word)
        self._points += points
        self._text = f"Score: {self._points}"
