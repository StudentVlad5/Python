# SciPy 
# Загальні відомості
# SciPy - це бібліотека Python з відкритим вихідним кодом, яка використовується для вирішення наукових та математичних задач. Вона побудована на розширенні NumPy та дозволяє користувачеві маніпулювати та візуалізувати дані за допомогою широкого набору команд високого рівня.

# Встановлення SciPy у Windows можна виконати через pip
# Опис	Назва
# Введення/виведення файлів	scipy.io
# Спеціальні функції	scipy.special 
# Операції лінійної алгебри	scipy.linalg
# Інтерполяція	scipy.interpolate 
# Оптимізація та припасування	scipy.optimize 
# Статистика та випадкові числа	scipy.stats
# Чисельне інтегрування	scipy.integrate
# Перетворення Фур'є	scipy.fftpack
# Обробка сигналів	scipy.signal
# Обробка зображень	scipy.ndimage
# Щоб дізнатися більше про ці функції, ви можете використовувати функції help,

from scipy import constants
# help(constants)

# Рядок ідентифікації константи	Змінна	Значення	Одиниці вимірювання
# 'atomic mass constant’	m_u	1.6605390666e-27	кг
# Avogadro constant’	Avogadro	 6.02214076e+23	 1/моль
# 'Boltzmann constant'	k	1.380649e-23	Дж/К
# 'electron mass’	m_e	9.1093837015e-31	кг
# 'elementary charge’	e	1.602176634e-19	Кл
# 'fine-structure constant’	alpha	0.0072973525693	              
# 'molar gas constant’	R	8.314462618	Дж/(К∙моль)
# 'neutron mass’	m_n	1.67492749804e-27	кг
# 'Newtonian constant of gravitation’	G	6.6743e-11	м3/(с2∙кг)
# 'Planck constant’	h	6.62607015e-34	Дж∙с
# 'proton mass’’	m_p	1.67262192369e-27	кг
# 'Rydberg constant’	Rydberg	10973731.56816	1/м
# 'speed of light in vacuum'	c/td>	299792458.0	м/с

print(constants.m_u)
print(constants.Avogadro)
# 1.6605390666e-27
# 6.02214076e+23

# Спеціальні функції з пакету scipy.special містять безліч функцій математичної фізики. Спеціальні функції SciPy включають кубічний корінь, експоненту, логарифмічну експоненту і багато іншого.

# Функції, що надаються пакетом scipy.io, дозволяють нам працювати з різними форматами файлів, такими як Matlab, Arff, Wave, Matrix Market, IDL, NetCDF, TXT, CSV і двійковий формат.

# Математичне моделювання процесів та явищ є невід'ємною частиною досліджень у різних галузях науки та техніки. Складні обчислювальні завдання, що виникають при дослідженні фізичних та технічних проблем, можна розбити на ряд елементарних — таких як обчислення інтегралів, розв'язання диференціальних рівнянь тощо. Розглянемо тепер деякі підпакети детальніше.

# Інтегрування та розв'язок диференціальних рівнянь
# Пакет scipy.integrate містить методи для обчислення певних інтегралів. З їх допомогою можна обчислювати власні та невласні інтеграли. Ці методи дозволяють виконувати чисельне інтегрування систем звичайних диференціальних рівнянь.

from scipy import integrate
import numpy as np

result = integrate.quad(lambda x: np.sin(x), 0, np.pi)
print(result)

result = integrate.quad(lambda x: 1/x, 1, np.inf)
print(result)

# IntegrationWarning: The maximum number of subdivisions (50) has been achieved. If increasing the limit yields no
# improvement it is advised to analyze the integrand in order to determine the difficulties. If the position of a local
# difficulty can be determined (singularity, discontinuity) one will probably gain from splitting up the interval and
# calling the integrator on the subranges. Perhaps a special-purpose integrator should be used. result =
# integrate.quad(lambda x: 1/x, 1, np.inf) (40.996012819169536, 8.156214940493651)

# Фактично це говорить про те, що невласний інтеграл дорівнює ∞ і розходиться.

result = integrate.quad(lambda x: 1/(x**2), 1, np.inf)
print(result)
# (1.0, 1.1102230246251565e-14)

# Якщо потрібно інтегрувати функцію з точками розриву, необхідно передавати точки розриву в спеціальному параметрі списку points.
result = integrate.quad(lambda x: np.sin(x)/x, -1, 1, points=[0])
print(result)

# (1.8921661407343662, 2.1007264158594178e-14)

# Рішення звичайних диференціальних рівнянь (ДР) у чисельному вигляді виконується за допомогою методу scipy.integrate.solve_ivp ("solve an initial value problem")

# Метод solve_ivp вирішує диференціальні рівняння першого порядку. Для вирішення рівнянь вищого порядку, їх потрібно спочатку розкласти у систему ДР першого порядку.

# У метода solve_ivp можна змінювати алгоритм вирішення ДР за допомогою встановлення значення параметра method. Список можливих варіантів значень наведено нижче у таблиці. За замовчуванням method дорівнює 'RK45'.

# Метод	Опис
# RK45 	Явний метод Рунге-Кутти порядку 5(4)
# RK23	Явний метод Рунге-Кутти порядку 3(2)
# Radau	Неявний метод Рунге-Кутти сімейства Радау
# BDF	Наближена формула диференціювання (BDF) (зворотного диференціювання), явний метод, що підходить для вирішення жорстких завдань
# SODA	Гнучкий метод, який може автоматично визначати жорсткість завдання і перемикатися між методом (алгоритмом) Адамса (для нежорстких завдань) і BDF (для жорстких завдань)

# Розберемо наступне завдання. Припустимо, що ми рекламуємо наш інстаграм профіль. В момент часу  t  з числа потенційних N підписників про нього знає лише y людина. Ми реалізуємо рекламну кампанію через соцмережі і вважаємо, що після рекламних оголошень швидкість зміни кількості підписників пропорційна кількості самих підписників, тому що ми припускаємо, що інформація про наш блог поширюється серед самих підписників за допомогою спілкування.

# Якщо припустити, що час йде від рекламної кампанії, то ми прийдемо до диференціального рівняння такого виду: 
# def dydt(t, y):
#     return k * y * (1 - y / N)
# Саме рішення отримаємо викликом функції solve_ivp:
# soln = solve_ivp(dydt, (t0, tf), [y0])
# Порядок аргументів важливий. Початковий і кінцевий моменти часу повинні передаватися як кортеж (t0, tf), а початкові умови повинні бути представлені об'єктом типу масив, навіть якщо, як у нас це одне значення.

from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

k = 0.5
N = 1000
y0 = 10
t0, tf = 0, 25

def dydt(t, y):
    return k * y * (1 - y / N)

soln = solve_ivp(dydt, (t0, tf), [y0])
print(soln)

# Результат рішення - екземпляр класу OdeResult

#   message: 'The solver successfully reached the end of the integration interval.'
#      nfev: 68
#      njev: 0
#       nlu: 0
#       sol: None
#    status: 0
#   success: True
#         t: array([ 0.        ,  0.11510327,  1.26613592,  3.52149215,  6.23043272,
#         9.37534666, 12.80554684, 15.37357669, 17.94160655, 21.27577718,
#        25.        ])
#  t_events: None
#         y: array([[ 10.        ,  10.58612839,  18.6689464 ,  55.49820182,
#         185.51405174, 523.79286449, 859.53541686, 956.7843443 ,
#         987.63048739, 997.53709068, 999.56082114]])
#  y_events: None

soln = solve_ivp(dydt, (t0, tf), [y0])
t, y = soln.t, soln.y[0]
plt.plot(t, y, 'o', color='k', label='solve_ivp')
plt.legend()
plt.show()

# Якщо у функцію solve_ivp передати аргумент dense_output зі значенням True, то об'єкт OdeSolution, що повертається, буде із властивістю sol. Його можна використовувати для генерування інтерполяційних значень рішення для проміжних значень точок часу. Побудуємо графік інтерполяційних значень.

soln = solve_ivp(dydt, (t0, tf), [y0], dense_output=True)
t, y = soln.t, soln.y[0]
z, = soln.sol(t)
plt.plot(t, y, 'o', color='k', label='solve_ivp')
plt.plot(t, z, color='blue', label='Interpolation')
plt.legend()
plt.show()

# Об'єкт soln.sol є таким, що викликається, і значення незалежної змінної часу передається в нього, і повертається масив рішення в цей момент часу.

# Зараз функція dydt, що повертає похідну, використовує глобальні параметри k та N, але їх можна передати в метод solve_ivp в параметрі args.

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

k = 0.5
N = 1000
y0 = 10
t0, tf = 0, 25

def dydt(t, y, k, N):
    return k * y * (1 - y / N)

soln = solve_ivp(dydt, (t0, tf), [y0], dense_output=True, args=(k, N))

# Інтерполяція функцій
# Функціональність найпростішої та очевидної одновимірної інтерполяції надає метод scipy.interpolate.interp1d.

# Метод приймає масиви точок x і y, а повертає функцію, яку можна викликати для генерації інтерпольованих значень у проміжних точках x. За замовчуванням використовується лінійна схема інтерполяції, але можливі й інші варіанти, залежно від значення параметра kind.

# Способи інтерполяції методу interp1d, залежно від значення аргументу kind

# Значення	Опис
# linear 	Прийнята за замовчуванням лінійна інтерполяція, яка використовує лише значення із вихідних масивів даних, що охоплюють потрібну точку
# nearest	Прив'язка до найближчої точки даних
# zero	Сплайн нульового порядку: інтерполює за останнім значенням, що спостерігається, при проході масивами даних
# slinear	Інтерполяція сплайном першого порядку (фактично це той самий linear')
# quadratic	Інтерполяція сплайном другого порядку
# cubic	Інтерполяція кубічним сплайном
# previous	Використовується попередня точка даних
# next	Використовується наступна точка даних

# Лінійна інтерполяція
# Але функція interp1d за замовчуванням використовує найпростішу лінійну інтерполяцію, що найчастіше використовується.

# Вона полягає в тому, що задані точки з координатами xi yi  при i= 0,1, 2, …, n з'єднуються прямолінійними відрізками, а функцію y(x) можна приблизно уявити у вигляді ламаної.

# Рівняння кожного відрізка ламаної у загальному випадку різні. Оскільки є n інтервалів (xi −1, xi),
#  ), то для кожного з них як рівняння інтерполяційного багаточлена використовується рівняння прямої, що проходить через дві точки: 
# i−го інтервалу можна написати рівняння прямої, що проходить через точки 

# Отже, при використанні лінійної інтерполяції спочатку потрібно визначити інтервал, в який потрапляє значення аргументу  x, а потім підставити його у формулу (3) і знайти наближене значення функції в цій точці.

import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

date = np.linspace(1, 8, 8)
day = [23, 17, 17, 16, 15, 14, 17, 20]

f = interp1d(date, day, kind='linear')

plt.plot(date, day, 'o')
more_date = np.linspace(1, 8, 100)
plt.plot(more_date, f(more_date))
plt.ylim(0,25)
plt.show()

f = interp1d(date, day, kind='nearest')

plt.plot(date, day, 'o')
more_date = np.linspace(1, 8, 100)
plt.plot(more_date, f(more_date))
plt.ylim(0,25)
plt.show()

f = interp1d(date, day, kind='cubic')

plt.plot(date, day, 'o')
more_date = np.linspace(1, 8, 100)
plt.plot(more_date, f(more_date))
plt.ylim(0,25)
plt.show()

# Для задачі 4 з першого модуля: складіть рівняння параболи, що проходить через задані три точки (1,12), (3,54), (-1,2). Ми можемо побудувати графік інтерполяції від точки (-1,2) до точки (3,54) з параметром kind='quadratic'

import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

x = [-1, 1, 3]
y = [2, 12, 54]
f = interp1d(x, y, kind='quadratic')
plt.plot(x, y, 'o')
more_x = np.linspace(-1, 3, 100)
plt.plot(more_x, f(more_x))

# Багатовимірна інтерполяція
# Для двовимірної інтерполяції використовується метод scipy.interpolation.interp2d. Для нього потрібен двовимірний масив значень z і два одновимірних масиви координат x і y, що відповідають значенням даних. В аргументі kind можна передати один із трьох підтримуваних типів сплайну інтерполяції: 'linear' (за замовчуванням), 'cubic' або 'quintic'.

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from scipy.interpolate import LinearNDInterpolator

# Define x, y, and z ranges
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
z = np.linspace(0, 100, 100)

# Create meshgrid for X, Y
X, Y = np.meshgrid(x, y)

# Random points in x, y, and z for interpolation
px, py = np.random.choice(x, 50), np.random.choice(y, 50)
pz = np.random.choice(z, 50)

# Create the interpolator using LinearNDInterpolator for scattered data
interpolator = LinearNDInterpolator(list(zip(px, py)), pz)

# Interpolate at all points on the meshgrid
Z = interpolator(X, Y)

# Plotting the surface
fig = plt.figure()
ax = fig.add_subplot(projection="3d")
ax.plot_surface(X, Y, Z, cmap='viridis')

plt.show()

# Другий метод для інтерполяції неструктурованих даних — scipy.interpolate.griddata.
# Загальний вигляд виклику методу для двох вимірів:

# scipy.interpolate.griddata(points, values, xi, method='linear')
# де:
# points — кортеж масивів x та y або один масив розмірності (n, 2)
# values — дані, одновимірний масив довжиною n.
# xi — масив координатної сітки, за якою виконується інтерполяція (розмірність (m, 2)).
# method — тип інтерполяції: 'linear' (за замовчуванням), 'nearest' та 'cubic'.

from scipy.interpolate import griddata
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

x = np.linspace(-10, 10, 1000)
y = np.linspace(-10, 10, 1000)
X, Y = np.meshgrid(x, y)

def f(x, y):
    return x ** 2 * y ** 2 + 2

px, py = np.random.choice(x, 250), np.random.choice(y, 250)

z = griddata((px, py), f(px, py), (X, Y), method='cubic')

fig = plt.figure()
ax = fig.add_subplot(projection="3d")
ax.plot_surface(X, Y, z)

plt.show()
# Якщо набір координат (x,y) утворює рівномірно розподілену сітку, то найкращим методом інтерполяції є використання об'єкта scipy.interpolate.RectBivariateSpline

# Класифікація задач оптимізації

# Задача (1) є загальною постановкою задачі оптимізації. Класифікацію задач оптимізації можна проводити за декількома ознаками, залежно від виду функції 
# f(x)та множини U. Далі ми виділимо найважливіші для теорії та застосунків оптимізаційні задачі.

# Множину усіх точок мінімуму функції f(x) на U будемо надалі позначати через U∗. Множина U∗ може бути порожньою, складатися з кінцевої або нескінченної кількості точок.

# Мінімізація без обмежень

# Узагальнений алгоритм мінімізації для скалярної функції кількох змінних scipy.optimize.minimize приймає два обов'язкові аргументи:

# minimize(fun, x0)

# fun — функція для обчислення мінімізованої функції: ця функція повинна приймати масив значень, що визначає точки, в яких повинні виконуватися обчислення [x1, x2,…, xn]
# x0 — це масив значень, що представляють початкові значення, з яких алгоритм мінімізації повинен розпочати роботу.
# Метод minimize повертає об'єкт типу словник з інформацією про мінімізацію.

# Ключ	Опис
# success	Логічне значення, що повідомляє, була мінімізація успішною або ні
# x	Якщо мінімізація успішна, то містить рішення: значення (x1, x2, …, xn), у яких знайдено мінімум функції. Якщо алгоритм мінімізації завершився невдало, то x містить точку аварійного зупинника
# fun	Якщо мінімізація успішна, то містить значення функції в точці мінімуму, визначеної як x
# message	Рядок, що описує результат мінімізації 
# jac	Значення матриці Якобі: якщо мінімізація успішна, то значення в цьому масиві повинні бути близькими до нуля. 
# hess, hess_inv	Матриця Гессе і зворотна їй матриця (якщо використовувалася)
# nfev, njev, nhev	Кількість операцій обчислення функції, її якобіана та гесіана

# Виконаємо пошук мінімуму у параболоїда. Рівняння функції буде наступним z=x**2 +y**2  Спочатку побудуємо контурний графік функції.

from scipy.interpolate import griddata
from scipy.optimize import minimize
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 10000)
y = np.linspace(-10, 10, 10000)
X, Y = np.meshgrid(x, y)

px, py = np.random.choice(x, 2500), np.random.choice(y, 2500)

def paraboloid(arg):
    x, y = arg
    return x ** 2  + y ** 2
# довгий розрахунок, відключив
# z = griddata((px, py), paraboloid((px, py)), (X, Y), method='cubic')
# plt.contour(x, y, z)
# plt.show()

print(minimize(paraboloid, [1, 5]))

def f(arg):
  x, y = arg
  return x ** 2 * y ** 2 + 2

# z = griddata((px, py), f((px, py)), (X, Y), method='cubic')
# plt.contour(x, y, z)
# plt.show()
print("result", minimize(f, [1, 5], method='Nelder-Mead'))

# Значення аргументу method	Опис
# BFGS	Алгоритм BFGS (Broyden-Fletcher-Goldfarb-Shanno), прийнятий за замовчуванняи для мінімізації без обмежень або граничних умов
# Nelder-Mead	Метод сполучених градієнтів Powell Метод Пауелла (для цього алгоритму не потрібні похідні)
# dogleg	Ломано-лінійний алгоритм у довірчій області. Потрібні матриці Якобі та Гессе (які обов'язково повинні бути позитивно визначеними)
# TNC	Усічений алгоритм Ньютона для мінімізації з граничними умовами
# l-bfgs-b	Мінімізація з обмеженнями та граничними умовами з використанням алгоритму L-BFGS-B
# slsqp	мінімізація методом найменших квадратів» (sequential least-squares programming) з граничними умовами та обмеженнями щодо рівності та нерівності
# cobyla	Метод «оптимізації з обмеженнями з використанням лінійної апроксимації» (constrained optimization by linear approximation) для мінімізації з обмеженнями

# Мінімізація з обмеженнями
# Іноді необхідно знайти максимум або мінімум об'єкта функції з одним або кількома обмеженнями.
# Алгоритми l-bfgs-b, tnc та slsqp підтримують аргумент bounds для передачі в метод minimize. Значення аргументу bounds — це послідовність кортежів, кожен із яких містить пари (min, фmax) для кожної змінної функції, що визначають межі мінімізації для відповідної змінної. Якщо в будь-якому напрямку не існує обмежень, то використовується значення None.

xbounds = (1, None)
ybounds = (1, None)
bounds = (xbounds, ybounds)
result = minimize(paraboloid, [1, 5], bounds=bounds, method='slsqp')

# Складні функціональні обмеження задаються за допомогою аргументу constraints для методу minimize у вигляді послідовності словників, що визначають рядкові ключі: type визначає тип обмеження та fun функція, що реалізує обмеження. Значенням type може бути eq або ineq для обмеження, заснованого на рівності або нерівності
cons = ({'type': 'ineq', 'fun': lambda x:  x[0] - 2 * x[1] + 2},
        {'type': 'ineq', 'fun': lambda x: -x[0] - 2 * x[1] + 6},
        {'type': 'ineq', 'fun': lambda x: -x[0] + 2 * x[1] + 2})

# Знайдемо точку, в якій тіло підніметься на максимальну висоту. Приймемо, що кут польоту дорівнює 45 градусів (при такому значенні кута досягається максимум польоту тіла), а початкова швидкість, наприклад, 35 м/с

# Виконаємо побудову графіка функції

import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as pc
import scipy.optimize as opt

alpha = np.pi / 4
speed = 35
x = np.linspace(0, 120, 1000)
y = x * np.tan(alpha) - (pc.g * x**2)/(2 * speed**2 * np.cos(alpha) ** 2)

plt.grid()
plt.plot(x, y)

# Як бачимо максимум функції досягається на проміжку (40, 80). Але, враховуючи, що нам потрібно шукати мінімум, в метод minimize_scalar необхідно буде передати - f(x)

alpha = np.pi / 4
speed = 35

def angle_flight(x, alpha, speed): return x * np.tan(alpha) - (pc.g * x**2)/(2 * speed**2 * np.cos(alpha) ** 2)
# помилка в завданні
# result = minimize_scalar(lambda x, alpha, speed: -angle_flight(x, alpha, speed), bracket=(40, 60, 80), args=(alpha, speed))
# Using minimize_scalar and passing extra arguments through a lambda function
result = opt.minimize_scalar(lambda x: -angle_flight(x, alpha, speed), bracket=(40, 60, 80))


print("result", result)

# У бібліотеці SciPy узагальненою програмою нелінійного припасування методом найменших квадратів є scipy.optimize.leastsq, основна сигнатура виклику якої:
# scipy.optimize.leastsq(func, x0, args=())

# Метод намагається підігнати послідовність точок даних y до певної певної модельованої функції f, яка залежить від одного або декількох параметрів припасування. У метод leastsq передається функція func, яка повертає різницю між набором даних y і значенням бажаної функції f (нев'язки). Також потрібна осмислена початкова передумова для параметрів x0.

# Розберемо це на конкретному прикладі. Повернемося до наших даних про температуру за 8 днів [23, 17, 17, 16, 15, 14, 17, 20]

# Чисельні методи вирішення рівнянь

# Модуль scipy.optimize надає кілька методів для обчислення коренів одновимірних та багатовимірних функцій.

# Основним методом пошуку коренів, зручним для аналізу функції, є scipy.optimize.brentq, що реалізує алгоритм Брента зі зворотною квадратичною екстраполяцією.

# scipy.optimize.brentq(f, a, b)
# де:
# f функція Python, що повертає число. Функція повинна бути безперервною і мати протилежні знаки на відрізку [a, b].
# a початок інтервалу пошуку кореня.
# b кінець інтервалу пошуку кореня.

# Побудуємо графік на проміжку [-5, 5]

x = np.linspace(-5, 5, 50)
y = x ** 2 + 3 * x - 4
plt.grid()
plt.plot(x, y)
plt.axhline(linewidth=1, color='b')
plt.axvline(linewidth=1, color='b')
# помилка у формулі викладача
# left_root = opt.brentq(f, -5, 0)  # -4
# rigth_root = opt.brentq(f, 0, 5)  # 1

# Робота із зображеннями
# Так можна отримати зображення білого шуму розміром 500 на 500 точок.
import numpy as np
from matplotlib import pyplot as plt
random_image = np.random.random([500, 500])
plt.imshow(random_image, cmap='gray', interpolation='nearest')
plt.show()
# Давайте попрацюємо із зображенням з файлу.
# im = plt.imread("./img/lemur.jpg")
# plt.imshow(im)
# im.shape

# Давайте трохи покращимо виведення зображення:

# y = im.shape[0]
# x = im.shape[1]
# h = 7
# w = (y/x) * h
# plt.figure(figsize=(w,h))
# plt.imshow(im)

# Оскільки зображення є не більше, ніж масив, ми можемо використовувати зрізи для отримання необхідної частини зображення.

# y = im.shape[0]
# x = im.shape[1]
# h = 7
# w = (y/x) * h
# plt.figure(figsize=(w,h))
# plt.imshow(im[200:700, 100:650, :])

# Щоб отримати негатив, потрібно отримати зворотну різницю від одиниці.
# plt.imshow(1 - im[200:700, 100:650, :])

# Можна знебарвити зображення та зробити його чорно-білим.
# plt.imshow(np.mean(im[200:700, 100:650, :], axis=2), cmap='gist_gray')

# Якщо ми хочемо зберегти отримане зображення:
# plt.imshow(np.mean(im[200:700, 100:650, :], axis=2), cmap='gist_gray')
# plt.savefig("test.jpg")

# Перевернути зображення:
# im_flipud = np.flipud(im[200:700, 100:650, :])
# plt.imshow(im_flipud)

# from scipy import ndimage
# import matplotlib.pyplot as plt
# Ми можемо виконувати деякі базові операції, такі як поворот зображення. SciPy надає функцію rotate, яка повертає зображення на вказаний кут.

# im = plt.imread("./img/lemur.jpg")
# rotate_face = ndimage.rotate(im, -45)

# plt.imshow(rotate_face)
# plt.show()

# Наприклад, розглянемо розмитість. Розмитість - це метод, який використовується для зменшення шуму на зображенні. Приклад наведено нижче:

# from scipy import ndimage
# import matplotlib.pyplot as plt

# im = plt.imread("./img/lemur.jpg")[200:700, 100:650, :]
# blurred_im_2 = ndimage.gaussian_filter(im, sigma=2)
# blurred_im_4 = ndimage.gaussian_filter(im, sigma=4)

# fig, axs = plt.subplots(1, 3, figsize=(50,100))

# axs[0].imshow(im)
# axs[1].imshow(blurred_im_2)
# axs[2].imshow(blurred_im_4)

# plt.show()

# Перше завдання

# Є набір даних speed, який представляє значення швидкості для деякого транспортного засобу в певний момент спостереження. Очевидно, що дані мають дискретний вигляд. Відомо, що спостереження відбувалися з періодом в одну годину.

speed = [25, 35, 45, 30, 60, 120, 100, 100, 70, 75, 80, 65]

# 1. Приймемо, що в нульовій координаті у нас швидкість 25 км/год, відповідно до набору даних speed. Помістіть у змінну time - вектор часу, створений за допомогою np.linspace (всього 12 спостережень, від 0 до 11 годин)

# 2. Виконайте виведення масиву time
import pandas as pd

# Creating a custom Index
index_range = pd.Index(range(0, 11))  # Index from 1 to 10
print("index_range",index_range)

# Перше завдання

# Є набір даних speed, який представляє значення швидкості для деякого транспортного засобу в певний момент спостереження. Очевидно, що дані мають дискретний вигляд. Відомо, що спостереження відбувалися з періодом в одну годину.

speed = [25, 35, 45, 30, 60, 120, 100, 100, 70, 75, 80, 65]

# 1. Приймемо, що в нульовій координаті у нас швидкість 25 км/год, відповідно до набору даних speed. Помістіть у змінну time - вектор часу, створений за допомогою np.linspace (всього 12 спостережень, від 0 до 11 годин)

# 2. Виконайте виведення масиву time
import pandas as pd

# Creating a custom Index
index_range = pd.Index(range(0, 12))  # Index from 1 to 10
print("index_range",list(index_range))

# 3. Виконайте виведення графіка - значення точок швидкості (plot або scatter). Задайте розмір області, що відображається (0, 11) і (0, 130). Задайте відображення сітки
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")
df = pd.DataFrame({'time':index_range, 'speed': speed})
# Set the figure size (in inches)
plt.figure(figsize=(10, 6))
# Add grid to the plot
plt.grid(True)
# Set x and y axis limits
plt.xlim(0, 11)
plt.ylim(0, 130)
speed_list = sns.scatterplot(x="time", y="speed", data=df)
plt.show()
# Set the figure size (in inches)
plt.figure(figsize=(10, 6))
# Add grid to the plot
plt.grid(True)
# Set x and y axis limits
plt.xlim(0, 11)
plt.ylim(0, 130)
speed_list = sns.lineplot(x="time", y="speed", data=df)
plt.show()
# 4. Виконайте інтерполяцію за допомогою interp1d(kind='cubic') та отримайте функцію на 10000 значень. Побудуйте безперервний графік отриманої функції.

import numpy as np
from scipy.interpolate import interp1d

# Приклад даних (time і speed). Для цього прикладу використовуємо випадкові значення
# Якщо у вас вже є свої дані, використовуйте їх замість цього

# Створення функції для кубічної інтерполяції
interpolation_function = interp1d(index_range, speed, kind='cubic')

# Створення нових значень на 10000 точок для безперервного графіку
time_new = np.linspace(0, 11, 10000)  # 10000 точок між 0 і 10
speed_new = interpolation_function(time_new)  # Отримання інтерпольованих значень

# Побудова графіка
plt.figure(figsize=(10, 6))
plt.plot(time_new, speed_new, label='Cubic Interpolation', color='b')
plt.scatter(index_range, speed, color='r', label='Original Data')  # Показати оригінальні точки
plt.title('Cubic Interpolation')
plt.xlabel('Time')
plt.ylabel('Speed')
plt.grid(True)
plt.legend()
plt.show()

# Обчисліть інтеграл для отриманої інтерполяційної функції на проміжку [0, 11]
# Обчислення інтегралу на проміжку [0, 11]
from scipy.integrate import quad
result, error = quad(interpolation_function, 0, 11)
# Виведення результату
print(f"Інтеграл на проміжку [0, 11]: {result:.4f}")
print(f"Оцінка похибки: {error:.4f}")


# Створення функції для quadratic інтерполяції
interpolation_function = interp1d(index_range, speed, kind='quadratic')

# Створення нових значень на 10000 точок для безперервного графіку
time_new = np.linspace(0, 11, 10000)  # 10000 точок між 0 і 10
speed_new = interpolation_function(time_new)  # Отримання інтерпольованих значень

# Побудова графіка
plt.figure(figsize=(10, 6))
plt.plot(time_new, speed_new, label='Quadratic Interpolation', color='b')
plt.scatter(index_range, speed, color='r', label='Original Data')  # Показати оригінальні точки
plt.title('Quadratic Interpolation')
plt.xlabel('Time')
plt.ylabel('Speed')
plt.grid(True)
plt.legend()
plt.show()

# Обчисліть інтеграл для отриманої інтерполяційної функції на проміжку [0, 11]
# Обчислення інтегралу на проміжку [0, 11]
from scipy.integrate import quad
result, error = quad(interpolation_function, 0, 11)
# Виведення результату
print(f"Інтеграл на проміжку [0, 11]: {result:.4f}")
print(f"Оцінка похибки: {error:.4f}")

# Для прямокутної області площею 1000 м2, що примикає до прямої ділянки річки, необхідно побудувати огорожу (причому, зі сторони річки огорожу будувати не потрібно). За яких розмірів області a, b довжина огорожі буде мінімальною? Використовуйте функцію minimize з параметрами обмеженнями bounds і constraints

from scipy.optimize import minimize


# objective function: calculates the length of the fence without one side
def area(args):
    x, y = args
    return x + 2*y

# the area must be equal to 1000
constraints = ({'type': 'eq', 'fun': lambda args:  args[0] * args[1] - 1000})

xbounds = (0, 1000)
ybounds = (0, 1000)
bounds = (xbounds, ybounds)

result = minimize(area, [1, 999], bounds=bounds, constraints=constraints)
print("result", result)
# array([44.72136003, 22.36067954]) маю інший результат

# Нехай все населення (N індивідів) ділиться на три групи: індивіди, які сприйнятливі до цієї хвороби, але здорові (susceptible) S(t); заражені індивіди (infected) - I(t) (вони хворі самі і є носіями хвороби) і здорові індивіди, які мають імунітет до цієї хвороби (recovered) - R(t).

from scipy.optimize import leastsq, minimize, minimize_scalar
from scipy.integrate import solve_ivp
from scipy.interpolate import interp1d, interp2d, griddata
import numpy as np
import matplotlib.pyplot as plt

alpha = 0.5
beta = 0.3
N = 1000000

s0 = 990000
t0, tf = 0, 25

def dsdt(t, s):
    return -alpha * s
soln_s = solve_ivp(dsdt, (t0, tf), [s0], dense_output=True)
t_s, s = soln_s.t, soln_s.y[0]
s_func, = soln_s.sol(t_s)
plt.plot(t_s, s, 'o', color='k')
plt.plot(t_s, s_func, color='blue')
plt.show()

i0 =  7000

def didt(t, i):
    return alpha * soln_s.sol(t) - beta * i

soln_i = solve_ivp(didt, (t0, tf), [i0], dense_output=True)
t_i, i = soln_i.t, soln_i.y[0]
i_func, = soln_i.sol(t_i)
plt.plot(t_i, i, 'o', color='k')
plt.plot(t_i, i_func, color='blue')
plt.show()


def r(t):
    return N - soln_s.sol(t) - soln_i.sol(t)


r_timeline = np.linspace(t0, tf, tf)
r_array = np.array([r(t) for t in r_timeline]).flatten()
r_func = interp1d(r_timeline, r_array, kind='linear')
plt.plot(r_timeline, r_array, 'o', color='k')
plt.plot(r_timeline, r_func(r_timeline), color='blue')
plt.show()

plt.plot(t_s, s_func, color='blue')
plt.plot(t_i, i_func, color='red')
plt.plot(r_timeline, r_func(r_timeline), color='green')
plt.grid()
plt.show()


def S(t, s0, a):
    return s0 * np.exp(-a * t)

def diff_s(p, y, t):
    s0, a = p
    return y - S(t, s0, a)

p0 = (s0, 1)  # initial guess
aprx1, _ = leastsq(diff_s, p0, args=(s, t_s))

# array([9.89978640e+05, 4.99856001e-01])

s0 = aprx1[0]

def I(t, i0, a):
    return (i0 + a * s0 * t) * np.exp(-a * t)

def diff_i(p, y, t):
    i0, a = p
    return y - I(t, i0, a)

p0 = (1, 2)
aprx2, _ = leastsq(diff_i, p0, args=(i, t_i))
# array([4.20075795e+04, 3.43319240e-01])

new_s = aprx1[0] * np.exp(-aprx1[1]*t_s)
new_i = (aprx2[0] + aprx2[1] * s0 * t_i) * np.exp(-aprx2[1]*t_i)

plt.plot(t_s, new_s, color='blue')
plt.plot(t_i, new_i, color='red')
plt.plot(r_timeline, r_func(r_timeline), color='green')
plt.grid()
plt.show()

# find tmax (with I reaching its maximum)

i0 = aprx2[0]
a = aprx2[1]

# we use minus in fron of the function because we actually need to maximize the function
t_max = minimize_scalar(lambda r_timeline, i0, a: -I(r_timeline, i0, a), args=(i0, a)) 
# 2.789145111349731