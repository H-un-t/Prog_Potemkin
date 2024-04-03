# Вариант 20

"""
В последовательности на n целых элементов в первой ее половине найти
количество положительных элементов.
"""

import random


def count(seq):
    half_length = len(seq) // 2
    for i in range(half_length):
        if seq[i] > 0:
            yield 1
        else:
            yield 0


sequence = [random.randint(-5, 5) for n in range(random.randint(2, 10))]
print("Сгенерированная последовательность:", sequence)
result = sum(list(count(sequence)))
print("Количество положительных элементов в первой половине:", result)
