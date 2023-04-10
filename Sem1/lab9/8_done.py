# Эта программа предназначена для построчного перемножения матриц A и B одинаковой размерности и
# сложения всех элементов в столбцах матрицы C и записи их в массив V

# Входные данные: матрица A и матрица B

# Выходные данные: матрица C и массив D


from functions import is_float_or_int


# Ввод размерностей матрицы D
length_a = input('Введите длину матрицы: ').strip()
while not length_a.isdecimal() or int(length_a) == 0:
    print('Некорректное число')
    length_a = input('Введите длину матрицы: ').strip()
length_a = int(length_a)
width_a = input('Введите высоту матрицы: ').strip()
while not width_a.isdecimal() or int(width_a) == 0:
    print('Некорректное число')
    width_a = input('Введите высоту матрицы: ').strip()
width_a = int(width_a)
a = []
# Ввод элементов матрицы A
print('Заполняем матрицу A')
for i in range(width_a):
    a.append([])
    for j in range(length_a):
        element = input(f'Введите элемент номер {j + 1} в строку номер {i + 1}: ').strip()
        while not is_float_or_int(element):
            print('Некорректное число')
            element = input(f'Введите элемент номер {j + 1} в строку номер {i + 1}: ').strip()
        a[i].append(float(element))
b = []
# Ввод элементов матрицы B
print('Заполняем матрицу B')
for i in range(width_a):
    b.append([])
    for j in range(length_a):
        element = input(f'Введите элемент номер {j + 1} в строку номер {i + 1}: ').strip()
        while not is_float_or_int(element):
            print('Некорректное число')
            element = input(f'Введите элемент номер {j + 1} в строку номер {i + 1}: ').strip()
        b[i].append(float(element))
c = []
# Заполнение матрицы C
for i in range(width_a):
    c.append([])
    for j in range(length_a):
        c[i].append(a[i][j] * b[i][j])
v = [0] * length_a
# Заполнение массива V
for i in range(width_a):
    for j in range(length_a):
        v[j] += c[i][j]
# Печать
for i in range(width_a):
    line = ''
    for j in range(length_a):
        line += f'[{c[i][j]}]'
    if i == 0:
        line = 'Текущая матрица: ' + line
    else:
        line = ' ' * 17 + line
    print(line)
print(f'Массив V: {v}')