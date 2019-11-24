# -*- coding: utf-8 -*-
from chance import ChancesError


class ChanceFromA:
    def __init__(self, chance=1):
        self.chances = 1

    def get_chances(self):
        return self.chances

    def decrease(self):
        self.chances -= 1

        if self.chances == 0:
            raise ChancesError('No more chances :P')
