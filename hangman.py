# -*- coding: utf-8 -*-
from abstract_word import AbstractWord
from chance import Chance, ChancesError
from game_level.game_level import GameLevel
from words_from_file import WordsFromFile


class Hangman:
    def __init__(self, word: AbstractWord, chance):
        if not isinstance(word, AbstractWord):
            raise ValueError('word needs to be instance of AbstractWord')

        self.random_word = word.get_random_word()
        self.chance = chance
        self.word_to_guess = ['_' for i in self.random_word]

    def loose(self):
        print('Przegrałeś(aś) :P')
        self.print_word_to_find()

    def win(self):
        print('Gratulacje !!!')
        self.print_word_to_find()

    def play(self):
        while '_' in self.word_to_guess:
            print(' '.join(self.word_to_guess))
            print(f'Masz jeszcze {self.chance.get_chances()} szans')

            letter = input('Podaj literę lub całe słowo: ').lower()

            if letter == self.random_word:
                self.win()
                break

            try:
                letter = letter[0]
            except IndexError:
                print('\nTy pacanie, wpisz coś!!!!\n')
                continue

            try:
                if letter in self.word_to_guess:
                    print('Ale to już było... Czytać nie umiesz?')
                    self.chance.decrease()

                if letter not in self.random_word:
                    self.chance.decrease()

            except ChancesError:
                self.loose()
                break

            self.append_letter(letter)

        if '_' not in self.word_to_guess:
            self.win()

    def print_word_to_find(self):
        print(f'Szukane słowo to: "{self.random_word}"')

    def append_letter(self, letter):
        index_start = 0
        for i in range(self.random_word.count(letter)):
            letter_index = self.random_word.index(letter, index_start)
            index_start = letter_index + 1
            self.word_to_guess[letter_index] = letter


if __name__ == '__main__':
    while 't' == input('Wciśnij "t" aby grać...').lower():
        word = WordsFromFile()
        game_level = GameLevel(Chance)
        chance = game_level.get_level_chances()
        Hangman(word, chance).play()
