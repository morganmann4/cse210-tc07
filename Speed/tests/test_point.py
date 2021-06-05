""" class for testing point class functions"""
import pytest
from speed.game.point import Point

class Test_Point:
    def test_get_x(self):
        point = Point(5,6)
        assert point.get_x() == 5
    
    def test_get_y(self):
        point = Point(5,6)
        assert point.get_y() == 6
    
    def test_set_x(self):
        point = Point(5,6)
        point.set_x(10)
        assert point.get_x() == 10

    def test_set_y(self):
        point = Point(5,6)
        point.set_y(10)
        assert point.get_y() == 10
