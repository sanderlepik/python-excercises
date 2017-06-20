#-*- coding: utf-8 -*-
import helpers


class WordGuess():

    def word_game(self):
        """Contemplation..."""
        word = helpers.set_guess_word().lower()

        guesses = len(helpers.set_guess_word()) + 3
        letters_guessed = []
        print("===========")
        print(" WORD GAME")
        print("===========")
        print("Guess the word (it is " + str(len(word)) + " characters long): ")

        while guesses != 0:
            letter = raw_input("Enter a letter: ").lower()

            if letter in letters_guessed:
                print "You already guessed that letter."

            else:
                guesses = guesses - 1
                print "You have %d guesses left." % (guesses)
                letters_guessed.append(letter)
                guessed_word = helpers.word_update(word, letters_guessed)

                if (set(list(guessed_word)) < set(letters_guessed)):
                    print "Congratulations, %s is the correct word!" % (word.upper())
                    break

        if guesses == 0:
            print "YOU LOST!!"


if __name__=="__main__":
    game = WordGuess()
    game.word_game()


