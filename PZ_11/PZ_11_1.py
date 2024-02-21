# Вариант 20

"""
Средствами языка Python сформировать текстовый файл (.txt),
содержащий последовательность из целых положительных и отрицательных чисел.
Сформировать новый текстовый файл (.txt) следующего вида,
предварительно выполнив требуемую обработку элементов:
Исходные данные:
Количество элементов:
Минимальный элемент:
Числа кратные трем:
Количество чисел кратных трем:
"""

import random

with open('Номера_PZ_11_1.1.txt', 'w') as file:
    numbers = [random.randint(-100, 100) for i in range(15)]
    file.write(' '.join(map(str, numbers)))

with open('Номера_PZ_11_1.1.txt', 'r') as file:
    data = file.read().split()
    numbers = list(map(int, data))

    co_elements = len(numbers)
    min_element = min(numbers)
    multiples_of_three = [num for num in numbers if num % 3 == 0]
    co_multiples_of_three = len(multiples_of_three)

with open('Номера_PZ_11_1.2.txt', 'w') as file:
    file.write(f'Исходные данные: {numbers}\n')
    file.write(f'Количество элементов: {co_elements}\n')
    file.write(f'Минимальный элемент: {min_element}\n')
    file.write(f'Числа кратные трем: {" ".join(map(str, multiples_of_three))}\n')
    file.write(f'Количество чисел кратных трем: {co_multiples_of_three}\n')
