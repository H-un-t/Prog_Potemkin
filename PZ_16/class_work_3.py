class Per:
    count = 0

    def __init__(self, age):
        self.age = age
        Per.count += 1


    @staticmethod
    def static():
        print(f'Создано экземпляров класса: {Per.count}')


e1 = Per('20')
e2 = Per('2020')
e3 = Per('2030')
Per.static()
