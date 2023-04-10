# Входные данные: имя, фамилия, балл, оценка

# Выходные данные: результат операции в соответствии с меню


def initilize():
    name = input('Введите имя студента: ')
    while not name.isalpha() or len(name) == 0:
        print('Некорректный ввод')
        name = input('Введите имя студента: ')
    if name == 'stop':
        return 'stop'
    else:
        sur_name = input('Введите фамилию студента: ')
        while not sur_name.isalpha() or len(sur_name) == 0:
            print('Некорректный ввод')
            sur_name = input('Введите фамилию студента: ')
        points_math = input('Введите балл студента по мат.анализу от 0 до 100: ')
        while not points_math.isdecimal() or int(points_math) > 100:
            print('Некорректный ввод')
            points_math = input('Введите балл студента по мат.анализу от 0 до 100: ')
        points_math = int(points_math)
        points_prog = input('Введите балл студента по программированию от 0 до 100: ')
        while not points_prog.isdecimal() or int(points_prog) > 100:
            print('Некорректный ввод')
            points_prog = input('Введите балл студента по программированию от 0 до 100: ')
        points_prog = int(points_prog)
    return f'{name};{sur_name};{points_math};{points_prog}\n'


def vows_cons(s):
    cons = 'qwrtpsdfghjkllzxcvbnmцкнгшщзхфвпрлджчсмтб'
    vow = 'eyuioaуеыаоэяию'
    count_vow = 0
    count_cons = 0
    for i in s:
        if i in cons:
            count_cons += 1
        elif i in vow:
            count_vow += 1
    if count_cons > count_vow:
        print(f'{data[0]} {data[1]}')


file_path = ''
while True:
    print('''
----------------------------------------------------------------------------------------------
| Выберите операцию, которую применить к массиву:                                            |
| 0) Выйти из программы                                                                      |
| 1) Выбрать файл для работы                                                                 |
| 2) Инициализировать базу данных                                                            | 
| 3) Вывести содержимое базы данных                                                          |
| 4) Добавить запись в базу данных                                                           |
| 5) Определить студентов, у которых в имени согласных больше, чем гласных                   |
| 6) Определить студентов, у которых балл по программированию и мат.анализу больше 70        |
----------------------------------------------------------------------------------------------
''')
    # Инициализация операции
    operation = input('Введите номер операции от 0 до 6: ')
    while not operation.isdecimal() or int(operation) > 6:
        print('Некорректный ввод')
        operation = input('Введите номер операции от 0 до 6: ')
    operation = int(operation)
    if operation == 0:
        break
    if operation == 1:
        file_path = input('Введите путь до файла, который следует открыть или создать: ')
        length = len(file_path)
        while length <= 4 or not file_path[length - 4 : length] == '.txt':
            print('Файл должен иметь расширение .txt')
            file_path = input('Введите путь до файла, который следует открыть или создать: ')
            length = len(file_path)
        try:
            flag = True
            file = open(file_path, 'r')
            for line in file:
                try:
                    data = line.strip().split(';')
                    if len(data) != 4:
                        flag = False
                    if not data[0].isalpha() and not data[1].isalpha():
                        flag = False
                    if not data[2].isdecimal() or int(data[2]) > 100:
                        flag = False
                    if not data[3].isdecimal() or int(data[3]) > 100:
                        flag = False
                except:
                    flag = False
                    break
            file.close()
        except:
            file = open(file_path, 'w')
            file.close()
    if operation == 2:
        if file_path == '':
            print('Сначала выберите операцию 1')
        else:
            print('Если хотите прекратить запись в базу данных, в поле имя напишите stop')
            flag = True
            with open(file_path, 'w') as file:
                while True:
                    s = initilize()
                    if s =='stop':
                        break
                    else:
                        file.write(s)
    if operation == 3:
        if file_path == '':
            print('Сначала выберите операцию 1')
        else:
            if not flag:
                print('База данных заполнена неверно, перезапишите данные, выбрав операцию 2')
            else:
                with open(file_path, 'r') as file:
                    k = 0
                    for line in file:
                        k += 1
                        try:
                            data = line.strip().split(';')
                            print(f'Студент: {data[0]} {data[1]} имеет балл: {data[2]} и оценку: {data[3]}')
                        except:
                            print('База данных заполнена неверно, перезапишите данные, выбрав операцию 2')
                            flag = False
                            break
                    if k == 0:
                        print('Файл пуст')
    if operation == 4:
        if file_path == '':
            print('Сначала выберите операцию 1')
        else:
            print('Если хотите прекратить запись в базу данных, в поле имя напишите stop')
            with open(file_path, 'a') as file:
                while True:
                    s = initilize()
                    if s == 'stop':
                        break
                    else:
                        file.write(s)
    if operation == 5:
        if file_path == '':
            print('Сначала выберите операцию 1')
        else:
            if not flag:
                print('База данных заполнена неверно, перезапишите данные, выбрав операцию 2')
            else:
                with open(file_path, 'r') as file:
                    k = 0
                    for line in file:
                        k += 1
                        data = line.strip().split(';')
                        vows_cons(data[0])
                    if k == 0:
                        print('Файл пуст')
    if operation == 6:
        if file_path == '':
            print('Сначала выберите операцию 1')
        else:
            if not flag:
                print('База данных заполнена неверно, перезапишите данные, выбрав операцию 2')
            else:
                with open(file_path, 'r') as file:
                    k = 0
                    for line in file:
                        k += 1
                        data = line.strip().split(';')
                        if int(data[2]) > 70 and int(data[3]) > 70:
                            print(f'{data[0]} {data[1]}')
                    if k == 0:
                        print('Файл пуст')