# -*- coding: utf-8 -*-
class ChancesError(ValueError):
    pass


class Chance:
    def __init__(self, chances: int = 12):
        self.chances = chances

    def get_chances(self):
        return self.chances

    def decrease(self):
        self.chances -= 1

        if self.chances == 0:
            raise ChancesError('No more chances :P')
