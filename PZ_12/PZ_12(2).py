"""
Составить генератор (yield), который преобразует все буквенные символы
в строчные.
"""

import string

symbols = str(input("Введите буквенные символы: "))


def to_lower(_str: string) -> list:
    yield [char.lower() for char in _str]


[print(F'Ответ: {"".join(i)}') for i in to_lower(symbols)]
