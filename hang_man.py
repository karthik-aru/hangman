#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 17:35:26 2021

@author: karthikarumugam
"""

import random
import string

word_list = ["breaking bad", "terminator", "inception", "interstellar"]


"""
picks a random word from the list
"""

def choose_word(word_list):
    """
    picks a random word from the list
    """
    
    return random.choice(word_list)

"""
checks if the word has been guessed based on the player's guesses
"""

def is_word_guessed(word, lett_guesses):
    
    
    # word is a string chosen by the computer
    # lett_guesses: list of letters, guessed by the user
    # returns True if all the letters of word are in lett_guesses or False otherwise
    
    matched_chars = 0
    
    # count the number of matched characters from the lett_guesses in the word
    for char in lett_guesses:
        for schar in word:
            if char == schar:
                matched_chars += 1
                break
    
    # Return True if the length of the secret word matches the count of matched characters
    if matched_chars == len(set(word)):
        return True
    else:
        return False



"""
get the guessed word with letters-guessed by the player
"""

def get_guessed_word(word, lett_guesses):
    
    # word is a string chosen by the computer
    # lett_guesses: list of letters, guessed by the user
    # returns a string with the matching characters from the secret word or _ for letters remaining to be guessed
    

    guessed_word = []

    for i in range(len(word)):
        if word[i] == " ":
            guessed_word.append("*")
        else:
            if word[i] not in lett_guesses:
                guessed_word.append('_ ')
            else:
                guessed_word.append(word[i])

    guessed_word_string = ''.join(guessed_word)

    return guessed_word_string


    """
    get the letters that are available for the player to guess
    """


"""
gets the available letter that have not been guessed by the player
"""

def get_available_letters(lett_guesses = []):
    
    """
    Takes as input a list of the guessed letters and returns a string of the 
    unguessed letters
    """
    
    all_letters_list = list(string.ascii_lowercase) # create a list of alphabets
    index = 0
    available_letters = ''

    # Return all alphabets if no letters guessed, otherwise return the unguessed letters
    
    if len(lett_guesses) == 0:
        available_letters = ''.join(all_letters_list)
    else:
        for char in all_letters_list:
            if char not in lett_guesses:
                available_letters += all_letters_list[index]
            else:
                available_letters += "_"
            index += 1

    return available_letters


"""
give a hint if the user chooses ?
"""
def get_hints(word, hint_index):
    
    word_hints = {"breakingbad" : ["Actor : Bryan Cranston", "Blue Crystal", "Heisenberg"],
                  "terminator" : ["Actor : Arnold Schwarzenegger", "Skynet", "I'll be back"],
                  "interstellar" : ["Actress : Jessica Chastain", "Gargantua", "Space/Time travel"],
                  "inception" : ["Actress : Marion Cotillard", "An idea in a dream", "Cobb"]}
    
    hints = word_hints.get(word)
    
    return hints[hint_index]


"""
where everything comes together
"""

def hangman(sec_word):

    word_no_spaces = sec_word.replace(" ", "")
    word_uniq_lett = set(word_no_spaces) # get the unique letters in the word
    
    no_of_word_uniq_lett = len(word_uniq_lett)
    
    hint_indexes = [0, 1, 2]
    lett_guesses = []
    guesses_remaining = 6
    warnings = 3
    vowels = ['a','e','i','o','u']
    
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is ", len(word_no_spaces), " letters long")
    print("-----------")
 
    while guesses_remaining > 0:
        print("You have",guesses_remaining, "guesses,", len(hint_indexes), "hints and", warnings, "warnings left.")
        print("Available letters: ", get_available_letters(lett_guesses))
        char = input("Please guess a letter: ").lower()
        if char == "?":
            if len(hint_indexes) > 0:
                hint_index = random.choice(hint_indexes)
                print("Your hint is : ", get_hints(word_no_spaces, hint_index))
                hint_indexes.remove(hint_index)
                print("You have " + str(len(hint_indexes)) + " hints left.")
            else:
                print("No more hints left")
        elif char == "!":
            lucky_guess = set(input("Please enter the full word : "))
            if is_word_guessed(word_no_spaces, lucky_guess):
                print("Congratulations you won!")
                print("Your total score for this game is:", guesses_remaining * no_of_word_uniq_lett)
                lett_guesses = lucky_guess
                break
            else:
                print("Nope, that's not it")
        elif char.isalpha():
            if char not in lett_guesses:
                lett_guesses.append(char.lower())
                if char in word_uniq_lett:
                    if is_word_guessed(word_no_spaces, lett_guesses):
                        print("Congratulations you won!")
                        print("Your total score for this game is:", guesses_remaining * no_of_word_uniq_lett)
                        break
                    else:
                        print("Good guess:", get_guessed_word(sec_word, lett_guesses))
                else:
                    print("Oops that letter is not in my word:", get_guessed_word(sec_word, lett_guesses))
                    if char in vowels:
                        guesses_remaining -= 2
                    else:
                        guesses_remaining -= 1
            else:
                if warnings > 0:
                    warnings -= 1
                else:
                    guesses_remaining -= 1
                print("Oops! You've already guessed that letter. You now have", warnings, "warnings:", get_guessed_word(sec_word, lett_guesses))
        else:
       
            if warnings > 0:
                warnings -= 1
            else:
                guesses_remaining -= 1
            print("Oops that is not a valid letter. You have", warnings, "warnings left")
        print("----------------------------")
    if not is_word_guessed(word_no_spaces, lett_guesses):
        print("Sorry, you ran out of guesses. The word was", sec_word)
        

if __name__ == "__main__":
    
    hangman(choose_word(word_list))
