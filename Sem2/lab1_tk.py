# Программа предназначена для сложения/вычитания двух чисел в девятеричной системе

import tkinter as tk
from tkinter import messagebox


# Подсчет суммы и разности
def SummSign(a, b):
    var = ['', False]
    if a.startswith('-') and b.startswith('-'):
        var[0] = '-'
    elif not a.startswith('-') and not b.startswith('-'):
        var[0] = ''
    elif not a.startswith('-') and b.startswith('-'):
        var[1] = True
        if float(a) > float(b.lstrip('-')):
            var[0] = ''
        else:
            var[0] = '-'
    else:
        var[1] = True
        if float(a) > float(b.lstrip('-')):
            var[0] = '-'
        else:
            var[0] = ''
    return var

def SubtrSign(a, b):
    var = ['', False]
    if a.startswith('-') and b.startswith('-'):
        if float(a.lstrip('-')) > float(b.lstrip('-')):
            var[0] = '-'
        else:
            var[0] = ''
    elif not a.startswith('-') and not b.startswith('-'):
        if float(a) > float(b):
            var[0] = ''
        else:
            var[0] = '-'
    elif not a.startswith('-') and b.startswith('-'):
        var[0] = ''
        var[1] = True
    else:
        var[1] = True
        var[0] = '-'
    return var

def FullNum(a, b, s):
    var = list()
    if not '.' in a:
        a += '.0'
    if not '.' in b:
        b += '.0'
    if a.endswith('.'):
        a += '0'
    if b.endswith('.'):
        b += '0'
    if s == "+":
        var = SummSign(a, b)
    else:
        var = SubtrSign(a, b)
    b = b.lstrip('-')
    a = a.lstrip('-')
    if float(a) < float(b):
        a, b = b, a
    aL, aR = a.split('.')
    bL, bR = b.split('.')
    bL = '0' * (len(aL) - len(bL)) + bL
    point = max(len(aR), len(bR))
    if len(aR) > len(bR):
        bR += '0' * (len(aR) - len(bR))
    else:
        aR += '0' * (len(bR) - len(aR))
    a = aL + aR
    b = bL + bR
    if s == '+':
        if var[1]:
            ans = SubtrNine(a, b)
        else:
            ans = SumNine(a, b)
    else:
        if var[1]:
            ans = SumNine(a, b)
        else:
            ans = SubtrNine(a, b)
    ans = ans[:len(ans) - point] + '.' + ans[len(ans) - point:]
    ans = ans.strip('0')
    if ans.endswith('.'):
        ans += '0'
    if ans.startswith('.'):
        ans = '0' + ans
    if ans == '0.0':
        return ans
    return var[0] + ans

# Сложение
def SumNine(a, b):
    ans = ''
    add = 0
    for i in range(len(a) - 1, -1, -1):
        summ = int(a[i]) + int(b[i]) + add
        ans = f'{summ - summ // 9 * 9}' + ans
        add = summ // 9
    if add == 1:
        ans = '1' + ans
    return ans

# Вычитание
def SubtrNine(a, b):
    ans = ''
    minus = 0
    for i in range(len(a) - 1, -1, -1):
        sub = int(a[i]) - int(b[i]) - minus
        if sub < 0:
            ans = f'{sub + 9}' + ans
            minus = 1
        else:
            ans = f'{sub}' + ans
            minus = 0
    return ans


def ShowInfo():
    messagebox.showinfo(title="Что делает программа?",
                        message="Программа предназначена для сложения и вычитания\nчисел в девятичной системе счисления")


def ShowCreator():
    messagebox.showinfo(title="Информация о создателе", message="Ваше имя")


def ShowButtonsInfo():
    messagebox.showinfo(title="Функции кнопок",
                        message='''
                        0,1,2,3,4,5,6,7,8 - вводимые цифры
                        -,+ - операции
                        , - разделение целой части и десятичной
                        C - очищение поля
                        << - удаление последнего символа
                        ''')


def ClickNumberButton(event, success):
    if not success:
        txt1.config(state='normal')
        txt1.insert(len(txt1.get()), event.widget['text'])
        txt1.config(state='readonly')


def ClickDelButton(event, success):
    if not success:
        if txt1.get().endswith('.'):
            variables[0] -= 1
        txt1.config(state='normal')
        txt1.delete(len(txt1.get()) - 1, len(txt1.get()))
        txt1.config(state='readonly')


def ClickClearButton(event, variables):
    variables[1] = False
    variables[0] = 0
    txt1.config(state='normal')
    txt2.config(state='normal')
    txt1.delete(0, len(txt1.get()))
    txt2.delete(0, len(txt2.get()))
    txt1.config(state='readonly')
    txt2.config(state='readonly')


def KeyBoardNumber(event, num, success):
    if not success:
        txt1.config(state='normal')
        txt1.insert(len(txt1.get()), num)
        txt1.config(state='readonly')


def ClickEqualButton(event, variables):
    currentAnswer = ''
    if len(txt2.get()) != 0:
        if len(txt1.get()) == 0:
            currentAnswer = txt2.get()[:len(txt2.get()) - 1]
        else:
            currentAnswer = FullNum(txt2.get()[:len(txt2.get()) - 1], txt1.get(), txt2.get()[-1])
            variables[1] = True
        txt2.config(state='normal')
        txt2.delete(0, len(txt2.get()))
        txt2.config(state='readonly')
        txt1.config(state='normal')
        txt1.delete(0, len(txt1.get()))
        txt1.insert(0, currentAnswer)
        txt1.config(state='readonly')


def ClickDotButton(event, variables):
    if not variables[1]:
        if variables[0] == 0 and not len(txt1.get()) == 0:
            txt1.config(state='normal')
            txt1.insert(len(txt1.get()), '.')
            txt1.config(state='readonly')
            variables[0] += 1


def ClickPlusMinus(event, sign, variables):
    variables[0] = 0
    variables[1] = False
    if len(txt1.get()) != 0:
        if len(txt2.get()) != 0:
            middleAnswer = FullNum(txt2.get()[:len(txt2.get()) - 1], txt1.get(), sign) + sign
        else:
            middleAnswer = txt1.get() + sign
        txt1.config(state='normal')
        txt1.delete(0, len(txt1.get()))
        txt1.config(state='readonly')
        txt2.config(state='normal')
        txt2.delete(0, len(txt2.get()))
        txt2.insert(0, middleAnswer)
        txt2.config(state='readonly')


# Переменные
variables = [0, False]

# Создание окна
window = tk.Tk()
window.title("Калькулятор")
window.geometry('346x526+200+100')
window.resizable(width=False, height=False)
window.configure(background="floral white")

# Создание верхнего меню
mainmenu = tk.Menu(window)
window.config(menu=mainmenu)

infomenu = tk.Menu(mainmenu, tearoff=0)
infomenu.add_command(label="О программе", command=ShowInfo)
infomenu.add_command(label="О создателе", command=ShowCreator)

helpmenu = tk.Menu(mainmenu, tearoff=0)
helpmenu.add_command(label="Функции кнопок", command=ShowButtonsInfo)

mainmenu.add_cascade(label="Помощь", menu=helpmenu)
mainmenu.add_cascade(label="Справка", menu=infomenu)

# Создание полей ввода
txt1 = tk.Entry(window, width=19,
                foreground="darkorange2",
                font=("Courier", 22,"bold"),
                justify="right",
                state='readonly',
                readonlybackground="white")
txt1.place(x=10, y=20, height=60)
txt2 = tk.Entry(window, width=19,
                state="readonly",
                font=("Courier", 22,"bold"),
                justify="right",
                readonlybackground="white")
txt2.place(x=10, y=110, height=40)


# Связь кнопок клавиатуры с кнопками калькулятора
for i in range(9):
    window.bind(f'{str(i)}', lambda event, num=f'{str(i)}', success=variables[1]: KeyBoardNumber(event, num, success))
window.bind("=", ClickEqualButton)
window.bind("<Return>", lambda event, var=variables: ClickEqualButton(event, var))
window.bind(".", lambda event, var=variables: ClickDotButton(event, var))
window.bind("-", lambda event, sign="-", var=variables: ClickPlusMinus(event, sign, var))
window.bind("+", lambda event, sign="+", var=variables: ClickPlusMinus(event, sign, var))
window.bind("c", lambda event, var=variables: ClickDelButton(event, var))
window.bind("<BackSpace>", lambda event, success=variables[1]: ClickDelButton(event, success))

# Создание кнопок
btn7 = tk.Button(window, text="7",
              bg="seashell2",
              fg="navy",
              padx="15",
              pady="5",
              font=("Courier bold", 30))
btn7.bind("<Button-1>", lambda event, success=variables[1]: ClickNumberButton(event, success))
btn7.place(x=10, y=175)

btn8 = tk.Button(window, text="8",
              bg="seashell2",
              fg="navy",
              padx = "15",
              pady = "5",
              font=("Courier bold", 30),)
btn8.bind("<Button-1>", lambda event, success=variables[1]: ClickNumberButton(event, success))
btn8.place(x=92, y=175)

btnDel = tk.Button(window, text="<<",
              bg="seashell2",
              fg="darkorange2",
              padx="9",
              pady="5",
                   justify='left',
              font=("Courier bold", 30))
btnDel.bind("<Button-1>", lambda event, success=variables[1]: ClickDelButton(event, success))
btnDel.place(x=174, y=175)

btnC = tk.Button(window, text="C",
              bg="seashell2",
              fg="darkorange2",
              padx="10",
              pady="5",
              font=("Courier bold", 30))
btnC.bind("<Button-1>", lambda event, var=variables: ClickClearButton(event, var))
btnC.place(x=256, y=175)

btn4 = tk.Button(window, text="4",
              bg="seashell2",
              fg="navy",
              padx="15",
              pady="5",
              font=("Courier bold", 30))
btn4.bind("<Button-1>", lambda event, success=variables[1]: ClickNumberButton(event, success))
btn4.place(x=10, y=260)

btn5 = tk.Button(window, text="5",
              bg="seashell2",
              fg="navy",
              padx="15",
              pady="5",
              font=("Courier bold", 30))
btn5.bind("<Button-1>", lambda event, success=variables[1]: ClickNumberButton(event, success))
btn5.place(x=92, y=260)

btn6 = tk.Button(window, text="6",
              bg="seashell2",
              fg="navy",
              padx="15",
              pady="5",
              font=("Courier bold", 30))
btn6.bind("<Button-1>", lambda event, success=variables[1]: ClickNumberButton(event, success))
btn6.place(x=174, y=260)

btnPlus = tk.Button(window, text="+",
              bg="seashell2",
              fg="darkorange2",
              padx="13",
              pady="5",
              font=("Courier bold", 30))
btnPlus.bind("<Button-1>", lambda event, sign="+", var=variables: ClickPlusMinus(event, sign, var))
btnPlus.place(x=256, y=260)

btn1 = tk.Button(window, text="1",
              bg="seashell2",
              fg="navy",
              padx="15",
              pady="5",
              font=("Courier bold", 30))
btn1.bind("<Button-1>", lambda event, success=variables[1]: ClickNumberButton(event, success))
btn1.place(x=10, y=345)

btn2 = tk.Button(window, text="2",
              bg="seashell2",
              fg="navy",
              padx="15",
              pady="5",
              font=("Courier bold", 30))
btn2.bind("<Button-1>", lambda event, success=variables[1]: ClickNumberButton(event, success))
btn2.place(x=92, y=345)

btn3 = tk.Button(window, text="3",
              bg="seashell2",
              fg="navy",
              padx="15",
              pady="5",
              font=("Courier bold", 30))
btn3.bind("<Button-1>", lambda event, success=variables[1]: ClickNumberButton(event, success))
btn3.place(x=174, y=345)

btnMinus = tk.Button(window, text="-",
              bg="seashell2",
              fg="darkorange2",
              padx="18",
              pady="5",
              font=("Courier bold", 30))
btnMinus.bind("<Button-1>", lambda event, sign="-", var=variables: ClickPlusMinus(event, sign, var))
btnMinus.place(x=256, y=345)

btn0 = tk.Button(window, text="0",
              bg="seashell2",
              fg="navy",
              padx="56",
              pady="5",
              font=("Courier bold", 30))
btn0.bind("<Button-1>", lambda event, success=variables[1]: ClickNumberButton(event, success))
btn0.place(x=10, y=430)

btnDot = tk.Button(window, text=",",
              bg="seashell2",
              fg="darkorange2",
              padx="20",
              pady="5",
              font=("Courier bold", 30))
btnDot.bind("<Button-1>", lambda event, var=variables: ClickDotButton(event, var))
btnDot.place(x=174, y=430)

btnEqual = tk.Button(window, text="=",
              bg="darkorange2",
              fg="white",
              padx="13",
              pady="5",
              font=("Courier bold", 30))
btnEqual.bind("<Button-1>", lambda event, var=variables: ClickEqualButton(event, var))
btnEqual.place(x=256, y=430)

window.mainloop()
