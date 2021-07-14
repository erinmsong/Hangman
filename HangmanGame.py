"""
Erin Song
7.12.21
Hangman Game (fruits)
"""

import random
MAX_STRIKES = 5

def get_random_word():
    words = ['apple', 'banana', 'coconut', 'dill', 'eggplant', 'fruit', 'grape', 'mango', 'pear', 'strawberry']
    ind = random.randint(0, len(words)-1)
    return words[ind].upper()

def update_blanks(gues, targ, t_print):
    index = 0
    for i in targ:
        if(i == gues):
            t_print[index] = i.upper()
        index = index + 1
    return t_print

def update_num_strikes(gues, targ, n_strikes):
    if gues in targ:
        n_strikes
    else:
        n_strikes = n_strikes + 1
    return n_strikes
    
def print_word(t_print):
    for i in range(len(t_print)):
        print(t_print[i] , end = ' ')

def print_strikes(n_strikes):
    print("\nStrikes: ", end = ' ')
    for i in range(n_strikes):
        print("X" , end = ' ')

def make_array(targ):
    arr = []
    for i in targ:
        arr.append("_")
    return arr

def get_input():
    g = str(input("\nGuess a letter from A-Z: ")).upper()
    while(g.isalpha() == False):
        g = str(input("\nPlease try again with a letter: ")).upper()

    return g

def get_keep_going(t_print, n_strikes):
    if("_" not in t_print):
        return False
    elif(n_strikes < MAX_STRIKES):
        return True
    elif(n_strikes > MAX_STRIKES):
        return False

def main():
    target = get_random_word()
    to_print = make_array(target)
    num_strikes = 0

    print_word(to_print)

    while(get_keep_going(to_print, num_strikes)):

        print_strikes(num_strikes)
        guess = get_input()
        num_strikes = update_num_strikes(guess, target, num_strikes)
        print_word(update_blanks(guess, target, to_print))

    if("_" not in to_print):
        print("\nYou won :)")
    elif("_" in to_print):
        print("\nStrikes:", end = ' ')
        for i in range(MAX_STRIKES):
            print("X", end = ' ')
        print("\nYou lost :(")
        print("The word was '" + target + "'")
    

main()
