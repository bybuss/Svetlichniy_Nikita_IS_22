"""
В матрице элементы последнего столбца заменить на -1.
"""

import random

N = int(input("Введите N размерность матрицы: "))

matrix = [[random.randint(0, 1) for el in range(N)]for row in range(N)]

print("Матрица:")
[print(i) for i in matrix]

print("Замененная матрица:")
[print(i) for i in [row[:-1] + [-1] for row in matrix]]
