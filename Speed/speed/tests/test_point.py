""" class for testing point class functions"""
import pytest
from game.point import Point

class Test_Point:
    """Tests the class function get_x and its ability to return the x coordinate on the screen"""
    def test_get_x(self):
        point = Point(5,6)
        assert point.get_x() == 5
    
    def test_get_y(self):
        """Tests the class function get_y and its ability to return the y coordinate on the screen"""
        point = Point(5,6)
        assert point.get_y() == 6
    
    def test_set_x(self):
        """Tests the class function set_x and its ability to set the x coordinate on the screen"""
        point = Point(5,6)
        point.set_x(10)
        assert point.get_x() == 10

    def test_set_y(self):
        """Tests the class function set_y and its ability to set the y coordintate on the screen"""
        point = Point(5,6)
        point.set_y(10)
        assert point.get_y() == 10
