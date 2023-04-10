# Вариант 8

# Программа предназначена для проверки времени, затрачиваемого на сортировку массивов методом расчески

# Входные данные: 3 количества элементов в массивах

# Выходные данные: таблица со временем, потраченным на сортировку

from random import randint
import time


def comb_sort(m, n):
    step_el = n
    swap = True
    while step_el > 1 or swap:
        step_el = max(1, int(step_el / 1.243))
        swap = False
        for i in range(n - step_el):
            if m[i] > m[i + step_el]:
                m[i], m[i + step_el] = m[i + step_el], m[i]
                swap = True
    return massive


def generate_ordered_list(n):
    mass = []
    left = -1000
    for i in range(n):
        value = randint(left, 1000)
        mass.append(value)
        left = value
    return mass


def generate_reversed_ordered_list(n):
    mass = []
    right = 1000
    for i in range(n):
        value = randint(-1000, right)
        mass.append(value)
        right = value
    return mass


# Ввод размеровов списков
N1 = input('Введите количество элементов первого массива: ')
while not N1.isdecimal() or int(N1) == 0:
    print('Некорректный ввод')
    N1 = input('Введите количество элементов первого массива: ')
N1 = int(N1)
N2 = input('Введите количество элементов второго массива: ')
while not N2.isdecimal() or int(N2) == 0:
    print('Некорректный ввод')
    N2 = input('Введите количество элементов второго массива: ')
N2 = int(N2)
N3 = input('Введите количество элементов третьего массива: ')
while not N3.isdecimal() or int(N3) == 0:
    print('Некорректный ввод')
    N3 = input('Введите количество элементов третьего массива: ')
N3 = int(N3)

list_of_length = [N1, N2, N3]
list_of_times = []
for i in list_of_length:
    # Сортировка неотсортированного массива
    massive = [randint(-1000, 1000) for _ in range(i)]
    start = time.time()
    massive = comb_sort(massive, i)
    list_of_times.append(time.time() - start)
    # Сортировка отсортированного массива
    massive = generate_ordered_list(i)
    start = time.time()
    massive = comb_sort(massive, i)
    list_of_times.append(time.time() - start)
    # Сортировка отсортированного в обратную сторону массива
    massive = generate_reversed_ordered_list(i)
    start = time.time()
    massive = comb_sort(massive, i)
    list_of_times.append(time.time() - start)
# Вывод сортировок
print(
f'''
------------------------------------------------------------------
|                                  | {N1 : <7} | {N2 : <7} | {N3 : <7} |
------------------------------------------------------------------
|       Упорядоченный список       | {list_of_times[1] : <7.5} | {list_of_times[4] : <7.5} | {list_of_times[7] : <7.5} |
------------------------------------------------------------------
|         Случайный список         | {list_of_times[0] : <7.5} | {list_of_times[3] : <7.5} | {list_of_times[6] : <7.5} |
------------------------------------------------------------------
| Упорядоченный в обратном порядке | {list_of_times[2] : <7.5} | {list_of_times[5] : <7.5} | {list_of_times[8] : <7.5} |
------------------------------------------------------------------
'''
)