""" class for testing actor class functions"""
import pytest
from speed.game.actor import Actor
from speed.game.point import Point

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
        actor = Actor("bear")
        actor._position = Point(6,5)
        actor._velocity = Point(1,1)
        actor.move_next()
        assert actor._position.get_x() == 7 and actor._position.get_y() == 6

    def test_move_next_near_max_y(self):
        """Tests the ability of class function move_next if a word gets to the top to make it bounce back down"""
        actor = Actor("bear")
        actor._position = Point(5,18)
        actor._velocity = Point(1,1)
        actor.move_next() 
        assert actor._velocity.get_y() == -1

    def test_move_next_near_max_x(self):
        """Tests the ability of class function move_next near reaching end of x axis"""
        actor = Actor("bear")
        actor._position = Point(58,5)
        actor._velocity = Point(1,0)
        actor.move_next()
        assert actor.get_word() == "" and actor.get_velocity().get_x() == 0 and actor.get_velocity().get_y() == 0 and actor.get_position().get_x() == 65 and actor.get_position().get_y() == 5

    def test_kill_word(self):
        actor = Actor("bear")
        actor._position = Point(18, 5)
        actor._velocity = Point(1,0)
        actor.kill_word()
        assert actor.get_word() == "" and actor.get_position().get_x() == 65 and actor.get_position().get_y() == 5 and actor.get_velocity().get_x() == 0 and actor.get_velocity().get_y() == 0
    

   