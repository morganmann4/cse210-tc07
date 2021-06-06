""" class for testing active_actors class functions"""
import pytest
from speed.game.actor import Actor
from speed.game.active_actors import Active_Actors
from speed.game.words import Words
from speed.game.score import Score


class Test_Active_Actors:
    def test_prepare_actors_list(self):
        #tests that the class function prepare_actors creates a list of 5 new actors
        words = Words()
        score = Score()
        active_actors = Active_Actors(words, score) #calls prepare_actors_list
        
        assert len(active_actors._active_words) == 5

    def test_actor_list(self):
        #tests the ability of class function actor_list to return a list of 5 actors that are currently set
        words = Words()
        score = Score()
        active_actors = Active_Actors(words, score) #calls prepare_actors_list

        assert len(active_actors.actor_list()) == 5


    def test_replace_word(self):
        words = Words()
        score = Score()
        active_actors = Active_Actors(words, score)
        active_actors._active_words[0]._word = "hello"
        check = active_actors.replace_word(0)

        assert active_actors._active_words[0]._word != "hello"

    def test_check_guess(self):
        words = Words()
        score = Score()
        active_actors = Active_Actors(words, score)
        active_actors._active_words[0]._word = "hello"
        check = active_actors.check_guess("hello")

        assert check == True

    
        

    