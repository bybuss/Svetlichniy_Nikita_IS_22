# Выполнить обратную сортировку словаря d = {'a': 1, 'b': 2, 'c': 3}

# Сделал еще для 26 варианта, тк сначала задание было отсортировать словарь, но он
# уже был отсортирован и потом Вы сказали, чтобы я сделал обратную сортировку

d = {'a': 1, 'b': 2, 'c': 3}

reversedDict = {key: value for key, value in reversed(d.items())}
print(reversedDict)
