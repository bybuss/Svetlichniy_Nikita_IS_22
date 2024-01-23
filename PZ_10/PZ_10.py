"""
Книжные магазины предлагают следующие коллекции книг.
    "Магистр": {"Лермонтов", "Достоевский", "Пушкин", "Тютчев"},
    "ДомКниги": {"Толстой", "Грибоедов", "Чехов", "Пушкин"},
    "БукМаркет": {"Пушкин", "Достоевский", "Маяковский"},
    "Галерея": {"Чехов", "Тютчев", "Пушкин"}
Определить в каких магазинах нельзя приобрести книги Грибоедова и Маяковского
"""

stores = {
    "Магистр": {"Лермонтов", "Достоевский", "Пушкин", "Тютчев"},
    "ДомКниги": {"Толстой", "Грибоедов", "Чехов", "Пушкин"},
    "БукМаркет": {"Пушкин", "Достоевский", "Маяковский"},
    "Галерея": {"Чехов", "Тютчев", "Пушкин"}
}

stores_without = [
    store for store, books in stores.items() if "Грибоедов" not in books and "Маяковский" not in books
]

print("Нельзя приобрести книги Грибоедова и Маяковского:", stores_without)
