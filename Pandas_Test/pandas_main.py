import pandas as pd
pd.options.plotting.backend = "matplotlib"


mountains_height = pd.Series([2061, 2035.8, 2028.5, 2022.5, 2016.4])

print(mountains_height)

# Об'єкту Series можна присвоїти рядок імені name і тип даних dtype. У прикладі вище індекс не був явно встановлений, і тоді для індексування за замовчуванням використовується послідовність цілих чисел (починаючи з 0). Ми можемо вказати явну індексацію елементів, передаючи послідовність як аргумент index, або коли створюємо об'єкт Series зі словника.

mountains_height = pd.Series(
    data=[2061, 2035.8, 2028.5, 2022.5, 2016.4],
    index=["Goverla", "Brebenskyl", "Pip_Ivan", "Petros", "Gutin_Tomnatik"],
    name="Height, m",
    dtype=float,
)

print(mountains_height)
# Вирізання елементів у стилі Python теж працює. Існує можливість навіть використання нотації, схожої на стиль вирізання, але в цьому випадку зазначений кінцевий елемент включається в групу, що вирізається:

print(mountains_height[1:3])
print(mountains_height["Brebenskyl":"Petros"])

# Можливе виконання числових операцій з даними Series з використанням векторизації, як і для масивів NumPy.

print(mountains_height > 2030)
print(mountains_height[mountains_height > 2030])
# Виведення:

# Goverla            True
# Brebenskyl         True
# Pip_Ivan          False
# Petros            False
# Gutin_Tomnatik    False
# Name: Height, m, dtype: bool

# Goverla       2061.0
# Brebenskyl    2035.8
# Name: Height, m, dtype: float64

# Операції перевірки на існування елемента в Series використовують індекс, а не значення:
print("Goverla" in mountains_height) # True

# Сортування виконується за індексом або за значеннями, дивлячись, що необхідно для конкретного випадку. Використовуються методи Series.sort_index та Series.sort_values відповідно. Методи за замовчуванням повертають новий об'єкт Series, але за допомогою аргументу inplace=True можна оновити вихідний об'єкт. Аргумент ascending визначає порядок сортування за замовчуванням, містить значення True
sort_index = mountains_height.sort_index()
print(sort_index)
mountains_height.sort_values(inplace=True, ascending=False)
print(mountains_height)

# Елементи NaN (не число) в об'єкті Series можна замінити на задане значення, використовуючи метод fillna:
mountains_height.fillna(0, inplace=True)
# Goverla           2061.0
# Brebenskyl        2035.8
# Pip_Ivan          2028.5
# Petros               0.0
# Gutin_Tomnatik       0.0
# Name: Height, m, dtype: float64

# Метод apply дозволяє застосовувати користувацьку функцію до кожного елемента Series.
def square(x):
    return x**2

squared_height = mountains_height.apply(square)
print(squared_height)
# Також Pandas пропонує простий спосіб візуалізації даних в Series.
mountains_height.plot(kind='bar')

# Останнім розглянемо метод concat який дозволяє з'єднувати два або більше об'єктів Series в один.

other_mountains = pd.Series([2001.1, 1998.4], index=['Rebra', 'Menchul'])
all_mountains = pd.concat([mountains_height, other_mountains])
print(all_mountains)

# Створення DataFrame можливо зі списків:
data = [[1, 'Alice'], [2, 'Bob']]
df = pd.DataFrame(data, columns=['ID', 'Name'])
print('DataFrame зі списків:', df)
# Зі словників:
data = {'ID': [1, 2], 'Name': ['Alice', 'Bob']}
df = pd.DataFrame(data)
print('DataFrame зі словників:', df)
# З NumPy масивів:
import numpy as np
data = np.array([[1, 'Alice'], [2, 'Bob']])
df = pd.DataFrame(data, columns=['ID', 'Name'])
print('DataFrame з NumPy масивів:', df)
# Об'єкт DataFrame має наступні властивості:

# shape - повертає розмір DataFrame (кількість рядків, кількість стовпців).
# columns - повертає назви стовпців.
# index - повертає індекси рядків.
# dtypes - повертає типи даних кожного стовпця.

# Операція	Синтаксис	Результат, що повертається
# Вибір стовпця	df[col]	Series.
# Вибір рядка за міткою	df.loc[label]	Series
# Вибір рядка за індексом	df.iloc[loc]	Series
# Зріз за рядками	df[0:3]	DataFrame
# Вибір рядків, які відповідають умовій	df[bool_vec]	DataFrame

contacts = pd.DataFrame(
    {
        "name": [
            "Allen Raymond",
            "Chaim Lewis",
            "Kennedy Lane",
            "Wylie Pope",
            "Cyrus Jackson",
        ],
        "email": [
            "nulla.ante@vestibul.co.uk",
            "dui.in@egetlacus.ca",
            "mattis.Cras@nonenimMauris.net",
            "est@utquamvel.net",
            "nibh@semsempererat.com",
        ],
        "phone": [
            "(992) 914-3792",
            "(294) 840-6685",
            "(542) 451-7038",
            "(692) 802-2949",
            "(501) 472-5218",
        ],
        "favorite": [False, False, True, False, True],
    },
    index=[1, 2, 3, 4, 5],
)

print(contacts)

print(contacts["name"]) # Вибір стовпця
print(contacts.loc[1]) # Виведення рядка за міткою
print(contacts.iloc[1])  # Виведення рядка за індексом
print(contacts[contacts["favorite"]]) # Вибір рядків, які відповідають умовій
contacts.set_index('name', inplace=True) # Встановлення індексу
print(contacts)

df.rename(columns={'name': 'Full Name'}, inplace=True) # Перейменування стовпця

# Використання inplace=True може зробити ваш код трохи швидшим та ефективнішим з точки зору використання пам'яті, оскільки воно змінює дані "на місці" без створення нового об'єкта. Однак це також означає, що ви можете втратити початковий об'єкт, тому будьте обережні при використанні цього параметра, особливо якщо вам потрібно зберегти оригінальний стан даних.

# Ми можемо скинути індекс назад:
contacts.reset_index(inplace=True)
print(contacts)

# Ми можемо як для прикладу змінити тип стовпця "favorite" на int64:
contacts['favorite'] = contacts['favorite'].astype('int64')
print(contacts.dtypes)
# Ми можемо перейменувати стовпці:
contacts.rename(columns={'name': 'Full Name', 'email': 'Email Address'}, inplace=True)
print(contacts)

# Метод fillna використовується для заміни відсутніх значень на конкретне значення або за допомогою визначеного методу (наприклад, вперед чи назад заповнення даними).

# Заміна всіх NaN на конкретне значення
df.fillna(0, inplace=True) # Замінює всі NaN на 0

df.fillna(method='ffill', inplace=True) # Заповнює NaN попереднім значенням у рядку
df.fillna(method='bfill', inplace=True) # Заповнює NaN наступним значенням у рядку
df = pd.DataFrame({
    'A': [1, np.nan, 3],
    'B': [np.nan, 5, np.nan]
})

# Застосування методу 'ffill'
df_ffill = df.fillna(method='ffill')

# Застосування методу 'bfill'
df_bfill = df.fillna(method='bfill')

print("Using ffill:")
print(df_ffill)

print("\\nUsing bfill:")
print(df_bfill)

# Видалення рядків з будь-яким NaN
df.dropna(inplace=True) # Видаляє всі рядки, які містять хоча б один NaN
df.dropna(axis=1, inplace=True) # Видаляє всі стовпці, які містять хоча б один NaN
# Видалення рядків, де NaN в конкретному стовпці
# df.dropna(subset=['column_name'], inplace=True)
 # Видаляє рядки, де NaN в стовпці 'column_name'

# Для читання текстових файлів з даними у форматі CSV в об'єкті DataFrame існує метод read_csv. Метод приймає велику кількість можливих аргументів, але ми розберемо тільки основні, які стануть у пригоді нам у роботі:

# filepath_or_buffer— шлях до зчитуваного файлу. Є обов'язковим параметром. Шлях може вказувати як локальний файл, так і URL для завантажування даних з мережі;
# sep— роздільник стовпців. За замовчуванням кома ,, але можна використовувати значення:
# /s+ для стовпців, розділених пробільними символами,
# \\t для роздільників-табуляцій
# None, щоб бібліотека pandas сама спробувала логічно визначити символ-роздільник.
# delimiter— псевдонім для аргументу sep;
# header— номери рядків (індекси), які використовуються для імен стовпців. За замовчуванням header=0, що говорить про використання першого рядка для імен стовпців. Іноді у файлі немає заголовка, тоді потрібно присвоїти значення header=None і визначити імена стовпців в аргументі names;
# names— послідовність неповторюваних імен стовпців, які використовуватимуться під час читання файлу;
# nrows — кількість рядків, які зчитуються з файлу. Буває необхідно під час читання декількох рядків з дуже великого файлу для тестування або дослідження даних, що містяться в ньому;
# comment — визначає символ, наприклад #, який при виявленні на початку рядка повідомляє про те, що весь рядок необхідно пропустити;
# skip_blank_lines — за замовчуванням встановлено значення True– пропуск порожніх рядків у вхідному файлі. При встановленні значення False порожні рядки інтерпретуються як рядки із значень NaN;
# delim_whitespace — можна встановити для цього аргументу значення True, замість визначення аргументу sep='\\s+', щоб встановити, що стовпці даних розділяються символами пробілів.

# Щоб записати дані у файл CSV — необхідно використовувати метод об'єкта DataFrame to_csv, який зберігає дані відповідно до значень параметрів:

# path_or_buf— ім'я файлу;
# sep — символ роздільник полів (за замовчуванням кома ',');
# na_rep — рядок для заміни відсутніх даних (за замовчуванням порожній рядок);
# columns — послідовність, що ідентифікує виведені стовпці;
# header — за замовчуванням значення True, що означає, що імена стовпців повинні виводитися. Можна встановити значення False або список імен стовпців;
# index — за замовчуванням значення True, що означає, що індекси повинні зберігатись;

# Бібліотека pandas має можливість зчитувати вміст файлів Excel з розширеннями .xls та .xlsx в об'єкт DataFrame за допомогою методу pd.read_excel.

# Щоб зберегти вміст об'єкта DataFrame у файл Excel на одному листі необхідно скористатися методом to_excel:
#  ℹ️ Примітка: можливо буде необхідно встановити додаткові пакети як openpyxl або xlrd для роботи з файлами Excel.


# Для читання даних у форматі JSON використовується метод read_json.

# Параметри методу, що найчастіше використовуються:

# path_or_buf — шлях до файлу на диску, URL або JSON рядок, вміст якого - коректний JSON.
# orient — орієнтація, значення за замовчуванням None
# typ — Тип структури pandas: 'series' - це Series, 'frame' - DataFrame. За замовчуванням значення frame
orient = 'split'
# employees = pd.read_json("./json/split.json", orient="split")
# records = pd.read_json("./json/records.json", orient="records")
# index = pd.read_json("./json/index.json", orient="index")
# columns = pd.read_json("./json/columns.json", orient="columns")
# values = pd.read_json("./json/values.json", orient="values")

# Але необхідно знати, що залежно від значення typ, ми можемо використовувати певні значення orient. Якщо typ='series', то orient може бути split, records або index, якщо typ='frame', то orient розширює свої значення до списку: split, records, index, columns, values.

# При записі даних у форматі JSON необхідна зворотна операція перетворення даних. Для цього використовується метод to_json

# employees.to_json("employees.json", orient="split")

# практичне завдання

students_data = {
    'Імена': ['Anna', 'Bohdan', 'Olena', 'Ivan', 'Maria', 'Petro', 'Sophia', 'Max', 'Natalia', 'Vadym'],
    'Вік': [21, 22, 20, 19, 23, 22, 21, 20, 19, 21],
    'Спеціальність': ['Math', 'Physics', 'Biology', 'Chemistry', 'Math', 'Physics', 'Biology', 'Chemistry', 'Math', 'Physics']
}

students_df = pd.DataFrame(students_data)
print(students_df)

# Знаходимо всіх студентів, вік яких понад 20 років
older_students = students_df[students_df['Вік'] > 20]
print(older_students)

# Зберігаємо оброблені дані в новий CSV-файл.
students_df.to_csv('students.csv', index=False)

# Зчитуємо дані з CSV-файлу та виводимо перші 5 рядків. Метод head в Pandas використовується для отримання перших n рядків DataFrame або Series. Це корисно, коли вам потрібно швидко переглянути початок великого набору даних без необхідності завантажувати весь набір даних у пам'ять. Синтаксис DataFrame.head(n=5), де n це кількість рядків для виведення. За замовчуванням n=5.

file_path = 'students.csv'
data_df = pd.read_csv(file_path)
print(data_df.head())

# Виведення розміру DataFrame
print("Shape of the DataFrame:", data_df.shape)# Shape of the DataFrame: (10, 3)

# Отримаємо опис статистичних характеристик за допомогою методу describe. Метод describe дуже корисний для швидкого огляду ключових статистичних характеристик вашого набору даних, що може допомогти вам зрозуміти розподіл та тенденції в ваших даних.
print("describe method:",data_df.describe())

# count — кількість ненульових значень
# mean — середнє значення
# std — стандартне відхилення
# min — мінімальне значення
# 25%, 50%, 75% — перший, другий (медіана) та третій квартилі
# max — максимальне значення

data_df.describe(percentiles=None, include=None, exclude=None)

# percentiles — список значень в діапазоні від 0 до 1 для визначення квартилів. За замовчуванням використовуються квартилі [.25, .5, .75]
# include — типи даних, які слід включити в опис. Можна вказати 'all' для включення всіх стовпців
# exclude — типи даних, які слід виключити з опису. Можна вказати 'all' для виключення всіх стовпців

data_df.info()


# data_df.info(verbose=None, buf=None, max_cols=None, memory_usage=None,null_counts=None)

# verbose, якщо False, виводиться лише коротка інформація. Якщо True, виводиться повна інформація. За замовчуванням виводиться повна інформація, коли DataFrame має менше ніж 100 стовпців. Це наш випадок
# buf, де виводити інформацію. За замовчуванням виводиться в системний вивід
# max_cols це максимальна кількість стовпців, для яких виводиться інформація. При перевищенні цього числа виводиться коротка інформація
# memory_usage, якщо True, виводиться використана пам'ять. Якщо 'deep', обчислюється точна величина використаної пам'яті
# null_counts, якщо True, виводиться кількість ненульових значень

# Та нарешті побудуємо гістограму для вікової групи студентів.
import matplotlib.pyplot as plt
data_df['Вік'].plot(kind='hist', title='Вікова група студентів', color='green', edgecolor='black')
plt.show()

# Значення параметру	Опис
# bar (barh)	Побудова стовпчикової діаграми
# hist	Побудова гістограм
# box	Коробчаста діаграма
# kde	Побудова графіка щільності 
# area	Діаграма зі сферами 
# scatter	Точковий графік
# hexbin	Візуалізація даних із використанням шестикутників
# pie	Кругова діаграма

students_df = pd.DataFrame({
    'Імена': ['Anna', 'Bohdan', 'Olena', 'Ivan', 'Kateryna'],
    'Вік': [21, 22, 20, 21, 23],
    'Спеціальність': ['Math', 'Physics', 'Biology', 'Math', 'Physics']
    }, index=['st1', 'st2', 'st3', 'st4', 'st5'])

# Виконаємо вибірку конкретного рядка та стовпця за мітками, фактично знайдемо комірку віку студента st2
value = students_df.loc['st2', 'Вік']
print(value) # 22
# Вибірка зрізу рядків та стовпців за мітками можна виконати наступним чином:
subset = students_df.loc['st2':'st4', 'Імена':'Вік']
print(subset) 
#       Імена  Вік
# st2  Bohdan   22
# st3   Olena   20
# st4    Ivan   21
# Якщо ми хочемо вибірку за декількома конкретними мітками:

subset = students_df.loc[['st1', 'st3'], ['Імена', 'Спеціальність']]
print(subset)
# Виведення:
#      Імена Спеціальність
# st1   Anna          Math
# st3  Olena       Biology

# Метод iloc використовується для вибірки даних за числовими індексами, та має наступний синтаксис:
# DataFrame.iloc[rows, columns]
# Виконаємо такі самі вибірки, але тепер за допомогою методу iloc. Вибірка конкретного рядка та стовпця за індексами

value = students_df.iloc[1, 1]
print(value) # 22
# Вибірка зрізу рядків та стовпців за індексами. Зверніть увагу на відповідність, що зрізи 1:4 відповідають 'st2':'st4', а 0:2 відповідають 'Імена':'Вік' зрізам методу loc

subset = students_df.iloc[1:4, 0:2]
print(subset)
# Вибірка за декількома конкретними індексами
subset = students_df.iloc[[0, 2], [0, 2]]
print(subset)

# Перше, loc працює за мітками, iloc працює за числовими індексами. 
# Друге, loc включає останній елемент в зрізі, а iloc ні.
# Третє, loc може приймати булеві умови, тоді як iloc працює лише з цілими числами.

# Ви можете використовувати зрізи для вибору діапазону рядків. Синтаксис виглядає так:
# subset = df[start:end]

subset = students_df[1:3]
print(subset)
#       Імена  Вік Спеціальність
# st2  Bohdan   22       Physics
# st3   Olena   20       Biology

# Вибірка всіх рядків, починаючи з індексу 3
subset = students_df[3:]
print(subset)
# Вибірка перших 2 рядків
subset = students_df[:2]
print(subset)

# Slicing в Pandas може бути менш зрозумілим інтуїтивно для стовпців, оскільки зазвичай зрізи застосовуються до рядків. Для стовпців краще використовувати loc або iloc.

# Вибірка стовпців між 'Імена' та 'Вік' (включно)
subset = students_df.loc[:, 'Імена':'Вік']
print(subset)

# Групування даних є однією з найважливіших операцій при аналізі даних. В Pandas для цього використовується метод groupby, який дозволяє групувати дані за однією або декількома колонками та застосовувати функції агрегації до кожної групи окремо.

# grouped = DataFrame.groupby(by, axis=0, level=None, as_index=True, sort=True, group_keys=True, squeeze=False, observed=False)

# Метод groupby надзвичайно потужний та гнучкий завдяки параметрам, які дозволяють виконувати складні операції групування з різними варіантами налаштування.

# Параметри:

# by — ключ, за яким відбувається групування. Може бути ім'ям стовпця, списком імен, функцією або рівнями індексу
# axis — вісь, за якою відбувається групування. За замовчуванням дорівнює 0 для групування за рядками, та 1 для групування за стовпцями
# level — якщо об'єкт має ієрархічний (багаторівневий) індекс, цей параметр вказує рівень, за яким потрібно згрупувати
# as_index — якщо True, то мітки груп будуть індексами у вихідному об'єкті. Якщо False, то мітки груп будуть стовпцями. За замовчуванням True
# sort — якщо True, то дані будуть відсортовані за мітками груп. Якщо False, то сортування не відбувається, і дані можуть бути швидшими. За замовчуванням True
# group_keys — якщо True, то мітки груп будуть додані до індексу для збереження інформації про групу. Якщо False, то мітки групи не будуть додані. За замовчуванням True
# squeeze — якщо True, то зменшує розмір вихідного об'єкта, якщо можливо. За замовчуванням False
# observed — цей параметр використовується, коли групуємо за категоріальними змінними. Якщо False, то пусті категорії будуть включені. Якщо True, то пусті категорії будуть виключені. За замовчуванням False

students_data = {
    'Імена': ['Anna', 'Bohdan', 'Olena', 'Ivan', 'Kateryna'],
    'Вік': [21, 22, 20, 21, 23],
    'Спеціальність': ['Math', 'Physics', 'Biology', 'Math', 'Physics']
}

students_df = pd.DataFrame(students_data)
print("students_df", students_df)
grouped = students_df.groupby('Спеціальність')
print("grouped", grouped)
mean_age = grouped['Вік'].mean()
print("mean_age", mean_age)

# Метод agg (або aggregate) використовується з об'єктом groupby для застосування однієї або декількох функцій агрегації до одного або декількох стовпців у кожній групі. Це надає можливість виконувати різні операції агрегації одночасно та отримувати згрупований результат.

# grouped.agg(func=None, *args, **kwargs)
# Де, func функція, список функцій, словник або лямбда-функція, яку потрібно застосувати до кожної групи.

# Ось деякі з типових функцій агрегації:
# 'sum' - сума значень
# 'mean' - середнє значення
# 'max' - максимальне значення
# 'min' - мінімальне значення
# 'count' - кількість непустих значень
# 'std' - стандартне відхилення

min_max_age = grouped['Вік'].agg(['min', 'max'])
print("min_max_age", min_max_age)

summary = grouped.agg({
  'Вік': ['min', 'max', 'mean'],
  'Імена': 'count'
})
print("summary", summary)

# Також можна використовувати власні функції або лямбда-функції. Використаємо лямбда-функцію для обчислення різниці між максимальним та мінімальним віком студентів в кожній спеціальності

result = grouped['Вік'].agg(lambda x: x.max() - x.min())
print(result)

# Використання функцій агрегації
total_age = students_df['Вік'].sum() # 107
average_age = students_df['Вік'].mean() # 21.4
median_age = students_df['Вік'].median() # 21.0
min_age = students_df['Вік'].min() # 20
max_age = students_df['Вік'].max() # 23
std_age = students_df['Вік'].std() # 1.1401754250991378
variance_age = students_df['Вік'].var() # 1.2999999999999998 - дисперсія
# Диспе́рсія — це міра розсіяння значень випадкової величини відносно середнього значення розподілу.
count_age = students_df['Вік'].count() # 5
# Метод count знаходить кількість непустих значень.
# Кількість унікальних значень знаходить метод nunique()
unique_specialties = students_df['Спеціальність'].nunique() # 3
# Метод quantile(q) знаходить квантиль з заданим значенням q.
first_quartile_age = students_df['Вік'].quantile(0.25) # 21.0
# Квантиль - это, условно, перцентиль без процентов
# Метод idxmax() знаходить індекс максимального значення.
idx_max_age = students_df['Вік'].idxmax() # 4
# 
idx_min_age = students_df['Вік'].idxmin() # 2
# Метод prod() знаходить добуток всіх значень.
product_age = students_df['Вік'].prod() # 4462920
# Стандартна помилка середнього метод sem(). Обчислюємо стандартну помилку середнього віку студентів.
sem_age = students_df['Вік'].sem() # 0.5099019513592784

# Метод sort_values у Pandas використовується для сортування DataFrame або Series за значеннями в одному або декількох стовпцях. Він надає гнучке сортування за різними критеріями та в різних напрямках.
# DataFrame.sort_values(by, axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last')

# by — ім'я або список імен стовпців, за якими потрібно відсортувати
# axis — 0 для сортування за рядками, 1 для сортування за стовпцями
# ascending — True для сортування за зростанням, False для сортування за спаданням. Може бути списком для кожного стовпця у by
# inplace — True для сортування DataFrame на місці, False для повернення нового об'єкта
# kind — алгоритм сортування 'quicksort', 'mergesort', 'heapsort'. За замовчуванням Pandas використовує 'quicksort', який є досить ефективним для більшості випадків.
# na_position — позиція NaN у сортуванні 'last' або 'first'

# Сортування за віком за зростанням:
sorted_df = students_df.sort_values(by='Вік')
print(sorted_df)
# Сортування за спеціальністю за спаданням:
sorted_df = students_df.sort_values(by='Спеціальність', ascending=False)
print(sorted_df)
# Сортування за декількома стовпцями:
sorted_df = students_df.sort_values(by=['Спеціальність', 'Вік'], ascending=[True, False])
print(sorted_df)


# Метод dropna видаляє рядки або стовпці з відсутніми даними.
# DataFrame.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
# axis — 0 для видалення рядків, 1 для видалення стовпців
# how — 'any' видаляє рядки/стовпці, якщо є хоч одне відсутнє значення; 'all' видаляє, якщо всі значення відсутні
# thresh — мінімальна кількість непорожніх значень для збереження рядка/стовпця
# subset — список стовпців, що розглядаються при видаленні рядків
# inplace — змінює дані без створення нового об'єкта

students_data = {
    'Імена': ['Anna', 'Bohdan', None],
    'Вік': [21, None, 20],
    'Спеціальність': ['Math', 'Physics', 'Biology']
}

students_df = pd.DataFrame(students_data)

cleaned_df = students_df.dropna()
print(cleaned_df)
#    Імена  Вік           Спеціальність
# 0  Anna   21.0          Math

# Метода fillna заповнює відсутні дані вказаним значенням або методом.
# DataFrame.fillna(value=None, method=None, axis=None, inplace=False, limit=None)
# value — значення або словник значень для заповнення
# method — метод заповнення ('ffill', 'bfill')
# axis — ось, по якій відбувається заповнення
# inplace — відбувається зміна на місці чи ні
# limit — максимальна кількість послідовних відсутніх значень для заповнення

data = pd.DataFrame([[1, 2, 3], [4, np.nan, 6], [7, np.nan, np.nan]])

data = data.fillna({0: data[0].mean(), 1: data[1].mean(), 2: data[2].mean()})

print(data)
#    0    1    2
# 0  1  2.0  3.0
# 1  4  2.0  6.0
# 2  7  2.0  4.5
# Метод drop використовується для видалення конкретних рядків або стовпців з DataFrame.
# DataFrame.drop(labels=None, axis=0, index=None, columns=None, level=None, inplace=False, errors='raise')
# labels — мітки рядків або стовпців для видалення
# axis — визначає, чи будуть видалені рядки (axis=0) чи стовпці (axis=1)
# index — альтернативний спосіб вказувати рядки для видалення
# columns — альтернативний спосіб вказувати стовпці для видалення
# level — для видалення за конкретним рівнем у випадку MultiIndex
# inplace — якщо True, зміни застосовуються безпосередньо до об'єкта
# errors — якщо 'raise', буде викинуте виключення, якщо деякі мітки не знайдені. Якщо 'ignore', відсутні мітки будуть проігноровані.

students_data = {
    'Імена': ['Anna', 'Bohdan', 'Olena'],
    'Вік': [21, 22, 20],
    'Спеціальність': ['Math', 'Physics', 'Biology']
}

students_df = pd.DataFrame(students_data)

students_df.drop([1], inplace=True)
print(students_df)

# Щоб видаляти стовпці, необхідно вказати вісь через параметр axis. За замовчуванням axis=0, що означає роботу з рядками. Якщо вказати axis=1, то це дозволить видаляти стовпці:
students_data = {
    'Імена': ['Anna', 'Bohdan', 'Olena'],
    'Вік': [21, 22, 20],
    'Спеціальність': ['Math', 'Physics', 'Biology']
}
students_df = pd.DataFrame(students_data)
students_df = students_df.drop(['Вік'], axis=1)
print(students_df)


# Необхідно виконати конвертація віку в цілочисельний тип
students_data = {
  'Імена': ['Anna', 'Bohdan', 'Olena'],
  'Вік': [21.0, 22.0, 20.0],# Вік як float
  'Спеціальність': ['Math', 'Physics', 'Biology']
}
students_df = pd.DataFrame(students_data)
# Конвертація типу стовпця 'Вік' в int
students_df['Вік'] = students_df['Вік'].astype(int)
print(students_df.dtypes)
# Ми можемо вирівняти всі спеціальності до нижнього регістру для забезпечення узгодженості даних.

students_data = {
    'Імена': ['Anna', 'Bohdan', 'Olena'],
    'Вік': [21, 22, 20],
    'Спеціальність': ['Math', 'PHYSICS', 'biology']
}

students_df = pd.DataFrame(students_data)

# Приведення спеціальностей до нижнього регістру
students_df['Спеціальність'] = students_df['Спеціальність'].str.lower()
print(students_df)

# Середні температури за дні місяця
temperature_data = {
    'День': list(range(1, 31)),
    'Температура': [15, 18, None, 20, 17, 18, 20, None, 14, 16, 18, 19, None, 15, 14, 17, 16, None, 17, 20, 15, 16, 15, 19, 20, None, 15, 18, 17, 16]
}

temperature_df = pd.DataFrame(temperature_data)

# Знаходження середньої температури за місяць, виключаючи відсутні значення
mean_temperature = temperature_df['Температура'].mean()

# Заміна відсутніх значень температури середньою температурою за місяць
temperature_df['Температура'].fillna(mean_temperature, inplace=True)
print(temperature_df)

# Дублікати можуть спотворювати результати аналізу. Для видалення дублюючих даних можна використовувати метод drop_duplicates
# DataFrame.drop_duplicates(subset=None, keep='first', inplace=False)
# subset: Стовпці для врахування.
# keep: Який з дублікатів зберігти ('first', 'last', False).
# inplace: Змінює дані без створення нового об'єкта.

data = {
    "name": ["Michael", "Steve", "Liza", "Jhon", "Liza", "Jhon"],
    "country": ["Canada", "USA", "Australia", "Denmark", "Australia", "Denmark"],
    "age": [25, 32, 19, 23, 19, 23]
}

employees = pd.DataFrame(data)

employees = employees.drop_duplicates()
print(employees)

# Метод replace використовується для заміни одного або декількох значень у DataFrame або Series. Він може бути корисний для заміни певних значень, які можуть бути неправильними або небажаними.
# DataFrame.replace(to_replace=None, value=None, inplace=False, method='pad')
# to_replace — значення, яке потрібно замінити. Може бути скалярним, списком або словником.
# value — значення, на яке потрібно замінити. Може бути скалярним, списком або словником.
# inplace — якщо True, зміни відбудуться безпосередньо у вихідному об'єкті.
# method — метод, який використовується для заміни (наприклад, 'pad' для заповнення відсутніх значень).
data = {
    'Дата': ['2023-08-01', '2023-08-02', '2023-08-03'],
    'Температура': [25, 28, 24],
    'Вологість': ['висока', 'низька', 'висока']
}

weather_df = pd.DataFrame(data)
# Ми хочемо замінити "висока" на 80 і "низька" на 30, щоб отримати числові значення вологості. Для цього використовуємо метод replace:
weather_df['Вологість'].replace({'висока': 80, 'низька': 30}, inplace=True)

# Класи pandas для роботи з часовими рядами
# Клас	Створення	Опис
#  Timestamp	to_datetime, Timestamp	Одинична часова мітка
# DatetimeIndex	to_datetime, date_range, bdate_range, DatetimeIndex	 Набір об'єктів Timestamp
# Period 	Period	Одиничний часовий інтервал
# PeriodIndex 	period_range, PeriodIndex	Набір об'єктів Period


# В pandas розрізняють часові мітки та часові інтервали.

# Часова мітка — це конкретне значення дати та часу, наприклад: 2021-09-10 3:39:05. Часовий інтервал передбачає наявність неповної часової мітки та маркера, який визначає період, наприклад мітка 2021-09 матиме маркер M, що означає — місяць. DatetimeIndex — це клас, що дозволяє зберігати масив часових міток. PeriodIndex - клас, що зберігає масив часових інтервалів. Функціонал створення часових міток та часових інтервалів дуже великий, і можливість його розглянути виходить за межі цього конспекту.

# Для створення часової мітки можна скористатися конструктором Timestamp.
date = pd.Timestamp("2021-09-10")

print(date)# 2021-09-10 00:00:00

date = pd.to_datetime("2021-09-10 2:54:13")
print(date)# 2021-09-10 2:54:1
# pd.to_datetime(arg, errors='raise', dayfirst=False, yearfirst=False, utc=None, format=None, exact=True)

# arg: Об'єкт для конвертації.
# errors: Управляє обробкою помилок.
# dayfirst: Чи вважати першим днем місяця в датах.
# yearfirst: Чи вважати першим роком в датах.
# utc: Конвертація в UTC.
# format: Рядковий формат дати.
# exact: Визначає, чи повинен бути точний збіг формату.

# Наприклад, створимо DatetimeIndex — ряд часових міток з відсіченням в один день тривалістю вісім днів, змінна date. На основі отриманого об'єкта створимо структуру Series з денною температурою у місті Полтава у ці дні.

date = pd.date_range(start='2021-09-01', freq='D', periods=8)
temperature = pd.Series([23, 17, 17, 16, 15, 14, 17, 20], index=date)

# Для визначення кроку діапазону параметр freq може містити наступні значення.



# Значення параметру	Опис
# D  День
# W  Тиждень
# M	Місяць
# Q	 Квартал
# Y	Рік
#  H	Година
# T	Хвилина
# S 	Секунда

data = {
    'Місто': ['Київ', 'Львів', 'Одеса', 'Харків', None, 'Львів'],
    'Температура': [25, 32, None, 24, 23, 32],
    'Вологість': ['60%', '70%', '65%', '55%', None, '70%'],
    'Дата': ['2021-08-01', '2021-08-01', '2021-08-02', '2021-08-02', '2021-08-03', '2021-08-01']
}
df = pd.DataFrame(data)

# Проблеми:
# 1. Дублікати: Дані про місто Львів зустрічаються двічі
# 2. Відсутні дані: Відсутні дані в стовпцях "Місто" та "Температура"
# 3. Несумісні типи даних: Вологість представлена як рядок з відсотковим знаком. Рядок "Дата" не є об'єктом datetime

# Рішення:
# Видалимо дублікати за містом і датою.
df.drop_duplicates(subset=['Місто', 'Дата'], inplace=True)

# Для стовпчика "Місто" логічним буде видалити рядки з відсутніми значеннями. Для стовпця "Температура" ми можемо заповнити відсутні дані середнім значенням температури.
df.dropna(subset=['Місто'], inplace=True)
df['Температура'].fillna(df['Температура'].mean(), inplace=True)

# Останнім ми конвертуємо "Вологість" в число, видаливши знак відсотка та конвертуємо "Дата" в об'єкт datetime.

df['Вологість'] = df['Вологість'].str.rstrip('%').astype('float') / 100
df['Дата'] = pd.to_datetime(df['Дата'])

# Тепер набір даних очищений і готовий до подальшої аналітики та візуалізації.

#     Місто   Температура Вологість   Дата
# 0   Київ    25.0        0.60        2021-08-01
# 1   Львів   32.0        0.70        2021-08-01
# 2   Одеса   27.0        0.65        2021-08-02
# 3   Харків  24.0        0.55        2021-08-02

# Основні методи об'єднання DataFrame у Pandas:

# concat — конкатенує DataFrame вздовж вказаної осі
# merge — з'єднує DataFrame на основі спільних стовпців
# join — об'єднує DataFrame на основі індексів

# Метод concat використовується для конкатенації вздовж вказаної осі (рядків або стовпців). Цей метод може об'єднувати два або більше DataFrame.
# Основні параметри:
# objs — структура Series або DataFrame.
# axis — значення 0 об'єднання здійснюється по рядках, 1 - по стовпцях.
# join — значення за замовчуванням: 'outer'. Якщо 'outer', підсумкова структура буде результатом об'єднання (логічне АБО) переданих структур, 'inner' - підсумкова структура буде результатом перетину (логічне І) переданих структур.
# ignore_index — логічний вираз має значення за замовчуванням False. Якщо значення True, то не використовується значення індексу в процесі об'єднання, а якщо False - використовується.
data1 = {
    "name": {"1": "Michael", "2": "John"},
    "country": {"1": "Canada", "2": "USA"},
    "age": {"1": 25, "2": 32}
}
data2 = {
    "name": {"3": "Liza", "4": "Jhon"},
    "country": {"3": "Australia", "4": "Denmark"},
    "age": {"3": 19, "4": 23}
}
employees1 = pd.DataFrame(data1)
employees2 = pd.DataFrame(data2)
employees = pd.concat([employees1, employees2])
print(employees)

# Метод merge об'єднує DataFrame або іменовані об'єкти Series за зазначеними стовпцями або індексами.
# Основні параметри:
# left та right — об'єкти DataFrame або іменовані Series для об'єднання
# how — визначає тип з'єднання: 'left', 'right', 'outer', 'inner'. За замовчуванням 'inner'
# on — стовпці для з'єднання. Мають бути присутніми в обох DataFrame
# left_on та right_on — стовпці з лівого та правого DataFrame, які будуть використані для з'єднання
# suffixes — суфікси для додавання до спільних стовпців
# Об'єднаємо два набори даних за спільним стовпцем "name":

data1 = {
    "name": ["Michael", "John"],
    "country": ["Canada", "USA"],
}

data2 = {
    "name": ["Michael", "Liza"],
    "age": [25, 19]
}

employees1 = pd.DataFrame(data1)
employees2 = pd.DataFrame(data2)

merged = pd.merge(employees1, employees2, on='name', how='outer')
print(merged)

# Метод join використовується для об'єднання стовпців двох DataFrame за індексами.
# Основні параметри:
# other — DataFrame для з'єднання
# on — Колонка або індекс для з'єднання
# how — Визначає тип з'єднання: 'left', 'right', 'outer', 'inner'. За замовчуванням 'left'
# lsuffix та rsuffix — Суфікси для додавання до спільних стовпців
# Він схожий на метод merge, але використовується як метод екземпляра DataFrame, тобто ви можете викликати його на одному DataFrame і передати інший як параметр. Ви також можете вказати, як обробляти індекси на інших осях (за замовчуванням outer для об'єднання і inner для перетину), які суфікси додавати до спільних стовпців (якщо вони є) і чи сортувати результат за ключем об'єднання.

data1 = {
    "name": {"1": "Michael", "2": "John", "3": "Liza", "4": "Jhon"},
    "country": {"1": "Canada", "2": "USA", "3": "Australia", "4": "Denmark"}
}

data2 = {
    "age": {"1": 25, "2": 32, "3": 19, "4": 23}
}

employees1 = pd.DataFrame(data1)
employees2 = pd.DataFrame(data2)

joined = employees1.join(employees2)
print(joined)

# Якщо індекси не збігаються, можна використовувати параметр on, щоб вказати стовпець для об'єднання.
data1 = {
    "name": ["Michael", "John"],
    "country": ["Canada", "USA"],
}

data2 = {
    "name": ["Michael", "Liza"],
    "age": [25, 19]
}

employees1 = pd.DataFrame(data1)
employees2 = pd.DataFrame(data2)

employees2 = employees2.set_index("name")

joined = employees1.join(employees2, on="name", how="outer")
print(joined)

employees1 = pd.DataFrame(data1).set_index("name")
employees2 = pd.DataFrame(data2).set_index("name")

joined = employees1.join(employees2, how="outer")
print(joined)

# Метод apply у Pandas дозволяє застосовувати функцію до кожного елемента стовпця або рядка DataFrame. Це може бути корисно для виконання власних операцій з даними. Метод apply може використовуватися разом із вбудованими функціями Python, а також з вашими звичайними функціями або lambda-функціями.
# DataFrame.apply(func, axis=0, raw=False, result_type=None, args=(), kwds)
# func — функція для застосування. Може бути ім'ям функції або lambda-функцією, головне це функція повинна повертати значення
# axis — вказує, чи застосовувати функцію до рядків (axis=1) чи до стовпців (axis=0)
# raw — якщо дорівнює True, то функція застосовується до масиву NumPy, інакше до серії Pandas
# result_type — визначає тип результату та діє тільки коли axis=1
# args — кортеж позиційних аргументів, які передаються до func

# Розглянемо приклад, де ми хочемо конвертувати температуру з градусів Цельсія C в градуси Фаренгейта F в наступному DataFrame:

data = {
    'Дата': ['2023-08-01', '2023-08-02', '2023-08-03'],
    'Температура C': [25, 28, 24]
}

weather_df = pd.DataFrame(data)
weather_df['Температура F'] = weather_df['Температура C'].apply(lambda temp: (temp * 9/5) + 32)

# Якщо ви хочете застосувати функцію до рядків, ви можете задати параметр axis=1. Розгляньмо наступний приклад:
# Дані про продукти та їх ціни та знижки
data = {
    'Product': ['iPhone 13', 'MacBook Pro', 'Apple Watch'],
    'Price': [699, 1299, 399],
    'Discount': [0.1, 0.05, 0.15]
}

# Створення DataFrame з цими даними
df = pd.DataFrame(data)

# Застосування lanbda-функції до кожного рядка за допомогою apply з axis=1
df['Final Price'] = df.apply(lambda row: row['Price'] * (1 - row['Discount']), axis=1)

print(df)

# Метод applymap можна використовувати для застосування функції до кожного елемента DataFrame. Це відрізняється від методу apply, який застосовує функцію до кожного стовпця або рядка. Він працює лише на рівні елементів, тому відмінно підходить для операцій, які не залежать від інших стовпців або рядків.

# Дані про товари та їх ціни
data = {
    'iPhone 13 (64GB)': [699, 799],
    'MacBook Pro (13-inch)': [1299, 1499]
}

# Створення DataFrame з цінами
df = pd.DataFrame(data)

# Застосування 10% знижки до всіх цін за допомогою applymap і лямбда-функції
df_discounted = df.applymap(lambda price: price * 0.9)

print(df_discounted)

# Створення pivot_table є потужним засобом для агрегації та переорганізації даних в Pandas. За допомогою методу pivot_table можна легко створювати зведені таблиці, які допомагають аналізувати та підсумовувати великі набори даних.

# DataFrame.pivot_table(values=None, index=None, columns=None, aggfunc='mean', fill_value=None, margins=False, dropna=True, margins_name='All')
# Параметри методу:

# values — стовпці, які потрібно агрегувати
# index — стовпці, за якими потрібно згрупувати дані у рядках зведеної таблиці
# columns — стовпці, за якими потрібно згрупувати дані у стовпцях зведеної таблиці
# aggfunc — функція агрегації, яку потрібно застосувати до values. Може бути 'sum', 'mean', 'max' тощо або користувацька функція
# fill_value — значення, яке використовується для заповнення відсутніх значень
# margins — якщо True, додає рядки/стовпці з підсумками
# dropna — якщо True, видаляє стовпці з усіма відсутніми значеннями
# margins_name — ім'я стовпця або рядка з підсумками

df = pd.DataFrame({
  "Фрукт": ["Яблуко", "Яблуко", "Груша", "Груша", "Банан", "Банан"],
  "Колір": ["Червоний", "Зелений", "Жовтий", "Зелений", "Жовтий", "Зелений"],
  "Кількість": [10, 12, 15, 9, 20, 18],
  "Ціна": [5, 4, 6, 7, 3, 2]
})

# Створимо таблицю table з середньою ціною по фруктах і кольорах
table = df.pivot_table(values="Ціна", index="Фрукт", columns="Колір")


# Додамо загальну суму по рядках і стовпцях і заповнимо пропущені значення нулями

table = df.pivot_table(values="Ціна", index="Фрукт", columns="Колір", margins=True, fill_value=0)

import seaborn as sns

# Завантаження набору даних "Titanic"
titanic = sns.load_dataset('titanic')
print(titanic.head())

# Створення зведеної таблиці
pivot_table = pd.pivot_table(titanic, values='age', index=['class'], columns=['sex'], aggfunc='mean')

# Виведення зведеної таблиці
print(pivot_table)

# Створення зведеної таблиці з двома рівнями індексу
pivot_table = pd.pivot_table(titanic, values='age', index=['class', 'survived'], columns=['sex'], aggfunc='mean')

# Якщо ви хочете застосувати різні функції агрегації до різних стовпців, наприклад, розрахувати середню ціну на квиток (стовпець "fare") та кількість пасажирів (стовпець "survived"), ви можете зробити це так:

# Створення зведеної таблиці з різними функціями агрегації
pivot_table = pd.pivot_table(titanic, values=['fare', 'survived'], index=['class', 'sex'], aggfunc={'fare': 'mean', 'survived': 'count'})

# Виведення зведеної таблиці
print(pivot_table)

# Тепер ми можемо створити зведену таблицю для цього набору даних. Наприклад, ми можемо згрупувати дані за класом кают (стовпець "class") та статтю (стовпець "sex") і розрахувати середній вік для кожної групи.

# Створення зведеної таблиці
pivot_table = pd.pivot_table(titanic, values='age', index=['class'], columns=['sex'], aggfunc='mean')

# Виведення зведеної таблиці
print(pivot_table)

tables =pd.read_html("https://uk.wikipedia.org/wiki/%D0%9D%D0%B0%D1%81%D0%B5%D0%BB%D0%B5%D0%BD%D0%BD%D1%8F_%D0%A3%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D0%B8#%D0%9D%D0%B0%D1%80%D0%BE%D0%B4%D0%B6%D1%83%D0%B2%D0%B0%D0%BD%D1%96%D1%81%D1%82%D1%8C")
table = tables[16]


# Вивести перші рядки таблиці за допомогою методу head
print(table.head())
# Визначте кількість рядків і стовпців у датафреймі (атрибут shape)
print(table.shape)
# Замініть у таблиці значення "—" на значення NaN
table.replace(to_replace="—", value=np.nan, inplace=True)
# Визначте типи всіх стовпців за допомогою dataframe.dtypes
print(table.dtypes)
# Замініть типи нечислових колонок на числові. Підказка - це колонки, де знаходився символ "—"
table[['Кількість народжень', 'Коефіцієнт народжуваності', 'Коефіцієнт фертильності']] = table[['Кількість народжень', 'Коефіцієнт народжуваності', 'Коефіцієнт фертильності']].apply(pd.to_numeric, errors='coerce').astype('Int64')  # Use 'Int64' to keep NaNs as nulls.
# Порахуйте, яка частка пропусків міститься в кожній колонці (використовуйте методи isnull та sum)
missing_values = table.isnull().sum() / table.shape[0]
print(missing_values)
# Виведіть статистику по числовим колонкам (метод describe)
print(table.describe())
# Видаліть з таблиці дані по всій країні, останній рядок таблиці
table = table.drop(table.index[-1])
# Замініть відсутні дані в стовпцях середніми значеннями цих стовпців (метод fillna)

# Temporarily convert the columns to float to compute the mean
table["Кількість народжень"] = table["Кількість народжень"].astype(float)
table["Коефіцієнт народжуваності"] = table["Коефіцієнт народжуваності"].astype(float)
table["Коефіцієнт фертильності"] = table["Коефіцієнт фертильності"].astype(float)

# Fill missing values with the mean of each column
table = table.fillna({
    "Кількість народжень": table["Кількість народжень"].mean(),
    "Коефіцієнт народжуваності": table["Коефіцієнт народжуваності"].mean(),
    "Коефіцієнт фертильності": table["Коефіцієнт фертильності"].mean()
})
# Отримайте список регіонів, де рівень народжуваності у 2019 році був вищим за середній по Україні
regions = table[table["Коефіцієнт народжуваності"] > table["Коефіцієнт народжуваності"].mean()]
print("regions",regions)
# У якому регіоні була найвища народжуваність у 2014 році?
region = table[table["Коефіцієнт народжуваності"] == table["Коефіцієнт народжуваності"].max()]
print("region",region)
# Побудуйте стовпчикову діаграму народжуваності по регіонах у 2019 році
table.plot(x="Рік", y="Коефіцієнт народжуваності", kind="bar")
plt.show()
# Вивести  таблицю
print("tables",table)

# Проведіть аналіз файлу 2017_jun_final.csv. Файл містить результати опитування розробників у червні 2017 року.
# Прочитайте файл 2017_jun_final.csv за допомогою методу read_csv
import gdown
file_id = "1_axik7rpXu46YlLtAGpUaoYKD6mLYP2j"
url = f"https://drive.google.com/uc?id={file_id}"
output = "file.csv"
gdown.download(url, output, quiet=False)
survey = pd.read_csv("file.csv")
# Прочитайте отриману таблицю, використовуючи метод head
print(survey.head())
# Визначте розмір таблиці за допомогою методу shape
print("survay.shape", survey.shape)
# Визначте типи всіх стовпців за допомогою dataframe.dtypes
print("survay.dtypes", survey.dtypes)
# Порахуйте, яка частка пропусків міститься в кожній колонці (використовуйте методи isnull та sum)
missing_values = survey.isnull().sum() / survey.shape[0]
print("missing_values", missing_values)
# Видаліть усі стовпці з пропусками, крім стовпця Мова.програмування
survey = survey.loc[:, ['Язык.программирования'] + [col for col in survey.columns if col == 'Язык.программирования' or not survey[col].isnull().any()]]
# Знову порахуйте, яка частка пропусків міститься в кожній колонці і переконайтеся, що залишився тільки стовпець "Мова.програмування"
missing_values = survey.isnull().sum() / survey.shape[0]
print("missing_values", missing_values)
# Видаліть усі рядки у вихідній таблиці за допомогою методу dropna
survey = survey.dropna()
# Визначте новий розмір таблиці за допомогою методу shape
print("survey.shape", survey.shape)

# Видаляємо зайві пробіли у назвах стовпців
survey.columns = survey.columns.str.strip()
# Перевіряємо наявність дублікатів
duplicates = survey.columns[survey.columns.duplicated()].tolist()
if duplicates:
    print("Знайдено дублікати у стовпцях:", duplicates)
    survey = survey.loc[:, ~survey.columns.duplicated()]  # Видаляємо дубльовані стовпці

# Створіть нову таблицю python_data, в якій будуть тільки рядки зі спеціалістами, які вказали мову програмування Python
# Фільтруємо дані для Python
if "Язык.программирования" in survey.columns:
    python_data = survey[survey["Язык.программирования"] == "Python"]
    print(python_data.head())
else:
    print("Помилка: стовпець 'Язык.программирования' не знайдено у DataFrame!")
    print("Ось доступні стовпці:", survey.columns.tolist())

# Визначте розмір таблиці python_data за допомогою методу shape
print("python_data.shape", python_data.shape)
# Використовуючи метод groupby, виконайте групування за стовпчиком "Посада"
grouped = python_data.groupby('Должность').size()
# Виведіть результат групування
print("grouped", grouped)
# Створіть новий DataFrame, де для згрупованих даних за стовпчиком "Посада", виконайте агрегацію даних за допомогою методу agg і знайдіть мінімальне та максимальне значення у стовпчику "Зарплата.в.місяць"
aggregated = python_data.groupby('Должность').agg({'Зарплата.в.месяц': ['min', 'max']})
print("aggregated", aggregated)
# Створіть функцію fill_avg_salary, яка повертатиме середнє значення заробітної плати на місяць. Використовуйте її для методу apply та створіть новий стовпчик "avg"
def fill_avg_salary(row):
    return (row[("Зарплата.в.месяц", "min")] + row[("Зарплата.в.месяц", "max")])/2
aggregated[("Зарплата.в.месяц", "avg")] = aggregated.duplicated(keep=False)
aggregated['avg'] = aggregated.apply(fill_avg_salary, axis=1)
# Виведіть результат
print("aggregated", aggregated)
# Створіть описову статистику за допомогою методу describe для нового стовпчика.
print(aggregated["avg"].describe())
# Збережіть отриману таблицю в CSV файл
aggregated.to_csv("aggregated.csv")
print(python_data.head())

# Частина третя: Аналіз датасету з Kaggle.com
# Прочитайте csv файл (використовуйте функцію read_csv)
# Виведіть перші п'ять рядків (використовується функція head)
# Виведіть розміри датасету (використовуйте атрибут shape)
# Відповідь: Про скільки книг зберігає дані датасет? 550

books = pd.read_csv("bestsellers with categories.csv")
books.columns = ['name', 'author', 'user_rating', 'reviews', 'price', 'year', 'genre']

# Первинне дослідження даних

# Перевірте, чи у всіх рядків вистачає даних: виведіть кількість пропусків (na) у кожному зі стовпців (використовуйте функції isna та sum)
print("кількість пропусків",books.isnull().sum()) # ні
# Відповідь: Чи є в якихось змінних пропуски? (Так / ні)


# Перевірте, які є унікальні значення в колонці genre (використовуйте функцію unique)
print("унікальні значення",books['genre'].unique()) #['Non Fiction' 'Fiction']
# Відповідь: Які є унікальні жанри?

# Тепер подивіться на розподіл цін: побудуйте діаграму (використовуйте kind='hist')
books["price"].plot(kind="hist", bins=30, edgecolor="black", alpha=0.7)
# Додамо підпис для осі X і заголовок
plt.xlabel("Ціна книг")
plt.ylabel("Частота")
plt.title("Розподіл цін книг")
plt.show()
# Визначте, яка ціна у нас максимальна, мінімальна, середня, медіанна (використовуйте функції max, min, mean, median)
print(books["price"].max())
print(books["price"].min())
print(books["price"].mean())
print(books["price"].median())

# Відповідь: Максимальна ціна? #105
# Відповідь: Мінімальна ціна? #0
# Відповідь: Середня ціна? #13.1
# Відповідь: Медіанна ціна? #11

# Пошук та сортування даних

# Відповідь: Який рейтинг у датасеті найвищий?
print(books["user_rating"].max()) #4.9
# Відповідь: Скільки книг мають такий рейтинг?
print(books[books["user_rating"] == 4.9].shape[0]) #52
# Відповідь: Яка книга має найбільше відгуків?
print(books[books["reviews"] == books["reviews"].max()]["name"].values[0]) #Where the Crawdads Sing
# Відповідь: З тих книг, що потрапили до Топ-50 у 2015 році, яка книга найдорожча (можна використати проміжний датафрейм)?
top_books_2015 = books[(books["year"] == 2015) & (books["user_rating"] >= 4.6)].sort_values("price", ascending=False)
print(top_books_2015.head(1)["name"].values[0]) #Diagnostic and Statistical Manual of Mental Disorders, 5th Edition: DSM-5
# Відповідь: Скільки книг жанру Fiction потрапили до Топ-50 у 2010 році (використовуйте &)?
print(books[(books["year"] == 2010) & (books["genre"] == "Fiction")].shape[0]) #20
# Відповідь: Скільки книг з рейтингом 4.9 потрапило до рейтингу у 2010 та 2011 роках (використовуйте | або функцію isin)?
print(books[(books["year"].isin([2010, 2011])) & (books["user_rating"] == 4.9)].shape[0]) #6
# І насамкінець, давайте відсортуємо за зростанням ціни всі книги, які потрапили до рейтингу в 2015 році і коштують дешевше за 8 доларів (використовуйте функцію sort_values).
books_2015 = books[(books["year"] == 2015) & (books["price"] < 8)].sort_values("price", ascending=True)
# Відповідь: Яка книга остання у відсортованому списку?
print(books_2015.tail(1)["name"].values[0]) #The Wright Brothers


# Агрегування даних та з'єднання таблиць

# Для початку давайте подивимося на максимальну та мінімальну ціни для кожного з жанрів (використовуйте функції groupby та agg, для підрахунку мінімальних та максимальних значень використовуйте max та min). Не беріть усі стовпці, виберіть тільки потрібні вам
ganres_price = books.groupby("genre")["price"].agg(["max", "min"])
print("ganres_price",ganres_price)
# Відповідь: Максимальна ціна для жанру Fiction 82
# Відповідь: Мінімальна ціна для жанру Fiction 0
# Відповідь: Максимальна ціна для жанру Non Fiction 105
# Відповідь: Мінімальна ціна для жанру Non Fiction 0

# Тепер створіть новий датафрейм, який вміщатиме кількість книг для кожного з авторів (використовуйте функції groupby та agg, для підрахунку кількості використовуйте count). Не беріть усі стовпці, виберете тільки потрібні
authors_books = books.groupby("author")["name"].count().sort_values(ascending=False)
print("authors_books",authors_books)

# Відповідь: Якої розмірності вийшла таблиця? 248
print("authors_books",authors_books.shape)
# Відповідь: Який автор має найбільше книг? Jeff Kinney
print("authors_books",authors_books.idxmax())
# Відповідь: Скільки книг цього автора? 12
print("authors_books",authors_books.max())


# Тепер створіть другий датафрейм, який буде вміщати середній рейтинг для кожного автора (використовуйте функції groupby та agg, для підрахунку середнього значення використовуйте mean). Не беріть усі стовпці, виберете тільки потрібні
authors_rating = books.groupby("author")["user_rating"].mean().sort_values(ascending=True)
print("authors_rating",authors_rating)

# Відповідь: У якого автора середній рейтинг мінімальний?
print("authors_rating",authors_rating.idxmin()) #Kyle Keeley
# Відповідь: Який у цього автора середній рейтинг?
print("authors_rating",authors_rating.min()) #4.3

# З'єднайте останні два датафрейми так, щоб для кожного автора було видно кількість книг та середній рейтинг (Використовуйте функцію concat з параметром axis=1). Збережіть результат у змінну
authors = pd.concat([authors_books, authors_rating], axis=1)
# Відсортуйте датафрейм за зростаючою кількістю книг та зростаючим рейтингом (використовуйте функцію sort_values)
authors = authors.sort_values(by=["name", "user_rating"], ascending=[True, True])
# Відповідь: Який автор перший у списку?
print("authors",authors.head(1)) #Muriel Barbery     1          4.0


print(books.head())
print(books.shape)

