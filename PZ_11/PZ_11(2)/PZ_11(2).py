"""
Из предложенного текстового файла (text18-29.txt) вывести на экран его содержимое,
количество символов в тексте. Сформировать новый файл, в который поместить текст в
стихотворной форме предварительно поставив последнюю строку между второй и третьей.
"""
filename = "text18-19"

with open(f"{filename}.txt", encoding="utf-16") as file:
    data = [i.split("\n")[0] for i in file.readlines()]

print(f"**Содержимое файла:**\n{"\n".join([text for text in data])}")
print(f"**Количество символов в тексте: {sum([len(i) for i in data])}**")

with open(f"processed_{filename}.txt", "w", encoding="utf-16") as file:
    file.writelines([
        "\n".join(data[:2]) + "\n",
        "".join(data[6]) + "\n",
        "\n".join(data[2:6])
    ])

