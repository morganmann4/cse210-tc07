""" class for testing active_actors class functions"""

import pytest
from speed.game.active_actors import Active_Actors
from speed.game.screen import screen




def test_check_guess(guess):
    active_actors = Active_Actors()
    active_actors._active_words = ["blue", "red","green"]
    guess = "blue"
    answer = active_actors(guess)
    assert answer == True


    
    
# set PYTHONPATH=.;speed
# py.test



