n = int(input("Введите значение для n: "))

multiplication = 1

for i in range(n):
    multiplication += 0.1
    multiplication *= multiplication

print(f"Произведение N сомножителей = {multiplication}")