# -*- coding: utf-8 -*-
from random import randint

from abstract_word import AbstractWord


class Word(AbstractWord):
    words = ('test',)

    def get_random_word(self) -> str:
        word_index = randint(0, len(self.words) - 1)
        return self.words[word_index]


if __name__ == '__main__':
    print(Word().get_random_word())
