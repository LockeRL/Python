# Вариант 47

# Эта программа предназначена для отрисовки графика функции y = x - 1.4^x

# Входные данные: начальное значение, шаг, конечное значение

# Таблица значений графика и сам график


import math as m

# Ввод значений и проверка

x_start = float(input('Введите начальное значение для х: '))

# Ввод и проверка конца отрезка
x_finish = float(input('Введите конечное значение для х: '))
while (x_finish - x_start) <= 0.01:
    print('Конечное значение должно быть больше начального')
    x_finish = float(input('Введите конечное значение для х: '))

# Ввод и проверка шага
x_step = float(input('Введите шаг значений: '))
while ((x_finish - x_start - x_step) <= 0.01) or (x_step <= 0):
    if (x_finish - x_start - x_step) <= 0.01:
        print('Шаг слишком большой')
    elif x_step < 0:
        print('Шаг  не может быть отрицательным')
    else:
        print('Шаг не может быть равен 0')
    x_step = float(input('Введите шаг значений: '))

serif_num = int(input('Введите количество засечек на оси ординат из диапазона [4,8]: '))
while not (3 < serif_num < 9):
    print('Количество засечек выходит из диапазона [4,8]')
    serif_num = int(input('Введите количество засечек на оси ординат из диапазона [4,8]: '))
# x_start = 2.0
# x_finish = 6.0
# x_step = 0.2
# serif_num = 6

# Инициализация минимума и максимума
min_value = m.inf
max_value = -m.inf

# Отрисовка таблицы значений
print('-' * 43)
print('|' + ' ' * 6 + 'x' + ' ' * 6 + '|' + ' ' * 6 + 'y1' + ' ' * 4 + '|' + ' ' * 6 + 'y2' + ' ' * 6 + '|')
print('-' * 43)
x = x_start
while x < (x_finish + 0.0001):
    y1 = x ** 3 - 14.5 * (x ** 2) + 60.7 * x - 71
    y2 = x - 1.4 ** x
    print(f'|{x:12.6f} |{y1:12.6f} |{y2:12.6f} |')
    x += x_step
    if y2 > max_value:
        max_value = y2
    if y2 < min_value:
        min_value = y2
print('-' * 43 + '\n\n\n')

# Отрисовка графика

print('Отрисовка графика функции y = x - 1.4^x \n')

# Отрисовка оси ординат
ordinate_value_step = (max_value - min_value) / (serif_num - 1)
ordinate_space_step = (max_value - min_value) / 80
space_between_values = int((80 - serif_num * 8) / (serif_num - 1))
ordinate_axis = ' ' * 10 + f'{min_value:8.4f}'
ordinate_value = min_value
for i in range(serif_num - 2):
    ordinate_value += ordinate_value_step
    ordinate_axis += (' ' * space_between_values + f'{ordinate_value:8.4f}')
ordinate_axis += (' ' * space_between_values + f'{max_value:10.4f}')
print(ordinate_axis)

# Отрисовка графика
x = x_start
while x < (x_finish + 0.001):
    y = x - 1.4 ** x
    y_step_num = int((y - min_value) / ordinate_space_step) - 1
    x_axis = int((0 - min_value) / ordinate_space_step) - 1
    x_ordinate = f'{x:10.4f}' + '|'
    if y_step_num < 0:
        y_step_num = 0
    if x_axis > y_step_num:
        x_ordinate += (' ' * y_step_num + '*' + ' ' * (x_axis - y_step_num - 1) + '|')
    elif x_axis < y_step_num:
        x_ordinate += (' ' * x_axis + '|' + ' ' * (y_step_num - x_axis) + '*')
    else:
        x_ordinate += (' ' * x_axis + '*')
    print(x_ordinate)
    x += x_step
