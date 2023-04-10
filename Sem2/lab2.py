from tkinter import *
from tkinter.messagebox import showerror, showinfo
from matplotlib import pyplot as plt
from scipy import optimize


def make_graph(data, graph_data_x, graph_answers_x):
    plt.get_current_fig_manager().window.wm_geometry('+1000+100')
    plt.title('График функции')
    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    plt.axis([data[0], data[1], int(f(data[0])) - 10, int(f(data[1])) + 10])
    graph_data_y = []
    graph_answers_y = []
    for y in graph_data_x:
        graph_data_y.append(f(y))
    for y in graph_answers_x:
        graph_answers_y.append(0)
    plt.plot(graph_data_x, graph_data_y)
    plt.scatter(graph_answers_x, graph_answers_y, color='red', s=40, marker='*')
    plt.grid()
    plt.show()


def get_answers(event):
    table.config(state="normal")
    table.delete(0.0, END)
    # data = [left, right, h, nmax, eps, flag]
    data = [''] * 6
    check_input(data)
    #data = [-2, 4, 0.2, 100, 1e-4, True]
    graph_data = []
    graph_answers = []
    if data[5]:
        table.insert(1.0, '-----------------------------------------------------\n')
        table.insert(2.1, '| № корня |  [Xi; Xi + 1]  |    x\'    |     f(x\')   |\n')
        table.insert(3.0, '-----------------------------------------------------\n')

        left = data[0]
        right = left + data[2]
        root_count = 0
        while right <= data[1]:
            graph_data.append(left)
            flag = True
            try:
                answer = optimize.brentq(f, left, right)
            except:
                flag = False
            if flag:
                graph_data.append(answer)
                graph_answers.append(answer)
                root_count += 1
                index = str(2 + root_count * 2) + '.0'
                table.insert(index, f'|{root_count:<9d}| [{left:<5.2f}; {right:<5.2f}] | {answer:<8.5g} | '
                                    f'{f(answer):<11.5g} |\n')
                table.insert(str(3 + root_count * 2) + '.0', '-----------------------------------------------------\n')
            left = right
            right += data[2]
        table.config(state="disabled")
        make_graph(data, graph_data, graph_answers)



def f(x):
    return x**3 - 3 * x**2 + 3


def input_error(n):
    if n == 0:
        message = "Функция введена неверно"
    elif n == 1:
        message = "Левая граница введена неверно"
    elif n == 2:
        message = "Правая граница введена неверно"
    else:
        message = "Шаг введен неверно"
    showerror(title='Ошибка!', message=message)


def check_input(data):
    data[5] = True
    left = left_input.get()
    if not check_number(left):
        data[5] = False
        input_error(1)
    else:
        data[0] = float(left)
    right = right_input.get()
    if not check_number(right):
        data[5] = False
        input_error(2)
    else:
        if check_number(left) and float(right) > float(left):
            data[1] = float(right)
        else:
            data[5] = False
            input_error(2)
    h = h_input.get()
    if not check_number(h):
        data[5] = False
        input_error(3)
    else:
        data[2] = float(h)


def check_number(n):
    try:
        float(n)
    except:
        return False
    return True


def clear():
    left_input.delete(0, END)
    right_input.delete(0, END)
    h_input.delete(0, END)
    table.config(state="normal")
    table.delete(0.0, END)
    table.config(state="disabled")


def show_info():
    showinfo(title="Что делает программа?", message="Программа предназначена для поиска корней функции "
                                "при помощи метода Брента и построения графика этой функции")


def show_creator():
    showinfo(title="Информация о создателе", message="Ваше имя")

data = [''] * 6

window = Tk()

# Создание окна
window.title('Метод Брента')
window.geometry('900x400+50+100')
window.resizable(width=False, height=False)

# Создание верхнего меню
mainmenu = Menu(window)
window.config(menu=mainmenu)

infomenu = Menu(mainmenu, tearoff=0)
infomenu.add_command(label="О программе", command=show_info)
infomenu.add_command(label="О создателе", command=show_creator)

mainmenu.add_cascade(label="Очистить поля", command=clear)
mainmenu.add_cascade(label="Справка", menu=infomenu)

# Создание полей и кнопок
table = Text(window)
table.place(x=450, y=50, width=440, height=300)

left_label = Label(window, text='Введите начало отрезка:', font='Arial 12')
left_label.place(x=5, y=90)
left_input = Entry(window, background='white', font='Arial 12')
left_input.place(x=240, y=90, width=200, height=30)

right_label = Label(window, text='Введите конец отрезка:', font='Arial 12')
right_label.place(x=5, y=130)
right_input = Entry(window, background='white', font='Arial 12')
right_input.place(x=240, y=130, width=200, height=30)

h_label = Label(window, text='Введите шаг:', font='Arial 12')
h_label.place(x=5, y=170)
h_input = Entry(window, background='white', font='Arial 12')
h_input.place(x=240, y=170, width=200, height=30)

solve_btn = Button(text='Получить корни!', font=('Arial', '12'))
solve_btn.bind('<Button-1>', get_answers)
solve_btn.place(x=120, y=330, width=200, height=50)

window.mainloop()