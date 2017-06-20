import random


def set_guess_word():
    # type: () -> object
    word_list = ["Taevas", "Piljard", "Tugitool", "Kaevik", "Juurikas"]
    guess_word = random.choice(word_list)
    return guess_word

def word_update(word, letters_guessed):
    masked_word = ""
    for letter in word:
        if letter in letters_guessed:
            masked_word += letter
        else: masked_word += "-"
    print "The word:", masked_word
    return masked_word
