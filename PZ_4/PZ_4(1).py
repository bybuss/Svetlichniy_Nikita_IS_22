# Дано целое число N (>0). Найти произведение 1.1 • 1.2 • 1.3 •... (N сомножителей).
from decimal import Decimal

n = int(input("Введите значение для n: "))

multiplication = 1

for i in range(n + 1):
    multiplication *= Decimal("1") + Decimal(i) / Decimal("10")

print(f"Произведение N сомножителей = {multiplication}")
