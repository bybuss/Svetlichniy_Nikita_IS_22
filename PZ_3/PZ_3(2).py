#Дописать условие задачи


A, B, C = input("Введите значение для точки А: "), input("Введите значение для точки В: "), input("Введите значение для точки С: ")

while type(A) == str:
 try:
    A = float(A)
 except ValueError:
    print("\nНеправильно ввели тип данных для А!")
    A = input("Введите значение для точки А: ")

while type(B) == str:
 try:
    B = float(B)
 except ValueError:
    print("\nНеправильно ввели тип данных для В!")
    B = input("Введите значение для точки В: ")

while type(C) == str:
 try:
    C = float(C)
 except ValueError:
    print("\nНеправильно ввели тип данных для С!")
    C = input("Введите значение для точки С: ")

distance_B = B - A
distance_C = C - A

if distance_B < 0:
    distance_B *= -1
if distance_C < 0:
    distance_C *= -1

if distance_C < distance_B:
    print(f"\nТочка С ближе к точке А, чем точка В.\nТочка С: {C} -> pасстояние до точки А: {distance_C}")
elif distance_B < distance_C:
    print(f"\nТочка B ближе к точке А, чем точка C.\nТочка B: {B} -> pасстояние до точки А: {distance_B}")
else:
    print(f"\nУ точек В и С одинаковое расстояние до точки А.\nТочка B: {B} -> pасстояние до точки А: {distance_B}\nТочкB С: {C} -> pасстояние до точки А: {distance_C}")