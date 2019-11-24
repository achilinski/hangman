# -*- coding: utf-8 -*-
from chance_from_a import ChanceFromA


class GameLevel:
    __levels = (
        {'name': 'Easy', 'chances': 21},
        {'name': 'Normal', 'chances': 12},
        {'name': 'Hard', 'chances': 6},
        {'name': 'Super Hard', 'chances': 3},
    )

    def __init__(self, chances):
        self.chances = chances

    def get_level_chances(self):
        for i in range(len(self.__levels)):
            print('{lp}. {level}'.format(
                lp=str(i + 1),
                level=self.__levels[i]['name'])
            )
        level = int(input('Wybierz stopień trudności: '))

        if 0 < level <= len(self.__levels):
            return self.chances(self.__levels[level - 1]['chances'])

        return self.get_level_chances()


if __name__ == '__main__':
    level = GameLevel(ChanceFromA)
    level.get_level_chances()
