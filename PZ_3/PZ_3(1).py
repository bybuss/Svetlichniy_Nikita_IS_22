x, y = input("Введите значение для x: "), input("Введите значение для y: ")
x1, y1 = input("Введите значение для x1: "), input("Введите значение для y1: ")
x2, y2 = input("Введите значение для x2: "), input("Введите значение для y2: ")

while type(x) != int:
    try:
        x = int(x)
    except ValueError:
        print("Вы ввели неккоректные данные, пожалуйста, введите значение для x еще раз!")
        x = input("Введите значение для x: ")

while type(y) != int:
    try:
        y = int(y)
    except ValueError:
        print("Вы ввели неккоректные данные, пожалуйста, введите значение для y еще раз!")
        y = input("Введите значение для y: ")

while type(x1) != int:
    try:
        x1 = int(x1)
    except ValueError:
        print("Вы ввели неккоректные данные, пожалуйста, введите значение для x1 еще раз!")
        x1 = input("Введите значение для x1: ")

while type(y1) != int:
    try:
        y1 = int(x)
    except ValueError:
        print("Вы ввели неккоректные данные, пожалуйста, введите значение для y1 еще раз!")
        y1 = input("Введите значение для y1: ")

while type(x2) != int:
    try:
        x2 = int(x2)
    except ValueError:
        print("Вы ввели неккоректные данные, пожалуйста, введите значение для x2 еще раз!")
        x2 = input("Введите значение для x2: ")

while type(y2) != int:
    try:
        y2 = int(y2)
    except ValueError:
        print("Вы ввели неккоректные данные, пожалуйста, введите значение для y2 еще раз!")
        y2 = input("Введите значение для y2: ")


if (x1 <= x <= x2) and (y2 <= y <= y1):
    print(f"Точка с координатами ({x}, {y}) лежит внутри прямоугольника.")
else:
    print(f"Точка с координатами ({x}, {y}) не лежит внутри прямоугольника.")
