"""
Для задачи из блока 1 создать две функции, save_def u load_def,
которые позволяют сохранять информацию из экземпляров класса (3 шт.) в файл и загружать ее обратно.
Использовать модуль pickle для сериализации и десериализации объектов Python в бинарном формате.
"""


import pickle


class Counter:
    def __init__(self, znachenie):
        self.znachenie = znachenie

    def incriment(self):
        self.znachenie += 1

    def uncriment(self):
        self.znachenie -= 1

def save_def(obj, filename):
    with open(filename, 'wb') as file:
        pickle.dump(obj, file)

def load_def(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)


counter1 = Counter(10)
counter2 = Counter(5)
counter3 = Counter(20)


counter1.incriment()
counter2.incriment()
counter3.incriment()

counter1.uncriment()
counter2.uncriment()
counter3.uncriment()

save_def(counter1, 'counter1.pkl')
save_def(counter2, 'counter2.pkl')
save_def(counter3, 'counter3.pkl')


loaded_counter1 = load_def('counter1.pkl')
loaded_counter2 = load_def('counter2.pkl')
loaded_counter3 = load_def('counter3.pkl')


print(loaded_counter1.znachenie)
print(loaded_counter2.znachenie)
print(loaded_counter3.znachenie)
