import datetime
from dateutil.relativedelta import relativedelta
from datetime import datetime
from art import *

Day = int(input("Введите свой день рождения: "))
mecyac = int(input("Введите свой месяц рождения: "))
year = int(input("Введите свой год рождения: "))

date_of_birth = datetime(year, mecyac, Day)

print(f"День недели рождения: {date_of_birth.strftime('%A')}")

def kos_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False

if kos_year(year):
    print(f"{year} год является високосным.")
else:
    print(f"{year} год не является високосным.")

let = relativedelta(datetime.now(), date_of_birth).years
print(f'Вам {let} лет.')

def display_date_as_stars(Day, mecyac, year):
    day_str = f"{Day:02d}"
    month_str = f"{mecyac:02d}"
    year_str = f"{year:04d}"
    date_str = f"{day_str} {month_str} {year_str}"
    print(text2art(date_str))

display_date_as_stars(Day, mecyac, year)