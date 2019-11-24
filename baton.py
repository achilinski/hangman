# -*- coding: utf-8 -*-


class Baton:
    def __init__(self, sweet: int = 8, nuts: int = 9):
        self.__sweet = sweet
        self.nuts = nuts

    def set_sweet(self, sweet):
        if sweet > 10:
            raise ValueError('Wywaliło skalę')

        self.__sweet = sweet

    def get_sweet(self):
        return self.__sweet


snickers = Baton(10)
mars = Baton(nuts=0)
print(Baton().get_sweet())
print(f'snickers jest słodki na: {snickers.get_sweet()}')
snickers.set_sweet(5)
print(f'snickers jest słodki na: {snickers.get_sweet()}')
print(f'mars jest słodki na: {mars.get_sweet()}')
