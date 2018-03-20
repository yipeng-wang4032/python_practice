# predefined items for user to guess
# each round script will pick up an item randomly
# players need to guess each letters in this secret word at each time
# gameover when the number of wrong guess letters reaches 7
# Win, when user guessed all the letters in the secret word
# In the end , either continue play another round, or quit the game.

import os
import random
import sys

# make a list of words
words = [
    'apple',
    'banana',
    'orange',
    'coconut',
    'strawberry',
    'lime',
    'grape',
    'kumquat',
    'blueberry',
    'melon'
]

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
def draw(bad_guess, good_guess,secret_word):
    clear()
    
    print('Strikes: {}/7'.format(len(bad_guess)))
    print('')
    
    for letter in bad_guess:
        print(letter, end=' ')
    print('\n\n')
    
    for letter in secret_word:
        if letter in good_guess:
            print(letter, end='')
        else:
            print('_',end='')
    print('')
    
def get_guess(bad_guess, good_guess):
    while True:
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1:
            print("You can only guess a single letter!")
        elif guess in bad_guess or guess in good_guess:
            print("You've already guessed that letter!")
        elif not guess.isalpha():
            print("You can only guess letters!")
        else:
            return guess 

def play(done):
    clear()
    secret_word = random.choice(words)
    bad_guess = []
    good_guess = []
    
    while True:
        draw(bad_guess,good_guess, secret_word)
        guess = get_guess(bad_guess, good_guess)
        
        if guess in secret_word:
            good_guess.append(guess)
            found = True
            for letter in secret_word:
                if letter not in good_guess:
                    found = False
            if found:
                print("You win!")
                print("The secret word was {}".format(secret_word))
                done = True 
        else:
            bad_guess.append(guess)
            if len(bad_guess) == 7:
                print("You lost!")
                print("The secret word was {}".format(secret_word))
                done = True
                      
        if done:
            play_again = input("Play again? Y/n ").lower()
            if play_again != 'n':
                return play(done=False)
            else:
                print("Bye!")
                sys.exit()

def welcome():
    start = input("Press enter/return to start or Q to quit ").lower()
    if start == 'q':
        print("Bye!")
        sys.exit()
    else:
        return True
print('Welcome to Letter Guess!')

done = False
                      
while True:
    clear()
    welcome()
    play(done)
               
