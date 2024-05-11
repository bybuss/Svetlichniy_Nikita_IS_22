"""
Создайте класс «Календарь», который имеет атрибуты год, месяц и день. Добавьте
методы для определения дня недели, проверки на високосный год и определения
количества дней в месяце.
"""

import datetime
import calendar
import pickle


class Calendar:
    def __init__(self, day: int, month: int, year: int):
        self.year = year
        self.month = month
        self.day = day
        try:
            self.date = datetime.datetime(self.year, self.month, self.day)
        except ValueError:
            print("Нет такого дня в этом месяце\n")

    def day_of_week(self) -> str:
        days_of_week = {
            1: "Понедельник",
            2: "Вторник",
            3: "Среда",
            4: "Четверг",
            5: "Пятница",
            6: "Суббота",
            7: "Воскресенье",
        }
        try:
            return days_of_week[self.date.isoweekday()]
        except AttributeError:
            return "Нет такого дня в этом месяце"

    def is_leap_year(self) -> str:
        return "Високосный" if self.year % 4 == 0 else "Не високосный"

    def days_in_month(self) -> int:
        return calendar.monthrange(self.year, self.month)[1]


def save_def(calendars: list[Calendar]) -> None:
    with open("calendar.pickle", "wb") as file:
        pickle.dump(calendars, file)


def load_def() -> list[Calendar]:
    with open("calendar.pickle", "rb") as file:
        return pickle.load(file)


date1 = Calendar(29, 2, 2024)
date2 = Calendar(11, 5, 2011)
date3 = Calendar(24, 12, 2023)
save_def([date1, date2, date3])

list_data = load_def()
for date in list_data:
    print(
        f"{'='*60}\n"
        f"День недели: {date.day_of_week()}\n"
        f"Год: {date.is_leap_year()}\n"
        f"Количество дней в месяце: {date.days_in_month()}\n"
        f"{'=' * 60}\n"
    )
