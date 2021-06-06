""" class for testing word class functions"""
from game.words import Words
import pytest

class Test_Words:

    def test_get_word(self):
        words = Words()
        word1 = words.get_word()
        word2 = words.get_word()
        assert word1 != word2

#py.main(["-v", "--tb=no", "test_word.py"])