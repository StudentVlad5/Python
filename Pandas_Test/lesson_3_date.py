# import datetime
# now = datetime.datetime.now()
# print(now)

from datetime import datetime

current_datetime = datetime.now()

print(current_datetime.year)
print(current_datetime.month)
print(current_datetime.day)
print(current_datetime.hour)
print(current_datetime.minute)
print(current_datetime.second)
print(current_datetime.microsecond)
print(current_datetime.tzinfo)
# В об'єкта datetime є методи, щоб отримати дату (без часу) та час (без дати):

current_datetime = datetime.now()
print(current_datetime.date())
print(current_datetime.time())

import datetime

# Створення об'єктів date і time
date_part = datetime.date(2023, 12, 14)
time_part = datetime.time(12, 30, 15)

# Комбінування дати і часу в один об'єкт datetime
combined_datetime = datetime.datetime.combine(date_part, time_part)

print(combined_datetime)  # Виведе "2023-12-14 12:30:15"
# Отримання номера дня тижня
day_of_week = combined_datetime.weekday()

# Створення двох об'єктів datetime
datetime1 = datetime.datetime(2023, 3, 14, 12, 0)
datetime2 = datetime.datetime(2023, 3, 15, 12, 0)

# Порівняння дат
print(datetime1 == datetime2)  # False, тому що дати не однакові
print(datetime1 != datetime2)  # True, тому що дати різні
print(datetime1 < datetime2)   # True, тому що datetime1 передує datetime2
print(datetime1 > datetime2)   # False, тому що datetime1 не наступає за datetime2

# У модулі datetime є клас timedelta, який використовується для представлення різниці між двома моментами в часі. Об'єкти timedelta можуть представляти дні, години, хвилини, секунди та мікросекунди. Вони корисні для розрахунків, що включають додавання або віднімання часу від конкретних дат або порівняння часових інтервалів.

from datetime import timedelta
delta = timedelta(
    days=50,
    seconds=27,
    microseconds=10,
    milliseconds=29000,
    minutes=5,
    hours=8,
    weeks=2
)
print(delta)
# 64 days, 8:05:56.000010

from datetime import datetime

seventh_day_2019 = datetime(year=2019, month=1, day=7, hour=14)
seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)

difference = seventh_day_2020 - seventh_day_2019
print(difference)  # 365 days, 0:00:00
print(difference.total_seconds())  # 31536000.0

from datetime import datetime, timedelta

now = datetime.now()
future_date = now + timedelta(days=10)  # Додаємо 10 днів до поточної дати
print(future_date)
# 2023-12-28 14:08:46.342976

# Але якщо потрібно робити обчислення або порівняння, засновані на послідовності дат, наприклад, для визначення кількості днів між двома датами.

# Ми можемо використати метод toordinal(), який повертає порядковий номер дня, враховуючи кількість днів з 1 січня року 1 нашої ери (тобто з початку християнського календаря). Цей метод перетворює об'єкт datetime в ціле число, що представляє порядковий номер даного дня.

# Отримання порядкового номера
ordinal_number = future_date.toordinal()
print(f"Порядковий номер дати {future_date} становить {ordinal_number}")

from datetime import datetime

# Встановлення дати спалення Москви Наполеоном (14 вересня 1812 року)
napoleon_burns_moscow = datetime(year=1812, month=9, day=14)

# Поточна дата
current_date = datetime.now()

# Розрахунок кількості днів
days_since = current_date.toordinal() - napoleon_burns_moscow.toordinal()
print(days_since)

from datetime import datetime

# Поточний час
now = datetime.now()

# Конвертація datetime в timestamp
timestamp = datetime.timestamp(now)
print(timestamp)  # Виведе timestamp поточного часу

# 1702854066.56633

from datetime import datetime

# Припустимо, є timestamp
timestamp = 1617183600

# Конвертація timestamp назад у datetime
dt_object = datetime.fromtimestamp(timestamp)
print(dt_object)  # Виведе відповідний datetime

# Синтаксис методу strftime виглядає наступним чином:
# datetime_object.strftime(format)
# Де datetime_object - це об'єкт datetime, а format - рядок формату, який визначає, як дата та час повинні бути представлені.

# Кожен код у рядку формату починається з символу % і представляє певний компонент дати або часу. Ось деякі з найбільш використовуваних кодів:

# %Y - рік з чотирма цифрами (наприклад, 2023).
# %y - рік з двома цифрами (наприклад, 23).
# %m - місяць як номер (наприклад, 03 для березня).
# %d - день місяця як номер (наприклад, 14).
# %H - година (24-годинний формат) (наприклад, 15).
# %I - година (12-годинний формат) (наприклад, 03).
# %M - хвилини (наприклад, 05).
# %S - секунди (наприклад, 09).
# %A - повна назва дня тижня (наприклад, Tuesday).
# %a - скорочена назва дня тижня (наприклад, Tue).
# %B - повна назва місяця (наприклад, March).
# %b або %h - скорочена назва місяця (наприклад, Mar).
# %p - AM або PM для 12-годинного формату.

# Форматування дати і часу
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date) 

# Форматування лише дати
formatted_date_only = now.strftime("%A, %d %B %Y")
print(formatted_date_only)

# Форматування лише часу
formatted_time_only = now.strftime("%I:%M %p")
print(formatted_time_only)  

# Форматування лише дати
formatted_date_only = now.strftime("%d.%m.%Y")
print(formatted_date_only)

# Метод strptime в Python використовується для перетворення рядків у об'єкти datetime. Цей метод є протилежністю до strftime, який перетворює об'єкти datetime у рядки. strptime дозволяє аналізувати рядки, що містять дату та/або час, і перетворювати їх на структуровані об'єкти datetime за допомогою визначеного формату.

# datetime_object = datetime.strptime(string, format)

date_string = "2023.03.14"
datetime_object = datetime.strptime(date_string, "%Y.%m.%d")
print(datetime_object)  # Виведе об'єкт datetime, що відповідає вказаній даті та часу

from datetime import datetime

# Поточна дата та час
now = datetime.now()
# Конвертація у формат ISO 8601
iso_format = now.isoformat()
print(iso_format)
# 2023-12-14T15:43:42.651309
# Для зворотного перетворення рядка у форматі ISO 8601 на об'єкт datetime, можна використати метод fromisoformat():
iso_date_string = "2023-03-14T12:39:29.992996"

# Конвертація з ISO формату
date_from_iso = datetime.fromisoformat(iso_date_string)
print(date_from_iso)

# Метод isoweekday() у об'єкті datetime використовується для отримання дня тижня відповідно до ISO 8601. Згідно з цим стандартом, тиждень починається з понеділка, який має значення 1, і закінчується неділею, яка має значення 7.

from datetime import datetime

# Створення об'єкта datetime
now = datetime.now()

# Використання isoweekday() для отримання дня тижня
day_of_week = now.isoweekday()

print(f"Сьогодні: {day_of_week}")  # Поверне число від 1 до 7, що відповідає дню тижня

# Також розглянемо корисний метод isocalendar(), який використовується для отримання кортежу, що містить ISO рік, номер тижня в році та номер дня тижня відповідно до ISO 8601.
# Вивід isocalendar() - це кортеж (ISO_рік, ISO_тиждень, ISO_день_тижня), де:
# ISO_рік - це рік у форматі ISO.
# ISO_тиждень - номер тижня в році за ISO 8601 (від 1 до 53).
# ISO_день_тижня - день тижня за ISO 8601, де 1 означає понеділок, а 7 - неділю.

from datetime import datetime

# Створення об'єкта datetime
now = datetime.now()

# Отримання ISO календаря
iso_calendar = now.isocalendar()
print("iso_calendar", iso_calendar)
print(f"ISO рік: {iso_calendar[0]}, ISO тиждень: {iso_calendar[1]}, ISO день тижня: {iso_calendar[2]}")

# ISO рік: 2023, ISO тиждень: 50, ISO день тижня: 4

# Ключові аспекти: методи для роботи з ISO форматом дати

# Метод isoformat() використовується для конвертації об'єкта datetime в рядок у форматі ISO 8601.
# Метод fromisoformat() використовується для конвертації рядка у форматі ISO 8601 в об'єкт datetime.
# Метод isoweekday() використовується для отримання дня тижня відповідно до ISO 8601.
# Метод isocalendar() використовується для отримання кортежу, що містить ISO рік, номер тижня в році та номер дня тижня відповідно до ISO 8601.

# Щоб вивести дату у форматі UTC це можна зробити, додавши інформацію про часову зону до об'єкта datetime:
from datetime import datetime, timezone
local_now = datetime.now()
utc_now = datetime.now(timezone.utc)

print(local_now)
print(utc_now)  # Виведе поточний час в UTC
# Створення часової зони для Східного часового поясу (UTC-5)
utc_time = datetime.now(timezone.utc)
eastern_time = utc_time.astimezone(timezone(timedelta(hours=-5)))
# Перетворює час UTC в час Східного часового поясу
print(eastern_time)  

# Припустимо, місцевий час належить до часової зони UTC+2
local_timezone = timezone(timedelta(hours=2))
local_time = datetime(year=2023, month=3, day=14, hour=12, minute=30, second=0, tzinfo=local_timezone)

# Конвертація локального часу в UTC
utc_time = local_time.astimezone(timezone.utc)
print(utc_time)  # Виведе час в UTC
# 2023-03-14 10:30:00+00:00

# Робота з часом
# Метод time.time() повертає поточний час у секундах з 1 січня 1970 року (epoch time).

import time

current_time = time.time()
print(f"Поточний час: {current_time}")
# Поточний час: 1702857932.326853
# Метод time.sleep(seconds) зупиняє виконання програми на вказану кількість секунд. Наприклад цей код зупиняє виконання програми на 5 секунд.
print("Початок паузи")
time.sleep(5)
print("Кінець паузи")
# Метод time.ctime([seconds]) перетворює часову мітку (кількість секунд) у зрозуміле для людини текстове представлення. Якщо аргумент не вказаний, використовується поточний час.
import time

current_time = time.time()
print(f"Поточний час: {current_time}")
# Поточний час: 170285823.9412928
readable_time = time.ctime(current_time)
print(f"Читабельний час: {readable_time}")
# Читабельний час: Mon Dec 18 02:08:43 2023

# Метод time.localtime([seconds]) перетворює часову мітку в структуру struct_time у місцевій часовій зоні.
local_time = time.localtime(current_time)
print(f"Місцевий час: {local_time}")
# Місцевий час: time.struct_time(tm_year=2023, tm_mon=12, tm_mday=18, tm_hour=2, tm_min=57, tm_sec=50, tm_wday=0, tm_yday=352, tm_isdst=0)

# Об'єкт time.struct_time в Python є іменованим кортежем, який використовується для представлення часу. Кожен елемент кортежу має особливе значення, що представляє певний компонент дати та часу:
# tm_year - рік
# tm_mon - місяць від 1 до 12
# tm_mday - день місяця від 1 до 31
# tm_hour - години від 0 до 23
# tm_min - хвилини від 0 до 59
# tm_sec - секунди від 0 до 59
# tm_wday - день тижня від 0 до 6
# tm_yday - день року від 1 до 366
# tm_isdst - прапорець літнього часу. 0 означає, що літній час не діє, -1 - інформація відсутня, 1 - літній час діє

# Метод time.gmtime([seconds]) схожий на localtime, але повертає struct_time у UTC.
# Досить важливим є метод time.perf_counter(), який надає доступ до лічильника з високою точністю, та є ідеальним для вимірювання коротких інтервалів часу.
import time

# Записуємо час на початку виконання
start_time = time.perf_counter()

# Виконуємо якусь операцію
for _ in range(1_000_000):
    pass  # Просто проходить цикл мільйон разів

# Записуємо час після виконання операції
end_time = time.perf_counter()

# Розраховуємо та виводимо час виконання
execution_time = end_time - start_time
print(f"Час виконання: {execution_time} секунд")

# представлення чисел з підкресленнями _ є способом зробити великі числа більш читабельними.
# оператор pass, який використовується як заповнювач або "пуста" інструкція. Він не робить нічого і використовується там, де синтаксис вимагає наявності хоча б однієї інструкції, але вам не потрібно виконувати жодних дій.

# time.time(): Повертає поточний час у секундах з 1 січня 1970 року (epoch time).
# time.sleep(seconds): Зупиняє виконання програми на вказану кількість секунд.
# time.ctime([seconds]): Перетворює часову мітку в текстове представлення, зрозуміле для людини.
# time.localtime([seconds]): Перетворює часову мітку в структуру struct_time у місцевій часовій зоні.
# time.gmtime([seconds]): Аналогічно localtime, але повертає struct_time у форматі UTC.
# time.perf_counter(): Повертає лічильник з високою точністю для вимірювання коротких інтервалів часу.