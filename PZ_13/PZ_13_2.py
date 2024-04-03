# Вариант 20

"""
В матрице найти минимальный и максимальные элементы.
"""

from random import randint

while True:
    try:
        m = int(input("Введите количество строк: "))
        n = int(input("Введите количество столбцов: "))


        def find_min_max(matrix):
            min_element = matrix[0][0]
            max_element = matrix[0][0]

            for row in matrix:
                for element in row:
                    if element < min_element:
                        min_element = element
                    if element > max_element:
                        max_element = element

            return min_element, max_element


        matrica = [[randint(1, 10) for j in range(n)] for i in range(m)]

        print("Исходная матрица:")
        for i in matrica:
            print(i)

        min_element, max_element = find_min_max(matrica)
        print("Минимальный элемент в матрице:", min_element)
        print("Максимальный элемент в матрице:", max_element)
        break
    except ValueError:
        print("Нужно ввести число")