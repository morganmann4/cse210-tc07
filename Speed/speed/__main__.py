from game.director import Director
from game.input import Input
from game.screen import Screen
from asciimatics.screen import Screen 

def main(screen):
    input_service = InputService(screen)
    output = Screen(screen)
    director = Director(input, screen)
    director.start_game()

Screen.wrapper(main)