""" class for testing active_actors class functions"""

import pytest 
from speed.game.active_actors import Active_Actors
from speed.game.screen import screen


class test_active_actors():

    def test_check_guess():
        """Tests the class function check_guess and its ability to detrmine if the guess was correct or not"""
        active_actors = Active_Actors()
        active_actors._active_words = ["blue", "red", "green"]
        guess = "blue"
        answer = active_actors.check_guess(guess)
        assert answer == True


    def test_actor_list():
        """Tests the class function actor_list and its ability to create a list of the words provided"""
        active_actors = Active_Actors()
        active_actors._active_words = ["blue", "red", "green"]
        output = active_actors.actor_list 
        assert output == ["blue", "red","green"]


    def test_replace_word():
        """Tests the class function replace_word and its ability to replace a word in the list with a new word"""
        active_actors = Active_Actors()
        active_actors.replace_word().new_word = "pink"
        active_actors._active_words = ["blue", "red", "green"]
        active_actors.replace_word(0)
        assert active_actors._active_words == ["pink", "red", "green"]
    
   

