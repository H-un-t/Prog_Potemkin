# Вариант 20
"""
Составить функцию, которая напечатает сорок любых символов.
"""
from random import randint


def arbuz_228():
    for i in range(1, 41):
        f = randint(-10000, 10000)
        print(f' номер {i}: число {f} ')


arbuz_228()
