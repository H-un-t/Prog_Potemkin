# Вариант 20

"""
Из заданной строки отобразить только символы нижнего регистра.
Использовать библиотеку string. Строка 'In PyCharm,
you can specify third-party standalone applications and run them as External Tools'.
"""

import string

input_string = 'In PyCharm, you can specify third-party standalone applications and run them as External Tools'

lowercase_chars = (char for char in input_string if char in string.ascii_lowercase)

for char in lowercase_chars:
    print(char, end='')
