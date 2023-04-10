# Эта программа предназначена для подсчета в каждой строке матрицы D количества элементов, превышающих
# сумму элементов соответствующих строк матрицы Z, размещения этих количеств в массиве G,
# умножения матрицы D на максимальный элемент массива G

# Входные данные: матрица D, матрица Z

# Выходные данные: измененная матрица D


from functions import is_float_or_int


# Ввод размерностей
length_d = input('Введите длину матрицы D: ').strip()
while not length_d.isdecimal() or int(length_d) == 0:
    print('Некорректное число')
    length_d = input('Введите длину матрицы D: ').strip()
length_d = int(length_d)
width_d = input('Введите высоту матрицы D: ').strip()
while not width_d.isdecimal() or int(width_d) == 0:
    print('Некорректное число')
    width_d = input('Введите высоту матрицы D: ').strip()
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
# Ввод размерностей
length_z = input('Введите длину матрицы Z: ').strip()
while not length_z.isdecimal() or int(length_z) == 0:
    print('Некорректное число')
    length_z = input('Введите длину матрицы Z: ').strip()
length_z = int(length_z)
width_z = input('Введите высоту матрицы Z: ').strip()
while not width_z.isdecimal() or int(width_z) == 0 or int(width_z) < width_d:
    print('Некорректное число' + (', в матрице Z строк должно быть не меньше, чем в матрице D'
                                  if int(width_z) < width_d else ''))
    width_z = input('Введите высоту матрицы Z: ').strip()
width_z = int(width_z)
z = []
# Ввод элементов матрицы Z
for i in range(width_z):
    z.append([])
    for j in range(length_z):
        element = input(f'Введите элемент номер {j + 1} в строку номер {i + 1}: ').strip()
        while not is_float_or_int(element):
            print('Некорректное число')
            element = input(f'Введите элемент номер {j + 1} в строку номер {i + 1}: ').strip()
        z[i].append(float(element))
# Заполнение массива G
g = []
for i in range(width_d):
    summ_z = sum(z[i])
    count = 0
    for j in range(length_d):
        if d[i][j] > summ_z:
            count += 1
    g.append(count)
# Подсчет максимума и переопределение матрицы D
max_ = max(g)
for i in range(width_d):
    for j in range(length_d):
        d[i][j] *= max_
# Прохождение по каждому элементу и создание строки ответа
for i in range(width_d):
    line = ''
    for j in range(length_d):
        line += f'[{d[i][j]:4.3g}]'
    if i == 0:
        line = 'Текущая матрица: ' + line
    else:
        line = ' ' * 17 + line
    print(line)