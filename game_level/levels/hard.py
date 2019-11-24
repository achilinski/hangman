# -*- coding: utf-8 -*-
from game_level.abstract_level import AbstractLevel


class Hard(AbstractLevel):

    def get_chances(self):
        return 5

    @staticmethod
    def get_name():
        return 'Hard'
