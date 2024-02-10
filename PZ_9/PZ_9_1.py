# вариант 20

"""
Используя словарь посчитать количество уникальных слов в заданном предложении <<Изучаем язык Питон>>.
Вывести на экран каждую пару <<ключ:значение>>.
"""
sen = "Изучаем язык язык Питон"
words = sen.split()

word_co = {}

for word in words:
    if word in word_co:
        word_co[word] += 1
    else:
        word_co[word] = 1

print("Количество уникальных слов в предложении:", len(word_co))

for key, value in word_co.items():
    print(key, ":", value)
