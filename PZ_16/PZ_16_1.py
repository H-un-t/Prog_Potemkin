# Вариант 20

"""
Создайте класс «Счетчик»,
который имеет атрибут текущего значения
и методы для инкремента и декремента значения.
"""


class Counter:

    def __init__(self, znachenie):
        self.znachenie = znachenie


    def incriment(self):
        self.znachenie += 1


    def uncriment(self):
        self.znachenie -= 1



Counter = Counter(10)
print(Counter.znachenie)

Counter.incriment()
print(Counter.znachenie)

Counter.uncriment()
print(Counter.znachenie)
