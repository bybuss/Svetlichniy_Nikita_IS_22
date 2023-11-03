#


def Swap(x, y):
    print(x, y)
    c = x
    x = y
    y = c
    print(x, y)
    print()


A, B, C, D = input("Введите число А: "), input("Введите число B: "), input("Введите число C: "), input("Введите число D: ")

Swap(A, B)
Swap(C, D)
Swap(B, C)
