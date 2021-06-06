""" class for testing screen class functions"""

import pytest
from speed.game.screen_output import Screen_Output


class test_screen:

    def test_draw_actor():
        """Tests the class function sraw_actor and its ability to take inputs for variables and correctly display them"""
        screen = Screen()
        screen.draw_actor().text = "blue"
        screen.draw_actor().x = 3
        screen.draw_actor().y = 4
        output = screen.draw_actor()._screen.print_at(text, x, y, 7)
        output = _screen.print_at("blue", 3, 4, 7)
        