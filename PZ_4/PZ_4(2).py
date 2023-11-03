# Найти кол-во квадратов С, размещенных на прямоугольнике A х B (без наложений). Умножения и деления не использовать.
A, B, C = input("Введите значение для А: "), input("Введите значение для В: "), input("Введите значение для С: ")

while type(A) != int:
 try:
    A = int(A)
 except ValueError:
    print("\nНеправильно ввели тип данных для А!")
    A = input("Введите значение для точки А: ")

while type(B) != int:
 try:
    B = int(B)
 except ValueError:
    print("\nНеправильно ввели тип данных для В!")
    B = input("Введите значение для точки В: ")

while type(C) != int:
 try:
    C = int(C)
 except ValueError:
    print("\nНеправильно ввели тип данных для С!")
    C = input("Введите значение для точки С: ")

sqr, count = 0, 0

while sqr < A * B:
    sqr += C ** 2
    count += 1

if sqr > A * B:
    count -= 1

print(f"Количество квадратов, размещенных на прямоугольнике: {count}")
