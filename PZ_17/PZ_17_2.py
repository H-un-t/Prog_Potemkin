
 #Скрость первого автомобиля Vi км/ч, второго - V2 км/ч, расстояние между ними S км. Определить расстояние между ними
# через Т часов, если автомобили удаляются друг от друга. Данное расстояние равно сумме начального растояния и общего пути,
# проделанного автомобилями; общий путь + время * суммарная скорость.

"""
Разработать программу с применением пакета tk, взяв в качестве условия одну
любую задачу из ПЗ NoNo 2 – 9.
"""

import tkinter as tk
from tkinter import messagebox


def calculate_distance():
    try:
        dis = float(entry1.get())
        vi = float(entry2.get())
        v2 = float(entry3.get())
        t = float(entry4.get())
        s = dis + (vi + v2) * t
        result_label.config(text=str(s) + " >> расстояние между машинами через " + str(t) + " часов")
    except ValueError:
        messagebox.showerror("Ошибка", "Нужно ввести число")


r = tk.Tk()
r.geometry('400x230')
r.title("Расчет расстояния между машинами")

label1 = tk.Label(r, text="Расстояние между машинами")
label1.pack()
entry1 = tk.Entry(r)
entry1.pack()

label2 = tk.Label(r, text="Скорость первой машины")
label2.pack()
entry2 = tk.Entry(r)
entry2.pack()

label3 = tk.Label(r, text="Скорость второй машины")
label3.pack()
entry3 = tk.Entry(r)
entry3.pack()

label4 = tk.Label(r, text="Время в часах")
label4.pack()
entry4 = tk.Entry(r)
entry4.pack()

calculate_button = tk.Button(r, text="Вычислить", command=calculate_distance)
calculate_button.pack()

result_label = tk.Label(r, text="")
result_label.pack()

r.mainloop()