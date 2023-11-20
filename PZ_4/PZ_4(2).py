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

area_of_sqr, count = 0, 0
area_of_rectangle = A * B

while area_of_sqr < area_of_rectangle:
    area_of_sqr += C ** 2
    count += 1

if area_of_sqr > area_of_rectangle:
    count -= 1

print(f"Количество квадратов, размещенных на прямоугольнике: {count}")
