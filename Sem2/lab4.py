from tkinter import *
from tkinter.messagebox import showerror, showinfo
import math as m


# сведения о программе
def show_info():
    showinfo(title="Что делает программа?", message="Программа предназначена для рисования точек и окружностей "
                                                    "и поиска прямой, пересекающей большее количество окружностей")


# сведения о создателе
def show_creator():
    showinfo(title="Информация о создателе", message="Ваше имя")


# как пользоваться программой
def use():
    showinfo(title="Помощь", message="Нажмите левой кнопкой мыши, чтобы поставить точку. \n\n"
                                     "Нажмите и задержите правую кнопку мыши, проведите и отпустите, "
                                     "чтобы нарисовать окружность")


# очистить полотно, данные всех точек и окружностей
def clear(circles, points):
    canvas.delete("all")
    circles.clear()
    points.clear()


# добавить точку в массив (Х, У)
def add_point(event, points, circles):
    new_dot = (event.x, event.y)
    # добавить точку в массив, если такой еще нет
    if not (new_dot in points):
        points.append(new_dot)
    # отрисовать картинку заново
    draw_all(points, circles)


# обнаружить центр окружности нажатием
def add_center(event, circle_center):
    circle_center.append(event.x)
    circle_center.append(event.y)


# определить радиус, расстояние между двумя точками
def dist(x1, y1, x2, y2):
    return ((x1 - x2) **2 + (y1 - y2) **2) **0.5


# добавить круг (центр_Х, центр_У, радиус)
def add_circle(event, circles, circle_center, points):
    # конечная точка окружности
    r_dot = [event.x, event.y]
    # определение радиуса
    r = int(dist(circle_center[0], circle_center[1], r_dot[0], r_dot[1]))
    # добавить новый круг, если такого еще нет
    new_circle = (circle_center[0], circle_center[1], r)
    if not (new_circle in circles):
        circles.append(new_circle)
    # очистить переменную для центра, для добавления нового
    circle_center.clear()
    # отрисовать картинку
    draw_all(points, circles)


# проверка, пересекаются ли окружность и прямая
# уравнение прямой через 2 точки + расстояние от точки до прямой
# расстояние от центра окружности до прямой <= радиусу
def cross(dot1, dot2, circle):
    return abs(circle[1] * (dot2[0] - dot1[0]) + circle[0] * (dot1[1] - dot2[1]) + dot1[0] * (dot2[1] - dot1[1]) + dot1[1] * (dot1[0] - dot2[0])) \
           / m.sqrt((dot2[0] - dot1[0]) ** 2 + (dot1[1] - dot2[1]) ** 2) <= circle[2]


# нарисовать бесконечную линию
def draw_line(dot1, dot2):
    # проверка на то, является ли прямая вертикальной
    if dot2[0] == dot1[0]:
        x1 = x2 = dot2[0]
        y1 = 0
        y2 = 600
    else:
        # тангенс наклона линии
        tg = (dot2[1] - dot1[1]) / (dot2[0] - dot1[0])
        # максимальная размерность полотна
        max_size = 800
        # подсчет координат гарантировано далеко за пределами холста
        x1 = dot1[0] - max_size
        y1 = dot1[1] - int(tg * max_size)
        x2 = dot2[0] + max_size
        y2 = dot2[1] + int(tg * max_size)
    # отрисовка новой линии
    canvas.create_line(x1, y1, x2, y2, fill="black", width=3)


# отрисовка картинки с добавлениями
def draw_all(points, circles):
    # очистка полотна
    canvas.delete("all")
    # отрисовка кругов
    for i in circles:
        canvas.create_oval(i[0] - i[2], i[1] - i[2], i[0] + i[2], i[1] + i[2],
                           outline="green", width=4)
    # отрисовка точек как круг
    for i in points:
        x1, y1 = (i[0] - 1), (i[1] - 1)
        x2, y2 = (i[0] + 1), (i[1] + 1)
        canvas.create_oval(x1, y1, x2, y2, fill="red", outline="red", width=5)
    max_count = 0
    dots = ()
    # проверять только если можно построить прямую и есть хотя бы одна окружность
    if len(points) >= 2 and len(circles) >= 1:
        # перебор точек парами
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                cur_count = 0
                # для каждой пары точек просчитать все окружности
                for k in circles:
                    # подсчитать количество пересечений
                    if cross(points[i], points[j], k):
                        cur_count += 1
                # найти максимальное количество пересечений и запомнить эти точки
                if cur_count > max_count:
                    max_count = cur_count
                    dots = (points[i], points[j])
    # если точки нашлись, то рисовать линию
    if max_count != 0:
        draw_line(dots[0], dots[1])


# точки, центр новой окружности, окружности
points = []
circles = []
circle_center = []

# окно
window = Tk()

# Создание окна
window.title('Рисовалка')
window.geometry('720x620+50+100')
window.resizable(width=False, height=False)

# Создание верхнего меню
mainmenu = Menu(window)
window.config(menu=mainmenu)

# Каскады
infomenu = Menu(mainmenu, tearoff=0)
infomenu.add_command(label="О программе", command=show_info)
infomenu.add_command(label="О создателе", command=show_creator)

mainmenu.add_cascade(label="Справка", menu=infomenu)
mainmenu.add_cascade(label="Как пользоваться", command=use)
# команда очистить не только поле, но и все переменные
mainmenu.add_cascade(label="Очистить", command=lambda points=points, circles=circles: clear(points, circles))

# Рисовалка
canvas = Canvas(window, bg="white", height=600, width=700)
canvas.pack()
# если нажать левую кнопку мыши, то нарисовать точку
canvas.bind("<ButtonPress-1>", lambda event, points=points, circles=circles: add_point(event, points, circles))
# если нажать правую кнопку мыши, то запомнится центр окружности
canvas.bind("<ButtonPress-3>", lambda event, circlecenter=circle_center: add_center(event, circle_center))
# как только правая кнопка мыши отожмется, запомнится вторая точка окружности, по это точкам построится окружность
canvas.bind("<ButtonRelease-3>", lambda event, circles=circles, circle_center=circle_center, points=points: add_circle(event, circles, circle_center, points))

# бесконечный процесс
window.mainloop()