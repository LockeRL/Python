# Эта программа предназначена для транспонирования квадратной матрицы

# Входные данные: матрица

# Выходные данные: транспонированная матрица


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
        massive[i].append(input(f'Введите элемент номер {j + 1} в строку номер {i + 1}: '))
# Транспонирование
for i in range(length):
    for j in range(length):
        if i > j:
            continue
        massive[i][j], massive[j][i] = massive[j][i], massive[i][j]
# Вывод массива
if len(massive) == 0:
    print(f'Текущая матрица: {massive}')
# Прохождение по каждому элементу и создание строки ответа
for i in range(length):
    line = ''
    for j in range(length):
        line += f'[{massive[i][j]}]'
    if i == 0:
        line = 'Текущая матрица: ' + line
    else:
        line = ' ' * 17 + line
    print(line)