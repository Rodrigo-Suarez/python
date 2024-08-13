### DATES ###

#AGRUPA FECHAS Y HORARIOS
from datetime import datetime

def date_now(date): 
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.microsecond)
    print(date.timestamp())

date = datetime.now()
date_now(date)

year = datetime(2022, 8, 29)
print(year)


#HORARIOS
from datetime import time

today = time(16, 30, 40)
print(today)
print(today.hour)
print(today.minute)
print(today.second)


#FECHAS
from datetime import date

fecha = date.today()
print(fecha)

fecha = date(2023, 5, 1)
print(fecha)
print(fecha.year)
print(fecha.month)
print(fecha.day)


#OPERAR CON DATES
year = date(2024, 8, 3)
year_two = date(year.year + 1, year.month + 1, year.day + 1)

print(year_two)


#OPERACIONES CON FECHAS
from datetime import timedelta

fecha_1 = timedelta(days= 10, hours=8, minutes= 50)
fecha_2 = timedelta(days= 8, hours=1, minutes= 40)

print(fecha_1 + fecha_2)
print(fecha_1 - fecha_2)

