# Вариант 20

"""
Создание базового класса "Работник" и его наследование для создания классов "Менеджер" и "Инженер".
В классе "Работник" будут общие методы, такие как "работать" и "получать зарплату",
а классы-наследники будут иметь свои уникальные методы и свойства,
такие как "управлять командой" и "проектировать системы".
"""

class Rabotnik:
    def __init__(self, name, age, zp):
        self.name = name
        self.age = age
        self.zp = zp

    def rabotat(self):
        print(f"{self.name} работает")

    def get_zp(self):
        print(f"{self.name} получает зарплату в размере {self.zp}")


class Meneger(Rabotnik):
    def ypravlit_comandoi(self):
        print(f"{self.name} управляет командой")


class Inginer(Rabotnik):
    def proectirovat_sistemy(self):
        print(f"{self.name} проектирует системы")



Rabotnik1 = Rabotnik("Иван", 30, 50000)
Rabotnik1.rabotat()
Rabotnik1.get_zp()

Meneger1 = Meneger("Мария", 35, 60000)
Meneger1.rabotat()
Meneger1.get_zp()
Meneger1.ypravlit_comandoi()

Inginer1 = Inginer("Петр", 28, 55000)
Inginer1.rabotat()
Inginer1.get_zp()
Inginer1.proectirovat_sistemy()
