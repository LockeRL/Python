# Вариант 4,3

# Программа предназначена для выполнения действий с массивом

# Входные данные: номер команды, который стоит применить к программе

# Выходные данные: проделывание операции с массивом


count = 0
massive = []

while True:
    # Вывод меню
    if count % 3 == 0:
        print('''1) Очистить список и ввести его с клавиатуры
2) Добавить элемент в произвольное место списка
3) Удалить произвольный элемент из списка (по номеру)
4) Очистить список
5) Поиск элемента с наибольшим числом подряд идущих пробелов
6) Замена всех заглавных согласных английских букв на строчные
          ''')
    # Проверка на корректность операции
    operation = int(input('Введите номер операции: '))
    while not 1 <= operation <= 6:
        print('Неверный номер операции')
        operation = int(input('Введите номер операции: '))

    if operation == 1:
        i = 1
        massive.clear()
        # Ввод элементов
        while True:
            new_str = input(f'Введите элемент списка номер {i} или нажмите \'Enter\', чтобы завершить ввод: ')
            if new_str == '':
                break
            massive.append(new_str)
            i += 1

    elif operation == 2:
        if len(massive) == 0:
            print('Невозможно выполнить операцию: список пуст')
        else:
            # Инициализация элемента
            value = input('Введите элемент, которые следует добавить: ')
            place = int(input('Введите место, в которое нужно вставить элемент: '))
            while not 1 <= place <= len(massive):
                print('Неправильный номер элемента')
                element = int(input(f'Введите место для элемента из промежутка [1, {len(massive)}]: '))
            massive.append(value)
            # Перемещение элемента на нужное место
            for i in range(len(massive) - 1, place - 1, -1):
                massive[i - 1], massive[i] = massive[i], massive[i - 1]

    elif operation == 3:
        if len(massive) == 0:
            print('Невозможно выполнить операцию: список пуст')

        else:
            # Ввод и проверка номера элемента на допустимое значение
            element = int(input('Введите номер элемента, которые стоит удалить: '))
            while not 1 <= element <= len(massive):
                print('Неправильный номер элемента')
                element = int(
                    input(f'Введите номер элемента из промежутка [1, {len(massive)}], которые стоит удалить: '))
            # Перемещение элемента в конец и обрезка
            for i in range(element - 1, len(massive) - 1):
                massive[i], massive[i + 1] = massive[i + 1], massive[i]
            massive.pop()

    elif operation == 4:
        massive.clear()

    elif operation == 5:
        if len(massive) == 0:
            print('Невозможно выполнить операцию: список пуст')

        else:
            max_i = 0
            max_item_len = 0
            max_massive_len = 0
            # Проход по всем элементам массива
            for i in range(len(massive)):
                len_i = 0
                # Проход по каждому символу и подсчет подпоследовательностей
                for _ in massive[i]:
                    if _ == ' ':
                        len_i += 1
                    else:
                        # Сравнение наибольших подпоследовательностей элемента
                        if len_i > max_item_len:
                            max_item_len = len_i
                            len_i = 0
                # Сравнение максимальной длины подпоследовательности среди всех элементов
                if max_item_len > max_massive_len:
                    max_i = i
                    max_massive_len = max_item_len
            print(f'Элемент с наибольшим числом подряд идущих пробелов: {massive[max_i]}')

    elif operation == 6:
        check_cons = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'q', 'v', 'w',
                  'x', 'z']
        # Пройтись по списку и заменить согласные заглавными в каждом элементе
        for symbol in check_cons:
            for item in range(len(massive)):
                massive[item] = massive[item].replace(symbol, symbol.title())

    print(f'Текущий массив: {massive}')

    count += 1