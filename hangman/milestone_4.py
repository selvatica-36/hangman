import random

class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word = random.choice(word_list)
        self.word_guessed = len(self.word) * ['_'] 
        self.num_letters = len(set(self.word))
        self.word_list = word_list
        self.num_lives = num_lives
        self.list_of_guesses = []


    def check_guess(self, guess) -> None:
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for letter in self.word:
                if letter == guess: 
                    self.word_guessed[self.word.index(letter)] == letter
            self.num_letters -= 1
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
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
        

if __name__ == '__main__':
    word_list_1 = ["plum", "apple", "banana", "mango", "nectarine"]
    game_test = Hangman(word_list_1)
    game_test.ask_for_input()

    