# Вариант 20
'''
Проверить истинность высказывания: «Среди трех данных целых чисел есть хотя бы одна пара взаимно противоположных».
'''
i = 0
while i == 0:
    try:
        z = int(input("введите первое число ->"))
        x = int(input("введите второе число ->"))
        c = int(input("введите третье число ->"))
        if (abs(z) == abs(x) and z != x) or (abs(x) == abs(c) and x != c) or (abs(z) == abs(c) and z != c):
            print("<ИСТИНА>")
        else:
            print("<ЛОЖЬ>")
        i = 1
    except ValueError:
        print("Нужно ввести число")


# abs это абсолютное число (модуль)

