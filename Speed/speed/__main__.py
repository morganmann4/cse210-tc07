from game.director import Director
from game.input import Input
from game.screen_output import Screen_Output
from asciimatics.screen import Screen 

def main(screen):
    imported_screen = screen #we have a screen class, so I am changing the name of this to hopefully make it less confusing
    input_service = Input(imported_screen)
    output = Screen_Output(imported_screen)
    director = Director(input_service, output)
    director.start_game()

Screen.wrapper(main)