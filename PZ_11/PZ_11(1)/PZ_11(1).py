"""
Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной последовательности из
целых положительных и отрицательных чисел. Сформировать новый текстовый файл (.txt) следующего вида,
предварительно выполнив требуемую обработку элементов:
1) Элементы первого и второго файлов
2) Количество элементов первого и второго файлов
3) Количество элементов, общих для двух файлов
4) Количество четных элементов первого файла
4) Количество нечетных элементов второго файла
"""
import random


def subsequence(sign: int = random.choice([1, -1])) -> list:
    """Создаю рандомную последовательность"""
    return [random.randint(1, 1000) * sign for i in range(random.randint(175, 200))]


def ints_file(_subsequence: list, name: str) -> None:
    """Записываю последовательности в файлы"""
    with open(f"{name}_subsequence.txt", "w") as file:
        file.write(" ".join(map(str, _subsequence)))


def get_data_from_file(name: str) -> list:
    with open(f"{name}_subsequence.txt") as file:
        data_file = [int(i) for i in file.read().split(" ")]
        return data_file


ints_file(subsequence(1), "positive")
ints_file(subsequence(-1), "negative")

"""Обрабатываю файлы, как по условию"""
positive_data = get_data_from_file("positive")
negative_data = get_data_from_file("negative")

# Определяю кол-во схожих элементов в 2-х файлах
identical_items, identical_items_without_sign = [], []
for i in positive_data:
    for j in negative_data:
        print(f"{i}: {j}")
        # Если учитывать минус
        if j == i:
            identical_items.append(j)
        # Если не учитывать минус
        elif j * -1 == i:
            identical_items_without_sign.append(j)

with open("report.txt", "w", encoding="utf-8") as file:
    file.writelines([
            f"Элементы первого файла: {" ".join(map(str, positive_data))}\n",
            f"Элементы второго файла: {" ".join(map(str, negative_data))}\n",

            f"Количество элементов первого файла: {len(positive_data)}\n",
            f"Количество элементов второго файла: {len(negative_data)}\n",

            f"Количество элементов, общих для двух файлов: {len(identical_items)}\n"
            f"                  Если минус не учитывается: {len(identical_items_without_sign)}\n",

            f"Количество четных элементов первого файла: {
                len([i for i in positive_data if i % 2 == 0])
            }\n",
            f"Количество нечетных элементов второго файла: {
                len([i for i in positive_data if i % 2 != 0])
            }\n"
        ]
    )
