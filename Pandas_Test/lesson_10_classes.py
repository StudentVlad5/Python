class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

point = Point(2, 3)
print(repr(point))  # Виводить: Point(x=2, y=3)

# ☝ Використання __repr__ дозволяє розробникам отримати детальне представлення об'єкта, яке може бути використане для точного відтворення об'єкта або для налагодження програми, допомагаючи ідентифікувати та виправляти помилки.

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

original_point = Point(2, 3)
print(repr(original_point))  

# Використання рядка, повернутого __repr__, для створення нового об'єкта
new_point = eval(repr(original_point))
print(new_point)

#Функція eval() використовується для виконання рядкового виразу як коду. Вона приймає рядок і виконує його як вираз Python, повертаючи результат виконання цього виразу. Коли метод __repr__ класу повертає рядок, його можна передати до eval(). Ідея полягає в тому, щоб виклик eval() з результатом __repr__ створив новий об'єкт, ідентичний оригіналу.
# ☝ Важливо пам'ятати про обережне використання eval(), оскільки виконання коду, отриманого з ненадійних джерел, може призвести до серйозних проблем з безпекою.

# Метод __str__ призначений для повернення рядкового представлення об'єкта, яке має бути читабельним і зрозумілим для людини. Коли ви викликаєте функцію str() для об'єкта або друкуєте об'єкт за допомогою print(), Python автоматично використовує метод __str__ вашого класу. Це дає вам, як розробнику, можливість визначити, як об'єкт має бути представлений у зрозумілій формі.

class Human:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Human named {self.name} who is {self.age} years old"
    
    def __repr__(self):
        return f"Human({self.name}, {self.age})"

human = Human("Alice", 30)
print(human)


class SimpleDict:
    def __init__(self):
        self.__data = {}

    def __getitem__(self, key):
        return self.__data.get(key, "Key not found")

    def __setitem__(self, key, value):
        self.__data[key] = value

# Використання класу
simple_dict = SimpleDict()
simple_dict['name'] = 'Boris'
print(simple_dict['name'])  
print(simple_dict['age']) 

# У прикладі, SimpleDict використовує внутрішній приватний словник __data для зберігання своїх елементів. Метод __getitem__ дозволяє отримати значення за ключем, а __setitem__ – встановити нове значення для ключа.

from collections import UserList

class BoundedList(UserList):
    def __init__(self, min_value: int, max_value: int, initial_list=None):
        super().__init__(initial_list if initial_list is not None else [])
        self.min_value = min_value
        self.max_value = max_value
        self.__validate_list()

    def __validate_list(self):
        for item in self.data:
            self.__validate_item(item)

    def __validate_item(self, item):
        if not (self.min_value <= item <= self.max_value):
            raise ValueError(f"Item {item} must be between {self.min_value} and {self.max_value}")

    def append(self, item):
        self.__validate_item(item)
        super().append(item)

    def insert(self, i, item):
        self.__validate_item(item)
        super().insert(i, item)

    def __setitem__(self, i, item):
        self.__validate_item(item)
        super().__setitem__(i, item)

    def __repr__(self):
        return f"BoundedList({self.max_value}, {self.min_value})"

    def __str__(self):
        return str(self.data)

if __name__ == '__main__':
    temperatures = BoundedList(18, 26, [19, 21, 22])
    print(temperatures)

    for el in [27, 22, 25, 20]:
        try:
            temperatures.append(el)
        except ValueError as e:
            print(e)

    print(temperatures)

class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real_part, imag_part)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

if __name__ == "__main__":
    num1 = ComplexNumber(1, 2)
    num2 = ComplexNumber(3, 4)
    print(f"Сума: {num1 + num2}")
    print(f"Різниця: {num1 - num2}")
    print(f"Добуток: {num1 * num2}")

# Ось деякі з найпоширеніших спеціальних методів для перевизначення математичних операторів:



# __add__(self, other) для оператора +
# __sub__(self, other) для оператора -
# __mul__(self, other) для оператора *
# __truediv__(self, other) для оператора /
# __floordiv__(self, other) для оператора цілочисельного ділення //
# __mod__(self, other) для оператора залишку від ділення %
# __pow__(self, other) для оператора * піднесення до степеня


#     Тому операції порівняння, як і інші оператори, мають свої "магічні" методи:

# __eq__(self, other) — визначає поведінку під час перевірки на відповідність (==).
# __ne__(self, other) — визначає поведінку під час перевірки на невідповідність. !=.
# __lt__(self, other) — визначає поведінку під час перевірки на менше <.
# __gt__(self, other) — визначає поведінку під час перевірки на більше >.
# __le__(self, other) — визначає поведінку під час перевірки на менше-дорівнює <=.
# __ge__(self, other) — визначає поведінку під час перевірки на більше-дорівнює >=.

'''
У мові програмування Python, поля - це змінні, які зберігають інформацію про стан об'єкта. Доступ до цих полів та їх модифікація зазвичай відбувається безпосередньо, але іноді необхідно контролювати цей процес, наприклад, для валідації даних або інкапсуляції. Для цього існують спеціальні методи які називають гетерами та сетерами. В Python застосовують декоратор @property, який дозволяє їх зручно створювати та використовувати.

Гетери (від англ. get - отримувати) - це методи, які дозволяють отримати значення поля. Вони використовуються, коли доступ до поля потребує якоїсь додаткової обробки або коли безпосередній доступ до поля не бажаний з міркувань інкапсуляції. Наприклад, якщо потрібно завжди повертати значення поля у вигляді рядка, навіть якщо воно зберігається як число.

Сетери (від англ. set - встановлювати) - це методи, які дозволяють встановити значення поля. Вони найчастіше використовуються для валідації даних, які намагаються присвоїти полю. Наприклад, якщо ми маємо поле, який повинно приймати значення лише додатні числа, можна в сетері додати перевірку, яка буде викидати виняток або повертати помилку, якщо намагатися присвоїти йому від'ємне число.
'''

class Person:
    def __init__(self, age):
        # Спочатку встановлюємо __age як None
        self.__age = None
    # Використовуємо сеттер для встановлення віку, що дозволяє валідацію вхідного значення
        self.age = age

    @property
    def age(self):
        return self.__age  # Геттер повертає значення приватного поля

    @age.setter
    def age(self, value):
        if value < 0:
            # Валідація вхідного значення
            raise ValueError("Вік не може бути від'ємним")  
        # Присвоєння валідного значення приватному полю
        self.__age = value  

if __name__ == "__main__":
    person = Person(10)
    print(person.age)
    # person.age = -5
    # person.age = '10'
    # print(person.age)

def my_generator():
    received = yield "Ready"
    yield f"Received: {received}"

gen = my_generator()
print(next(gen))  
print(gen.send("Hello"))  

def my_generator():
    try:
        yield "Working"
    except GeneratorExit:
        print("Generator is being closed")

gen = my_generator()
print(next(gen))  # Отримуємо "Working"
gen.close()  # Викликаємо закриття генератора

class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if (type(x) == int) or (type(x) == float):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if (type(y) == int) or (type(y) == float):
            self.__y = y

    def __str__(self):
        return f"Point({self.x},{self.y})"


class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates

    def __setitem__(self, index, value):
        if index == 0:
            self.coordinates.x = value
        if index == 1:
            self.coordinates.y = value

    def __getitem__(self, index):
        if index == 0:
            return self.coordinates.x
        if index == 1:
            return self.coordinates.y

    def __call__(self, value=None):
        if value:
            self.coordinates.x = self.coordinates.x * value
            self.coordinates.y = self.coordinates.y * value
        return self.coordinates.x, self.coordinates.y

    def __add__(self, vector):
        x = self.coordinates.x + vector.coordinates.x
        y = self.coordinates.y + vector.coordinates.y
        return Vector(Point(x, y))

    def __sub__(self, vector):
        x = self.coordinates.x - vector.coordinates.x
        y = self.coordinates.y - vector.coordinates.y
        return Vector(Point(x, y))

    def __mul__(self, vector):
        return (
                self.coordinates.x * vector.coordinates.x
                + self.coordinates.y * vector.coordinates.y
        )

    def len(self):
        return (self.coordinates.x ** 2 + self.coordinates.y ** 2) ** 0.5

    def __str__(self):
        return f"Vector({self.coordinates.x},{self.coordinates.y})"

    def __eq__(self, vector):
        return self.coordinates.x == vector.coordinates.x and self.coordinates.y == vector.coordinates.y

    def __ne__(self, vector):
        return self.coordinates.x != vector.coordinates.x or self.coordinates.y != vector.coordinates.y

    def __lt__(self, vector):
        return self.coordinates.x < vector.coordinates.x or self.coordinates.y < vector.coordinates.y

    def __gt__(self, vector):
        return self.coordinates.x > vector.coordinates.x and self.coordinates.y > vector.coordinates.y

    def __le__(self, vector):
        return self.coordinates.x <= vector.coordinates.x and self.coordinates.y <= vector.coordinates.y

    def __ge__(self, vector):
        return self.coordinates.x >= vector.coordinates.x and self.coordinates.y >= vector.coordinates.y
    

vector1 = Vector(Point(1, 10))
vector2 = Vector(Point(3, 10))

print(vector1 == vector2)  # False
print(vector1 != vector2)  # True
print(vector1 > vector2)  # False
print(vector1 < vector2)  # True
print(vector1 >= vector2)  # False
print(vector1 <= vector2)  # True


class Iterable:
    MAX_VALUE = 10

    def __init__(self):
        self.current_value = 0

    def __next__(self):
        if self.current_value < Iterable.MAX_VALUE:
            self.current_value += 1
            return self.current_value
        raise StopIteration


class CustomIterator:
    def __iter__(self):
        return Iterable()


c = CustomIterator()
for i in c:
    print(i)