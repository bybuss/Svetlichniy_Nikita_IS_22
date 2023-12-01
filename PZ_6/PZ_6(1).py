# Дан список A размера N и целое число K (1 < K < N). Преобразовать список,
# увеличив каждый его элемент на исходное значение элемента A[K].

N = input("Введите значения для N: ")
K = input("Введите значения для K: ")

while type(N) != int:
    try:
        N = int(N)
    except ValueError:
        print("\nВведите целый тип данных для N")
        N = input("Введите значение для N: ")

while type(K) != int:
    try:
        K = int(K)
    except ValueError:
        print("\nВведите целый тип данных для K")
        K = input("Введите значение для K: ")

while 1 >= K or K > N:
    print("(1 < K < N)")
    K = int(input("Введите значения для K: "))


A = list(range(N))

print(f"До:    {A}")

for i in A:
    A[i] += K

print(f"После: {A}")
