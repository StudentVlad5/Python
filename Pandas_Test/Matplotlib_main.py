import matplotlib.pyplot as plt
import pandas as pd

date = pd.date_range(start='2021-09-01', freq='D', periods=8)
plt.plot(date, [23, 17, 17, 16, 15, 14, 17, 20])

# xlabel (або ylabel) — рядок тексту підпису.
# А також параметри конструктора класу matplotlib.text.Text:

# fontsize або size — розмір шрифту, число або значення зі списку xx-small, x-small, small, medium, large, x-large, xx-large
# fontstyle — стиль шрифту значення зі списку normal, italic, oblique
# fontweight — товщина шрифту може визначатися або числом в діапазоні від 0 до 1000, або значенням зі списку ultralight, light, normal, regular, book, medium, roman, semibold, demibold, demi, bold, heavy, extra bold, black
# color — значення кольору для тексту підпису. Можливості вибору кольору занадто великі і подивитися варіанти можна за цим посиланням (https://matplotlib.org/stable/gallery/color/named_colors.html), де вони теж наведені не повністю.
plt.xlabel('Дата', fontsize='small', color='midnightblue')
plt.ylabel('Температура', fontsize='small', color='midnightblue')
# Назву графіка можна задати методом title
plt.title('Денна погода у м. Полтава', fontsize=15)
plt.text(date[0], 15, 'Осінь досить тепла', color="blue")
# І додати легенду можна, викликавши метод legend, не забувши додати параметр label у метод plot. І остаточний результат буде наступним.
plt.show()

date = pd.date_range(start='2021-09-01', freq='D', periods=8)
plt.figure(figsize=(10, 4))# Збільшення ширини графіка до 10 дюймів
plt.plot(date, [23, 17, 17, 16, 15, 14, 17, 20], label='середньоденна температура')
plt.xlabel('Дата', fontsize='small', color='midnightblue')
plt.ylabel('Температура', fontsize='small', color='midnightblue')
plt.title('Температура в м. Полтава', fontsize=15)
plt.text(date[0], 15, 'Осінь досить тепла', color="blue")
plt.legend()
plt.show()

# Якщо ми хочемо розмістити два графіки, хорошим способом буде використовувати метод subplots. Функція subplots повертає два об'єкти, перший - це Figure, підкладка, на якій будуть розміщені поля з графіками, другий - об'єкт (або масив об'єктів) Axes, через який можна отримати повний доступ до налаштування зовнішнього вигляду елементів, що відображаються.

import matplotlib.pyplot as plt
import pandas as pd

date = pd.date_range(start='2021-09-01', freq='D', periods=8)
fig, axs = plt.subplots(figsize=(10, 4))
axs.plot(date, [23, 17, 17, 16, 15, 14, 17, 20], label='day temperature')
axs.plot(date, [19, 11, 16, 11, 10, 10, 11, 16], label='night temperature')
plt.xlabel('Дата', fontsize='small', color='midnightblue')
plt.ylabel('Температура', fontsize='small', color='midnightblue')
plt.title('Температура в м. Полтава', fontsize=15)
plt.text(date[0], 15, 'Осінь досить тепла', color="blue")
plt.legend()
plt.show()

# Якщо ми хочемо розділити графіки на частини, то у функцію subplots ми повинні передати кількість рядків та стовпців. 
import matplotlib.pyplot as plt
import pandas as pd

date = pd.date_range(start='2021-09-01', freq='D', periods=8)
fig, axs = plt.subplots(2, 1, figsize=(10, 6))

axs[0].plot(date, [23, 17, 17, 16, 15, 14, 17, 20], label='day temperature')
axs[1].plot(date, [19, 11, 16, 11, 10, 10, 11, 16], label='night temperature')

axs[0].set_title('Денна', fontsize=10)
axs[1].set_title('Нічна', fontsize=10)

fig.suptitle('Температура в м. Полтава', fontsize=15)

plt.show()
# Мнемонічне значення	Текстове значення	Опис
# -	solid	Безперервна лінія
# --	dashed	 Штрихова лінія
# -. 	dashdot	Штрихпунктирна лінія
# : 	dotted	Пунктирна лінія
# None	пробіл або порожній рядок	Не відображати лінію

# Колір лінії графіка задається через параметр color (c — скорочений варіант). Варіантів встановлення формату, як уже говорилося, - багато. Так можна використовувати формат RGB або RGBA — кортеж значень з рухомою крапкою в діапазоні [0, 1] (0.5, 0.6, 0.1) або значення в hex форматі #0a0a0a. Також колір можна задати за допомогою набору символів b, g, r, c, m, y, k, w

import matplotlib.pyplot as plt
import pandas as pd

date = pd.date_range(start="2021-09-01", freq="D", periods=8)
plt.figure(figsize=(10, 4))# Збільшення ширини графіка до 10 дюймів
plt.plot(
    date,
    [23, 17, 17, 16, 15, 14, 17, 20],
    label="day temperature",
    linestyle="--",
    color="#FF5733",
)
plt.plot(
    date,
    [19, 11, 16, 11, 10, 10, 11, 16],
    label="night temperature",
    linestyle=":",
    color="#061358",
)
plt.xlabel("Дата", fontsize="small", color="midnightblue")
plt.ylabel("Температура", fontsize="small", color="midnightblue")
plt.title("Температура в м. Полтава", fontsize=15)
plt.legend()
plt.show()

# Щоб встановити для межі осі інше значення, використовуються методи xlim та ylim.
# Також можна відобразити сітку за допомогою методу grid
# Товщина лінії визначається значенням аргументу lineweight (або просто lw) в пунктах (pt).
# Щоб під час виклику методу plot включити маркери — це символи, що виводяться в кожній точці даних графіка, потрібно визначити аргумент marker.
# од	Маркер	Опис
# .	.	Крапка
# o	○	 Круг
# + 	+	Знак плюс
# x	×	Хрестик
# D	◇	Ромб
# v	◇	Ромб
# D	▽	Трикутник вершиною вниз
# ^	△	Трикутник вершиною вгору
# s	□	Квадрат
# *	✭	Зірка (п'ятикутна)
# І остаточно гарно оформлений графік буде виглядати так:
import matplotlib.pyplot as plt
import pandas as pd

date = pd.date_range(start="2021-09-01", freq="D", periods=8)
plt.plot(
    date,
    [23, 17, 17, 16, 15, 14, 17, 20],
    label="day temperature",
    linestyle="--",
    color="#FF5733",
    linewidth=2,
    marker="D",
)
plt.plot(
    date,
    [19, 11, 16, 11, 10, 10, 11, 16],
    label="night temperature",
    linestyle=":",
    color="#061358",
    linewidth=2,
    marker="^",
)
plt.ylim(0, 25)
plt.xlabel("Дата", fontsize="small", color="midnightblue")
plt.ylabel("Температура", fontsize="small", color="midnightblue")
plt.title("Температура в м. Полтава", fontsize=15)
plt.legend()
plt.grid()
plt.show()

# Стовпчикові діаграми
# Для створення стовпчикової діаграми використовується метод bar (barh) модуля pyplot, який формує графік із прямокутних смуг, що визначаються їх лівою межею та висотою.

# bar — вертикальна стовпчаста діаграма;
# barh — горизонтальна стовпчаста діаграма.
# За замовчуванням значення ширини прямокутників дорівнює 0.8, але воно змінюється за допомогою аргументу width.
# Аргумент	Опис
# width Ширина стовпців. Якщо встановлено скалярне значення, то ширина всіх стовпців однакова. Можна передати масив з різними значеннями ширини стовпців
# bottom  Координати біля нижніх меж стовпців
# height	Послідовність значень висоти стовпців
# color	 Колір заливання стовпців (значення або масив)
# edgecolor Колір меж стовпців (значення або масив).
#  linewidth Значення товщини ліній меж стовпців в pt (значення або масив)
# xerr, yerr Граничні значення для діаграм похибок (значення або масив)
# align	За замовчуванням значення edge визначає вирівнювання стовпців по їх лівих межах (для вертикальних стовпців) або нижніх межах (для горизонтальних стовпців). Значення center центрує стовпці по їх осях
# log	Якщо встановлено значення True, то використовується вісь з логарифмічною шкалою
# orientation vertical (за замовчуванням) або horizontal
# hatch Визначає тип штрихування стовпців: один із символів '/', '\', '|', '-', '+', 'x', 'o', 'O', '.', '* '. Повторення символу дає щільніше штрихування
import matplotlib.pyplot as plt

plt.bar(
    ["США", "Китай", "Японія", "Велика Британія"],
    [39, 38, 27, 22],
    color=["b", "r", "y", "g"],
)

plt.xlabel("Країна", fontsize="small", color="midnightblue")
plt.ylabel("Кількість", fontsize="small", color="midnightblue")
plt.title("Золоті медалі: Літня олімпіада Токіо 2020", fontsize=15)
plt.show()

# Кругові діаграми
# Кругову або секторну діаграму можна побудувати за допомогою методу pie. Значення нормалізуються за їх сумою, якщо ця сума більша за 1, інакше значення безпосередньо інтерпретуються як частки.
# Аргумент	Опис
#  colors 	Послідовність специфікаторів кольору для заливання сегментів
# labels 	Послідовність рядків написів для сегментів
# explode	Послідовність значень, що визначають дробову частину радіуса кругової діаграми, на яку зміщується кожен клиноподібний сегмент (0 для відсутності ефекту винесення сегмента)
# shadow	True або False: визначає зображення або відсутність декоративної тіні під круговою діаграмою
# startangle  Визначає поворот "початкової позиції" кругової діаграми на задане число градусів проти годинникової стрілки щодо горизонтальної осі..
# autopct	 Рядок формату для підписів до сегментів: відповідні значення у відсотках або функція, що генерує необхідний рядок з даних
# pctdistance Радіальне положення тексту підпису autopct щодо радіусу кругової діаграми. За замовчуванням 0.6
# labeldistance	Радіальне положення тексту напису label щодо радіуса кругової діаграми. За замовчуванням 1.1
# radius	Радіус кругової діаграми (за замовчуванням 1)
import matplotlib.pyplot as plt

labels = [
  "Junior Software Engineer",
  "Senior Software Engineer",
  "Software Engineer",
  "System Architect",
  "Technical Lead",
]

data = [63, 31, 100, 2, 11]
explode = [0.15, 0, 0, 0, 0]
plt.pie(
  data,
  labels=labels,
  shadow=True,
  explode=explode,
  autopct="%.2f%%",
  pctdistance=1.15,
  labeldistance=1.35,
)

plt.show()

# Діаграми в полярних координатах
# Для отримання графіка в полярних координатах (r,θ) використовується метод polar, в який передаються аргументи theta (незалежна змінна) і r.

# Побудуємо, наприклад, графік полярної троянди: r(θ)=sin⁡(6⋅θ)
import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0, 2.0 * np.pi, 1000)

r = np.sin(6 * theta)
plt.polar(theta, r)
plt.show()

# Тривимірні графіки
# Бібліотека Matplotlib підтримує побудову тривимірних графіків. Для створення тривимірного графіка необхідно імпортувати об'єкт Axes3D з модуля mpl_toolkits.mplot3d і визначити аргумент projection внутрішнього графіка значенням 3d:
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D

# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')

# Лінійний графік

# Приклад рівняння спіралі у тривимірному просторі
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(projection="3d")

theta_max = 8 * np.pi
n = 1000
theta = np.linspace(0, theta_max, n)
x = theta
z = np.sin(theta)
y = np.cos(theta)
ax.plot(x, y, z, "g")

plt.show()

# Діаграма розсіювання

# Для побудови тривимірної діаграми розсіювання використовується функція scatter з Axes3D. Крім параметрів масивів з координатами точок по осях x, y та z, вона приймає параметр s з розмірами маркера, що дорівнює за замовчуванням 20, який може бути масивом розмірів для кожного маркера.

# Покажемо побудову на прикладі.

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(projection="3d")

x = [5, 10, 15, 20]
z = [10, 0, 5, 15]
y = [0, 10, 5, 25]
s = [150, 130, 30, 160]
ax.scatter(x, y, z, s=s)

plt.show()
# Каркасна поверхня
# Для побудови каркасної поверхні використовується функція plot_wireframe з Axes3D
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(projection="3d")

grid = np.arange(-10, 10, 0.5)
x, y = np.meshgrid(grid, grid)
z = x ** 2 * y ** 2 + 2

ax.plot_wireframe(x, y, z)

plt.show()

# Поверхня
# Для побудови поверхні використовується функція plot_surface

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(projection="3d")

grid = np.arange(-10, 10, 0.5)
x, y = np.meshgrid(grid, grid)
z = x ** 2 * y ** 2 + 2

ax.plot_surface(x, y, z)

plt.show()

# Реалізуйте програму, яка буде будувати візерунок Серпінського. Історія дослідження цього візерунка досить довга, а сам візерунок представляє особливий інтерес у такій галузі, як геометрія фракталів. Візерунок Серпінського є випадковим об'єктом, визначеним рекурсивно, але в межі його форма прямує до детермінованого об'єкта.

# Алгоритм побудови наступний:
# Припустимо, що у вихідному стані ми маємо три точки на площині, причому їх положення описано координатами в деякій відповідній системі координат: (x1,y1),(x2,y2),(x3,y3).
# Випадково вибирається деяка точка всередині трикутника, утвореного заданими вершинами.
# Випадково вибирається одна із трьох вершин.
# Вибирається точка, рівновіддалена від першої обраної точки та від обраної вершини.
# Нова точка включається до зображення
# Вихідна точка замінюється цією новою точкою із зображення.
# Повторюється вся процедура, починаючи з кроку 2.
# Таким чином, кожна нова точка, створена на 3 кроці, включається у зображення.

import random as rand
import matplotlib.pyplot as plt


class RandomPoint():
    def __init__(self, sizex=100, sizey=100, num_points=500):
        self.num_points = num_points
        self.x_val = []
        self.y_val = []
        self.p0 = {
            "x": 50,
            "y": 50
        }
        self.traingl = [
            {
                "x": 0,
                "y": 0
            },
            {
                "x": sizex,
                "y": 0
            },
            {
                "x": sizex // 2,
                "y": sizey
            }
        ]

    def random_vertex(self):
        temp = rand.randint(0, 2)
        return self.traingl[temp]

    def middle(self, start, end):
        x = (start["x"] + end["x"]) // 2
        y = (start["y"] + end["y"]) // 2
        return {"x": x, "y": y}

    def finding(self):
        for index in range(self.num_points):
            vertex = self.random_vertex()
            p1 = self.middle(self.p0, vertex)
            self.x_val.append(p1["x"])
            self.y_val.append(p1["y"])
            self.p0["x"] = p1.get("x")
            self.p0["y"] = p1.get("y")


rs = RandomPoint(1000, 1000, 25000)

rs.finding()
plt.figure(figsize=(15, 10))
point_numbers = list(range(rs.num_points))
plt.scatter(rs.x_val, rs.y_val, s=0.1)
plt.show()