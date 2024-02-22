
import numpy as np
import pandas
from numpy import random
import pandas as pd
from pandas import DataFrame

#----------------------------------------------------------------------------------------------------------------
#
# NumPy
#
#----------------------------------------------------------------------------------------------------------------

#1 Створіть масив NumPy із 10 випадкових цілих чисел. Виконайте наступні операції:
#Знайдіть середнє, медіану та стандартне відхилення масиву.
#Замініть всі парні числа у масиві на 0.

x = random.randint(1000, size=10)
x_mean = np.mean(x)
x_median = np.median(x)
x_std = np.std(x)
print(f'Array {x} \nMean {x_mean} \nMedian {x_median} \nArray standard deviation {x_std}')
x[x % 2 == 0] = 0
print(f' Array {x}')

#2 Створіть 2D масив NumPy (матрицю) розміром (3, 3) із випадковими цілими числами.
#Виведіть перший рядок матриці.
#Виведіть останній стовпець матриці.
#Виведіть діагональні елементи матриці.
x = np.random.randint(0, 1000, (3, 3))
print(x)
x_first_line = x[:1]
print(f'First line {x_first_line}')
x_last_column = x[:, -1]
print(f'Last column {x_last_column}')
x_diagonal = np.diagonal(x)
print(f'Diagonal {x_diagonal}')

#3 Створіть 2D масив NumPy розміром (3, 3) та 1D масив розміром (3,).
# Використайте broadcasting для додавання 1D масиву до кожного рядка 2D масиву.

x = random.randint(0, 100, (3, 3))
y = random.randint(0, 1000, size=3)
c = y + x
print(f'2D array {x} \n 1D array {y} \n Concatenation {c}')

#4 Створіть 2D масив NumPy розміром (5, 5) з випадковими цілими числами.
#Знайдіть та виведіть всі унікальні елементи у масиві.
#виведіть всі рядки, сума елементів у яких більша за певне значення. (значення оберіть самі)

x = random.randint(0, 100, (5, 5))
x_unic = np.unique(x)
n = 300
list_row_bigger_n = []
for row in x:
    if np.sum(row) > n:
        list_row_bigger_n.append(row)
x_row_sum_bigger_n = np.array(list_row_bigger_n)
print(f'2D array {x} \n Unic elements {x_unic} \n Rows with a sum greater than {n} \n{x_row_sum_bigger_n}')

#5 Створіть 1D масив NumPy, що містить цілі числа від 1 до 20 (включно).
#Використайте оператор shape, щоб перетворити 1D масив у 2D масив розміром (4, 5).
# Переконайтеся, що отриманий перетворений масив має бажаний розмір.

x = np.arange(0, 20)
x_2d = x.reshape(4, 5)
print(x, x_2d)
x_2d_shape = np.shape(x_2d)
matching_size_x_2d = False
if x_2d_shape == (4, 5):
    matching_size_x_2d = True
print(f'Matching size 2D X  {matching_size_x_2d}')


#------------------------------------------------------------------------------------------------------------------
#
# Pandas
#
#------------------------------------------------------------------------------------------------------------------

#1 Створіть DataFrame Pandas із щонайменше 5 рядками та 3 стовпцями.
# Стовпці можуть представляти різні атрибути (наприклад, Ім'я, Вік, Місто).

country_info = {
    'Country': ['Ukraine', 'Poland', 'Germany', 'Italy', 'France'],
    'Capital': ['Kyiv', 'Warsaw', 'Berlin', 'Rome', 'Paris'],
    'Population': [41, 38, 83, 60, 67]
}
df = pandas.DataFrame(country_info)
print(df)

# Додайте новий стовпець до DataFrame, який представляє числове значення.

df.insert(loc=3, column='Area', value=[603628, 312696, 357021, 301340, 551695])
print(df)

#3 Відфільтруйте DataFrame, щоб показати лише рядки, де числове значення більше
# певного порогу (ви можете визначити поріг)

population_for_comparing = 50
df_filter_by_population = df[df['Population'] > population_for_comparing]
print(f'Countries with a population greater than {population_for_comparing}\n {df_filter_by_population}')

#4 Завантажте набір даних за допомогою Pandas
# (ви можете використовувати будь-який набір даних у форматі CSV або wine.csv).

df = pd.read_csv('wine.csv', header=0)
print(df)

#5 Відобразіть перші 5 рядків набору даних.

df_rows = df.head(5)
print(df_rows)

#6 Розрахуйте та виведіть загальну статистику для числових стовпців у наборі даних.

df_statistics = df.describe()
print(df_statistics)

#7 Знайдіть та виведіть унікальні значення у категорійному стовпці.

header = [f'Column{i + 1}' for i in range(len(df.columns))]
df.columns = header
df_column2_unique = df['Column2'].unique()
print(df, df_column2_unique)



