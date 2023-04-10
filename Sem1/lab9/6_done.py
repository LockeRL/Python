# Эта программа предназначена для вычисления значения максимальных элементов исходной матрицы,
# определения среднего арифметического вычисленных максимальных значений.

# Входные данные: матрица и массив

# Выходные данные: матрица D, массивы I и R, среднее арифметическое значение


from functions import is_float_or_int


# Ввод размерностей матрицы D
length_d = input('Введите длину матрицы: ').strip()
while not length_d.isdecimal() or int(length_d) == 0:
    print('Некорректное число')
    length_d = input('Введите длину матрицы: ').strip()
length_d = int(length_d)
width_d = input('Введите высоту матрицы: ').strip()
while not width_d.isdecimal() or int(width_d) == 0:
    print('Некорректное число')
    width_d = input('Введите высоту матрицы: ').strip()
width_d = int(width_d)
d = []
# Ввод элементов матрицы D
for i in range(width_d):
    d.append([])
    for j in range(length_d):
        element = input(f'Введите элемент номер {j + 1} в строку номер {i + 1}: ').strip()
        while not is_float_or_int(element):
            print('Некорректное число')
            element = input(f'Введите элемент номер {j + 1} в строку номер {i + 1}: ').strip()
        d[i].append(float(element))
# Ввод размерностей массива D
length_i = input('Введите длину массива: ').strip()
while not length_i.isdecimal() or int(length_i) == 0:
    print('Некорректное число')
    length_i = input('Введите длину массива: ').strip()
length_i = int(length_i)
i_mass = []
# Заполнение массива строк
for i in range(length_i):
    element = input(f'Введите элемент номер {i + 1}: ').strip()
    while not element.isdecimal() or not 1 <= int(element) <= width_d:
        print('Некорректное число')
        element = input(f'Введите элемент номер {i + 1} из промежутка [1, {width_d}]: ').strip()
    i_mass.append(int(element))
r = []
# Заполнение массива R
for i in range(length_i):
    r.append(max(d[i_mass[i] - 1]))
# Подсчет среднего арифметического
mean = sum(r) / length_i
# Печать
for i in range(width_d):
    line = ''
    for j in range(length_d):
        line += f'[{d[i][j]}]'
    if i == 0:
        line = 'Текущая матрица: ' + line
    else:
        line = ' ' * 17 + line
    print(line)
print(f'Массив I: {i_mass}')
print(f'Массив R: {r}')
print(f'Среднее значение: {mean}')
