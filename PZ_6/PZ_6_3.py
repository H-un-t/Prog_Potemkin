# Вариант 20
"""
Дан список размера N, все элементы которого, кроме одного, упорядочены по убыванию.
Сделать список упорядоченным, переместив элемент, нарушающий упорядоченность, на новую позицию.
"""
while True:
    try:
        from random import randint
        N = int(input("Введите длину списка: "))
        a = []
        for i in range(0, N):
            a.append(randint(-100, 100))
        a.sort(reverse=True)


        d = int(input("число: "))

        a.append(d)
        print('Неотсортированый список' + str(a))
        a.sort(reverse=True)
        print('Отсортированый список' + str(a))
        break
    except ValueError:
        print('Введи число')