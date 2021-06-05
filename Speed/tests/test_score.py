""" class for testing score class functions"""
import pytest
from speed.game.score import Score

class Test_Score:


    def test_add_points(self):
        """tests the ability of class function add_points to return set _points to the correct number of points
        """
        score = Score()
        score.add_points("abcde")
        assert score._points == 5
