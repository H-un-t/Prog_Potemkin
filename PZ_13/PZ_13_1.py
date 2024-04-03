# Вариант 20

"""
В матрице найти сумму элементов первых двух строк.
"""
from random import randint

while True:
    try:
        m = int(input("Введите количество строк: "))
        n = int(input("Введите количество столбцов: "))


        def sum_of_first_two_rows(matrix):
            suma = sum(sum(row) for row in matrix[:2])
            return suma


        matrica = [[randint(1, 10) for j in range(n)] for i in range(m)]

        print("Исходная матрица:")
        for i in matrica:
            print(i)

        result = sum_of_first_two_rows(matrica)
        print("Сумма элементов первых двух строк матрицы:", result)
        break
    except ValueError:
        print("Нужно ввести число")