import random

word_list = ["plum", "apple", "banana", "mango", "nectarine"]
print(word_list)

word = random.choice(word_list)
print(word)

guess = input("Please, enter a letter: ")

if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")