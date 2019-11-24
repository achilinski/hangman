from chance import Chance
from hangman import Hangman
from word import Word

if __name__ == '__main__':
    while 't' == input('Wciśnij "t" aby grać...').lower():
        Hangman(Word(), Chance()).play()
