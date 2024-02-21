# Вариант 20

"""
Из предложенного текстового файла (text18-20.txt) вывести на экран его содержимое,
количество символов в тексте. Сформировать новый файл,
в который поместить строку наибольшей длины.
"""


with open('text18-20.txt', 'r', encoding="UTF-16") as file:
    text = file.read()
    char_count = len(text)

    print("Содержимое файла:")
    print(text)
    print(f"Количество символов в тексте: {char_count}")

lines = text.split('\n')
max_length_line = max(lines, key=len)


with open('Строка_наибольшей_длины_PZ_11_2.txt', 'w') as file:
    file.write(max_length_line)

