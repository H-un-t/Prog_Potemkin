# Вариант 20
#  https://itkoding.com/wp-content/uploads/2020/05/contoh-tampilan-form-pendaftaran-
# dengan-html.png

"""
В соответствии с номером варианта перейти по ссылке на прототип. Реализовать
его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально
приближенный к оригиналу (см. таблицу 1).
"""

import tkinter as tk
from tkinter import ttk


def submit():
    print('Form submitted')


def reset():
    username_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    birthdate_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    gender_var.set('Pria')
    agree_var.set(0)


def on_entry_click(event):
    if username_entry.get() == 'Username anda':
        username_entry.delete(0, "end")
        username_entry.insert(0, '')
        username_entry.config(fg='black')


def on_focusout(event):
    if username_entry.get() == '':
        username_entry.insert(0, 'Username anda')
        username_entry.config(fg='grey')


def on_entry_click_2(event):
    if email_entry.get() == 'almat email':
        email_entry.delete(0, "end")
        email_entry.insert(0, '')
        email_entry.config(fg='black')


def on_focusout_2(event):
    if email_entry.get() == '':
        email_entry.insert(0, 'almat email')
        email_entry.config(fg='grey')


def on_entry_click_3(event):
    if address_entry.get() == 'almat rumah':
        address_entry.delete(0, "end")
        address_entry.insert(0, '')
        address_entry.config(fg='black')


def on_focusout_3(event):
    if address_entry.get() == '':
        address_entry.insert(0, 'almat rumah')
        address_entry.config(fg='grey')


def on_entry_click_4(event):
    if age_entry.get() == 'usia anda':
        age_entry.delete(0, "end")
        age_entry.insert(0, '')
        age_entry.config(fg='black')


def on_focusout_4(event):
    if age_entry.get() == '':
        age_entry.insert(0, 'usia anda')
        age_entry.config(fg='grey')


def on_entry_click_date(event):
    if birthdate_entry.get() == 'mm/dd/yyyy':
        birthdate_entry.delete(0, "end")
        birthdate_entry.insert(0, '')
        birthdate_entry.config(fg='black')


def on_focusout_date(event):
    if birthdate_entry.get() == '':
        birthdate_entry.insert(0, 'mm/dd/yyyy')
        birthdate_entry.config(fg='black')


r = tk.Tk()
r.geometry('400x350')
r.title('User Form')


login_frame = ttk.LabelFrame(r, text='User login info')
login_frame.grid(row=0, column=0, padx=0, pady=10)

tk.Label(login_frame, text='Username:').grid(row=0, column=0, sticky=tk.W)
username_entry = tk.Entry(login_frame)
username_entry.grid(row=0, column=1)
username_entry.insert(0, 'Username anda')
username_entry.bind('<FocusIn>', on_entry_click)
username_entry.bind('<FocusOut>', on_focusout)
username_entry.config(fg='grey')

tk.Label(login_frame, text='Email:').grid(row=1, column=0, sticky=tk.W)
email_entry = tk.Entry(login_frame)
email_entry.grid(row=1, column=1)
email_entry.insert(0, 'almat email')
email_entry.bind('<FocusIn>', on_entry_click_2)
email_entry.bind('<FocusOut>', on_focusout_2)
email_entry.config(fg='grey')

tk.Label(login_frame, text='Password:').grid(row=2, column=0, sticky=tk.W)
password_entry = tk.Entry(login_frame, show='*')
password_entry.grid(row=2, column=1)


data_frame = ttk.LabelFrame(r, text='Data diri')
data_frame.grid(row=1, column=0, padx=10, pady=10)

tk.Label(data_frame, text='Alamat:').grid(row=0, column=0, sticky=tk.W)
address_entry = tk.Entry(data_frame)
address_entry.grid(row=0, column=1)
address_entry.insert(0, 'almat rumah')
address_entry.bind('<FocusIn>', on_entry_click_3)
address_entry.bind('<FocusOut>', on_focusout_3)
address_entry.config(fg='grey')

tk.Label(data_frame, text='Tanggal lahir:').grid(row=1, column=0, sticky=tk.W)
birthdate_entry = tk.Entry(data_frame)
birthdate_entry.grid(row=1, column=1)
birthdate_entry.insert(0, 'mm/dd/yyyy')
birthdate_entry.bind('<FocusIn>', on_entry_click_date)
birthdate_entry.bind('<FocusOut>', on_focusout_date)
birthdate_entry.config(fg='black')

tk.Label(data_frame, text='Usia:').grid(row=2, column=0, sticky=tk.W)
age_entry = tk.Entry(data_frame)
age_entry.grid(row=2, column=1)
age_entry.insert(0, 'usia anda')
age_entry.bind('<FocusIn>', on_entry_click_4)
age_entry.bind('<FocusOut>', on_focusout_4)
age_entry.config(fg='grey')
tk.Label(data_frame, text='Jenis kelamin:').grid(row=3, column=0, sticky=tk.W)
gender_var = tk.StringVar(value='Pria')
tk.Radiobutton(data_frame, text='Pria', variable=gender_var, value='Pria').grid(row=3, column=1, sticky=tk.W)
tk.Radiobutton(data_frame, text='Wanita', variable=gender_var, value='Wanita').grid(row=3, column=2, sticky=tk.W)


agree_var = tk.IntVar()
tk.Checkbutton(r, text="Saya bersedia mengikuti aturan forum", variable=agree_var).grid(row=2, column=0, padx=10,
                                                                                           pady=10)


button_frame = tk.Frame(r)
button_frame.grid(row=3, column=0, pady=10)

tk.Button(button_frame, text="Reset", command=reset).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Submit", command=submit).pack(side=tk.LEFT, padx=5)


r.mainloop()


