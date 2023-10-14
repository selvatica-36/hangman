
import random


class Hangman:

    #TODO: ammend docstrings to reflect the names of my methods
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
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
    list_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    '''


    def __init__(self, word_list, num_lives = 5):
        self.word = random.choice(word_list)
        self.word_guessed = len(self.word) * ['_'] 
        self.num_letters = len(set(self.word))
        self.word_list = word_list
        self.num_lives = num_lives
        self.list_of_guesses = []


    def check_letter_guess(self, guess) -> None:
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess!The letter '{guess}' is in the word.")
            self.num_letters -= 1
            print(f"Number of unique letters left: {self.num_letters}")

            for letter in self.word:
                if letter == guess: 
                    all_letter_indexes = [position for position, char in enumerate(self.word) if char == letter]
                    for each_index in all_letter_indexes:
                        self.word_guessed[each_index] = letter

            print(f"State of word guess: {self.word_guessed}")

        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")

    
    def ask_for_input(self):
        while True:
            guess = input("Please, guess a letter: ")
            if len(guess) != 1 or guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_letter_guess(guess)
                self.list_of_guesses.append(guess)
                break


    def guess_word(self):
        while True:
            guess_type_choice = input("Would you like to guess the full word? Enter 'yes' or 'no':  ")
            if guess_type_choice == 'yes':
                full_word_guess = input("Guess the word: ")
                if full_word_guess == self.word:
                    self.num_letters = 0
                    break
                else:
                    self.num_lives -= 1
                    print(f"Sorry, {full_word_guess} is not the word. Try again.")
                    print(f"You have {self.num_lives} lives left.")
                    break

            elif guess_type_choice == 'no':
                self.ask_for_input()
                break

            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

                


def play_game(word_list):
    ''' 
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
    game = Hangman(word_list, num_lives=5)
    print(f"The word to be guessed is: {game.word_guessed}")
    
    while True:
        if game.num_lives == 0:
            print(f"You lost! The word is '{game.word}'")
            break
        elif game.num_letters > 0:
            game.guess_word()
        elif game.num_lives > 0 and game.num_letters == 0:
            print(f"Congratulations, you won the game! The word is '{game.word}'")
            break




if __name__ == '__main__':
    word_list_1 = ["banana", "nectarine", "mango", "plum", "apple"]
    print(play_game.__doc__)
    play_game(word_list_1)


# TODO: add error handling when inputting incorrect parameters to play_game
# TODO: add comments throughout
# TODO: add docstrings to the class. Ammend current docstrings
# TODO: update README file

