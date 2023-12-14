# Вариант 20
"""
 Дан целочисленный список размера N, Найти максимальное количество его одинаковых элементов.
"""

from random import randint

while True:
    try:
        a = int(input("Введите количество элементов в списке ->"))
        break
    except ValueError:
        print("Нужно ввести число")
m = 0
f = []
for i in range(a):
    f.append(randint(1, 10))
print(f)
for i in f:
    count = f.count(i)
    if count > m:
        m = count

print(f"Максимальное количество одинаковых элементов: {m}")