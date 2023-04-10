from tkinter import *
from tkinter.messagebox import showerror, showinfo
from tkinter import filedialog
import os
from PIL import Image, ImageDraw

def clear():
    ent.delete(0, END)
    out.config(state='normal')
    out.delete(0, END)
    out.config(state='readonly')


def image_save(image):
    try:
        image.save(filedialog.asksaveasfilename(filetype=(("bmp image *.bmp", "*.bmp"),)).split("/")[-1] + ".bmp")
        showinfo('Успех!', "Изображение было сохранено!")
    except:
        showerror("Ошибка!", "Что-то пошло не так")


def new_msg(msg):
    if len(msg) < 10:
        return f'0{len(msg)}{msg}'
    return f'{len(msg)}{msg}'


def encrypt_image(image):
    msg = new_msg(ent.get())
    length = len(msg)
    pos = 0
    try:
        img = Image.open(filedialog.askopenfilename())
        width = img.size[0] // 3 * 3
        for i in range(img.size[1]):
            if pos >= length:
                break
            for j in range(0, width, 3):
                if pos >= length:
                    break
                el = extra_code(ord(msg[pos]))
                pix = img.getpixel((i, j))
                img.putpixel((i, j), (new_colour(pix[0], el[0]), new_colour(pix[1], el[1]), new_colour(pix[2], el[2])))
                pix = img.getpixel((i, j + 1))
                img.putpixel((i, j + 1), (new_colour(pix[0], el[3]), new_colour(pix[1], el[4]), new_colour(pix[2], el[5])))
                pix = img.getpixel((i, j + 2))
                img.putpixel((i, j + 2), (new_colour(pix[0], el[6]), new_colour(pix[1], el[7]), pix[2]))
                pos += 1
        image[0] = img
        showinfo("Успех!", "Сообщение было зашифровано!")
    except:
        showerror("Ошибка!", "Что-то пошло не так")


def get_code(pix1, pix2, pix3):
    return f'{pix1[0] % 2}{pix1[1] % 2}{pix1[2] % 2}{pix2[0] % 2}{pix2[1] % 2}{pix2[2] % 2}{pix3[0] % 2}{pix3[1] % 2}'


def decrypt_image():
    out.config(state='normal')
    out.delete(0, END)
    try:
        img = Image.open(filedialog.askopenfilename())
        width = img.size[0] // 3 * 3
        length = 10
        pos = 0
        message = ''
        new_len = ''
        for i in range(img.size[1]):
            if pos >= length:
                break
            for j in range(0, width, 3):
                if pos >= length:
                    break
                pix1 = img.getpixel((i, j))
                pix2 = img.getpixel((i, j + 1))
                pix3 = img.getpixel((i, j + 2))
                symb = get_code(pix1, pix2, pix3)
                if j < 6:
                    new_len += chr(int(symb, 2))
                else:
                    length = int(new_len)
                    message += chr(int(symb, 2))
                    pos += 1
        out.insert(0, message)
    except:
        showerror("Ошибка!", "Что-то пошло не так")
    out.config(state='readonly')


def new_colour(col, bit):
    if bit == '0':
        if col % 2 == 0:
            return col
        else:
            return col - 1
    else:
        if col % 2 == 1:
            return col
        else:
            return col + 1


def extra_code(elem):
    elem = bin(elem)[2:]
    while len(elem) < 8:
        elem = "0" + elem
    return elem



def open_image():
    os.startfile(filedialog.askopenfilename())


def show_info():
    showinfo(title="Что делает программа?", message="Программа предназначена для шифрования сообщения в выбранном "
                                                    "изображении и расшифровка сообщения по изображению")


def show_creator():
    showinfo(title="Информация о создателе", message="Ваше имя")


window = Tk()
image = [1]

# Создание окна
window.title('Стенография')
window.geometry('630x140+50+100')
window.resizable(width=False, height=False)

# Создание верхнего меню
mainmenu = Menu(window)
window.config(menu=mainmenu)

# Каскады
infomenu = Menu(mainmenu, tearoff=0)
infomenu.add_command(label="О программе", command=show_info)
infomenu.add_command(label="О создателе", command=show_creator)

mainmenu.add_cascade(label="Справка", menu=infomenu)
mainmenu.add_cascade(label="Очистить поля", command=clear)

# Окна и кнопки
b1 = Button(text="Выбрать файл для кодирования сообщения", command=lambda: encrypt_image(image))
b1.place(x=15, y=35, height=30)
b2 = Button(text="Расшифровать сообщение", command=decrypt_image)
b2.place(x=415, y=35, height=30)
b3 = Button(text="Сохранить изображение с зашифрованным сообщением", command=lambda: image_save(image[0]))
b3.place(x=150, y=70, height=30)
b4 = Button(text="Открыть изображение", command=open_image)
b4.place(x=275, y=35, height=30)
ent = Entry(window, font=("Courier bold", 10))
ent.place(x=320, y=3, height=20, width=300)
out = Entry(window, font=("Courier bold", 10), state='readonly')
out.place(x=200, y=112, height=20, width=350)

# Лэйблы
lbl = Label(window, text="Введите сообщение, которое хотите зашифровать:", font=("Courier bold", 10))
lbl.place(x=5, y=0)
lbl1 = Label(window, text="Расшифрованное сообщение:", font=("Courier bold", 10))
lbl1.place(x=5, y=110)


window.mainloop()