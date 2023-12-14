# Вариант 20
"""
Дан список размера N и целые числа K и L (1 <K < L <N).
Найти среднее арифметическое элементов список с номерами от K до L включительно.
"""
while True:
    try:
        from random import randint
        N = int(input("Введите длину списка: "))
        a = []
        u = 0
        sr = 0
        summ = 0
        L = int(input("Введите первое число: "))
        K = int(input("Введите второе число: "))
        for i in range(0, N):
            a.append(randint(1, 2))
            if L <= i <= K:
                summ += a[i]
                u += 1
                print("Обрабатываемый элемент списка: " + str(a[i]))
        sr = summ/u
        print(f'Среднее арифметическое между элементами списка под номерами {L} и {K}: {sr} ')
        break
    except ValueError:
        print('Введи число')