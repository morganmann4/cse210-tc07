import random
import os

class Words:
    """A class for keeping track of the words found in words.txt.  
    
    Stereotype: 
        Information Holder

    Attributes:
        word_list: List of all the words from word.txt
        

    Functions:
        get_word(): Needs to return a word from words list.
    """
    def __init__(self):
        '''Reads in the word text and puts it into a list.
        
        Attributes:

        '''

        here = os.path.dirname(os.path.abspath(__file__)) #I have no idea what this is... i found it on the internet and it fixed our problem

        filename = os.path.join(here, 'words.txt')

        self.words = open(filename, 'r')
        self.word_list = []
        for word in self.words.readlines():

            self.word_list.append(word[0:len(word) - 1])

    def get_word(self):
        '''Gets a random word from the list and returns it to director.'''
        word = random.choice(self.word_list)
        
        return word

    

