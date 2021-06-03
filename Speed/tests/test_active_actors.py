""" class for testing active_actors class functions"""

_active_words = ["blue", "red","green"]

def check_guess(guess):

        for i in range (0, len(_active_words)):
            if guess == _active_words[i]:
                # _actor.score(guess)
                # _actor.kill_word(guess) 
                return True

            else:
                return False 

guess = "blue"

answer = check_guess(guess)

print(answer)



