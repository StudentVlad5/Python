import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.tools.tools import add_constant

rent_df = pd.read_csv("./House_Rent_Dataset.csv", encoding='utf-8')

print('приклади даних з БД:')
print(rent_df.sample(5))
print('-'*50)
print('Форма даних:')
print(rent_df.shape)
print('-'*50)
print('Назви даних:')
print(rent_df.columns)
print('-'*50)
print('Типи даних:')
print(rent_df.info())
print('-'*50)
print('Статистика даних:')
print(rent_df.describe())
print('-'*50)
print('Перевірка відсутніх  даних:')
print(rent_df.isnull().sum())
print('-'*50)
print('Перевірка дублікатів:')
print(rent_df.duplicated().sum())
print('-'*50)

'''
Маємо 12 колонок та 4746 рядків

Числові (int64):
BHK – кількість спалень
Rent – орендна плата
Size – площа в квадратних футах
Bathroom – кількість ванних кімнат

Категоріальні (object):
Posted On (перетворити в datetime)
Floor (рядок типу "2 out of 5" – потребує розділення)
Area Type (потребує обробки)
Area Locality (потребує обробки)
City (потребує обробки)
Furnishing Status (потребує обробки)
Tenant Preferred (потребує обробки)
Point of Contact (потребує обробки)


Пропущені значення — відсутні
Великий розкид в Rent і Size може вказувати на наявність викидів.
'''


print("Mean House Rent:", round(rent_df["Rent"].mean()))
print("Median House Rent:", round(rent_df["Rent"].median()))
print("Highest House Rent:", round(rent_df["Rent"].max()))
print("Lowest House Rent:", round(rent_df["Rent"].min()))
'''
Дані мають високу асиметрію та наявність викидів.
Медіана — краща характеристика "типової" квартири.
 Середнє значення завищене через декілька елітних дорогих об'єктів.
'''
# print(rent_df["Rent"].sort_values(ascending = False)[:5])
# print(rent_df["Rent"].sort_values()[:5])

# Візуалізація розподілу орендної плати

num_cols = ['BHK', 'Rent', 'Size', 'Bathroom']
for col in num_cols:
    sns.histplot(rent_df[col], kde=True)
    plt.title(f'Distribution of {col}')
    plt.show()

# Перетворення "Posted On" у datetime і виділення року та місяця
rent_df['Posted On'] = pd.to_datetime(rent_df['Posted On'], errors='coerce')
rent_df['Posted Year'] = rent_df['Posted On'].dt.year
rent_df['Posted Month'] = rent_df['Posted On'].dt.month
rent_df.drop(columns='Posted On', inplace=True)

# Обробка колонки "Floor"
def extract_floor_info(floor_str):
    try:
        floor_str = floor_str.strip()
        if 'Ground' in floor_str:
            return 0, int(floor_str.split('out of')[-1])
        elif 'Upper Basement' in floor_str:
            return -1, int(floor_str.split('out of')[-1])
        elif 'Lower Basement' in floor_str:
            return -2, int(floor_str.split('out of')[-1])
        elif 'out of' in floor_str:
            parts = floor_str.split(' out of ')
            return int(parts[0]), int(parts[1])
        else:
            return np.nan, np.nan
    except:
        return np.nan, np.nan

rent_df[['Floor_Level', 'Total_Floors']] = rent_df['Floor'].apply(lambda x: pd.Series(extract_floor_info(str(x))))
rent_df.dropna(subset=['Floor_Level', 'Total_Floors'], inplace=True)
rent_df.drop(columns='Floor', inplace=True)

# Обробка Area Locality
top_localities = rent_df['Area Locality'].value_counts().nlargest(10).index
rent_df['Area Locality'] = rent_df['Area Locality'].apply(lambda x: x if x in top_localities else 'Other')

# Для всіх категоріальних змінних краще використати One-Hot Encoding, наприклад:
categorical_cols = ['Area Type', 'City', 'Furnishing Status', 'Tenant Preferred', 'Point of Contact', 'Area Locality']
rent_df = pd.get_dummies(rent_df, columns=categorical_cols, drop_first=True)

'''Висновки:
Дати перетворено
Floor — розбито на числові ознаки
Бінарні/категоріальні змінні — підготовлено для кодування
Дані готові до нормалізації/моделювання
'''

# Кореляційна матриця

corr = rent_df.corr(numeric_only=True)
sns.heatmap(corr, annot=False, cmap='coolwarm')
# sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()
'''
Це показує наскільки зміна однієї змінної пов’язана зі зміною іншої:

+1.0 — ідеальна пряма залежність

-1.0 — ідеальна обернена залежність

0 — немає лінійної залежності

Rent найбільш позитивно корелює з:
Size (розмір квартири)
Bathroom (кількість ванних кімнат)
BHK (кількість спалень)

Rent слабо або майже не корелює з:
Total_Floors чи Floor_Level (етажність), хоча іноді може бути значущим у великих містах.
Posted Month — що логічно, бо місяць публікації не завжди визначає ціну.
Якщо є однакові ознаки (наприклад, Size і BHK часто йдуть разом), то між ними буде також висока кореляція → може бути мультиколінеарність (для лінійних моделей це погано).


'''


# Parth 2.

# Формування X та y
X = rent_df.drop(columns=['Rent'])
y = rent_df['Rent']

# Розділення та масштабування
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Модель 1: Лінійна регресія
lin_reg = LinearRegression()
lin_reg.fit(X_train_scaled, y_train)
y_pred_lin = lin_reg.predict(X_test_scaled)
mse_lin = mean_squared_error(y_test, y_pred_lin) # середнє квадратичне відхилення
r2_lin = r2_score(y_test, y_pred_lin) # коефіцієнт детермінації

# Модель 2: Random Forest
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)
mse_rf = mean_squared_error(y_test, y_pred_rf)  # середнє квадратичне відхилення
r2_rf = r2_score(y_test, y_pred_rf) # коефіцієнт детермінації

# Візуалізація
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
sns.scatterplot(x=y_test, y=y_pred_lin)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.title('Лінійна регресія: Справжнє vs Прогноз')
plt.xlabel("Справжнє значення")
plt.ylabel("Прогнозоване значення")

plt.subplot(1, 2, 2)
sns.scatterplot(x=y_test, y=y_pred_rf)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.title('Random Forest: Справжнє vs Прогноз')
plt.xlabel("Справжнє значення")
plt.ylabel("Прогнозоване значення")

plt.tight_layout()
plt.show()

# Метрики
print("Лінійна регресія:")
print(f"MSE: {mse_lin:.2f}")
print(f"R²: {r2_lin:.4f}")

print("Random Forest:")
print(f"MSE: {mse_rf:.2f}")
print(f"R²: {r2_rf:.4f}")

'''
1. Mean Squared Error (MSE)
MSE — це середнє квадратичне відхилення між справжніми та передбаченими значеннями:

Чим менше MSE, тим точніший прогноз.

Вимірюється у квадратних одиницях цільової змінної — тобто тут у квадратних рупіях.

Модель	MSE (менше — краще)
Лінійна регресія	1,847,380,849
Random Forest	1,417,235,287 

Random Forest точніше прогнозує орендну плату, має менше середнє відхилення.

2. R² (Коефіцієнт детермінації)
Показує, яка частка варіації цільової змінної пояснюється моделлю.

Значення від 0 до 1 (іноді може бути від’ємним при дуже поганій моделі):

0 — модель нічого не пояснює

1 — модель повністю пояснює дані

> 0.5 — прийнятна модель

Модель	R² (більше — краще)
Лінійна регресія	0.5501
Random Forest	0.6548 

Random Forest краще "вловлює" залежності між ознаками і рентою.

Чому так?
Лінійна регресія — дуже проста модель, яка передбачає лише лінійні зв'язки. Вона може бути недоцільною для складних взаємозалежностей між ознаками (наприклад, нелінійний вплив площі, поверху, типу меблів тощо).

Random Forest — ансамблева модель, яка враховує взаємодії між ознаками та нелінійні залежності, і тому дає кращий результат.

Висновки:
Порівняння	Висновок
Якість	Random Forest точніший за всіма метриками.
Складність	Random Forest складніший у навчанні.
Інтерпретованість	Лінійна регресія простіша для пояснення.
'''

# --- VIF (Multicollinearity)
X_const = add_constant(X_train_scaled)
vif_data = pd.DataFrame()
vif_data['Feature'] = X.columns
vif_data['VIF'] = [variance_inflation_factor(X_const, i+1) for i in range(X.shape[1])]
print("\n📌 VIF (Multicollinearity):")
print(vif_data.sort_values(by='VIF', ascending=False))

# --- GridSearch for RandomForest
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
param_grid = {
    'n_estimators': [50, 100],
    'max_depth': [10, 20, None],
    'min_samples_split': [2, 5],
}
rf = RandomForestRegressor(random_state=42)
grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=3, scoring='r2', n_jobs=-1)
grid_search.fit(X_train, y_train)
best_rf = grid_search.best_estimator_

print("\n Найкращі параметри RandomForest:")
print(grid_search.best_params_)

# --- Feature Importance
feature_importance = pd.Series(best_rf.feature_importances_, index=X.columns).sort_values(ascending=False)
print("\n🔝 Топ-10 важливих ознак:")
print(feature_importance.head(10))

# --- Residual Plot
y_pred = best_rf.predict(X_test)
residuals = y_test - y_pred
plt.figure(figsize=(10, 6))
sns.scatterplot(x=y_pred, y=residuals)
plt.axhline(0, color='red', linestyle='--')
plt.xlabel("Предсказана оренда (Predicted Rent)")
plt.ylabel("Залишки (Residuals)")
plt.title("Графік залишків Random Forest")
plt.tight_layout()
plt.show()
'''
Висновок по Random Forest:
Ознака	Інтерпретація
Залишки випадкові	 Модель добре вловлює залежності
Немає трендів	 Немає ознак недообучення або перекосів
Помилки на крайніх значеннях	Часто трапляється, бо Random Forest обмежує екстраполяцію

Спостереження з  графіка:
На середніх і нижчих значеннях оренди — помилки мінімальні.

На дуже дорогих квартирах — помилки більші, модель недооцінює їх (часто через обмеження глибини дерева та впливу меншості даних).
'''


'''
Мультиколінеарність (VIF – Variance Inflation Factor)
Що це таке:
VIF показує, наскільки одна ознака залежить від інших ознак.

Якщо VIF > 5 (або 10), це ознака мультиколінеарності — тобто ознака надто сильно корелює з іншими i може заважати моделі.

 Інтерпретація:
VIF	Інтерпретація
~1	Ознака незалежна від інших
1–5	Слабка мультиколінеарність
>5 або >10	Сильна мультиколінеарність 

Висновок: Якщо ознак з VIF > 10 кілька — варто або видалити, або об'єднати, або зменшити через PCA.

GridSearchCV для Random Forest
▶ Що це таке:
Перебір параметрів max_depth, n_estimators, min_samples_split для підбору найкращої комбінації гіперпараметрів.

Автоматично обирає найкращу модель на крос-валідації.

✅ Висновок:
Покращення якості прогнозу.

Уникає пере/недообучення за рахунок оптимальних налаштувань.

3. Важливість ознак (Feature Importance)
▶ Що це:
Random Forest автоматично оцінює, які ознаки найсильніше впливають на цільову змінну (Rent).

Важливість — у відсотках від впливу на рішення дерева.

✅ Висновок:
Найвпливовіші ознаки можна залишити в моделі (для спрощення та інтерпретації).

Малозначущі — видалити або зменшити для уникнення "шуму".

Приклад типових топ-ознак:

Size (розмір площі)

BHK (кількість кімнат)

Bathroom

Floor_Level

City_<...> (місто)

4. Графік залишків (Residuals Plot)
▶ Що це:
Покажчик якість передбачень.

Залишки = Справжні значення – Прогноз.

Ідеально: залишки розподілені випадково навколо 0.

Інтерпретація:
Ознака	Що означає
Рівномірне розсіювання	Модель адекватна 
Віялоподібна структура	Варіація не константна (гетероскедастичність) 
Систематичний малюнок	Модель щось не вловлює — можливо, треба іншу модель

🧾 Загальний висновок:
Аналіз	Висновок
✅ VIF	Виявити ознаки з надлишковою інформацією
✅ GridSearch	Знайдено оптимальні параметри Random Forest
✅ Feature Importance	Виділено ключові ознаки, які впливають на вартість оренди
✅ Residuals Plot	Дає уявлення про якість моделі та її похибки

🔧 Що можна зробити далі:

Видалити або об'єднати висококорельовані ознаки.

Спробувати моделі LightGBM або XGBoost.

Використати крос-валідацію для всіх метрик.
'''

# Ознаки з високим VIF (наприклад, VIF > 5)
vif_data_sorted = vif_data.sort_values(by='VIF', ascending=False)
high_vif_features = vif_data_sorted[vif_data_sorted['VIF'] > 5]
print("⚠️ Ознаки з високим рівнем мультиколінеарності (VIF > 5):")
print(high_vif_features)

# Графік важливості ознак (топ-20)
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 8))
feature_importance.head(20).sort_values().plot(kind='barh', color='skyblue')
plt.xlabel("Feature Importance")
plt.title("🔝 Топ-20 важливих ознак (Random Forest)")
plt.tight_layout()
plt.show()

'''
Тип ознак	Дія
🟥 Area Type_Carpet Area і Area Type_Super Area	❗ Видалити одну або обидві для усунення мультиколінеарності
🟨 Bathroom, BHK, Size, Total_Floors, Floor_Level	🔄 Необхідно відслідковувати їхній вплив — вони логічно корельовані
🟩 Інші ознаки (місто, контакт, меблювання)	✅ Можна залишити — мають низьку мультиколінеарність
🟫 Posted Year	❔ Перевірити — можливо, має одну унікальну категорію
'''