# Дана строка, содержащая минимум 1 пробел. Вывести подстроку, расположенную между 1-м и 2-м пробелом исходной строки.
# Если строка содержит только 1 пробел, то вывести пустую строку.

S = str(input("Введите значение для строки S: "))


if len(S.split(" ")) >= 3:
    print("".join(S.split(" ")[1:2]))
else:
    print("Пустая строка: < >")