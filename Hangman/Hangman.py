import random
from Words import words
import string

def get_valid_word(words):
    word = random.choice(words) # Randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # What the user has guessed

    # getting user input
    while len(word_letters) > 0:
        #letters used
        print("You have used these letters: ", " ".join(used_letters)) # " ".join([a', 'b', 'cd']) --> 'a b cd'
        
        # what current word is (i.e. W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", ' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

        elif user_letter in used_letters:
            print("You have already used that character. Please choose another.")
        else:
            print("Invalid character. Please choose another.")

hangman()

