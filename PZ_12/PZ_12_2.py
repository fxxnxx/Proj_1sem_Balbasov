# Составить функцию, которая напечатает сорок любых символов.
import random
import string
from tkinter import *


rand_string = 0


def close():
    root.destroy()
    root.quit()


def generate(length):  # Генерация случайных символов
    global rand_string
    letters_and_digits = string.ascii_letters + string.digits
    rand_string = ''.join(random.sample(letters_and_digits, length))
    str(rand_string)
    lb0 = Label(text='')
    lb0.place(x=400, y=231, width=800, anchor='center')
    lb3 = Label(text=rand_string, font=('Times', 17))
    lb3.place(x=530, y=180, anchor='center') # Результат генерации


root = Tk()
root.title("Генератор")
root.geometry('900x400') # Окно


lb1 = Label(text='Введите количество символов, которое нужно сгенерировать (не больше 62): ', font=('Times', 15))
lb2 = Label(text='Результат:', font=('Times', 15))


lb1.place(x=450, y=10, anchor='center')  # Ввод
lb2.place(x=400, y=180, anchor='center')  # Результат


ent1 = Entry(bd=2, width=24)
ent1.place(x=450, y=70, anchor='center') # Поле ввода


def bttn_clicked():
    x = int(ent1.get())
    generate(x)


bt1 = Button(text='Сгенерировать', width=15, font=('Times', 14), command=bttn_clicked)
bt1.place(x=450, y=110, anchor='center') # Кнопка сгенерировать

root.mainloop()