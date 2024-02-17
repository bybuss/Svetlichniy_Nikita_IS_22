"""
Организовать и вывести последовательность на N произвольных целых
элементов, сформировать новую последовательность куда поместить положительные
четные элементы, найти их сумму и среднее арифметическое.
"""

from random import randint

N = int(input("Введите число N: "))

rnd_list = [randint(-10, 10) for i in range(N)]
print(f"Производные числа: {rnd_list}")

positive_list = [i for i in rnd_list if i > 0 and i % 2 == 0]
print(f"Положительные и четные элементы: {positive_list}")

print(f"Сумма: {sum(positive_list)}")
try:
    print(f"Среднее арифметическое: {sum(positive_list) / len(positive_list)}")
except ZeroDivisionError:
    print(f"Из {N} произвольных чисел не были найдены положительные и четные элементы")

