from datetime import datetime, timedelta


def get_upcoming_birthdays(users):

    today = datetime.today().date()  # отримання поточної дати
    upcoming_birthdays = []  # 4. Створюємо порожній список, куди будемо додавати інформацію про користувачів, яких потрібно привітати:

    for user in users:
        birthday = datetime.strptime(user["birthday"],
                                     "%Y.%m.%d").date()  # Перетворюємо рядкову дату народження в об'єкт datetime та отримуємо лише дату:
        birthday_this_year = birthday.replace(year=today.year)  # визнач день народж в поточн році

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(
                year=today.year + 1)  # переносим на наступний рік якщо ДР минув

        days_until_birthday = (birthday_this_year - today).days  # Обчислюємо кількість днів до дня народження:

        if days_until_birthday <= 7:
            if birthday_this_year.weekday() >= 5:  # Якщо день народження випадає на вихідний, переносимо його на наступний понеділок:
                days_until_birthday += (7 - birthday_this_year.weekday())
            congratulation_date = today + timedelta(
                days=days_until_birthday)  # Обчислюємо нову дату привітання та додаємо інформацію про користувача до списку upcoming_birthdays:
            upcoming_birthdays.append(
                {"name": user["name"], "congratulation_date": congratulation_date.strftime("%Y.%m.%d")})

    return upcoming_birthdays  # Повертаємо список привітань на цьому тижні:
# Приклад використання
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "James Bond", "birthday": "1990.02.25"}
]

upcoming_birthdays = get_upcoming_birthdays(users)

# Виведення списку привітань на цьому тижні
print("Список привітань на цьому тижні:")
for birthday_info in upcoming_birthdays:
    print(f"Ім'я: {birthday_info['name']}, Дата привітання: {birthday_info['congratulation_date']}")
