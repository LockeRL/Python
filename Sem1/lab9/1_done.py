# Эта программа предназначена для формирования матрицы A по формуле ajk = sin(dj+fk),
# 0пределения среднего арифметического положительных чисел каждой строки матрицы
# и количества элементов, меньших среднего арифметического

# Входные данные: массивы D и F

# Выходные данные: матрицу A в виде матрицы и рядом столбцы AV и L


# Библиотеки
import math as m
from functions import is_float_or_int


# Ввод длин массивов
length_d = input('Введите длину массива d: ').strip()
while not length_d.isdecimal() or int(length_d) == 0:
    print('Некорректное число')
    length_d = input('Введите длину массива d: ').strip()
length_d = int(length_d)
length_f = input('Введите длину массива f: ').strip()
while not length_f.isdecimal() or int(length_f) == 0:
    print('Некорректное число')
    length_f = input('Введите длину массива f: ').strip()
length_f = int(length_f)
# Ввод массивов
d = []
f = []
print('Заполняем массив D')
for i in range(length_d):
    element = input(f'Введите элемент номер {i + 1}: ').strip()
    while not is_float_or_int(element):
        print('Некорректное число')
        element = input(f'Введите элемент номер {i + 1}: ').strip()
    d.append(float(element))
print('Заполняем массив F')
for i in range(length_f):
    element = input(f'Введите элемент номер {i + 1}: ').strip()
    while not is_float_or_int(element):
        print('Некорректное число')
        element = input(f'Введите элемент номер {i + 1}: ').strip()
    f.append(float(element))
# Формирование матрицы и подсчет среднего арифметического
a = []
av = []
for i in range(length_d):
    a.append([])
    summ = 0
    count = 0
    for j in range(length_f):
        el = m.sin(d[i] + f[j])
        a[i].append(el)
        if el > 0:
            summ += el
            count += 1
    if count == 0:
        av.append(0)
    else:
        av.append(summ / count)
# Подсчет элементов, меньших среднего арифметического
l = []
for i in range(length_d):
    num = 0
    for j in range(length_f):
        if a[i][j] < av[i]:
            num += 1
    l.append(num)
# Вывод массива
if len(a) == 0:
    print(f'Текущая матрица: {a}')
# Прохождение по каждому элементу и создание строки ответа
for i in range(length_d):
    line = ''
    for j in range(length_f):
        line += f'[{a[i][j]:4.3g}]'
    if i == 0:
        line = 'Текущая матрица: ' + line
    else:
        line = ' ' * 17 + line
    line += f' {av[i]} {l[i]}'
    print(line)

