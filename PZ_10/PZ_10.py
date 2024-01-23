"""
Книжные магазины предлагают следующие коллекции книг.
Магистр – Лермонтов, Достоевский, Пушкин, Тютчев
ДомКниги – Толстой, Грибоедов, Чехов, Пушкин.
БукМаркет – Пушкин, Достоевский, Маяковский.
Галерея – Чехов, Тютчев, Пушкин.
Определить в каких магазинах
нельзя приобрести книги Грибоедова и Маяковского
"""

magistr = {'Лермонтов', 'Достоевский', 'Пушкин', 'Тютчев'}
domknigi = {'Толстой', 'Грибоедов', 'Чехов', 'Пушкин'}
bukmarket = {'Пушкин', 'Достоевский', 'Маяковский'}
galereya = {'Чехов', 'Тютчев', 'Пушкин'}

authors_to_check = {'Грибоедов', 'Маяковский'}

magistr_without = magistr - authors_to_check
domknigi_without = domknigi - authors_to_check
bukmarket_without = bukmarket - authors_to_check
galereya_without = galereya - authors_to_check

stores_without = {
    'Магистр': magistr_without == magistr,
    'ДомКниги': domknigi_without == domknigi,
    'БукМаркет': bukmarket_without == bukmarket,
    'Галерея': galereya_without == galereya
}

for store, has_no_authors in stores_without.items():
    if has_no_authors:
        print(f"В магазине {store} нельзя приобрести книги Грибоедова и Маяковского.")
