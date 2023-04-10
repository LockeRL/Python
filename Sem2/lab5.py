import pygame as pg
from math import cos, sin, pi


# Функция отрисовки паровоза
def draw_locomotive(screen, x, y, thickness, angle):
    # Трава
    pg.draw.rect(screen, GREEN, (0, y + 250, WIDTH, HEIGHT))
    # Небо
    pg.draw.rect(screen, BLUE, (0, 0, WIDTH, 490))

    # Корпус
    pg.draw.rect(screen, "red", (x, y, 100, 200))

    # Окно
    pg.draw.rect(screen, "blue", (x + 10, y + 35, 80, 80))

    # Крыша
    pg.draw.polygon(screen, "brown",
                    [(x - 25, y), (x + 125, y), (x - 25, y), (x + 50, y - 50), (x + 50, y - 50), (x + 125, y)])

    # Передняя часть
    pg.draw.rect(screen, "red", (x + 100 - thickness, y + 125, 100, 65 + thickness))

    # Труба
    pg.draw.rect(screen, "black", (x + 135, y + 50, 30, 80 - thickness))
    pg.draw.rect(screen, "black", (x + 115, y + 25, 70, 25 + thickness))

    # Нос
    pg.draw.polygon(screen, "brown",
                    [(x + 195, y + 125), (x + 250, y + 160),
                     (x + 250, y + 160), (x + 195, y + 190),
                     (x + 195, y + 190), (x + 195, y + 125)])

    # Заднее колесо
    draw_wheel(6, angle, surface=screen, color="black", center=(x + 25, y + 200), radius=50, width=thickness)
    draw_wheel(12, angle, surface=screen, color="black", center=(x + 25, y + 200), radius=35, width=thickness)

    # Переднее колесо
    draw_wheel(6, angle, surface=screen, color="black", center=(x + 150, y + 220), radius=30, width=thickness)
    draw_wheel(12, angle, surface=screen, color="black", center=(x + 150, y + 220), radius=15, width=thickness)


# Функция отрисовка колеса и спиц
def draw_wheel(count, angle, **kwargs):
    pg.draw.circle(**kwargs)
    delta_angle = 2 * pi / count
    curr_angle = angle
    for i in range(count):
        pg.draw.line(kwargs['surface'], "black", kwargs['center'],
                     (kwargs['center'][0] + kwargs['radius'] * cos(curr_angle),
                      kwargs['center'][1] + kwargs['radius'] * sin(curr_angle)))
        curr_angle += delta_angle


# Разрешение экрана
WIDTH, HEIGHT = SIZE = (600, 600)

pg.init()
screen = pg.display.set_mode(SIZE)
pg.display.set_caption('Максим Сидоров ИУ7-22Б')
clock = pg.time.Clock()
FPS = 60

# Цвета
GREEN = (93, 161, 48)
BLUE = (66, 170, 255)

# Параметры паровозика
x, y = 0, HEIGHT * 0.4
angle = 0
delta_angle = 0.02

running = True

while running:
    # Регулирование fps
    clock.tick(FPS)
    # Цикл отслеживания собыитий
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Отрисовка паровоза
    draw_locomotive(screen, x, y, 3, angle)

    # Изменение координаты паровоза
    x += 1
    # Изменение угла поворота колеса
    angle += delta_angle
    # Отрисовка изображения
    pg.display.flip()
# Закрытие окна
pg.quit()
