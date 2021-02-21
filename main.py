from tkinter import *
from math import sin, cos, pi, asin, acos, atan, sqrt, tan


root = Tk()
root.title("Movement of the body thrown at the angle to the horizon")
c = Canvas(root, bg='#F7DDC4', width=680, height=500)
root.geometry("680x500")
c.grid(row=0, column=0, columnspan=200, rowspan=70)

grafic = Canvas(root, bg='#D7E6FE', width=400, height=240)

b_home = Button(root)
vvod = []
g = 9.81

cifr = "1234567890."

def is_num(st):
    flag=True
    st.replace(' ', '')
    if (st==''):
        flag=False
    for a in st:
        if not(a in cifr):
            flag=False
    return(flag)


def change_button (b1, st):  # Изменение конпки
    b1['text'] = st
    b1['bg'] = '#79A9F1'
    b1['activebackground'] = '#99BEF4'
    b1['fg'] = '#ffffff'
    b1['activeforeground'] = '#ffffff'


def delete_main():  # Переход от главного окна к побочному
    c.delete("all")
    for a in main_buttons:
        a.destroy()

    global b_home
    b_home = Button(root, height=2, width=5)
    change_button(b_home, 'HOME')
    b_home.place(x=633, y=457)
    b_home.config(command=start_window)


def vvod_by_angle_zero():
    grafic.delete("all")
    V0 = vV0.get()
    A = vA.get()
    H = vH.get()
    T = vT.get()
    L = vL.get()
    col=0
    V0d = False
    Ad = False
    Hd = False
    Td = False
    Ld = False
    stroim = True
    if (is_num(V0)):
        col += 1
        V0d = True
        V0 = float(V0)
    if (is_num(A)):
        col += 1
        Ad = True
        A = float(A)
        A = A * pi / 180
    if (is_num(H)):
        col += 1
        Hd = True
        H = float(H)
    if (is_num(T)):
        col += 1
        Td = True
        T = float(T)
    if (is_num(L)):
        col += 1
        Ld = True
        L = float(L)
    if (V0d and Ad):
        L = (V0**2) *sin(2*A) / g
        H = (V0**2)*(sin(A) ** 2)/(2 * g)
        T = 2*V0*sin(A)/g
        vL.delete(0, END)
        vH.delete(0, END)
        vT.delete(0, END)
        vL.insert(0, round(L*1000)/1000)
        vH.insert(0, round(H*1000)/1000)
        vT.insert(0, round(T*1000)/1000)
    elif (V0d and Ld):
        if ((L*g)/(V0**2)) > 1:
            A = asin(1) / 2
        elif ((L*g)/(V0**2)) < -1:
            A = asin(-1) / 2
        elif  ((L*g)/(V0**2)) < 0:
            A = asin((L * g) / (V0 ** 2)) / 2 - pi/2
        else:
            A = asin((L*g)/(V0**2)) / 2
        H = (V0 ** 2) * (sin(A) ** 2) / (2 * g)
        T = 2 * V0 * sin(A) / g
        vA.delete(0, END)
        vH.delete(0, END)
        vT.delete(0, END)
        vA.insert(0, round(A*180/pi*1000)/1000)
        vH.insert(0, round(H*1000)/1000)
        vT.insert(0, round(T*1000)/1000)
    elif (V0d and Hd):
        if (sqrt(H*2*g/V0**2)) > 1:
            A = asin(1)
        elif (sqrt(H*2*g/V0**2)) < -1:
            A = asin(-1)
        else:
            A = asin(sqrt(H*2*g/V0**2))
        L=V0**2 * sin(2*A)**2 / g
        T = 2 * V0 * sin(A) / g
        vA.delete(0, END)
        vL.delete(0, END)
        vT.delete(0, END)
        vA.insert(0, round(A * 180 / pi * 1000) / 1000)
        vL.insert(0, round(L * 1000) / 1000)
        vT.insert(0, round(T * 1000) / 1000)
    elif (V0d and Td):
        if (T*g/(2*V0)) > 1:
            A = asin(1)
        elif (T*g/(2*V0)) < -1:
            A = asin(-1)
        else:
            A = asin(T*g/(2*V0))
        L = V0 ** 2 * sin(2 * A) ** 2 / g
        H = (V0 ** 2) * (sin(A) ** 2) / (2 * g)
        vA.delete(0, END)
        vL.delete(0, END)
        vH.delete(0, END)
        vA.insert(0, round(A*180/pi*1000)/1000)
        vL.insert(0, round(L*1000)/1000)
        vH.insert(0, round(H*1000)/1000)
    elif (Ad and Ld):
        A=A*180/pi
        V0 = sqrt(L*g/sin(2*A))
        H = (V0 ** 2) * (sin(A) ** 2) / (2 * g)
        T = 2 * V0 * sin(A) / g
        vV0.delete(0, END)
        vH.delete(0, END)
        vT.delete(0, END)
        vV0.insert(0, round(V0 * 1000) / 1000)
        vH.insert(0, round(H*1000)/1000)
        vT.insert(0, round(T*1000)/1000)
    elif (Ad and Hd):
        V0 = sqrt(H*2*g/(sin(A))**2)
        T = 2 * V0 * sin(A) / g
        L = V0 ** 2 * sin(2 * A) ** 2 / g
        vV0.delete(0, END)
        vL.delete(0, END)
        vT.delete(0, END)
        vV0.insert(0, round(V0*1000)/1000)
        vL.insert(0, round(L*1000)/1000)
        vT.insert(0, round(T*1000)/1000)
    elif (Ad and Td):
        V0 = T*g/(2*sin(A))
        L = V0 ** 2 * sin(2 * A) ** 2 / g
        H = (V0 ** 2) * (sin(A) ** 2) / (2 * g)
        vV0.delete(0, END)
        vL.delete(0, END)
        vH.delete(0, END)
        vV0.insert(0, round(V0 * 1000) / 1000)
        vL.insert(0, round(L * 1000) / 1000)
        vH.insert(0, round(H * 1000) / 1000)
    elif (Td and Ld):
        A = atan(g*T**2/(2*L))
        V0 = T*g/(2*sin(A))
        H = (V0 ** 2) * (sin(A) ** 2) / (2 * g)
        vV0.delete(0, END)
        vA.delete(0, END)
        vH.delete(0, END)
        vV0.insert(0, round(V0*1000)/1000)
        vA.insert(0, round(A*180/pi*1000)/1000)
        vH.insert(0, round(H*1000)/1000)
    elif (Hd and Ld):
        A=atan(4*H/L)
        V0 = sqrt(H*2*g/(sin(A))**2)
        L = V0 ** 2 * sin(2 * A) ** 2 / g
        T = 2 * V0 * sin(A) / g
        vV0.delete(0, END)
        vA.delete(0, END)
        vT.delete(0, END)
        vV0.insert(0, round(V0*1000)/1000)
        vA.insert(0, round(A*180/pi*1000)/1000)
        vT.insert(0, round(T*1000)/1000)
    else:
        vV0.delete(0, END)
        vA.delete(0, END)
        vT.delete(0, END)
        vL.delete(0, END)
        vH.delete(0, END)
        vV0.insert(0,"Рассчеты")
        vA.insert(0, "Невозможны")
        vH.insert(0, "Рассчеты")
        vT.insert(0, "Введите")
        vL.insert(0, "Другое")
        stroim = False

    if (stroim):
        k = min(370 / L, 190 / H)
        grafic.create_line(10, 10, 10, 210, arrow=FIRST)
        grafic.create_line(10, 210, 395, 210, arrow=LAST)
        grafic.create_text(15, 6, text="y(м)")
        grafic.create_text(385, 200, text="x(м)")
        grafic.create_line(10, 210, 10 + 30 * cos(A), 210 - 30 * sin(A), arrow=LAST)
        grafic.create_text(10 + 30 * cos(A) - 2, 210 - 30 * sin(A) - 14, text="Vo")
        grafic.create_line(30, 210, 10 + 20 * cos(A), 210 - 20 * sin(A))
        grafic.create_text(35, 210 - 10 * sin(A) , text="A")
        grafic.create_line(370, 10, 370, 40, arrow=LAST)
        grafic.create_text(361, 33, text="g")
        grafic.create_text(10, 220, text="0")
        grafic.create_text(17+len(str(round(H * 100)/100))*5, 200 - (H * k), text=str(round(H * 100)/100))
        grafic.create_line(5, 210 - (H * k), 390, 210 - (H * k), dash=True)
        grafic.create_text(10 + L * k, 220, text=str(round(L * 100)/100))
        grafic.create_line(10 + L * k, 10, 10 + L * k, 215, dash=True)
        grafic.create_text(10 + (L * k) / 2, 220, text=str(round(L/2 * 100)/100))
        grafic.create_line(10 + L * k / 2, 10, 10 + L * k / 2, 215, dash=True)
        for i in range(0, 2000):
            x = L / 2000 * i
            y = tan(A) * x - g / (2 * V0 ** 2 * cos(A) ** 2) * x ** 2
            x1 = L / 2000 * (i + 1)
            y1 = tan(A) * x1 - g / (2 * V0 ** 2 * cos(A) ** 2) * x1 ** 2

            grafic.create_line((x) * k + 10, 220 - ((y) * k + 10), ((x1) * k + 10), 220 - ((y1) * k + 10),
                               fill="#000814")


def del_by_angle_zero():
    vA.delete(0, END)
    vH.delete(0, END)
    vV0.delete(0, END)
    vT.delete(0, END)
    vL.delete(0, END)
    grafic.delete("all")


def file_by_angle_zero():
    with open('input.txt', "r") as file:
        line = file.readline()
        while line:
            print(line, end="")
            line = file.readline()


def by_angle_zero():  # Бросок под углом с земли
    global vvod
    vvod = []
    grafic.place(x=257, y=70)

    l1 = Label(text="Введите любые \n два значения", font="Cricket 12")
    l1.config(bd=20, bg='#F7DDC4', fg='#0C136F')
    l1.grid(row=1, column=0, columnspan=2, rowspan=1)
    vvod.append(l1)

    l2 = Label(text="Бросок под углом с земли", font="Cricket 18")
    l2.config(bd=20, bg='#F7DDC4', fg='#0C136F')
    l2.grid(row=0,  column=0, columnspan=100, rowspan=1)
    vvod.append(l2)

    delete_main()
    global vV0
    vV0= Entry(width=13)
    vV0.grid(row=2, column=2)
    vvod.append(vV0)

    bV0 = Label(text="Vo      =", font="Cricket 10")
    bV0.place(x=76, y=152)
    bV0.config(bg='#F7DDC4', fg='#0C136F')
    vvod.append(bV0)

    global vA
    vA= Entry(width=13)
    vA.grid(row=3, column=2)
    vvod.append(vA)

    bA = Label(text="Угол (В градусах) = ", font="Cricket 10")
    bA.place(x=5, y=175)
    bA.config(bg='#F7DDC4', fg='#0C136F')
    vvod.append(bA)

    global vH
    vH = Entry(width=13)
    vH.grid(row=4, column=2)
    vvod.append(vH)

    bH = Label(text="Hmax       = ", font="Cricket 10")
    bH.place(x=54, y=197)
    bH.config(bg='#F7DDC4', fg='#0C136F')
    vvod.append(bH)

    global vT
    vT = Entry(width=13)
    vT.grid(row=5, column=2)
    vvod.append(vT)

    bT = Label(text="Tполёта    = ", font="Cricket 10")
    bT.place(x=53, y=219)
    bT.config(bg='#F7DDC4', fg='#0C136F')
    vvod.append(bT)

    global vL
    vL = Entry(width=13)
    vL.grid(row=6, column=2)
    vvod.append(vL)

    bL = Label(text="Lполёта    = ", font="Cricket 10")
    bL.place(x=53, y=244)
    bL.config(bg='#F7DDC4', fg='#0C136F')
    vvod.append(bL)

    bvvesti = Button(root, height=2, width=17)
    change_button(bvvesti, "Ввести значения")
    bvvesti.place(x=20, y=275)
    vvod.append(bvvesti)
    bvvesti.config(command=vvod_by_angle_zero)

    bdel = Button(root, height=2, width=10)
    change_button(bdel, "Удалить\nзначения")
    bdel.place(x=163, y=275)
    vvod.append(bdel)
    bdel.config(command=del_by_angle_zero)

    bopen = Button(root, height=5, width=30)
    change_button(bopen, 'Считать значения из файла \n(введите 2 значения, на \nместе остальных "_" в\nследующем порядке: V0, A, H, T, L \n в файл "input.txt" в столбик)' )
    bopen.place(x=20, y=385)
    vvod.append(bopen)
    bopen.config(command=file_by_angle_zero)

    l3 = Label(text="ИЛИ", font="Cricket 12")
    l3.config(bd=20, bg='#F7DDC4', fg='#0C136F')
    l3.place(x=90, y=320)
    vvod.append(l3)

def start_window():  # Основное меню
    grafic.delete("all")
    grafic.place(x=1257, y=70)
    b_home.destroy()
    c.create_text(340, 50, text="Движение тела, брошенного под углом к горизонту", font="Cricket 18", fill = '#0C136F')
    for a in vvod:
        a.destroy()

    b1 = Button(root, text="1",  width=25, height=6)
    b1.place(x=40, y=120)
    b1.config(command = by_angle_zero)
    change_button(b1, "Бросок под углом \n с земли")


    b2 = Button(root, text="2",  width=25, height=6)
    b2.place(x=40, y=240)
    change_button(b2, "Бросок вертикально \n вверх с земли")


    b3 = Button(root, text="3",  width=25, height=6)
    b3.place(x=40, y=360)
    change_button(b3, "Бросок со скоростью, \n направленной горизонтально, \n с высоты ")


    b4 = Button(root, text="4",  width=25, height=6)
    b4.place(x=250, y=120)
    change_button(b4, "Бросок со скоростью, \n направленной под углом \n к горизонту, с высоты ")


    b5 = Button(root, text="5",  width=25, height=6)
    b5.place(x=250, y=240)
    change_button(b5, "Бросок с высоты со \n скоростью, направленной \nвертикально вверх или вниз")


    b6 = Button(root, text="6",  width=25, height=6)
    b6.place(x=250, y=360)
    change_button(b6, "Бросок под углом с высоты \n (с учетом сопротивления \n воздуха")


    b7 = Button(root, text="7",  width=25, height=6)
    b7.place(x=460, y=120)
    change_button(b7, "Бросок под углом с земли \n (с учетом сопротивления \n воздуха)")


    b8 = Button(root, text="8",  width=25, height=6)
    b8.place(x=460, y=240)
    change_button(b8, "СОХРАНЕННЫЕ \n РЕЗУЛЬТАТЫ")


    b9 = Button(root, text="9",  width=25, height=6)
    b9.place(x=460, y=360)
    change_button(b9, "ТЕОРИЯ")

    global main_buttons
    main_buttons = {b1, b2, b3, b4, b5, b6, b7, b8, b9}



start_window()
root.mainloop()