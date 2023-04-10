# Эта программа предназначена для замены всех гласных английских букв на точки

# Входные данные: матрица

# Выходные данные: измененная матрица


length = input('Введите длину матрицы: ').strip()
while not length.isdecimal() or int(length) == 0:
    print('Некорректное число')
    length = input('Введите длину матрицы: ').strip()
length = int(length)
width = input('Введите высоту матрицы: ').strip()
while not width.isdecimal() or int(width) == 0:
    print('Некорректное число')
    width = input('Введите высоту матрицы: ').strip()
width = int(width)
massive = []
# Ввод элементов
for i in range(width):
    massive.append([])
    for j in range(length):
        el = input(f'Введите элемент номер {j + 1} в строку номер {i + 1}: ')
        while len(el) != 1:
            print('Введен не один символ')
            el = input(f'Введите элемент номер {j + 1} в строку номер {i + 1}: ')
        massive[i].append(el)
check_massive = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U', 'y', 'Y']
# Проход по каждому элементу и проверка на гласную
for i in range(width):
    for j in range(length):
        if massive[i][j] in check_massive:
            massive[i][j] = '.'
if len(massive) == 0:
    print(f'Текущая матрица: {massive}')
# Прохождение по каждому элементу и создание строки ответа
for i in range(len(massive)):
    line = ''
    for j in range(len(massive[0])):
        line += f'[{massive[i][j]}]'
    if i == 0:
        line = 'Текущая матрица: ' + line
    else:
        line = ' ' * 17 + line
    print(line)