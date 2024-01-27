# вариант 20

"""
Используя словарь посчитать количество уникальных слов в заданном предложении <<Изучаем язык Питон>>.
Вывести на экран каждую пару <<ключ:значение>>.
"""
sen = "Изучаем язык Питон"
words = sen.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Количество уникальных слов в предложении:", len(word_count))

for key, value in word_count.items():
    print(key, ":", value)