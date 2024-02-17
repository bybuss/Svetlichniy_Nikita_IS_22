"""
В матрице элементы третьей строки заменить элементами из одномерного
динамического массива соответствующей размерности.
"""

import random

N = int(input("Введите N размерность матрицы: "))

matrix = [[random.randint(0, 1) for el in range(N)]for row in range(N)]
lst = list(range(N))

print("Матрица:")
[print(i) for i in matrix]

print("Замененная матрица:")
matrix = [[random.randint(5, 10) for _ in range(len(matrix[2]))] if i == 2 else row for i, row in enumerate(matrix)]
[print(i) for i in matrix]
