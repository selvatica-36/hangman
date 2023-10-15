# Hangman
## Summary
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Table of Contents
1. [Introduction](#1-introduction)
2. [Installation instructions](#2-installation-instructions)
3. [Usage instructions](#3-usage-instructions)
4. [File structure](#4-file-structure)
5. [License information](#5-license-information)


## 1. Introduction
This is a hangman game that asks the user for a letter and checks if it is in the word.
It also gives the user a chance to guess the whole word at once.
It starts with a default number of lives and a random word from the provided word_list.

**As a learner**, my aim in this project was to consolidate my python knowledge, with a specific focus on OOP-oriented programming. My main two learning points have been:
- Implementing error handling as a user friendly experience
- Keeping the code simple and making sure each dunction or method does only one thing. I have had to refactor my code multiple times and divide a larger function into multiple ones.
- Understanding access modifiers in python. 


## 2. Installation instructions
The game files are stored remotely in Github: https://github.com/selvatica-36/hangman.git
The repository contains:
- This README.md file
- .gitignore
- A folder called 'hangman', which contains:
        - milestone_2.py: This file only initialises the variables of the game.
        - milestone_3.py: This file creates the two base functions to ask user input and check user's guess.
        - milestone_4.py: Contains the an early version of the hangman class.
        - milestone_5.py: File needed to run the game. Contains:
            * Final version of the hangman class, including docstrings
            * play_game function: implementation of the hangman game

User should know that files milestone_2/3/4.py were part of the development process and are not needed to play the game. Only milestone_5.py is needed to play the game. 

To install the game, the user should clone this repository in their local environment. 
NOTE: the user should have conda or pip installed with a python package (python version 3.11.5).


## 3. Usage instructions
To play the game, the user can run file 'milestone_5.py' in their terminal, or alternatively, open it in VSCode and run it in the integrated terminal (using command: 'python milestone_5.py')

### Player instructions
In each round:
    - First, the player is asked if they want an attempt at guessing the full word.
    - They player enters 'yes' if they think they know the word. After, they can enter the word.
    - If the player doesn't know the full word yet, they enter 'no'. Then, they have a chance to guess a letter in the word.

In each round, the game will show you:
    - The number of lives left. The initial number of lives is set to five by default.
    - The progress at guessing the word 

### Modify word_list or number of lives

If the user would like to modify either parameter, they can open the file milestone_5.py.
At the end of the file the user will encounter a block that only runs if the file is executed directly:

if __name__ == '__main__':
    word_list = ["Banana", "nectarine", "mango", "plum", "apple"]
    print(play_game.__doc__)
    play_game(word_list)

This blocks allows the game to run whenever the user runs 'python milestone_5.py' in the terminal, as it calls the function play_game(word_list), which is the implementation of the game. Inside this block, the user can change the word_list.

To change parameter num_lives, the user should navigate to the body of the function play_game:

    def play_game(word_list):
 ---->  num_lives = 5
        # rest of the function body omitted here

### Error handling
If the program throws an error, follow the error instructions. They will likely be a TypeError, so check the following:
1. Make sure the word list used as a parameter of function play_game fulfills the conditions specified in the docstrings of the hangman class object.
1. Make sure parameter num_lives is an integer.

## 4. File structure
The main game file is milestone_5.py contains two main elements:
1. The **hangman class** object. Takes in two parameters (a word list and a number of lives, which is set to 5 by default). The class contains an __init__ constructor that defines all class attributes, as well as all methods of the class, needed to ask user for input and to check the guess against the hidden word. For complete information on the hangman class, user can run help(Hangman) or print the docstings: print(hangman.__doc__).
1. The **play_game** function. This function takes in the word list as a parameter. It creates an instance of the hangman class object using the word list and the variable num_lives (number of lives, which is set to 5 by default). It implements the logic of the game by calling the appropriate methods and attributes from the hangman instance. 
1. if __main__ == '__name__' block. This will run automatically when milestone_5.py is run from the terminal. It calls contains teh word list and it calls the function play_game. 

## 5. License information
This is an open source public repository. The original empty repository was forked from Aicore. 

