# Вариант 20

"""
Дано целое положительное число. Вывести символы,
изображающие цифры этого числа (в порядке слева направо).
"""
while True:
    try:
        number = input("Введите число: ")
        for i in range(len(number)):
            print(f'Код символа номер {i}: ' + str(ord(number[i])))
        break
    except ValueError:
        print('Введи число')