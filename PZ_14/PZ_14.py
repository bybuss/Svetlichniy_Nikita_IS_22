"""
В исходном текстовом файле(hotline1.txt) найти все номера телефонов, соответствующих шаблону 8(000)000-00-00.
Посчитать количество полученных элементов. После фразы «Горячая линия» добавить фразу «Министерства образования
Ростовской области», выполнив манипуляции в новом файле.
"""

import re

with open("hotline1.txt", encoding="utf-8") as f:
    data = f.read()

pattern = re.compile(r"8\([\d]{3}\)[\d]{3}-[\d]{2}-[\d]{2}")
numbers = pattern.findall(data)

with open("answer.txt", "w", encoding="utf-8") as file:
    file.writelines([
        re.sub("Горячая линия", "Горячая линия Министерства образования Ростовской области", data),
        f"Номера телефонов, соответствующих шаблону: {" | ".join(numbers)}\n",
        f"Количество полученных элементов: {len(numbers)}"
    ])
