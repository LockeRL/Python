# Эта программа предназначена для нахождения максимального значения над главной диагональю и минимального - под
# побочной диагональю

# Входные данные: матрица

# Выходные данные: два значения


from functions import is_float_or_int


# Ввод размерности
length = input('Введите размерность квадратной матрицы: ').strip()
while not length.isdecimal() or int(length) == 0:
    print('Некорректное число')
    length = input('Введите размерность квадратной матрицы: ').strip()
length = int(length)
# Ввод массива
massive = []
for i in range(length):
    massive.append([])
    for j in range(length):
        element = input(f'Введите элемент номер {j + 1} в строку номер {i + 1}: ').strip()
        while not is_float_or_int(element):
            print('Некорректное число')
            element = input(f'Введите элемент номер {j + 1} в строку номер {i + 1}: ').strip()
        massive[i].append(float(element))
if length < 2:
    print('Невозможно определить значения')
else:
    # Подсчет максимума
    max_ = massive[0][1]
    for i in range(1, length - 1):
        if massive[i][i + 1] > max_:
            max_ = massive[i][i + 1]
    min_ = massive[length - 1][1]
    # Подсчет минимума
    for i in range(length - 2, 0, -1):
        if massive[i][length - i] < min_:
            min_ = massive[i][length - i]
    for i in range(length):
        line = ''
        for j in range(length):
            line += f'[{massive[i][j]:4.3g}]'
        if i == 0:
            line = 'Текущая матрица: ' + line
        else:
            line = ' ' * 17 + line
        print(line)
    print(f'Максимальное значение: {max_}')
    print(f'Минимальное значение: {min_}')
