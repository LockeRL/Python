# Эта программа предназначена для вывода среза по второму инидексу трехмерного массива

# Входные данные: трехмерный массив, номер среза

# Выходные данные: срез


# Ввод размерности
length = input('Введите длину матрицы: ').strip()
while not length.isdecimal() or int(length) == 0:
    print('Некорректное число')
    length = input('Введите длину матрицы: ').strip()
length = int(length)
width = input('Введите ширину матрицы: ').strip()
while not width.isdecimal() or int(width) == 0:
    print('Некорректное число')
    width = input('Введите ширину матрицы: ').strip()
width = int(width)
height = input('Введите высоту матрицы: ').strip()
while not height.isdecimal() or int(height) == 0:
    print('Некорректное число')
    height = input('Введите высоту матрицы: ').strip()
height = int(height)
massive = []
# Ввод элементов
for i in range(height):  # 0Z
    massive.append([])
    for j in range(width):  # 0Y
        massive[i].append([])
        for k in range(length):  # 0X
            massive[i][j].append(input(f'Введите для {i + 1}-й матрицы элемент из {j + 1}-й строки номер {k + 1}: '))
# Ввод номера среза
element = input('Введите номер среза, который стоит вывести: ').strip()
while not element.isdecimal() or not 1 <= int(element) <= width:
    print('Неправильный номер среза')
    element = input(f'Введите номер среза из промежутка [1, {width}], который стоит вывести: ').strip()
element = int(element) - 1
# Вывод среза
for i in range(height - 1, -1, -1):
    line = ''
    for j in range(length):
        line += f'[{massive[i][element][j]}]'
    if i == (height - 1):
        line = 'Текущая матрица: ' + line
    else:
        line = ' ' * 17 + line
    print(line)
