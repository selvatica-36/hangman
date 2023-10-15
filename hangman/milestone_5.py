
import random


class Hangman:

    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It also gives the user a chance to guess the whole word at once.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game. Words must be formatted as strings
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_of_letter_guesses: list
        A list of the letters that have already been tried
    list_of_word_guesses: list
        A list of the words that have already been tried

    Methods:
    -------
    type_of_guess()
        Asks the user whether they want to guess the full word or a letter.
    ask_word_guess()
        Asks the user for a word.
    check_word_guess(word_guess)
        Checks if the word guessed is the word. 
    check_letter_guess(letter_guess)
        Checks if the letter guessed is in the word.
    ask_letter_input()
        Asks the user for a letter.
    _fill_word_with_guess(letter_guess)
        Protected method used by check_letter_guess method only if the letter guessed by the user is correct.
        Takes the letter guessed and fills the blank spaces in the word to be guessed.

    '''

    def __init__(self, word_list, num_lives = 5):
        ''' Constructor of the Hangman class
            Takes in word_list and a default number of lives num_lives as parameters.
            Sets the attributes of the class
            Adds error handling to for a user-friendly experience, to avoid TypeErrors
        '''
        # Error handling: makes sure parameters are the correct data type and raises an error otherwise
        if type(word_list) != list:
            raise TypeError("Parameter word_list must be a list.") # This works
        elif type(word_list) == list:
            for element in word_list:
                if type(element) != str:
                    raise TypeError("Parameter word_list must be a list containing one or more words as strings.")
        if type(num_lives) != int:
            raise TypeError("Parameter 'num_lives' must be an integer.")
        
        # Setting the attributes of the class:
        self.word = random.choice(word_list).lower()
        self.word_guessed = len(self.word) * ['_'] 
        self.num_letters = len(set(self.word))
        self.word_list = word_list
        self.num_lives = num_lives
        self.list_of_letter_guesses = []
        self.list_of_word_guesses = []


    def _fill_word_with_guess(self, letter_guess):
        ''' Protected method used by check_letter_guess method 
            only if the letter guessed by the user is correct.
            Takes the letter guessed and fills the blank spaces in the word to be guessed.
            Args:
                letter_guess(str): letter guessed by user
        '''
        for letter in self.word:
            if letter == letter_guess:
                # For a letter that appears multiple times inside a word, 
                # we need to create a list of the indexes of this letter in the word: all_letter_indexes 
                all_letter_indexes = [position for position, char in enumerate(self.word) if char == letter]
                # Iterate over the list of indexes
                for each_index in all_letter_indexes:
                    # Substitute correct letter in their right position (index)
                    self.word_guessed[each_index] = letter
        print(f"The word you need to guess is: {self.word_guessed}")
        

    def check_letter_guess(self, letter_guess) -> None:
        '''Checks if the letter guessed is in the word.
            Args:
                letter_guess(str): letter guessed by user 
        '''
        letter_guess = letter_guess.lower()
        if letter_guess in self.word:
            print(f"Good guess!The letter '{letter_guess}' is in the word.")
            self.num_letters -= 1
            self._fill_word_with_guess(letter_guess)

            # Debugging check - should not be shown to user
            print(f"Number of unique letters left: {self.num_letters}")
            
        else:
            self.num_lives -= 1
            print(f"Sorry, {letter_guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")

    
    def ask_letter_input(self):
        '''Asks the user for a letter.'''
        while True:
            letter_guess = input("Please, guess a letter: ")
            if len(letter_guess) != 1 or letter_guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif letter_guess in self.list_of_letter_guesses:
                print("You already tried that letter!")
            else:
                self.check_letter_guess(letter_guess)
                self.list_of_letter_guesses.append(letter_guess)
                break


    def check_word_guess(self, word_guess) -> None:
        '''Checks if the word guessed is the word.
           Args:
                word_guess (str): word guessed by user 
        '''
        if word_guess == self.word:
            self.num_letters = 0
        else:
            self.num_lives -= 1
            print(f"Sorry, '{word_guess}' is not the word. Try again.")
            print(f"You have {self.num_lives} lives left.")
    

    def ask_word_guess(self):
        ''' Asks the user for a word.'''
        while True:
            word_guess = input("Guess the word: ")
            if word_guess.isalpha() == False:
                print("Invalid word. Please, enter a word that only contains alphabetical characters.")
            elif word_guess in self.list_of_word_guesses:
                print("You already tried that word!")
            else:
                self.check_word_guess(word_guess)
                self.list_of_word_guesses.append(word_guess)
                break


    def type_of_guess(self):
        '''Asks the user whether they want to guess the full word or a letter.'''
        while True:
            guess_type = input("Would you like to guess the full word? Enter 'yes' or 'no':  ")
            if guess_type == 'yes':
                self.ask_word_guess()
                break
            elif guess_type == 'no':
                self.ask_letter_input()
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")




def play_game(word_list):
    ''' 
    Implementation of the Hangman game (see Hangman class).
    For more information run help(Hangman) or print(Hangman.__doc__)
    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game. Words must be formatted as strings.


    HANGMAN GAME: PLAYER INSTRUCTIONS
    ---------------------------------
        In each round:
        - First, you will be asked if you want an attempt at guessing the full word.
        - Enter 'yes' if you think you know the word. Afterwards, enter the word.
        - If you don't know the word yet, enter 'no'. Then, you will have a chance 
          to guess a letter in the word.

        In each round, the game will show you:
         - The number of lives you have left
         - Your progress at guessing the word 
         
         
         LET'S PLAY!!!!!
         
         
         '''
    

    num_lives = 5

    try:
        game = Hangman(word_list, num_lives)
        print(f"The word to be guessed is: {game.word_guessed}")  
        while True:
            if game.num_lives == 0:
                print(f"You lost! The word is '{game.word}'")
                break
            elif game.num_letters > 0:
                game.type_of_guess()
            elif game.num_lives > 0 and game.num_letters == 0:
                print(f"Congratulations, you won the game! The word is '{game.word}'")
                break
    
    # Throw error message if the try block encounter a TypeError
    except TypeError as e:
        print(f"Error: {e}")

    
    
if __name__ == '__main__':
    word_list = ["Banana", "nectarine", "mango", "plum", "apple"]
    print(play_game.__doc__)
    play_game(word_list)
