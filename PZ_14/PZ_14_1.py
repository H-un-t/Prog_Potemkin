# Вариант 20

"""
Из текстого файла (writer.txt) выбрать фамилии писателей, посчитать количество фамилий.
Создать новый файл, в котором выполнить замену слова «роман» на слово «произведение».
"""

import re


with open('writer.txt', 'r') as file:
    text = file.read()


surnames = re.findall(r'[A-Z][a-z]+', text)


num_surnames = len(surnames)
print(f"Количество фамилий писателей: {num_surnames}")


new_text = re.sub(r'роман', 'произведение', text)

with open('new_writer.txt', 'w') as new_file:
    new_file.write(new_text)

print("Замена выполнена. Результат записан в файл new_writer.txt")