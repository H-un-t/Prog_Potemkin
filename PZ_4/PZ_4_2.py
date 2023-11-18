
"""
Вариант 20
Дано целое число N (> 0). Найти сумму 1¹+ 2² + … + Nⁿ
"""


while True:
    try:
        N = int(input("введите целое число больше нуля =>"))
        S = 0
        for k in range(1, N+1):
            S = S + (k ** k)
        print(f'результат: {S}')
        break
    except ValueError:
        print("Нужно ввести число")
