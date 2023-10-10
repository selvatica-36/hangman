import random

# Define the list of possible words:
word_list = ["plum", "apple", "banana", "mango", "nectarine"]
print(word_list)

# Computer chooses a random word from the list, using the random module
word = random.choice(word_list)
print(word)

# Program asks for user input
guess = input("Please, enter a letter: ")


# Checks whether user input is valid: needs to be a single letter in the alphabet
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")