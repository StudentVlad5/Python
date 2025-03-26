from typing import Callable

def add(a: int, b: int) -> int:
    return a + b

def multiply(a: int, b: int) -> int:
    return a * b

def apply_operation(a: int, b: int, operation: Callable[[int, int], int]) -> int:
    return operation(a, b)

# Використання
result_add = apply_operation(5, 3, add)
result_multiply = apply_operation(5, 3, multiply)

print(result_add, result_multiply)

# Callable[[int, int], int]. Це означає, що параметр operation це функція, яка приймає два цілі числа та повертає ціле число.

from typing import Callable, Dict

# Визначення функцій
def add(a: int, b: int) -> int:
    return a + b

def multiply(a: int, b: int) -> int:
    return a * b

def power(exponent: int) -> Callable[[int], int]:
    def inner(base: int) -> int:
        return base ** exponent
    return inner

# Використання power для створення функцій square та cube
square = power(2)
cube = power(3)

# Словник операцій
operations: Dict[str, Callable] = {
    'add': add,
    'multiply': multiply,
    'square': square,
    'cube': cube
}

# Використання операцій
result_add = operations['add'](10, 20)  # 30
result_square = operations['square'](5)  # 25

print(result_add)  
print(result_square)  

from typing import Callable

def counter() -> Callable[[], int]:
    count = 0

    def increment() -> int:
        # використовуємо nonlocal, щоб змінити змінну в замиканні
        nonlocal count  
        count += 1
        return count

    return increment

# Створення лічильника
count_calls = counter()

# Виклики лічильника
print(count_calls())  # Виведе 1
print(count_calls())  # Виведе 2
print(count_calls())  # Виведе 3

def apply_discount(price: float, discount_percentage: int) -> float:
    return price * (1 - discount_percentage / 100)

# Використання
discounted_price = apply_discount(500, 10)  # Знижка 10% на ціну 500
print(discounted_price)

discounted_price = apply_discount(500, 20)  # Знижка 20% на ціну 500
print(discounted_price)
# Перетворимо функцію apply_discount, використовуючи каррінг. Це дозволить нам створити "замовлені" функції для різних рівнів знижок, кожна з яких буде приймати тільки ціну товару.
from typing import Callable

def discount(discount_percentage: int) -> Callable[[float], float]:
    def apply_discount(price: float) -> float:
        return price * (1 - discount_percentage / 100)
    return apply_discount

# Каррінг в дії
ten_percent_discount = discount(10)
twenty_percent_discount = discount(20)

# Застосування знижок
discounted_price = ten_percent_discount(500)  # 450.0
print(discounted_price)

discounted_price = twenty_percent_discount(500)  # 400.0
print(discounted_price)

# Ми можемо піти далі та створити словник, де ключами будуть назви знижок, а значеннями — відповідні функції обчислення знижки, створені за допомогою каррінгу. Це дозволить нам легко вибирати потрібну функцію знижки зі словника.

from typing import Callable, Dict

def discount(discount_percentage: int) -> Callable[[float], float]:
    def apply_discount(price: float) -> float:
        return price * (1 - discount_percentage / 100)
    return apply_discount

# Створення словника з функціями знижок
discount_functions: Dict[str, Callable] = {
    "10%": discount(10),
    "20%": discount(20),
    "30%": discount(30)
}

# Використання функції зі словника
price = 500
discount_type = "20%"

discounted_price = discount_functions[discount_type](price)
print(f"Ціна зі знижкою {discount_type}: {discounted_price}")

# Декоратори
# Є такий шаблон проектування — декоратор. Цей шаблон полягає в тому, щоб розширювати функціонал який вже існує, не вносячи змін в код цього самого функціоналу.

def complicated(x: int, y: int) -> int:
    return x + y

def logger(func):
    def inner(x: int, y: int) -> int:
        print(f"Викликається функція: {func.__name__}: {x}, {y}")
        result = func(x, y)
        print(f"Функція {func.__name__} завершила виконання: {result}")
        return result

    return inner

complicated = logger(complicated)
print(complicated(2, 3))

# Щоб спростити застосування цього шаблону проектування, в Python є спеціальний синтаксис декоратора. Декоратори використовуються з синтаксисом @, що робить їх застосування простим та елегантним. Точно той самий код, який робить в точності те саме, можна записати у вигляді:

def logger(func):
    def inner(x: int, y: int) -> int:
        print(f"Викликається функція: {func.__name__}: {x}, {y}")
        result = func(x, y)
        print(f"Функція {func.__name__} завершила виконання: {result}")
        return result

    return inner

@logger
def complicated(x: int, y: int) -> int:
    return x + y

print(complicated(2, 3))

# Логування - запис інформації про виклики функцій для забезпечення прозорості та відстеження.
# Перевірка доступу - перевірка прав користувача перед виконанням функції, щоб контролювати доступ.
# Кешування - збереження результатів функції для підвищення ефективності та скорочення часу виконання.
# Перевірка аргументів - аналіз та модифікація аргументів перед їх передачею функції для забезпечення правильності виклику.

# Дуже важливо при створенні декораторів використовувати модуль functools, це необхідно для збереження метаданих оригінальної функції, яку ми декоруємо. Функція functools.wraps допомагає в цьому, зберігаючи інформацію про оригінальну функцію, як-от ім'я функції та документацію.

from functools import wraps

def logger(func):
    @wraps(func)
    def inner(x: int, y: int) -> int:
        print(f"Викликається функція: {func.__name__}: {x}, {y}")
        result = func(x, y)
        print(f"Функція {func.__name__} завершила виконання: {result}")
        return result

    return inner

@logger
def complicated(x: int, y: int) -> int:
    return x + y

print(complicated(2, 3))
print(complicated.__name__)

# Подібні операції, які ми робимо зі змінюваними колекціями списків list, словників dict та множин set у циклі for. Для спрощення таких операцій в Python ввели конструкції Comprehensions .

# List Comprehensions

# List comprehensions використовуються для створення нових списків та мають наступний синтаксис:

# [new_item for item in iterable if condition]
sq = [x**2 for x in range(1, 6)]
print(sq)

# Set Comprehensions

# Set comprehensions використовуються аналогічно list comprehensions, але для створення множин.

# {new_item for item in iterable if condition}

numbers = [1, 4, 1, 3, 2, 5, 2, 6]
sq = {i ** 2 for i in numbers}
print(sq)

odd_squares = {x**2 for x in range(1, 10) if x % 2 != 0}
print(odd_squares)

# Dictionary Comprehensions

# Dictionary comprehensions використовуються для створення нових словників. Для словників синтаксис comprehension трохи відрізняється, оскільки потрібно явно вказати ключ та значення

# {key: value for item in iterable if condition}

sq = {x: x**2 for x in range(1, 10)}
print(sq)

# lambda arguments: expression
add = lambda x, y: x + y
print(add(5, 3))  # Виведе 8
#Насправді це "поганий тон" зберігати лямбда-функції у змінних, вони повинні створюватися там, де будуть використовуватися і більше ніде у коді не залишають слідів.

# map(function, iterable, ...)
# function - функція, яку треба застосувати до кожного елемента в iterable.
# iterable - об'єкт ітерації (список, кортеж тощо), елементи якого будуть оброблятися function.

# Давайте напишемо за допомогою map генератор, який підносить числа із списку numbers до квадрату:
numbers = [1, 2, 3, 4, 5]

for i in map(lambda x: x ** 2, numbers):
    print(i)

nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
sum_nums = [x + y for x, y in zip(nums1, nums2)]
print(sum_nums)

ddd = '1'
print(bool(ddd)) 

# Загалом, використання функцій any(), all(), map(), filter() і технік comprehensions забезпечує більш чистий, лаконічний та ефективний код, особливо при роботі з даними та колекціями.

print(None == '') #False
print(None == 0) #False
print(bool(None)) #False
print(bool('')) #False
print(bool(0)) #False
print(False == False) #True