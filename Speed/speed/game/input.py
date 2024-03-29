"""I don't think this needs to be changed at all
"""
import sys
from asciimatics.event import KeyboardEvent

class Input:
    """Detects player input. The responsibility of the class of objects is to detect player keypresses and translate them into a point representing a direction (or velocity).

    Stereotype: 
        Service Provider

    Attributes:
        _screen (Screen): An Asciimatics screen.
    """

    def __init__(self, screen):
        """The class constructor.
        
        Args:
            self (InputService): An instance of InputService.
        """
        #self._screen = screen
        self.input = ''
        self._screen = screen
        
    # def get_input(self):

        
    #     self.input = input("Buffer: ")
       
    #     return self.input
        

    def get_letter(self):
        """Gets the letter that was typed. If the enter key was pressed returns an asterisk.

        Args:
            self (InputService): An instance of InputService.

        Returns:
            string: The letter that was typed.
        """
        result = ""
        event = self._screen.get_key()
        if not event is None:
            if event == 27:
                sys.exit()
            elif event == 13: 
                result = "*" 
            elif event >= 97 and event <= 122: 
                result = chr(event)
        return result

        event = self._screen.get_event()
        if isinstance(event, KeyboardEvent):
            if event.key_code == 27:
                sys.exit()
            self._current = self._keys.get(event.key_code, self._current)
        return self._current