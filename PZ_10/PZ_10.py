'''
Книжные магазины предлагают следующие коллекции книг.
    "Магистр": ["Лермонтов", "Достоевский", "Пушкин", "Тютчев"]
    "ДомКниги": ["Толстой", "Грибоедов", "Чехов", "Пушкин"]
    "БукМаркет": ["Пушкин", "Достоевский", "Маяковский"]
    "Галерея": ["Чехов", "Тютчев", "Пушкин"]
Определить в каких магазинах нельзя приобрести книги Грибоедова и Маяковского
'''

import json

store = {
    "Магистр": ["Лермонтов", "Достоевский", "Пушкин", "Тютчев"],
    "ДомКниги": ["Толстой", "Грибоедов", "Чехов", "Пушкин"],
    "БукМаркет": ["Пушкин", "Достоевский", "Маяковский"],
    "Галерея": ["Чехов", "Тютчев", "Пушкин"]
}

griboedov, mayakovskiy = {}, {}

for store_name, writers in store.items():
    griboedov[store_name] = "Нельзя❌" if "Грибоедов" not in writers else "Можно✔️"
    mayakovskiy[store_name] = "Нельзя❌" if "Маяковский" not in writers else "Можно✔️"

sorted_store = {store_name[0]: {
        "Грибоедов": griboedov[store_name[0]],
        "Маяковский": mayakovskiy[store_name[0]]
    } for store_name in store.items()
}

print(sorted_store) # тут ужасно неудобный вывод для просмотра

# добавляю в json`чик, чтобы удобнее было просматривать
with open("sorted_store.json", "w", encoding='utf-8') as file:
    json.dump(sorted_store, file, ensure_ascii=False, indent=4)
