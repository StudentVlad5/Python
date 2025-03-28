import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Correct method to read the CSV file directly from the URL
# url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/car_crashes.csv"
# my_data = pd.read_csv(url)
# print("my_data:")
# print(my_data)


my_data = pd.read_csv("auto-mpg.csv")
print("my_data:")
print(my_data)
data = sns.load_dataset("mpg")
# print("data", data)

# Seaborn надає функції для візуалізації відносин в даних у вигляді лінійних графіків та діаграм розсіювання.

# relplot Загальний інтерфейс для візуалізації відносин з параметрами для налаштування компонування.
# lineplot Лінійний графік із семантичним групуванням.
# scatterplot Діаграма розсіювання із семантичним групуванням.
# Загальні параметри функцій:

# x, y — пов'язують вісь x та y з конкретними ознаками з набору даних, переданого через параметр data. Дані повинні мати числовий тип. Фактично це назви стовпців із набору даних. Якщо вказати значення None, то побудова буде для всіх наборів відразу.
# data — набір даних у форматі pandas.DataFrame, у якому стовпці - це імена змінних, рядки - їх значення.
# ci — чисельно визначає розмір довірчого інтервалу, що відображається. Якщо присвоїти  sd', то використовує стандартне відхилення. Щоб не відображати, присвоїти None`.
# hue — ім'я стовпця з набору data, який задає ознаку в наборі даних для колірного поділу даних.
# palette — палітра, яка буде використана для колірного поділу набору даних за значеннями ознаки, зазначеної в hue. Ім'я палітри можна вибрати відповідно до документації.
# hue_order — порядок застосування кольорів для даних з набору, переданого через параметр hue.
# size — ім'я стовпця з набору data, який буде використаний для поділу даних за розміром.
# size_order — задає порядок розподілу товщини лінії між елементами з набору даних, заданого через параметр size.
# style — ім'я стовпця з набору data, щоб задати ознаку в наборі даних, яка буде використана для поділу даних за стилем.
# markers — тип маркеру. Якщо параметр дорівнює False, то маркери не використовуватимуться.
# style_order — порядок застосування стилів.

# Функція lineplot
# Такий тип графіка найчастіше використовується для візуалізації часових рядів та залежностей між змінними, що мають безперервний характер.
# Встановимо стиль оформлення графіків:
sns.set_style("whitegrid")
date = pd.date_range(start="2021-09-01", freq="D", periods=8)
day = [23, 17, 17, 16, 15, 14, 17, 20]
night = [19, 11, 16, 11, 10, 10, 11, 16]
df = pd.DataFrame({'date':date, 'day_temperature': day, 'night_temperature': night})
sns.lineplot(data=df)
plt.show()
# Якщо ми спробуємо побудувати графік залежності нічної температури від денної, то отримаємо наступний графік:
sns.lineplot(x="night_temperature", y="day_temperature", data=df)
plt.show()
# Необхідно знати, що за замовчуванням seaborn здійснює сортування набору даних, цю опцію можна відключити, задаючи параметру sort значення False
sns.lineplot(x="night_temperature", y="day_temperature", data=df, sort=False)
plt.show()
# Після простого прикладу на температурах повернемося тепер до набору mpg. Побудуємо графік залежності потужності автомобіля від року випуску окремо для кожного регіону.
sns.set_style("darkgrid")
sns.lineplot(x='model_year', y='horsepower', hue="origin", data=data)
plt.show()

# Функція scatterplot
# Побудуємо точковий графік залежності об'єму двигуна (displacement) автомобіля від ефективності споживання палива (mpg):
sns.scatterplot(x='mpg', y='displacement', data=data)
# Ми можемо виділити кольором регіон виробника
sns.scatterplot(x='mpg', y='displacement', hue='origin', data=data)
plt.show()


# Функція relplot
# На відміну від попередніх функцій, ця функція надає можливість налаштовувати не лише зовнішній вигляд графіка, але й фігуру - підкладку, на якій розміщені всі графічні компоненти.

# Параметри для налаштування фігури:

# row, col — назва стовпців, за якими буде проводитися поділ фігури на рядки та стовпці. Можна використовувати лише категоріальні ознаки.
# col_wrap — кількість стовпців для об'єднання.
# row_order, col_order — список, що визначає порядок рядків та/або стовпців відповідно до перерахованих значень ознаки.
# kind — визначає тип графіка, що відображається, лінійний line і точковий scatter.
# height — висота поля графіка в дюймах.
# aspect — параметр, що визначає співвідношення сторін поля з графіком, ширина графіка розраховується за формулою $width = aspect \times height$.
# sns.relplot(x='mpg', y='displacement', kind='scatter', data=data)

# Зручність полягає в тому, що діаграму можна розмістити на трьох окремих полях, як роздільний параметр будемо використовувати регіон (origin)

sns.relplot(x='mpg', y='displacement', kind='scatter', hue='origin', col='origin', data=data)
plt.show()

# Візуалізація категоріальних даних
# Особливість категоріальних ознак полягає в тому, що вони приймають значення з невпорядкованої множини. Це ознаки кольору, форми тощо. І до них не можна застосувати операцію порівняння. Щоправда є окремий випадок порядкових ознак, коли можна провести порівняння, наприклад кафедра – деканат – університет.

# Seaborn надає набір функцій для категоріальних даних. Загальні параметри цих функцій наступні:
# x, y — імена змінних із набору data
# data — набір даних типу pandas.DataFrame, у якому стовпці - це імена ознак, рядки - значення.
# hue — ім'я змінної з набору data, яка визначає ознаку в наборі даних, який буде використаний для колірного поділу даних. Візуально групи будуть представлені у вигляді окремих елементів, що відрізняються кольором.
# order, hue_order — список, що визначає порядок відображення елементів.
# orient — орієнтація графіка, символ v вертикальна, символ h горизонтальна.
# color — колір для всіх елементів, що відображаються.
# palette — ім'я палітри.

# Функція stripplot
# Функція будує точкову діаграму і за функціоналом схожа на функцію scatterplot

sns.stripplot(x='origin', y='mpg', data=data)
# Тепер виділимо кольором кількість циліндрів у двигуна, для цього присвоїмо параметру hue значення cylinders:
sns.stripplot(x='origin', y='mpg', hue='cylinders', data=data)
plt.show()

# Функція swarmplot

# Функція аналогічна функції stripplot, але точки, що відображаються на діаграмі, не перекриваються, це дозволяє робити висновки про переважання тих або інших значень в наборах даних з їх візуального розподілу.
sns.swarmplot(x='origin', y='mpg', hue='cylinders',data=data)
plt.show()

# Візуалізації розподілу категоріальних даних
# Seaborn надає три функції для візуалізації розподілу категоріальних даних:

# boxplot — будує діаграму типу "скринька з вусами", на ній відображаються медіанне значення, квартілі та викиди

sns.boxplot(x="origin", y="mpg", hue="cylinders", data=data)
plt.show()

# violinplot — будує діаграму, схожу на "скриньку з вусами" з оцінкою щільності ядра
sns.violinplot(x="origin", y="mpg", data=data)
plt.show()

# boxenplot — будує діаграму з прямокутників, добре підходить для візуалізації великих наборів даних.
sns.boxenplot(x="origin", y="mpg", data=data)
plt.show()

# Візуалізація оцінок категоріальних даних

# Функція pointplot
# Відображає оцінку будь-якого набору даних як точку на полі графіка та довірчий інтервал у вигляді лінії, центр якої лежить на зазначеній точці.

sns.pointplot(x="origin", y="mpg", data=data)
plt.show()

# Функція barplot
# Функція будує стовпчасту діаграму: висота бару (стовпця) визначає чисельне значення оцінки ознаки (математичне очікування), лінія, що перетинає верхню межу бару - довірчий інтервал.

sns.barplot(x="origin", y="mpg", data=data)
plt.show()

# Функція countplot
# Функція визначає кількість елементів з набору даних, які належать до тієї або іншої категорії, і відображає отримане значення у вигляді стовпчастої діаграми.
sns.countplot(x="cylinders", data=data)
plt.show()

# Візуалізація моделі лінійної регресії
# Seaborn надає набір функцій для побудови моделі лінійної регресії за переданими даними та відображають її разом із вихідним набором даних.

# Функція regplot
# Функція regplot відображає набір даних та лінію регресії, побудовану за ними.
# Побудуємо лінію регресії залежності відстані, яку може проїхати автомобіль, від його потужності.

sns.lmplot(x="horsepower", y="displacement", data=data)
plt.show()

# Можна побудувати діаграму з медіанною оцінкою та необхідні параметри функції при цьому:

# x_estimator — функція для обчислення значення оцінки.
# x_bins — число для визначення кількості груп, на які буде розбито вихідна множина значень.
# x_ci — Число в діапазоні [0, 100] або None, розмір довірчого інтервалу.

from numpy import median
sns.lmplot(x="horsepower", y="displacement", data=data, x_estimator=median)
plt.show()

# Функція residplot
# Функція відображає відхилення елементів вихідного набору даних від регресійної моделі, побудованої за ними, у вигляді діаграми розсіювання. Кожна точка такої діаграми – це різниця між значенням елемента вихідного набору та значенням, яке видасть модель регресії у цій точці.

sns.residplot(x="horsepower", y="displacement", data=data)
plt.show()

# Функція lmplot
# Функція повний аналог функції regplot з можливістю управляти компонуванням полів з графіками на підкладці як для функції relplot.
sns.lmplot(x="horsepower", y="displacement", hue="origin", col="origin", data=data)
plt.show()

# Стилі
# Найпростіший і найшвидший спосіб задати оформлення для графіка seaborn - це використовувати один із заздалегідь підготовлених стилів за допомогою функції set_style або використовувати свої стилі з індивідуальним оформленням.
# set_style(style=None, rc=None)
# style — це або свій словник з параметрами, або ім'я стилю із заданого набору: darkgrid, whitegrid, dark, white, ticks.
# rc — словник, який перевизначає параметри аргументу style.
# Отримати список параметрів, що відповідають за оформлення графіка, можна за допомогою функції axes_style.

# Для набору mpg ми всі графіки будували у стилі darkgrid.

sns.set_style("darkgrid")
data = sns.load_dataset("mpg")
sns.lineplot(x='model_year', y='horsepower', hue="origin", data=data)
sns.axes_style()
{'axes.facecolor': '#EAEAF2',
 'axes.edgecolor': 'white',
 'axes.grid': True,
 'axes.axisbelow': True,
 'axes.labelcolor': '.15',
 'figure.facecolor': 'white',
 'grid.color': 'white',
 'grid.linestyle': '-',
 'text.color': '.15',
 'xtick.color': '.15',
 'ytick.color': '.15',
 'xtick.direction': 'out',
 'ytick.direction': 'out',
 'lines.solid_capstyle': 'round',
 'patch.edgecolor': 'w',
 'patch.force_edgecolor': True,
 'image.cmap': 'rocket',
 'font.family': ['sans-serif'],
 'font.sans-serif': ['Arial',
  'DejaVu Sans',
  'Liberation Sans',
  'Bitstream Vera Sans',
  'sans-serif'],
 'xtick.bottom': False,
 'xtick.top': False,
 'ytick.left': False,
 'ytick.right': False,
 'axes.spines.left': True,
 'axes.spines.bottom': True,
 'axes.spines.right': True,
 'axes.spines.top': True}
plt.show()

# Як мовилося раніше, ми можемо перевизначати параметри оформлення.
sns.set_style("darkgrid",  {'axes.labelcolor':"(0.5,0.5,0)", 'axes.edgecolor':'#061358',
'xtick.color':'#0A5806'})
sns.lineplot(x='model_year', y='horsepower', hue="origin", data=data)
plt.show()

# Контекст
# Також в seaborn використовуються контексти для управління масштабом зображення.
# Для встановлення контексту використовується функція set_context:
# set_context(context=None, font_scale=1, rc=None)
# Параметри:
# context — параметр з набору: paper, notebook, talk, poster.
# font_scale — коефіцієнт для зміни розміру шрифту.
# rc — словник із параметрами для перевизначення властивостей, заданого через аргумент context.
# Для отримання списку параметрів контексту використовується функція plotting_context
sns.set_context("poster")
sns.scatterplot(x='mpg', y='displacement', data=data)

# Сітка
# Параметр	Опис
#  axes.grid 	True – відобразити сітку, False – ні.
# grid.color	Колір лінії сітки.
# grid.linestyle	Стиль лінії сітки.
# axes.axisbelow	Розміщення сітки під (True) або над (False) діаграмою.
#  axes.edgecolor	Колір межі поля графіка
# axes.facecolort	 Колір поля графіка.
# axes.labelcolor	Колір підписів осей.
# axes.spines.bottom	Розміщення осі у нижній частині поля (True).
# axes.spines.left	Розміщення осі у лівій частині поля (True).
# axes.spines.right	Розміщення осі у правій частині поля (True)
# axes.spines.top	Розміщення осі у верхній частині поля (True).

# Параметри стилю для налаштування сітки
# Параметр	Опис
# grid.linewidth 	Товщина лінії сітки
# axes.linewidth	Товщина осей графіка
# axes.titlesize	Розмір заголовка

# Легенда
# Легенда на графіку відображається автоматично, якщо ви використовуєте якийсь додатковий параметр для групування даних за тими або іншими ознаками.
# Безпосередньо сама бібліотека seaborn не надає інструментів для налаштування візуального оформлення легенди. Єдиний параметр - це legend.fontsize для управління розміром шрифту легенди.

# Шрифт
# За налаштування шрифту відповідають параметри font.family (із стилю) та font_scale (з контексту).

# Колір
# Функція color_palette повертає список кольорів.
# color_palette(palette=None, n_colors=None, desat=None)
# Параметри функції:
# palette — назва палітри або набір кольорів. Якщо значення дорівнює None, то буде повернута поточна палітра.
# n_colors — кількість кольорів в палітрі.
# desat — коефіцієнт насиченості, початкове значення 1.
# Функція set_palette встановлює колірну палітру як поточну. Призначення параметрів збігається із зазначеними для функції color_palette.

# Щоб побачити поточну схему кольорів:
# sns.palplot(sns.color_palette())

# таблиці наведені дані про взаємонезалежні прибутковості трьох акцій: A, B, C.
# Момент спостереження	Прибутковість A, %	Прибутковість B, %	Прибутковість C, %
# 1	25	0	10
# 2	-10	15	25
# 3	10	-5	-15
# 4	5	5	-5
# 5	35	20	-5
# 6	13	25	15
# Побудуйте лінії регресії за допомогою функції regplot, залежності прибутковості однієї акції від іншої. Всього три графіки. Виберіть пару акцій, які найменш залежні в прибутковостях одна від одної.

date = pd.date_range(start="2010-01-01", freq="D", periods=6)
stock_A  = [25,-10,10,5,35,13]
stock_B  = [0,15,-5,5,20,25]
stock_C  = [10,25,-15,-5,-5,15]
stock_market = pd.DataFrame({'date':date, 'Прибутковість A': stock_A, 'Прибутковість B': stock_B, 'Прибутковість C': stock_C })
print("stock_market", stock_market)
# sns.lineplot(x='date', y='Прибутковість', hue="origin", data=stock_market)

# Розрахуємо кореляцію між кожною парою акцій
correlation_matrix = stock_market[['Прибутковість A', 'Прибутковість B', 'Прибутковість C']].corr()
print("Correlation Matrix:\n", correlation_matrix)

# Створимо графіки для кожної пари акцій
plt.figure(figsize=(12, 10))

# 1-й графік: Прибутковість A vs B
plt.subplot(3, 1, 1)
sns.regplot(x='Прибутковість A', y='Прибутковість B', data=stock_market)
plt.title('Регресія: Прибутковість A vs B')

# 2-й графік: Прибутковість B vs C
plt.subplot(3, 1, 2)
sns.regplot(x='Прибутковість B', y='Прибутковість C', data=stock_market)
plt.title('Регресія: Прибутковість B vs C')

# 3-й графік: Прибутковість A vs C
plt.subplot(3, 1, 3)
sns.regplot(x='Прибутковість A', y='Прибутковість C', data=stock_market)
plt.title('Регресія: Прибутковість A vs C')

# Показати графіки
plt.tight_layout()
plt.show()

# Вивести матрицю кореляцій для кращого розуміння
print("Кореляція між прибутковістю акцій:")
print(correlation_matrix)
# Щоб вибрати пару акцій, які найменш залежні одна від одної, ми повинні звернути увагу на кореляцію між їх прибутковістю. Кореляція — це статистичний показник, що описує, як дві змінні змінюються разом. Якщо кореляція близька до +1, то зміни в одній змінній сильно корелюють зі змінами в іншій (позитивна залежність). Якщо кореляція близька до -1, то зміни відбуваються в протилежних напрямках (негативна залежність). Якщо кореляція близька до 0, то між змінними немає лінійної залежності.
# Відповідь А та В.