# -*- coding: utf-8 -*-
from game_level.abstract_level import AbstractLevel


class Easy(AbstractLevel):
    def __init__(self, chances=21):
        self.chances = chances

    def get_chances(self):
        return self.chances

    @staticmethod
    def get_name():
        return 'Easy'
