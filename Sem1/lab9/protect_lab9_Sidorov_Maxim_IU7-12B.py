length = int(input('Введите размерность матрицы: '))
mass = []
for i in range(length):
    mass.append([])
    for j in range(length):
        mass[i].append(float(input(f'Введите элемент номер {j + 1} в строку номер {i + 1}: ')))
sum_main = 0
for i in range(length // 2 + 1, length):
    for j in range(length - i, i):
        sum_main += mass[i][j]
print(f'Сумма под главной диагональю: {sum_main}')
