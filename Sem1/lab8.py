# Вариант 4,2

# Программа предназначена для выполнения действий с матрицей

# Входные данные: номер команды, который стоит применить к матрице

# Выходные данные: проделывание операции с матрицей


# Функция проверки на int
def str_is_int(massive_item):
    if len(massive_item) == 0:
        return False
    if massive_item == '0':
        return True
    length = len(massive_item)
    if length >= 2 and massive_item[:2] == '-0':
        return False
    for i in range(length):
        # Если начинается с 0, то неверный ввод
        if i == 0 and massive_item[i] == '0':
            return False
        # Проверка на знаки, отличные от '-', '.'
        if not massive_item[i].isdecimal():
            # Если '-' первый символ, то это просто число
            if massive_item[i] == '-' and i == 0 and not length == 1:
                continue
            # Все остальное некорректный ввод
            else:
                return False
    return True


# Инициализация переменных
massive = []
flag = True

while flag:
    # Меню
    print('''
-----------------------------------------------------------------------------------------------
| 1) Ввести матрицу                                                                           |
| 2) Добавить строку                                                                          |
| 3) Удалить строку                                                                           |
| 4) Добавить столбец                                                                         |
| 5) Удалить столбец                                                                          |
| 6) Найти строку, имеющую наименьшее количество четных элементов                             |
| 7) Переставить местами строки с наибольшим и наименьшим количеством отрицательных элементов |
| 8) Найти столбец, имеющий наименьшее количество отрицательных элементов                     |
| 9) Переставить местами столбцы с максимальной и минимальной суммой элементов                |
| 10) Вывести текущую матрицу                                                                 |
-----------------------------------------------------------------------------------------------
    ''')

    # Ввод и проверка номера операции на допустимое значение
    operation = input('Выберете номер операции от 1 до 10 или введите 0, чтобы выйти: ').strip()
    while not operation.isdecimal() or not 1 <= int(operation) <= 10:
        if operation == '0':
            flag = False
            break
        print('Неправильный номер операции')
        operation = input('Выберете номер операции от 1 до 10 или введите 0, чтобы выйти: ').strip()
    operation = int(operation)

    if operation == 1:
        # Очистка массива
        massive.clear()
        # Инициализация длины и высоты
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
        # Ввод элементов
        for i in range(width):
            massive.append([])
            for j in range(length):
                element = input(f'Введите элемент номер {j + 1} в строку номер {i + 1}: ').strip()
                while not str_is_int(element):
                    print('Некорректное число')
                    element = input(f'Введите элемент номер {j + 1} в строку номер {i + 1}: ').strip()
                massive[i].append(int(element))

    elif operation == 2:
        # Добавления строки любой длины
        if len(massive) == 0:
            massive.append([])
            check_str = input('Введите элементы новой строки через пробел: ').split()
            # Проверка каждого символа на корректность
            for i in range(len(check_str)):
                # Вводить значение, пока оно не будет корректно
                while not str_is_int(check_str[i]):
                    print(f'Элемент номер {i + 1} введен некорректно')
                    check_str[i] = input(f'Повторите ввод элемента номер {i + 1}: ').strip()
                massive[0].append(int(check_str[i]))
        else:
            # Инициализация элемента
            new_str = []
            place = input('Введите место, в которое нужно вставить строку: ').strip()
            while not place.isdecimal() or not 1 <= int(place) <= len(massive) + 1:
                print('Неправильный номер строки')
                place = input(f'Введите место для строки из промежутка [1, {len(massive) + 1}]: ').strip()
            place = int(place)
            # Добавление строки определенной длины
            for i in range(len(massive[0])):
                str_element = input(f'Введите элемент номер {i + 1}: ').strip()
                while not str_is_int(str_element):
                    print('Некорректное число')
                    str_element = input(f'Введите элемент номер {i + 1}: ').strip()
                new_str.append(int(str_element))
            command = input('Нажмите 1, чтобы добавить строку алгоритмически, или 2, чтобы добавить ее с помощью insert(): ').strip()
            while not (command == '1' or command == '2'):
                print('Неправилльный номер команды')
                command = input('Нажмите 1, чтобы добавить строку алгоритмически, или 2, чтобы добавить ее с помощью insert(): ').strip()
            # Выбор алгоритма добавления
            if command == '1':
                massive.append(new_str)
                # Перемещение элемента на нужное место
                for i in range(len(massive) - 1, place - 1, -1):
                    massive[i - 1], massive[i] = massive[i], massive[i - 1]
            else:
                massive.insert(place - 1, new_str)

    elif operation == 3:
        if len(massive) == 0:
            print('Невозможно выполнить операцию: матрица пустая')
        else:
            # Ввод и проверка номера элемента на допустимое значение
            element = input('Введите номер строки, которую стоит удалить: ').strip()
            while not element.isdecimal() or not 1 <= int(element) <= len(massive):
                print('Неправильный номер строки')
                element = input(f'Введите номер строки из промежутка [1, {len(massive)}], которую стоит удалить: ').strip()
            element = int(element)
            command = input('Нажмите 1, чтобы удалить строку алгоритмически, или 2, чтобы удалить ее с помощью pop(): ').strip()
            while not (command == '1' or command == '2'):
                print('Неправилльный номер команды')
                command = input('Нажмите 1, чтобы удалить строку алгоритмически, или 2, чтобы удалить ее с помощью pop(): ').strip()
            # Перемещение элемента в конец и обрезка
            if command == '1':
                for i in range(element - 1, len(massive) - 1):
                    massive[i] = massive[i + 1]
                massive.pop()
            else:
                massive.pop(element - 1)

    elif operation == 4:
        # Добавление столбца любой длины
        if len(massive) == 0:
            check_column = input('Введите элементы нового столбца через пробел: ').split()
            # Проверка каждого символа на корректность
            for i in range(len(check_column)):
                # Вводить значение, пока оно не будет корректно
                while not str_is_int(check_column[i]):
                    print(f'Элемент номер {i + 1} введен некорректно')
                    check_column[i] = input(f'Повторите ввод элемента номер {i + 1}: ').strip()
                check_column[i] = int(check_column[i])
            for i in range(len(check_column)):
                massive.append([])
                massive[i].append(check_column[i])
        else:
            # Инициализация элемента
            new_column = []
            place = input('Введите место, в которое нужно вставить столбец: ').strip()
            while not place.isdecimal() or not 1 <= int(place) <= len(massive[0]) + 1:
                print('Неправильный номер столбца')
                place = input(f'Введите место для столбца из промежутка [1, {len(massive[0]) + 1}]: ').strip()
            place = int(place)
            # Добавление столбца определенной длины
            for i in range(len(massive)):
                column_element = input(f'Введите элемент номер {i + 1}: ').strip()
                while not str_is_int(column_element):
                    print('Некорректное число')
                    column_element = input(f'Введите элемент номер {i + 1}: ').strip()
                new_column.append(int(column_element))
            command = input('Нажмите 1, чтобы добавить столбец алгоритмически, или 2, чтобы добавить его с помощью insert(): ').strip()
            while not (command == '1' or command == '2'):
                print('Неправилльный номер команды')
                command = input('Нажмите 1, чтобы добавить столбец алгоритмически, или 2, чтобы добавить его с помощью insert(): ').strip()
            # Выбор алгоритма добавления
            if command == '1':
                for i in range(len(massive)):
                    massive[i].append(new_column[i])
                # Перемещение элемента на нужное место
                for i in range(len(massive) - 1, place - 1, -1):
                    for j in range(len(massive[0])):
                        massive[i][j - 1], massive[i][j] = massive[i][j], massive[i][j - 1]
            else:
                for i in range(len(massive)):
                    massive[i].insert(place - 1, new_column[i])

    elif operation == 5:
        if len(massive) == 0:
            print('Невозможно выполнить операцию: матрица пустая')
        else:
            # Ввод и проверка номера элемента на допустимое значение
            element = input('Введите номер столбца, который стоит удалить: ').strip()
            while not element.isdecimal() or not 1 <= int(element) <= len(massive[0]):
                print('Неправильный номер стролбца')
                element = input(f'Введите номер столбца из промежутка [1, {len(massive[0])}], который стоит удалить: ').strip()
            element = int(element)
            command = input('Нажмите 1, чтобы удалить столбец алгоритмически, или 2, чтобы удалить его с помощью pop(): ').strip()
            while not (command == '1' or command == '2'):
                print('Неправилльный номер команды')
                command = input('Нажмите 1, чтобы удалить столбец алгоритмически, или 2, чтобы удалить его с помощью pop(): ').strip()
            # Перемещение элемента в конец и обрезка
            if command == '1':
                for i in range(len(massive)):
                    for j in range(element - 1, len(massive[0]) - 1):
                        massive[i][j] = massive[i][j + 1]
                    massive[i].pop()
            else:
                for i in range(len(massive)):
                    massive[i].pop(element - 1)

    elif operation == 6:
        if len(massive) == 0:
            print('Невозможно выполнить операцию: матрица пустая')
        elif len(massive) == 1:
            print(f'Строка с наименьшим количеством четных элементов: {massive[0]}')
        else:
            min_str = 0
            min_count = len(massive[0])
            # Проход по строкам
            for i in range(len(massive)):
                count = 0
                for j in range(len(massive[0])):
                    if massive[i][j] % 2 == 0:
                        count += 1
                if count < min_count:
                    min_count = count
                    min_str = i
            print(f'Строка с наименьшим количеством четных элементов: {massive[min_str]}')

    elif operation == 7:
        if len(massive) == 0:
            print('Невозможно выполнить операцию: матрица пустая')
        elif len(massive) == 1:
            print('Невозможно выполнить операцию: в матрице одна строка')
        else:
            max_num_str = -1
            i_max_str = 0
            i_min_str = 0
            min_num_str = -1
            # Проход по всем строкам, переопределение минимума и максимума
            for i in range(len(massive)):
                tek_num_str = 0
                for j in range(len(massive[0])):
                    if massive[i][j] < 0:
                        tek_num_str += 1
                if tek_num_str < min_num_str:
                    min_num_str = tek_num_str
                    i_min_str = i
                if tek_num_str > max_num_str:
                    max_num_str = tek_num_str
                    i_max_str = i
            # Перемещение строк
            massive[i_min_str], massive[i_max_str] = massive[i_max_str], massive[i_min_str]
            
    elif operation == 8:
        if len(massive) == 0:
            print('Невозможно выполнить операцию: матрица пустая')
        else:
            min_num_col = len(massive[0])
            j_min_col_sum = 0
            # Проход по каждому элементу столбца и переопределение минимума
            for j in range(len(massive[0])):
                tek_num_col = 0
                for i in range(len(massive)):
                    if massive[i][j] < 0:
                        tek_num_col += 1
                if tek_num_col < min_num_col:
                    min_num_col = tek_num_col
                    j_min_col_sum = j
            answer = '['
            # заись нужного столбца в ответ
            for i in range(len(massive)):
                answer += f'{massive[i][j_min_col_sum]}, '
            answer = answer.rstrip(', ') + ']'
            print('Столбец с минимальным количеством отрицательных элементов:', answer)

    elif operation == 9:
        if len(massive) == 0:
            print('Невозможно выполнить операцию: матрица пустая')
        elif len(massive[0]) == 1:
            print('Невозможно выполнить операцию: в матрице один столбец')
        else:
            max_sum_col = 0
            # Проход по первому столбцу для инициализации минимума и максимума
            for i in range(len(massive)):
                max_sum_col += massive[i][0]
            j_max_col = 0
            j_min_col = 0
            min_sum_col = max_sum_col
            # Проход по остальным столбцам, переопределение минимума и максимума
            for j in range(1, len(massive[0])):
                tek_sum_col = 0
                for i in range(len(massive)):
                    tek_sum_col += massive[i][j]
                if tek_sum_col > max_sum_col:
                    max_sum_col = tek_sum_col
                    j_max_col = j
                if tek_sum_col < min_sum_col:
                    min_sum_col = tek_sum_col
                    j_min_col = j
            # Перемещение элементов в каждой строке
            for i in range(len(massive)):
                massive[i][j_min_col], massive[i][j_max_col] = massive[i][j_max_col], massive[i][j_min_col]

    elif operation == 10:
        if len(massive) == 0:
            print(f'Текущий массив: {massive}')
        # Прохождение по каждому элементу и создание строки ответа
        for i in range(len(massive)):
            line = ''
            for j in range(len(massive[0])):
                line += f'[{massive[i][j]:>4}]'
            if i == 0:
                line = 'Текущий массив: ' + line
            else:
                line = ' ' * 16 + line
            print(line)