# Цей код визначає два символи x та y, які можна використовувати для створення математичних виразів. Тепер для створення математичного виразу достатньо використати символи та оператори:

import sympy as sp

x = sp.symbols('x')
y = sp.symbols('y')

expr1 = x + 2*y
expr2 = x**2 + 3*x + 2

expr3 = expr1 + expr2
expr4 = expr1 * expr2

print(expr3)
print(expr4)

simplified_expr = sp.simplify((x**2 + 2*x + 3)/x)
print(simplified_expr)
# x + 2 + 3/x

# Розширення виразів, таких як розкриття дужок, також є важливою функцією. Для цього використовується функція expand. Для розширення виразу потрібно викликати функцію expand:

expanded_expr = sp.expand(expr4)
print(expanded_expr)

# У цьому прикладі вираз expr4 , яка дорівнює (x + 2*y)*(x**2 + 3*x + 2) буде розширено до:

x**3 + 2*x**2*y + 3*x**2 + 6*x*y + 2*x + 4*y

# Для розв'язування лінійних рівнянь використовується функція solve:

import sympy as sp

x = sp.symbols('x')

equation = sp.Eq(2*x + 1, 0)
solution = sp.solve(equation, x)

print(solution)

# Точно так ми можемо розв'язати і квадратні рівняння.

equation = sp.Eq(x**2 + 5*x + 6, 0)
solution = sp.solve(equation, x)
print(solution)

# При розв'язанні рівнянь, які містить як алгебраїчні, так і трансцендентні функції, SymPy не завжди може знайти аналітичне рішення. У таких випадках ми можемо використати чисельні методи, такі як метод Ньютона, для знаходження коренів, це функція nsolve.

# Визначення рівняння
equation = sp.Eq(sp.sin(x) - x/2, 0)

# Використання nsolve для чисельного розв'язання
# Зазначимо початкове наближення (наприклад, x = 1)
solution = sp.nsolve(equation, x, 1)
print(solution)
# Щоб розв'язувати системи лінійних рівнянь функція solve використовується з
# декількома рівняннями та змінними.
x, y = sp.symbols('x y')
equation1 = sp.Eq(2*x + y, 1)
equation2 = sp.Eq(x - y, 2)
solution = sp.solve((equation1, equation2), (x, y))
print(solution)
# Для факторизації поліномів використовується функція factor:

polynomial = x**3 - 3*x**2 + 3*x - 1
factored = sp.factor(polynomial)
print(factored)

# Для розкладання полінома на множники використовується функція apart:
rational_expr = (x**2 + 2*x + 1) / (x**2 + x)
apart_expr = sp.apart(rational_expr)
print(apart_expr)
# Для знаходження коренів полінома використовується функція roots:
polynomial = x**3 - 6*x**2 + 11*x - 6
roots = sp.roots(polynomial, x)
print(roots)

# {3: 1, 2: 1, 1: 1}
# Це виведення мабуть потребує трошки пояснення. Результат означає, що поліном має три корені:

# x=3 з кратністю 1
# x=2 з кратністю 1
# x=1 з кратністю 1
# Кратність кореня означає, скільки разів цей корінь повторюється. В нашому випадку всі корені мають кратність 1, що означає, що кожен з них був знайдений лише один раз.

# Математичний аналіз
# Нагадаємо, що диференціювання – це процес знаходження похідної функції. Для знаходження похідної виразу використовується функція diff:
import sympy as sp
x = sp.symbols('x')
expr = x**3 + 2*x**2 + x
derivative = sp.diff(expr, x)
print(derivative)

# Для знаходження похідних вищого порядку необхідно додати відповідний аргумент до функції diff:

second_derivative = sp.diff(expr, x, 2)
print(second_derivative)
# 2*(3*x + 2)

# Інтегрування – це процес знаходження первісної функції. Для знаходження невизначеного інтегралу використовується функція integrate

import sympy as sp
x = sp.symbols('x')
expr = x**3 + 2*x**2 + x
integral = sp.integrate(expr, x)
print(integral)
# Результат:
x**4/4 + 2*x**3/3 + x**2/2

# Для знаходження визначеного інтегралу необхідно додати межі інтегрування:

defined_integral = sp.integrate(expr, (x, 0, 1))
print(defined_integral)
# 17/12
# Для знаходження границі функції використовується функція limit:
limit_expr = sp.limit(sp.sin(x)/x, x, 0)
print(limit_expr)