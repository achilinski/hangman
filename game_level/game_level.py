# -*- coding: utf-8 -*-
from chance import Chance
from game_level.abstract_level import AbstractLevel
from game_level.levels import Easy, Normal, Hard


class GameLevel:
    __levels = (
        Easy(),
        Normal(),
        Hard()
    )

    def __init__(self, chance):
        self.chances = chance

    def get_level_chances(self):
        for i in range(len(self.__levels)):

            if not isinstance(self.__levels[i], AbstractLevel):
                raise ValueError('Incorrect object Instance. Expected AbstractLevel')

            print('{lp}. {level}'.format(
                lp=str(i + 1),
                level=self.__levels[i].get_name()
            )
            )

        level = int(input('Wybierz stopień trudności: '))

        if 0 < level <= len(self.__levels):
            return self.chances(self.__levels[level - 1].get_chances())

        return self.get_level_chances()
