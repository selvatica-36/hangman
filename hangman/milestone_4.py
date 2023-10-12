import random

class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word = random.choice(word_list)
        self.word_guessed = len(self.word) * ['_'] #TODO: revise this here
        self.num_letters = len(set(word))
        self.word_list = word_list
        self.num_lives = num_lives
        self.list_of_guesses = []
