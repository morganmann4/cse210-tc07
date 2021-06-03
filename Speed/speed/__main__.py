from game.director import Director
from game.input_service import InputService
from game.output import Output
from asciimatics.screen import Screen 

def main(screen):
    input_service = InputService(screen)
    output = Output(screen)
    director = Director(input_service, output)
    director.start_game()

Screen.wrapper(main)