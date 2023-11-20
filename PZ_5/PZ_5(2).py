# Описать функцию Swap, меняющую содержимое переменных X и Y. С ее помощью для данных переменных A, B, C, D
# последовательно поменять содержимое следующих пар: A и B, C и D, B и C и вывести новые значения A, B, C, D.


def Swap(x, y):
    print(x, y)
    c = x
    x = y
    y = c
    print(x, y)
    print()


A, B, C, D = input("Введите число А: "), input("Введите число B: "), input("Введите число C: "), input("Введите число D: ")

while type(A) != int:
    try:
        A = int(A)
    except ValueError:
        print("\nВведите целый тип данных для A")
        A = input("Введите значение для A: ")

while type(B) != int:
    try:
        B = int(B)
    except ValueError:
        print("\nВведите целый тип данных для B")
        B = input("Введите значение для B: ")

while type(C) != int:
    try:
        C = int(C)
    except ValueError:
        print("\nВведите целый тип данных для C")
        C = input("Введите значение для C: ")

while type(D) != int:
    try:
        D = int(D)
    except ValueError:
        print("\nВведите целый тип данных для D")
        D = input("Введите значение для D: ")

Swap(A, B)
Swap(C, D)
Swap(B, C)
