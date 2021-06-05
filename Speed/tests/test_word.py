""" class for testing word class functions"""
from game.words import Words
import pytest as py

words = Word()


def test_word():
    word1 = words.get_word()
    word2 = words.get_word()
    assert word1 != word2

py.main(["-v", "--tb=no", "test_word.py"])