import random

# Define the list of possible words:
word_list = ["plum", "apple", "banana", "mango", "nectarine"]
word = random.choice(word_list)


# Create a function that checks user's guess is in the chosen word
def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! The letter {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")


# Create a function that asks for input, checks it is valid and feeds it to check_guess() function
def ask_for_input():
    while True:
        guess = input("Please, guess a letter: ")
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print("Invalid guess. Please, enter a single alphabetical character.")
    check_guess(guess)


# Call the function to check if code works
ask_for_input()