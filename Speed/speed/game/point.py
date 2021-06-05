class Point:
    """Represents distance from an origin (0, 0).

    Stereotype:
        Information Holder

    Attributes:
        _x (integer): The horizontal distance.
        _y (Point): The vertical distance.

        Functions: 
            get_x: returns x position (first number in the pairing)
            get_y: returns the y position (second number in the pairing)
            set_x
            set_y
    """
    def __init__(self, x, y):
        """The class constructor.
        
        Args:
            self (Point): An instance of Point.
            x (integer): A horizontal distance.
            y (integer): A vertical distance.
        """
        self._x = x
        self._y = y

    def get_x(self):
        """Gets the horizontal distance.
        
        Args:
            self (Point): An instance of Point.
            
        Returns:
            integer: The horizontal distance.
        """
        return self._x

    def get_y(self):
        """Gets the vertical distance.
        
        Args:
            self (Point): An instance of Point.
            
        Returns:
            integer: The vertical distance.
        """
        return self._y

    def set_x(self, new_x):
        """Used to set a new Horizontal distance.
        
        Args:
            self (Point): An instance of Point.
            new_x (Int): a new integer to be used as the x coordinate
            
        Returns:
            integer: The horizontal distance.
        """
        self._x = new_x
        return self._x

    def set_y(self, new_y):
        """Used to set a new Vertical distance.
        
        Args:
            self (Point): An instance of Point.
            new_y (Int): a new integer to be used as the y coordinate
            
        Returns:
            integer: The vertical distance.
        """
        self._y = new_y
        return self._y

