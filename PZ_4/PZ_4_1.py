# Вариант 20
"""
Дано вещественное число Х и целое число N (> 0).
1 - X²/(2!) +  X⁴/(4!) - … + (-1)ⁿ*¹/((2-N)!) (N! = 12 …N).
Полученное число является приближенным значением функции cos в точке X.
"""


while True:
    try:
        X = float(input("Введите вещественное число =>"))
        N = int(input("введите целое число больше нуля =>"))
        R = 1
        F = 1
        for i in range(1, N+1):
            F *= 2*i*(2*N+1)
            if i % 2 == 1:
                R -= X ** (2*i) / F
            else:
                R += X ** (2 * i) / F
        print(f"Значение  выражение:{R}")
        break
    except ValueError:
        print("Нужно ввести число")

# for in range цикл с счётчиком и он выполняется 1 до н +1
# R = R + X ** (2 * i) / FR += X ** (2 * i) / F сжато записывается так R += X ** (2 * i) / F