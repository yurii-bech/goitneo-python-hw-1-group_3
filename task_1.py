from datetime import datetime, timedelta
from collections import defaultdict

def get_birthdays_per_week(users):
    birthdays_by_day = defaultdict(list)

    today = datetime.today().date()

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days

        if delta_days < 0:
            continue

        day_of_week = (today + timedelta(days=delta_days)).strftime("%A")

        if day_of_week in ["Saturday", "Sunday"]:
            delta_days += 1
            day_of_week = "Monday"

        if 0 <= delta_days < 7:
            birthdays_by_day[day_of_week].append(name)

    for day, names in birthdays_by_day.items():
        print(f"{day}: {', '.join(names)}")

# Просто кілька прикладів:
users = [
    {"name": "Alice", "birthday": datetime(2023, 12, 3)},
    {"name": "Bob", "birthday": datetime(2023, 12, 4)},
    {"name": "Charlie", "birthday": datetime(2023, 12, 6)},
]

get_birthdays_per_week(users)