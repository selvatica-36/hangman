# Comment here
import random

word_list = ["plum", "apple", "banana", "mango", "nectarine"]
word = random.choice(word_list)


while True:
    guess = input("Please, guess a letter: ")
    if len(guess) == 1 and guess.isalpha():
        break
    else:
        print("Invalid guess. Please, enter a single alphabetical character.")


if guess in word:
    print(f"Good guess! The letter {guess} is in the word.")
else:
    print(f"Sorry, {guess} is not in the word. Try again.")