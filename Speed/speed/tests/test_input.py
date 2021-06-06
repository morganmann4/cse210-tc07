""" class for testing input_service class functions"""
# import pytest
# from speed.game.input import Input
# from asciimatics.screen import Screen 

# class Test_Input:
#     def test_input(self, screen):
#         def mock_key_press():
#             """ Return fake user keypress
#             """
#             return "a"
#         input_object = Input(screen)
#         monkeypatch.setattr('_screen.get_key', mock_key_press)
#         assert input_object.get_letter() == "a"
#     Screen.wrapper(test_input)


    # def test_read_letter(self, monkeypatch):
    #     """ if I input a capital letter I should get back a lowercase letter
    #     """
    #     def mock_input(prompt):
    #         """ Return fake user input
    #         """
    #         return "A"
    #     monkeypatch.setattr("builtins.input", mock_input)
    #     c = Console()
    #     letter = c.read_letter("")
    #     assert letter == "a"