"""
Разработать программу с применением пакета tk, взяв в качестве условия одну
любую задачу из ПЗ №№ 2 – 9.
"""

from tkinter import *
from PZ_5.PZ_5_2 import Swap


def swap_values():
    x = x_entry.get()
    y = y_entry.get()
    swapped_x, swapped_y = Swap(x, y)
    result_label.config(text=f"До: {x} | {y}\nПосле: {swapped_x} | {swapped_y}")


root = Tk()
root.title("Swap Values")
root.geometry("400x200")

x_label = Label(root, text="Введите значение для x:")
x_label.grid(row=0, column=0, padx=10, pady=5, sticky=E)
x_entry = Entry(root)
x_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

y_label = Label(root, text="Введите значение для y:")
y_label.grid(row=1, column=0, padx=10, pady=5, sticky=E)
y_entry = Entry(root)
y_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

swap_button = Button(root, text="Поменять местами", command=swap_values)
swap_button.grid(row=2, column=0, pady=10)

result_label = Label(root, text="")
result_label.grid(row=2, column=1, pady=10)

root.mainloop()
