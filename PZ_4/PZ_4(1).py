# Дано целое число N (>0). Найти произведение 1.1 • 1.2 • 1.3 •... (N сомножителей).
from decimal import Decimal

n = input("Введите значение для n: ")

while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        print("Введите целый тип данных для n")
        n = int(input("Введите значение для n: "))

while n < 0:
    print("Введите положительный n")
    n = input("Введите значение для n: ")

multiplication = 1

for i in range(n + 1):
    multiplication *= Decimal("1") + Decimal(i) / Decimal("10")

print(f"Произведение N сомножителей = {multiplication}")
