# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


class AbstractWord(ABC):
    @abstractmethod
    def get_random_word(self) -> str:
        pass