""" class for testing actor class functions"""
import pytest
from game.actor import Actor
from game.point import Point
from game import constants
from game.words import Words
from game.score import Score
from game.active_actors import Active_Actors

class Test_Actor:
    def test_get_position(self):
        """tests the ability of class function "get_position" to return the point object currently assigned to _position"""
        actor = Actor("bear")
        actor._position = Point(5, 5)
        assert actor.get_position() == actor._position #This position is a Point object, not just coordinates
    
    def test_get_word(self):
        """tests the class function get_word and its ability to return the word stored in it"""
        actor = Actor("bear")
        assert actor.get_word() == "bear"
    
    def test_move_next(self):
        """tests the class function "move_next" and its ability to give a correct next position given a position and a velocity"""
        words = Words()
        score = Score()
        active_actors = Active_Actors(words, score)
        active_actors._active_words[0]._word = "bear"
        active_actors._active_words[0]._position = Point(6,5)
        active_actors._active_words[0]._velocity = Point(1,1)
        active_actors._active_words[0].move_next(active_actors)
        assert active_actors._active_words[0]._position.get_x() == 7 and active_actors._active_words[0]._position.get_y() == 6

    def test_move_next_near_max_y(self):
        """Tests the ability of class function move_next if a word gets to the top to make it bounce back down"""
        """tests the class function "move_next" and its ability to give a correct next position given a position and a velocity"""
        words = Words()
        score = Score()
        active_actors = Active_Actors(words, score)
        active_actors._active_words[0]._word = "bear"
        active_actors._active_words[0]._position = Point(5,18)
        active_actors._active_words[0]._velocity = Point(1,1)
        active_actors._active_words[0].move_next(active_actors)
        
        assert active_actors._active_words[0]._velocity.get_y() == -1

    def test_move_next_near_max_x(self):
        """Tests the ability of class function move_next near reaching end of x axis"""
        words = Words()
        score = Score()
        active_actors = Active_Actors(words, score)
        active_actors._active_words[0]._word = "bear"
        active_actors._active_words[0]._position = Point(58,5)
        active_actors._active_words[0]._velocity = Point(1,0)
        active_actors._active_words[0].move_next(active_actors)

        assert active_actors._active_words[0] != "bear" and active_actors._active_words[0]._position.get_x() == 0