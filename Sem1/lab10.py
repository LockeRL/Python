# Вариант серединных прямоугольников, Уэддля

# Программа предназначена у для вычисления приближённого значения интеграла двумя разными методами

# Входные данные: начало, конец отрезка, N1, N2 - количества участков разбиения для численного интегрирования

# Выходные данные: таблица


import math as m
from functions import is_float_or_int


# Запись функции
def func(x):
    return 2 * (x ** 2)

# Первообразная
def primitive(x):
    return 2 * (x ** 3) / 3

# Уэддль
def veddle(f, start, end, n):
    h = (end - start) / n
    summ_ved = 0
    x1 = start
    x2 = start + h
    while x2 <= end:
        dx = (x2 - x1) / 6
        summ_ved += 3 * dx / 10 * (f(x1) + 5 * f(x1 + dx) + f(x1 + 2 * dx) + 6 * f(x1 + 3 * dx) +
                              f(x1 + 4 * dx) + 5 * f(x1 + 5 * dx) + f(x1 + 6 * dx))
        x1, x2 = x2, x2 + h
    return summ_ved

# Метод прямоугольников
def rect(f, start, end, n):
    interval = (end - start) / n
    begin_rect = start + interval / 2
    summ_rect = 0
    for i in range(n):
        summ_rect += f(begin_rect + interval * i) * interval
    return summ_rect


# Ввод данных
begin = input('Введите начало отрезка: ').strip()
while is_float_or_int(begin) == 0:
    print('Некорректное число')
    begin = input('Введите конец отрезка: ').strip()
begin = float(begin)
finish = input('Введите конец отрезка: ').strip()
while is_float_or_int(finish) == 0 or float(finish) <= begin:
    print('Некорректное число')
    finish = input('Введите конец отрезка: ').strip()
finish = float(finish)
N1 = input('Введите первое количество разбиений: ').strip()
while not N1.isdecimal() or int(N1) == 0:
    print('Некорректное число')
    N1 = input('Введите первое количество разбиений: ').strip()
N1 = int(N1)
N2 = input('Введите второе количество разбиений: ').strip()
while not N2.isdecimal() or int(N2) == 0:
    print('Некорректное число')
    N2 = input('Введите второе количество разбиений: ').strip()
N2 = int(N2)
# Подсчет методом серединных прямоугольников
summ_rect_N1 = rect(func, begin, finish, N1)
summ_rect_N2 = rect(func, begin, finish, N2)
# Подсчет по первообразной
summ_primitive = primitive(finish) - primitive(begin)
# Подсчет методом Уэддля
summ_veddle_N1 = veddle(func, begin, finish, N1)
summ_veddle_N2 = veddle(func, begin, finish, N2)
# Таблица
print(f'''------------------------------------------------------------------
|                                  | {N1:>12.9g} | {N2:>12.9g} |
------------------------------------------------------------------
| Метод серединных прямоугольников | {summ_rect_N1:>12.9g} | {summ_rect_N2:>12.9g} |
------------------------------------------------------------------
|           Метод Уэддля           | {summ_veddle_N1:>12.9g} | {summ_veddle_N2:>12.9g} |        
------------------------------------------------------------------''')
# Определение неточного и точного методов
min_veddle_error = summ_veddle_N1 if N1 < N2 else summ_veddle_N2
min_rect_error = summ_rect_N1 if N1 < N2 else summ_rect_N2
veddle_error = abs(min_veddle_error - summ_primitive)
rect_error = abs(min_rect_error - summ_primitive)
check_func = rect_error > veddle_error
bad_func = rect if check_func else veddle
if bad_func == rect:
    print('Наиболее точный метод: метод Уэддля')
    print(f'Абсолютная погрешность составила: {veddle_error:>12.9g}')
    if summ_primitive == 0:
        print('Невозможно вычислить относительную погрешность, значение интеграла 0')
    else:
        print(f'Относительная погрешность составила: {veddle_error / summ_primitive:>12.9g}')
    bad_summ = min_rect_error
else:
    print('Наиболее точные метод: метод серединных прямоугольников')
    print(f'Абсолютная погрешность составила: {rect_error:12.9g}')
    if summ_primitive == 0:
        print('Невозможно вычислить относительную погрешность, значение интеграла 0')
    else:
        print(f'Относительная погрешность составила: {rect_error / summ_primitive:12.9g}')
    bad_summ = min_veddle_error
# Ввод точности
eps = input('Введите точность: ').strip()
while is_float_or_int(eps) == 0 or float(eps) >= 1:
    print('Некорректное число')
    eps = input('Введите точность: ').strip()
eps = float(eps)
# Подсчет количества итераций
iter_start = min(N1, N2)
while abs(bad_func(func, begin, finish, iter_start) - bad_func(func, begin, finish, iter_start * 2)) > eps:
    iter_start += 1
if bad_func == rect:
    print(f'Для того, чтобы метод серединных прямоугольников имел точность {eps:8.6g} потребуется {iter_start} '
          f'итераций')
else:
    print(f'Для того, чтобы метод Уэддля имел точность {eps:8.6g} потребуется {iter_start} итераций')