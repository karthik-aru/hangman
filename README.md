<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Hangman


## Project Description
The game hangman allows the player to guesse a word (from a list of movies) randomly chosen by the computer.
I have included several features that exploit the use of if conditional statments, while loops, string/list indexing and manipulation and modular programming.
   
## Rules
The computer selects a random word from a list
The player gets 6 total guesses, 3 hints and 3 warnings
Wrong guess : -1 guess
Non-alphabetical character (except for ? or !) : -1 warning, after 0 warnings : -1 guess
Guessed a vowel that is wrong :  -2 guesses
Typing a “?” gives you a randomly chosen hint
Typing a “!” gives you the option to guess the whole word
Final score : unique letters *  no of remaining guesses


## Workflow

After researching the game, I found several rules and feature that I could implement in the code

I also thought about the get and set methods for the basic functioning of the game.
 
I then chose to write a function per feature, get or set methods

I split the program into 6 functions - 

1. choose_word(word_list)
2. is_word_guessed(word, lett_guesses)
3. get_guessed_word(word, lett_guesses)
4. get_available_letters(lett_guesses = [])
5. get_hints(word, hint_index)
6. hangman(sec_word)
 
 I first designed the functions 1-5 individually and tested them one at a time for any bugs. 
 Finally I designed the hangman function which connects all the functions and is the heart of the game.
 

