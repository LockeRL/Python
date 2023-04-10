def str_is_int(massive_item):
    if massive_item == '0':
        return 1

    length = len(massive_item)

    if length >= 2 and massive_item[:2] == '-0':
        return 0

    for i in range(length):

        # Если начинается с 0, то неверный ввод
        if i == 0 and massive_item[i] == '0':
            return 0

        # Проверка на знаки, отличные от '-', '.'
        if not massive_item[i].isdecimal():
            # Если '-' первый символ, то это просто число
            if massive_item[i] == '-' and i == 0 and not length == 1:
                continue
            # Все остальное некорректный ввод
            else:
                return 0
    return 1


# Функция проверяет, является ли строка числом
# 0-неверный ввод 1-целое -1-с плавающей точкой
def is_float_or_int(massive_item):
    # Переменные, отвечающающие за единственность знака
    dot_count = 0
    e_count = 0

    if len(massive_item) == 0:
        return 0

    for i in range(len(massive_item)):
        if massive_item[i] == '.':
            dot_count += 1
        if massive_item[i] == 'e':
            e_count += 1

    if dot_count == 1:

        item = massive_item.split('.')

        if not item[1].isdigit():
            return 0

        left_side = item[0]
        sign_count = 0

        for i in left_side:
            if i == '-':
                sign_count += 1

        if sign_count > 1:
            return 0

        else:
            left_side = left_side.strip('-')

            if len(left_side) == 0:
                return 0

            if left_side[0] == '0':

                if len(left_side) == 1:
                    return -1
                else:
                    return 0

            else:

                if left_side.isdigit():
                    return -1
                else:
                    return 0

    elif dot_count == 0 and e_count == 0:
        return str_is_int(massive_item)

    if e_count == 1:

        if massive_item == 'e':
            return 0

        new = massive_item.split('e')

        if not str_is_int(new[0]) == 1:
            return 0
        if not new[0].isnumeric() or new[0] == '0':
            return 0
        if len(new[1]) == 0:
            return 0
        if str_is_int(new[1]) == 1:

            if int(new[1]) < 0:
                return -1
            else:
                return 1

        return 0

    elif e_count > 1:
        return 0

    return 0