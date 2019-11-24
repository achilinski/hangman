# -*- coding: utf-8 -*-
from time import time


def nwd(a: int, b: int) -> int:
    if a == b:
        return a

    if a > b:
        return nwd(a - b, b)

    return nwd(a, b - a)


def nwd_w(a: int, b: int) -> int:
    while a != b:
        a, b = (a - b, b) if a > b else (a, b - a)

    return a


a, b = input('podaj a i b po przecinku: ').split(',')
nwd_w_start = time()
print(nwd_w(int(a), int(b)))
nwd_w_stop = time()
nwd_start = time()
print(nwd(int(a), int(b)))
nwd_stop = time()
print(nwd_start)
print(f'NWD W: {nwd_w_stop - nwd_w_start}')
print(f'NWD  : {nwd_stop - nwd_start}')