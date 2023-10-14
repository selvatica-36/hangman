
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
            print(f"Good guess!The letter '{guess}' is in the word.")
            self.num_letters -= 1
            print(f"Number of unique letters left: {self.num_letters}")

            for letter in self.word:
                if letter == guess: 
                    all_letter_indexes = [pos for pos, char in enumerate(self.word) if char == letter]
                    for each_index in all_letter_indexes:
                        self.word_guessed[each_index] = letter
                        
            print(f"State of word guess: {self.word_guessed}")
            print(f"All letter indexes: {all_letter_indexes}")

                    
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
        

def play_game(word_list):
    game = Hangman(word_list, num_lives=5)

    # Debugging checks:
    print(f"The word to be guessed is: {game.word}")
    print(f"the number of unique letters is: {game.num_letters}")
    print(game.word_guessed)
    
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        elif game.num_lives > 0 and game.num_letters == 0:
            print("Congratulations, you won the game!")
            break

# FIXME: while loop in play_game function does not work. Lives go to negative numbers


if __name__ == '__main__':
    word_list_1 = ["banana", "nectarine", "mango", "plum", "apple"]
    play_game(word_list_1)


