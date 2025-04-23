import matplotlib.pyplot as plt
import numpy as np


fig, ax = plt.subplots()


# Перемістимо лівий і нижній стовпчики до x = 0 і y = 0 відповідно
ax.spines[["left", "bottom"]].set_position(("data", 0))


# Сховаємо верхню та праву лінію
ax.spines[["top", "right"]].set_visible(False)


# Намалюємо стрілки (як чорні трикутники: ">k"/"^k") на кінцях осей
# Також вимкнемо відсікання (clip_on=False) стрілок
ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)


# Сформуємо ряд значень x. 100 елементів від -10 до 10
x = np.linspace(-10, 10., 100)


# Додамо проміжні лінії
ax.grid(True, linestyle='-.')


# Сформуємо функцію y = x**2+2
ax.plot(x, x**2+2)


# Запускаємо малювання графіка
plt.show()

import matplotlib.pyplot as plt
import numpy as np


fig, ax = plt.subplots()


# Перемістимо лівий і нижній стовпчики до x = 0 і y = 0 відповідно
ax.spines[["left", "bottom"]].set_position(("data", 0))


# Сховати верхню та праву лінію
ax.spines[["top", "right"]].set_visible(False)


# Намалюємо стрілки (як чорні трикутники: ">k"/"^k") на кінцях осей
# Також вимкнемо відсікання (clip_on=False) стрілок
ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)


# Додамо проміжні лінії
ax.grid(True, linestyle='-.')


# Сформуємо ряд значень x. 100 елементів від -5 до 5
x = np.linspace(-5, 5, 100, False)


# Задаємо 2 частини функціональної залежності
a = np.where(x>3, 2*x-1, np.nan)
b = np.where((x<=3), 4, np.nan)


# Генеруємо 2 графіки однакового кольору
ax.plot(x,a,color='blue')
ax.plot(x,b,color='blue')


# Запускаємо малювання графіка
plt.show()



import matplotlib.pyplot as plt
import numpy as np


fig, ax = plt.subplots()


# Перемістимо лівий і нижній стовпчики до x = 0 і y = 0 відповідно
ax.spines[["left", "bottom"]].set_position(("data", 0))


# Сховати верхню та праву лінію
ax.spines[["top", "right"]].set_visible(False)


# Намалюємо стрілки (як чорні трикутники: ">k"/"^k") на кінцях осей
# Також вимкнемо відсікання (clip_on=False) стрілок
ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)


# Додамо проміжні лінії
ax.grid(True, linestyle='-.')


# Сформуємо ряд значень x. 100 елементів від -5 до 5
x = np.linspace(-5, 5, 100, False)


# Функціональну залежність
ax.plot(x, -(2/3)*x-1/3)


# Запускаємо малювання графіка
plt.show()


# Practical task

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 1000)
fig, ax = plt.subplots()

# Перемістимо лівий і нижній стовпчики до x = 0 і y = 0 відповідно
ax.spines[["left", "bottom"]].set_position(("data", 0))


# Сховати верхню та праву лінію
ax.spines[["top", "right"]].set_visible(False)


# Намалюємо стрілки (як чорні трикутники: ">k"/"^k") на кінцях осей
# Також вимкнемо відсікання (clip_on=False) стрілок
ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)


# Додамо проміжні лінії
ax.grid(True, linestyle='-.')

# Створюємо лінії з label
lines = []
lines.append(ax.plot(x, 1/(x**2 + 2*x + 3), color="blue", label="1/(x² + 2x + 3)")[0])
lines.append(ax.plot(x, 1/(x**2 - 2*x + 3), color="red", label="1/(x² - 2x + 3)")[0])
lines.append(ax.plot(x, np.sin(np.floor(x)) + 2, color="green", label="sin(floor(x)) + 2")[0])
lines.append(ax.plot(x, np.sin(np.floor(x)) - 1, color="orange", label="sin(floor(x)) - 1")[0])
lines.append(ax.plot(x, (-x)**2, color="darkred", label="(-x)²")[0])
lines.append(ax.plot(x, np.sqrt(x + 1), color="cyan", label="√(x + 1)")[0])
lines.append(ax.plot(x, 6/(x - 3), color="purple", label="6 / (x - 3)")[0])

# Створюємо легенду
legend = ax.legend(loc="upper right", fancybox=True, shadow=True)
legend_lines = legend.get_lines()

# Встановлюємо легенді взаємозв’язок із лініями графіка
for leg_line, orig_line in zip(legend_lines, lines):
    leg_line.set_picker(5)  # Пікселі для клікабельності
    leg_line._associated_line = orig_line

# Подія кліку
def on_pick(event):
    leg_line = event.artist
    orig_line = leg_line._associated_line
    visible = not orig_line.get_visible()
    orig_line.set_visible(visible)
    leg_line.set_alpha(1.0 if visible else 0.2)
    fig.canvas.draw()

fig.canvas.mpl_connect("pick_event", on_pick)

plt.ylim(-10, 10)
plt.grid()
plt.show()


import numpy as np
import matplotlib.pyplot as plt

# Приклад 1: Квадратична функція
def quadratic_function(x):
    return x**2

# Приклад 2: Косинус
def cosine_function(x):
    return np.cos(x)

# Приклад 3: Модуль x
def absolute_value_function(x):
    return np.abs(x)

# Значення x для побудови графіку
x_values = np.linspace(-5, 5, 100)

# Графіки парних функцій
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.plot(x_values, quadratic_function(x_values), label=r'$f(x) = x^2$')
plt.plot(x_values, quadratic_function(-x_values), linestyle='--', label=r'$f(-x) = x^2$')
plt.title('Квадратична функція')
plt.legend()

plt.subplot(1, 3, 2)
plt.plot(x_values, cosine_function(x_values), label=r'$f(x) = \cos(x)$')
plt.plot(x_values, cosine_function(-x_values), linestyle='--', label=r'$f(-x) = \cos(x)$')
plt.title('Косинус')
plt.legend()

plt.subplot(1, 3, 3)
plt.plot(x_values, absolute_value_function(x_values), label=r'$f(x) = |x|$')
plt.plot(x_values, absolute_value_function(-x_values), linestyle='--', label=r'$f(-x) = |x|$')
plt.title('Модуль x')
plt.legend()

plt.tight_layout()
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Функція для побудови графіка періодичної функції
def plot_periodic_function(func, period, title):
    x_values = np.linspace(0, 3 * period, 1000)
    y_values = func(x_values)

    plt.plot(x_values, y_values)
    plt.title(title)
    plt.legend()

# Приклад 1: Синус
plt.subplot(2, 2, 1)
plot_periodic_function(np.sin, 2 * np.pi, 'Синус')

# Приклад 2: Косинус
plt.subplot(2, 2, 2)
plot_periodic_function(np.cos, 2 * np.pi, 'Косинус')

# Приклад 3: Тангенс
plt.subplot(2, 2, 3)
plot_periodic_function(np.tan, np.pi, 'Тангенс')

plt.tight_layout()
plt.show()



import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 100, 1)
y = (4*x**3+2 * x**2 + x - 2) / (2 * x**3 + 6 * x ** 2 - 3*x)

fig, ax = plt.subplots()
ax.plot(x,y)

ax.set(xlabel='x', ylabel='y',
       title='xy Graph')
ax.grid()
# bx.grid()

fig.savefig("test.png")
plt.show()

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-0.1, 0.1, 1000)
x = x[x != 0]  # уникаємо ділення на 0

y =  (x - 3 * x**2)/np.sin(x)

plt.plot(x, y, label=r'$\frac{\sin x}{x - 3x^2}$')
plt.axhline(1, color='green', linestyle='--', label='Границя = 1')
plt.axvline(0, color='gray', linestyle='--')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Границя при x → 0")
plt.grid()
plt.legend()
plt.show()