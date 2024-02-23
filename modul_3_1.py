# 1. імпорт модуля datetime
from datetime import datetime


def get_days_from_today(date):
    try:  # 2. Перетворення рядка дати у форматі 'РРРР-ММ-ДД' у об'єкт datetime
        date_object = datetime.strptime(date, '%Y-%m-%d')

        # 3.Отримання поточної дати
        current_date = datetime.today()

        # 4. Розрахунок різниці між поточною датою та заданою датою
        date_difference = date_object - current_date

        # 5. Повернення різниці у днях як ціле число.
        return date_difference.days

    except ValueError:
        return "Неправильний формат дати"


date_string = '2021-10-09'
print(get_days_from_today(date_string))
