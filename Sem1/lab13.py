# Входные данные: имя, фамилия, балл, оценка

# Выходные данные: результат операции в соответствии с меню


import struct
import os.path


# size = int(os.path.getsize('m.txt'))
# line_num = size // 34
# line = int(input('Line: '))
# with open('m.txt', 'rb+') as file:
#     for i in range(line_num - line):
#         file.seek(size - 34, 0)
#         note = file.read(34)
#         print(note)
#         file.seek((line - 1) * 34, 0)
#         file.write(note)
#         file.flush()
#     file.truncate(size - 34)


def initilize():
    name = input('Введите имя студента, оно должно содержать не более 15 символов: ').strip()
    while not name.isalpha() or len(name) == 0 or len(name) > 15:
        print('Некорректный ввод')
        name = input('Введите имя студента, оно должно содержать не более 15 символов: ').strip()
    if name == 'stop':
        return struct.pack(b'4s', b'stop')
    else:
        sur_name = input('Введите фамилию студента, она должно содержать не более 15 символов: ').strip()
        while not sur_name.isalpha() or len(sur_name) == 0 or len(sur_name) > 15:
            print('Некорректный ввод')
            sur_name = input('Введите фамилию студента, она должно содержать не более 15 символов: ').strip()
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
    return struct.pack(b'>15s15s2h', bytes(name, encoding='utf-8'), bytes(sur_name, encoding='utf-8'), points_math, points_prog)


def vows_cons(n, s):
    cons = 'qwrtpsdfghjkllzxcvbnmцкнгшщзхфвпрлджчсмтб'
    vow = 'eyuioaуеыаоэяию'
    count_vow = 0
    count_cons = 0
    for i in n:
        if i in cons:
            count_cons += 1
        elif i in vow:
            count_vow += 1
    if count_cons > count_vow:
        print(f'{n} {s}')


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
| 5) Удалить запись из базы данных по номеру строки                                          |
| 6) Определить студентов, у которых в имени согласных больше, чем гласных                   |
| 7) Определить студентов, у которых балл по программированию и мат.анализу больше 70        |
----------------------------------------------------------------------------------------------
''')
    # Инициализация операции
    operation = input('Введите номер операции от 0 до 7: ')
    while not operation.isdecimal() or int(operation) > 7:
        print('Некорректный ввод')
        operation = input('Введите номер операции от 0 до 7: ')
    operation = int(operation)
    if operation == 0:
        break
    if operation == 1:
        file_path = input('Введите путь до файла, который следует открыть или создать: ')
        length = len(file_path)
        while length <= 4 or not file_path[length - 4:length] == '.txt':
            print('Файл должен иметь расширение .txt')
            file_path = input('Введите путь до файла, который следует открыть или создать: ')
            length = len(file_path)
        try:
            flag = True
            file = open(file_path, 'rb')
            for i in range(0, os.path.getsize(file_path), 34):
                file.seek(i)
                try:
                    data = struct.unpack('>15s15s2h', file.read(34))
                except:
                    flag = False
                    break
                name1 = data[0].decode('utf-8').strip('\x00')
                surname = data[1].decode('utf-8').strip('\x00')
                if len(data) != 4:
                    flag = False
                if not name1.isalpha() and not surname.isalpha():
                    flag = False
                if data[2] > 100:
                    flag = False
                if data[3] > 100:
                    flag = False
            file.close()
        except:
            file = open(file_path, 'wb')
            file.close()
    if operation == 2:
        if file_path == '':
            print('Сначала выберите операцию 1')
        else:
            print('Если хотите прекратить запись в базу данных, в поле имя напишите stop')
            flag = True
            with open(file_path, 'wb') as file:
                while True:
                    s = initilize()
                    if s == struct.pack(b'4s', b'stop'):
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
                with open(file_path, 'rb') as file:
                    k = 0
                    for i in range(0, os.path.getsize(file_path), 34):
                        k += 1
                        file.seek(i)
                        try:
                            data = struct.unpack('>15s15s2h', file.read(34))
                            name1 = data[0].decode('utf-8').strip('\x00')
                            surname = data[1].decode('utf-8').strip('\x00')
                            print(f'{k}) Студент: {name1} {surname} имеет балл: {data[2]} и оценку: {data[3]}')
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
            with open(file_path, 'ab') as file:
                while True:
                    s = initilize()
                    if s == struct.pack(b'4s', b'stop'):
                        break
                    else:
                        file.write(s)
    if operation == 5:
        size = int(os.path.getsize(file_path))
        line_num = size // 34
        line = input('Введите номер записи, которую стоит удалить: ')
        while not line.isdecimal() or not 0 < int(line) <= line_num:
            print('Некорректный ввод')
            line = input(f'Введите номер записи из промежутка [{1}, {line_num}], которую стоит удалить: ')
        line = int(line)
        if size == 0:
            print('Файл пуст')
        else:
            with open(file_path, 'rb+') as file:
                file.seek((line - 1) * 34, 0)
                for i in range(line_num - line):
                    file.seek(34, 1)
                    note = file.read(34)
                    file.seek(-34 * 2, 1)
                    file.write(note)
                file.truncate(size - 34)
    if operation == 6:
        if file_path == '':
            print('Сначала выберите операцию 1')
        else:
            if not flag:
                print('База данных заполнена неверно, перезапишите данные, выбрав операцию 2')
            else:
                with open(file_path, 'rb') as file:
                    k = 0
                    for i in range(0, os.path.getsize(file_path), 34):
                        k += 1
                        file.seek(i)
                        data = struct.unpack('>15s15s2h', file.read(34))
                        name1 = data[0].decode('utf-8').strip('\x00')
                        surname = data[1].decode('utf-8').strip('\x00')
                        vows_cons(name1, surname)
                    if k == 0:
                        print('Файл пуст')
    if operation == 7:
        if file_path == '':
            print('Сначала выберите операцию 1')
        else:
            if not flag:
                print('База данных заполнена неверно, перезапишите данные, выбрав операцию 2')
            else:
                with open(file_path, 'rb') as file:
                    k = 0
                    for i in range(0, os.path.getsize(file_path), 34):
                        k += 1
                        file.seek(i)
                        data = struct.unpack('>15s15s2h', file.read(34))
                        name1 = data[0].decode('utf-8').strip('\x00')
                        surname = data[1].decode('utf-8').strip('\x00')
                        if int(data[2]) > 70 and int(data[3]) > 70:
                            print(f'{name1} {surname}')
                    if k == 0:
                        print('Файл пуст')