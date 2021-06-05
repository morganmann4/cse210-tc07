""" class for testing input_service class functions"""

from input import Input

def test_input():
    
    input = Input()
    input.input = "changing"
    assert input.get_input() == "changing"