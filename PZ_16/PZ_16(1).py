"""
Создайте класс «Календарь», который имеет атрибуты год, месяц и день. Добавьте
методы для определения дня недели, проверки на високосный год и определения
количества дней в месяце.
"""

import datetime
import calendar


class Calendar:
    def __init__(self, day: int, month: int, year: int) -> None:
        self.year = year
        self.month = month
        self.day = day
        try:
            self.date = datetime.datetime(self.year, self.month, self.day)
        except ValueError:
            print("day is out of range for month\n")

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
            return "Неверный формат даты"

    def is_leap_year(self) -> str:
        return "Високосный" if self.year % 4 == 0 else "Не високосный"

    def days_in_month(self) -> int:
        return calendar.monthrange(self.year, self.month)[1]


date = Calendar(27, 2, 2024)
print(
    f"День недели: {date.day_of_week()}\n"
    f"Год: {date.is_leap_year()}\n"
    f"Количество дней в месяце: {date.days_in_month()}"
)
