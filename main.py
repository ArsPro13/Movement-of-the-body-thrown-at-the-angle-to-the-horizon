from tkinter import *
from math import sin, cos, pi, asin, acos, atan, sqrt, tan
import datetime
from tkinter import messagebox as mb

root = Tk()
root.title("Movement of the body thrown at the angle to the horizon")
c = Canvas(root, bg='#F7DDC4', width=680, height=500)
root.geometry("680x500")
c.grid(row=0, column=0, columnspan=200, rowspan=70)

grafic = Canvas(root, bg='#D7E6FE', width=400, height=240)
stroim1=True
b_home = Button(root)
vvod = []
g = 9.81

cifr = "1234567890.-"
r = 4

telo=''
XY=[]

def col_znak(numObj, digits=0):
    return f"{numObj:.{digits}f}"

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


# Под углом к горизонту с земли
def vvod_by_angle_zero(x=True):
    grafic.delete("all")
    global V0
    global A
    global H
    global T
    global L
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
    global stroim
    stroim = x
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
        if (A > 0) and (A < 90):
            L = (V0 ** 2) * sin(2 * A) / g
            H = (V0 ** 2) * (sin(A) ** 2) / (2 * g)
            T = 2 * V0 * sin(A) / g
            vL.delete(0, END)
            vH.delete(0, END)
            vT.delete(0, END)
            vL.insert(0, round(L * 1000) / 1000)
            vH.insert(0, round(H * 1000) / 1000)
            vT.insert(0, round(T * 1000) / 1000)
        else:
            mb.showerror("Неверные данные","Рассчеты невозможны")
            stroim = False
    elif (V0d and Ld):
        if ((L*g)/(V0**2)) > 1:
            mb.showerror("Неверные данные","Рассчеты невозможны")
            stroim = False
        elif ((L*g)/(V0**2)) < -1:
            mb.showerror("Неверные данные", "Рассчеты невозможны")
            stroim = False
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
            mb.showerror("Неверные данные","Рассчеты невозможны")
            stroim = False
        elif (sqrt(H*2*g/V0**2)) < -1:
            mb.showerror("Неверные данные","Рассчеты невозможны")
            stroim = False
        else:
            A = asin(sqrt(H*2*g/V0**2))
            L=V0**2 * sin(2*A) / g
            T = 2 * V0 * sin(A) / g
            vA.delete(0, END)
            vL.delete(0, END)
            vT.delete(0, END)
            vA.insert(0, round(A * 180 / pi * 1000) / 1000)
            vL.insert(0, round(L * 1000) / 1000)
            vT.insert(0, round(T * 1000) / 1000)
    elif (V0d and Td):
        if (T*g/(2*V0)) > 1:
            mb.showerror("Неверные данные", "Рассчеты невозможны")
            stroim = False
        elif (T*g/(2*V0)) < -1:
            mb.showerror("Неверные данные", "Рассчеты невозможны")
            stroim = False
        else:
            A = asin(T*g/(2*V0))
            L = V0 ** 2 * sin(2 * A)  / g
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
        L = V0 ** 2 * sin(2 * A)  / g
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
        L = V0 ** 2 * sin(2 * A) / g
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
        global k
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
        global i
        global telo
        global xy, XY
        xy = Label(text="x=0.000 , y=0.000", font="Cricket 12")
        xy.config(bd=20, bg='#F7DDC4', fg='#0C136F')
        xy.place(x= 400, y=320)
        XY.append(xy)
        telo = grafic.create_oval(10 - r, 210 - r, 10 + r, 210 + r, fill="#c00300")
        i=0
        root.after(10, draw_angle_by_zero)

def draw_angle_by_zero():
    global i
    global telo
    global xy, XY
    if (stroim):
        grafic.delete(telo)
        xy.destroy()
        XY=[]

        x = L / 4500 * i
        y = tan(A) * x - g / (2 * V0 ** 2 * cos(A) ** 2) * x ** 2
        x1 = L / 4500 * (i + 1)
        y1 = tan(A) * x1 - g / (2 * V0 ** 2 * cos(A) ** 2) * x1 ** 2
        telo = grafic.create_oval(((x1) * k + 10) - r, 220 - ((y1) * k + 10) - r, ((x1) * k + 10) + r, 220 - ((y1) * k + 10) + r, fill="#c00300")
        grafic.create_line((x) * k + 10, 220 - ((y) * k + 10), ((x1) * k + 10), 220 - ((y1) * k + 10), fill="#c00300")
        i+=1
        xy = Label(text="x="+str(col_znak(round(x*1000)/1000, 3))+", y="+str(col_znak(round(y*1000)/1000, 3)), font="Cricket 12")
        xy.config(bd=20, bg='#F7DDC4', fg='#0C136F')
        xy.place(x=400, y=320)
        XY.append(xy)
        global vvod
        vvod.append(xy)
        if (i<=4500):
            root.after(1, draw_angle_by_zero)

def del_by_angle_zero():
    vA.delete(0, END)
    vH.delete(0, END)
    vV0.delete(0, END)
    vT.delete(0, END)
    vL.delete(0, END)
    global stroim, XY
    stroim = False
    for a in XY:
        a.destroy()
    grafic.delete("all")

def save_by_angle_zero():
    vvod_by_angle_zero(False)
    global stroim, XY
    stroim = False
    for a in XY:
        a.destroy()
    grafic.delete("all")
    if (is_num(vV0.get()) and is_num(vA.get())):
        now = datetime.datetime.now()
        cur_time = now.strftime("%d-%m-%Y(%H-%M-%S)") + ".txt "
        with open("saved_files.txt", "a") as file:
            file.write(cur_time+"\n")
        with open(cur_time, "w") as file:
            st = 'Бросок под углом к горизонту с земли \n'
            file.write(st)
            st = "Vo (м/с) = " + str(vV0.get()) + '\n'
            file.write(st)
            st = "A (градусов) = " + str(vA.get()) + '\n'
            file.write(st)
            st = "H (м) = " + str(vH.get()) + '\n'
            file.write(st)
            st = "L (м) = " + str(vL.get()) + '\n'
            file.write(st)
            st = "T (с) = " + str(vT.get()) + '\n'
            file.write(st)
            mb.showinfo(
                "Успешно",
                "Данные сохранены")

def file_by_angle_zero():
    colvo = 0
    n = 0
    with open('input.txt', "r") as file:
        st = file.readline()
        while st:
            colvo+=1
            st=st.rstrip('\n')
            if (colvo==1):
                fV0 = st
                if (is_num(fV0)):
                    n+=1
            if (colvo==2):
                fA = st
                if (is_num(fA)):
                    n+=1
            if (colvo==3):
                fH = st
                if (is_num(fH)):
                    n+=1
            if (colvo==4):
                fT = st
                if (is_num(fT)):
                    n+=1
            if (colvo==5):
                fL = st
                if (is_num(fL)):
                    n+=1
            st = file.readline()
    if (colvo==5) and (n==2):
        vL.delete(0, END)
        vH.delete(0, END)
        vT.delete(0, END)
        vV0.delete(0, END)
        vA.delete(0, END)
        if (is_num(fV0)):
            vV0.insert(0, str(fV0))
        if (is_num(fA)):
            vA.insert(0, str(fA))
        if (is_num(fH)):
            vH.insert(0, str(fH))
        if (is_num(fT)):
            vT.insert(0, str(fT))
        if (is_num(fL)):
            vL.insert(0, str(fL))
        vvod_by_angle_zero()

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

    bsave = Button(root, height=5, width=30)
    change_button(bsave,'Сохранить значения\n в файл')
    bsave.place(x=300, y=385)
    vvod.append(bsave)
    bsave.config(command=save_by_angle_zero)

    l3 = Label(text="ИЛИ", font="Cricket 12")
    l3.config(bd=20, bg='#F7DDC4', fg='#0C136F')
    l3.place(x=90, y=320)
    vvod.append(l3)



# Вертикально вверх с земли

def vvod_vert_zero(x=True):
    grafic.delete("all")
    global V0, H, T
    V0 = vV0.get()
    H = vH.get()
    T = vT.get()
    col = 0
    V0d = False
    Ad = True
    A = pi/2
    Hd = False
    Td = False
    global stroim
    stroim = x
    if (is_num(V0)):
        col += 1
        V0d = True
        V0 = float(V0)
    if (is_num(H)):
        col += 1
        Hd = True
        H = float(H)
    if (is_num(T)):
        col += 1
        Td = True
        T = float(T)
    if (V0d and Ad):
        H = (V0 ** 2) * (sin(A) ** 2) / (2 * g)
        T = 2 * V0 * sin(A) / g
        vH.delete(0, END)
        vT.delete(0, END)
        vH.insert(0, round(H * 1000) / 1000)
        vT.insert(0, round(T * 1000) / 1000)
    elif (Ad and Hd):
        V0 = sqrt(H * 2 * g / (sin(A)) ** 2)
        T = 2 * V0 * sin(A) / g
        vV0.delete(0, END)
        vT.delete(0, END)
        vV0.insert(0, round(V0 * 1000) / 1000)
        vT.insert(0, round(T * 1000) / 1000)
    elif (Ad and Td):
        V0 = T * g / (2 * sin(A))
        H = (V0 ** 2) * (sin(A) ** 2) / (2 * g)
        vV0.delete(0, END)
        vH.delete(0, END)
        vV0.insert(0, round(V0 * 1000) / 1000)
        vH.insert(0, round(H * 1000) / 1000)
    else:
        vV0.delete(0, END)
        vT.delete(0, END)
        vH.delete(0, END)
        vV0.insert(0, "Рассчеты")
        vH.insert(0, "Невозможны")
        vT.insert(0, "")
        stroim = False


    if (stroim):
        global k
        k = 190 / H
        grafic.create_line(10, 10, 10, 210, arrow=FIRST)
        grafic.create_line(10, 210, 395, 210, arrow=LAST)
        grafic.create_text(15, 6, text="y(м)")
        grafic.create_text(385, 200, text="x(м)")
        grafic.create_line(10, 210, 10 + 30 * cos(A), 210 - 30 * sin(A), arrow=LAST)
        grafic.create_text(10 + 30 * cos(A) - 2, 210 - 30 * sin(A) - 14, text="Vo")
        grafic.create_line(30, 210, 10 + 20 * cos(A), 210 - 20 * sin(A))
        grafic.create_text(35, 210 - 10 * sin(A), text="A")
        grafic.create_line(370, 10, 370, 40, arrow=LAST)
        grafic.create_text(361, 33, text="g")
        grafic.create_text(10, 220, text="0")
        grafic.create_text(17 + len(str(round(H * 100) / 100)) * 5, 200 - (H * k), text=str(round(H * 100) / 100))
        grafic.create_line(5, 210 - (H * k), 390, 210 - (H * k), dash=True)
        global i
        global telo
        telo = grafic.create_oval(10 - r, 210 - r, 10 + r, 210 + r, fill="#c00300")
        i = 0
        global xy, XY
        xy = Label(text="x=0.000 , y=0.000", font="Cricket 12")
        xy.config(bd=20, bg='#F7DDC4', fg='#0C136F')
        xy.place(x=400, y=320)
        XY.append(xy)
        root.after(10, draw_vert_zero)

def draw_vert_zero():
    global i
    global telo
    global xy, XY
    if (stroim):
        grafic.delete(telo)
        xy.destroy()
        XY=[]
        x = T / 2000 * i
        y = V0*x-g*x**2/2
        x1 = T / 2000 * (i + 1)
        y1 = V0*x1 - g*x1**2/2
        telo = grafic.create_oval(10 - r, 210 - y1*k - r, 10 + r, 210 - y1*k + r, fill="#c00300")
        grafic.create_line(10, 210 - y*k, 10, 210 - y1*k, fill="#c00300")
        i+=1
        xy = Label(text="x=0.000"+ ", y=" + str(col_znak(round(y * 1000) / 1000, 3)), font="Cricket 12")
        xy.config(bd=20, bg='#F7DDC4', fg='#0C136F')
        xy.place(x=400, y=320)
        global vvod
        XY.append(xy)
        vvod.append(xy)
        if (i<=2000):
            root.after(1, draw_vert_zero)

def del_vert_zero():
    vH.delete(0, END)
    vV0.delete(0, END)
    vT.delete(0, END)
    global stroim, XY
    stroim = False
    for a in XY:
        a.destroy()
    grafic.delete("all")

def file_vert_zero():
    colvo = 0
    n = 0
    with open('input.txt', "r") as file:
        st = file.readline()
        while st:
            colvo+=1
            st=st.rstrip('\n')
            if (colvo==1):
                fV0 = st
                if (is_num(fV0)):
                    n+=1
            if (colvo==2):
                fH = st
                if (is_num(fH)):
                    n+=1
            if (colvo==3):
                fT = st
                if (is_num(fT)):
                    n+=1
            st = file.readline()
    if (colvo==3) and (n==1):
        vH.delete(0, END)
        vT.delete(0, END)
        vV0.delete(0, END)
        if (is_num(fV0)):
            vV0.insert(0, str(fV0))
        if (is_num(fH)):
            vH.insert(0, str(fH))
        if (is_num(fT)):
            vT.insert(0, str(fT))
        vvod_vert_zero()

def save_vert_zero():
    vvod_vert_zero(False)
    global stroim, XY
    stroim = False
    for a in XY:
        a.destroy()
    grafic.delete("all")
    if (is_num(vV0.get()) and is_num(vT.get())):
        now = datetime.datetime.now()
        cur_time = now.strftime("%d-%m-%Y(%H-%M-%S)") + ".txt "
        with open("saved_files.txt", "a") as file:
            file.write(cur_time+"\n")
        with open(cur_time, "w") as file:
            st = 'Бросок под углом к горизонту с земли \n'
            file.write(st)
            st = "Vo (м/с) = " + str(vV0.get()) + '\n'
            file.write(st)
            st = "A (градусов) = 90" + '\n'
            file.write(st)
            st = "H (м) = " + str(vH.get()) + '\n'
            file.write(st)
            st = "L (м) = 0" + '\n'
            file.write(st)
            st = "T (с) = " + str(vT.get()) + '\n'
            file.write(st)
            mb.showinfo(
                "Успешно",
                "Данные сохранены")

def vert_zero():  # Бросок под углом с земли
    global vvod
    vvod = []
    grafic.place(x=257, y=70)

    l1 = Label(text="Введите любое \n значение", font="Cricket 12")
    l1.config(bd=20, bg='#F7DDC4', fg='#0C136F')
    l1.grid(row=1, column=0, columnspan=2, rowspan=1)
    vvod.append(l1)

    l2 = Label(text="Бросок вертикально вверх с земли", font="Cricket 18")
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
    vT.grid(row=3, column=2)
    vvod.append(vT)

    bT = Label(text="Tполёта    = ", font="Cricket 10")
    bT.place(x=53, y=174)
    bT.config(bg='#F7DDC4', fg='#0C136F')
    vvod.append(bT)



    bvvesti = Button(root, height=2, width=17)
    change_button(bvvesti, "Ввести значения")
    bvvesti.place(x=20, y=275)
    vvod.append(bvvesti)
    bvvesti.config(command=vvod_vert_zero)

    bdel = Button(root, height=2, width=10)
    change_button(bdel, "Удалить\nзначения")
    bdel.place(x=163, y=275)
    vvod.append(bdel)
    bdel.config(command=del_vert_zero)

    bopen = Button(root, height=5, width=30)
    change_button(bopen, 'Считать значения из файла \n(введите 1 значение, на \nместе остальных "_" в\nследующем порядке: V0, H, T \n в файл "input.txt" в столбик)' )
    bopen.place(x=20, y=385)
    vvod.append(bopen)
    bopen.config(command=file_vert_zero)

    bsave = Button(root, height=5, width=30)
    change_button(bsave,'Сохранить значения\n в файл')
    bsave.place(x=300, y=385)
    vvod.append(bsave)
    bsave.config(command=save_vert_zero)

    l3 = Label(text="ИЛИ", font="Cricket 12")
    l3.config(bd=20, bg='#F7DDC4', fg='#0C136F')
    l3.place(x=90, y=320)
    vvod.append(l3)



# Горизонтально с высоты h
def vvod_hor_h(x=True):
    grafic.delete("all")
    global h, V0, T, L, stroim
    V0 = vV0.get()
    h = vh.get()
    T = vT.get()
    L = vL.get()
    col = 0
    V0d = False
    hd = False
    Td = False
    Ld = False
    stroim = True
    if (is_num(V0)):
        col += 1
        V0d = True
        V0 = float(V0)
    if (is_num(h)):
        col += 1
        hd = True
        h = float(h)
    if (is_num(T)):
        col += 1
        Td = True
        T = float(T)
    if (is_num(L)):
        col += 1
        Ld = True
        L = float(L)
    if (V0d and hd):
        T = sqrt(2*h/g)
        L = V0*T
        vL.delete(0, END)
        vT.delete(0, END)
        vL.insert(0, round(L * 1000) / 1000)
        vT.insert(0, round(T * 1000) / 1000)
    elif (V0d and Td):
        h = T**2 * g/2
        L = V0*T
        vL.delete(0, END)
        vh.delete(0, END)
        vL.insert(0, round(L * 1000) / 1000)
        vh.insert(0, round(h * 1000) / 1000)
    elif (Ld and hd):
        V0 = L*sqrt(g/(2*h))
        T = sqrt(2 * h / g)
        vV0.delete(0, END)
        vT.delete(0, END)
        vV0.insert(0, round(V0 * 1000) / 1000)
        vT.insert(0, round(T * 1000) / 1000)
    elif (Td and Ld):
        V0 = L/T
        h=g*T**2 / 2
        vV0.delete(0, END)
        vh.delete(0, END)
        vV0.insert(0, round(V0 * 1000) / 1000)
        vh.insert(0, round(h * 1000) / 1000)
    elif (V0d and Ld):
        h = g/2 * (L/V0)**2
        T = sqrt(2 * h / g)
        vT.delete(0, END)
        vh.delete(0, END)
        vT.insert(0, round(T * 1000) / 1000)
        vh.insert(0, round(h * 1000) / 1000)
    else:
        vV0.delete(0, END)
        vh.delete(0, END)
        vL.delete(0, END)
        vT.delete(0, END)
        vV0.insert(0, "Невозможно")
        vh.insert(0, "Вычислить")
        vL.insert(0, "Введите")
        vT.insert(0, "Другое")
        stroim=False
    if (stroim):
        global k
        k = min(370 / L, 190 / h)
        grafic.create_line(10, 10, 10, 210, arrow=FIRST)
        grafic.create_line(10, 210, 395, 210, arrow=LAST)
        grafic.create_text(15, 6, text="y(м)")
        grafic.create_text(385, 200, text="x(м)")
        grafic.create_line(10, 210-h*k, 30, 210 - h*k, arrow=LAST)
        grafic.create_text(35, 200-h*k, text="Vo")
        grafic.create_line(370, 10, 370, 40, arrow=LAST)
        grafic.create_text(361, 33, text="g")
        grafic.create_text(10, 220, text="0")
        grafic.create_text(10 + L * k, 220, text=str(round(L * 100)/100))
        grafic.create_line(10 + L * k, 10, 10 + L * k, 215, dash=True)
        grafic.create_text(60, 200 - h* k, text=str(round(h * 100) / 100))
        grafic.create_line(10, 210-h*k, 400, 210-h*k, dash=True)
        global i
        global telo
        global xy
        xy = Label(text="x=0.000 , y=0.000", font="Cricket 12")
        xy.config(bd=20, bg='#F7DDC4', fg='#0C136F')
        xy.place(x=400, y=320)
        telo = grafic.create_oval(10 - r, 210 - h*k - r, 10 + r, 210 - h*k  + r, fill="#c00300")
        i = 0
        global XY
        XY.append(xy)
        root.after(10, draw_hor_h)

def draw_hor_h():
    global i
    global telo
    global xy, XY
    global stroim
    if (stroim):
        grafic.delete(telo)
        xy.destroy()
        XY=[]
        x = L / 2000 * i
        y = h - g * x ** 2 / (2 * V0 ** 2)
        x1 = L / 2000 * (i + 1)
        y1 = h - g * x1 ** 2 / (2 * V0 ** 2)

        grafic.create_line((x) * k + 10, 220 - ((y) * k + 10), ((x1) * k + 10), 220 - ((y1) * k + 10),fill="#c00300")
        telo = grafic.create_oval(((x1) * k + 10) - r, 220 - ((y1) * k + 10) - r, ((x1) * k + 10) + r, 220 - ((y1) * k + 10) + r, fill="#c00300")
        i+=1
        xy = Label(text="x="+str(col_znak(round(x*1000)/1000, 3))+", y="+str(col_znak(round(y*1000)/1000, 3)), font="Cricket 12")
        xy.config(bd=20, bg='#F7DDC4', fg='#0C136F')
        xy.place(x=400, y=320)
        global vvod
        XY.append(xy)
        vvod.append(xy)
        if (i<=2000):
            root.after(1, draw_hor_h)

def del_hor_h():
    vh.delete(0, END)
    vV0.delete(0, END)
    vT.delete(0, END)
    vL.delete(0, END)
    global stroim, XY
    stroim = False
    for a in XY:
        a.destroy()
    grafic.delete("all")

def file_hor_h():
    colvo = 0
    n = 0
    with open('input.txt', "r") as file:
        st = file.readline()
        while st:
            colvo+=1
            st=st.rstrip('\n')
            if (colvo==1):
                fV0 = st
                if (is_num(fV0)):
                    n+=1
            if (colvo==2):
                fh = st
                if (is_num(fh)):
                    n+=1
            if (colvo==3):
                fL= st
                if (is_num(fL)):
                    n+=1
            if (colvo==4):
                fT= st
                if (is_num(fT)):
                    n+=1
            st = file.readline()
    if (colvo==4) and (n==2):
        vh.delete(0, END)
        vL.delete(0, END)
        vT.delete(0, END)
        vV0.delete(0, END)
        if (is_num(fV0)):
            vV0.insert(0, str(fV0))
        if (is_num(fh)):
            vh.insert(0, str(fh))
        if (is_num(fL)):
            vL.insert(0, str(fL))
        if (is_num(fT)):
            vT.insert(0, str(fT))
        vvod_hor_h()
    else:
        mb.showerror("Ошибка", "Неверный формат входных данных")

def save_hor_h():
    vvod_hor_h(False)
    global stroim, XY
    stroim = False
    for a in XY:
        a.destroy()
    grafic.delete("all")
    if (is_num(vV0.get()) and is_num(vh.get())):
        now = datetime.datetime.now()
        cur_time = now.strftime("%d-%m-%Y(%H-%M-%S)") + ".txt "
        with open("saved_files.txt", "a") as file:
            file.write(cur_time+"\n")
        with open(cur_time, "w") as file:
            st = 'Бросок горизонтально с высоты \n'
            file.write(st)
            st = "Vo (м/с) = " + str(vV0.get()) + '\n'
            file.write(st)
            st = "h (м) = " + str(vh.get()) + '\n'
            file.write(st)
            st = "L (м) = " + str(vL.get()) + '\n'
            file.write(st)
            st = "T (с) = " + str(vT.get()) + '\n'
            file.write(st)
            mb.showinfo(
                "Успешно",
                "Данные сохранены")

def hor_h():
    global vvod
    vvod = []
    grafic.place(x=257, y=70)

    l1 = Label(text="Введите любые \n два значения", font="Cricket 12")
    l1.config(bd=20, bg='#F7DDC4', fg='#0C136F')
    l1.grid(row=1, column=0, columnspan=2, rowspan=1)
    vvod.append(l1)

    l2 = Label(text="Бросок горизонтально с высоты", font="Cricket 18")
    l2.config(bd=20, bg='#F7DDC4', fg='#0C136F')
    l2.grid(row=0, column=0, columnspan=100, rowspan=1)
    vvod.append(l2)

    delete_main()
    global vV0
    vV0 = Entry(width=13)
    vV0.grid(row=2, column=2)
    vvod.append(vV0)

    bV0 = Label(text="Vo(м/с)      =", font="Cricket 10")
    bV0.place(x=76, y=152)
    bV0.config(bg='#F7DDC4', fg='#0C136F')
    vvod.append(bV0)

    global vh
    vh = Entry(width=13)
    vh.grid(row=3, column=2)
    vvod.append(vh)

    bh = Label(text="Начальная высота (м)  = ", font="Cricket 10")
    bh.place(x=4, y=175)
    bh.config(bg='#F7DDC4', fg='#0C136F')
    vvod.append(bh)

    global vL
    vL = Entry(width=13)
    vL.grid(row=4, column=2)
    vvod.append(vL)

    bL = Label(text="       L(м)        =", font="Cricket 10")
    bL.place(x=60, y=197)
    bL.config(bg='#F7DDC4', fg='#0C136F')
    vvod.append(bL)

    global vT
    vT = Entry(width=13)
    vT.grid(row=5, column=2)
    vvod.append(vT)

    bT = Label(text="Tполёта(с)       = ", font="Cricket 10")
    bT.place(x=54, y=219)
    bT.config(bg='#F7DDC4', fg='#0C136F')
    vvod.append(bT)


    bvvesti = Button(root, height=2, width=17)
    change_button(bvvesti, "Ввести значения")
    bvvesti.place(x=20, y=275)
    vvod.append(bvvesti)
    bvvesti.config(command=vvod_hor_h)

    bdel = Button(root, height=2, width=10)
    change_button(bdel, "Удалить\nзначения")
    bdel.place(x=163, y=275)
    vvod.append(bdel)
    bdel.config(command=del_hor_h)

    bopen = Button(root, height=5, width=30)
    change_button(bopen,
                  'Считать значения из файла \n(введите 2 значения, на \nместе остальных "_" в\nследующем порядке: V0, h, L, T \n в файл "input.txt" в столбик)')
    bopen.place(x=20, y=385)
    vvod.append(bopen)
    bopen.config(command=file_hor_h)

    bsave = Button(root, height=5, width=30)
    change_button(bsave, 'Сохранить значения\n в файл')
    bsave.place(x=300, y=385)
    vvod.append(bsave)
    bsave.config(command=save_hor_h)

    l3 = Label(text="ИЛИ", font="Cricket 12")
    l3.config(bd=20, bg='#F7DDC4', fg='#0C136F')
    l3.place(x=90, y=320)
    vvod.append(l3)


# вертикально вверх с высоты
def vvod_vert_v_h(x=True):
    grafic.delete("all")
    global V0, h, H, T, Vk
    V0 = vV0.get()
    h = vh.get()
    H = vH.get()
    T = vT.get()
    Vk = vVk.get()
    col=0
    V0d = False
    hd = False
    Hd = False
    Td = False
    Vkd = False
    global stroim
    stroim = x
    if (is_num(V0)):
        col += 1
        V0d = True
        V0 = float(V0)
    if (is_num(h)):
        col += 1
        hd = True
        h = float(h)
    if (is_num(H)):
        col += 1
        Hd = True
        H = float(H)
    if (is_num(T)):
        col += 1
        Td = True
        T = float(T)
    if (is_num(Vk)):
        col += 1
        Vkd = True
        Vk = float(Vk)
    if (V0d and Vkd):
        if (Vk < V0):
            mb.showerror("Неверные данные", "Рассчеты невозможны")
            stroim = False
        else:
            h = (Vk**2-V0**2)/(2*g)
            H = h + V0**2/(2*g)
            T = (V0+sqrt(V0**2+2*g*h))/g
            vh.delete(0, END)
            vH.delete(0, END)
            vT.delete(0, END)
            vh.insert(0, round(h*1000)/1000)
            vH.insert(0, round(H*1000)/1000)
            vT.insert(0, round(T*1000)/1000)
    elif (V0d and hd):
        T=(V0+sqrt(V0**2+2*g*h))/g
        H = h + V0 ** 2 / (2 * g)
        Vk=sqrt(V0**2+2*g*h)
        vVk.delete(0, END)
        vH.delete(0, END)
        vT.delete(0, END)
        vVk.insert(0, round(Vk * 1000) / 1000)
        vH.insert(0, round(H * 1000) / 1000)
        vT.insert(0, round(T * 1000) / 1000)
    elif (V0d and Hd):
        h = H-V0**2/(2*g)
        T = (V0 + sqrt(V0 ** 2 + 2 * g * h)) / g
        Vk = sqrt(V0 ** 2 + 2 * g * h)
        vVk.delete(0, END)
        vh.delete(0, END)
        vT.delete(0, END)
        vVk.insert(0, round(Vk * 1000) / 1000)
        vh.insert(0, round(h * 1000) / 1000)
        vT.insert(0, round(T * 1000) / 1000)
    elif (V0d and Td):
        h = (g**2*(T-V0/g)**2-V0**2)/(2*g)
        H = h + V0 ** 2 / (2 * g)
        Vk = sqrt(V0 ** 2 + 2 * g * h)
        vVk.delete(0, END)
        vh.delete(0, END)
        vH.delete(0, END)
        vVk.insert(0, round(Vk * 1000) / 1000)
        vh.insert(0, round(h * 1000) / 1000)
        vH.insert(0, round(H * 1000) / 1000)
    elif (hd and Hd):
        if (H-h<0):
            mb.showerror("Ошибка",  "Расчеты невзможны")
            stroim = False
        else:
            V0 = sqrt((H - h) * 2 * g)
            T = (V0 + sqrt(V0 ** 2 + 2 * g * h)) / g
            Vk = sqrt(V0 ** 2 + 2 * g * h)
            vVk.delete(0, END)
            vT.delete(0, END)
            vV0.delete(0, END)
            vVk.insert(0, round(Vk * 1000) / 1000)
            vT.insert(0, round(T * 1000) / 1000)
            vV0.insert(0, round(V0 * 1000) / 1000)
    elif (hd and Td):
        V0 = (T**2*g-2*h)/(2*T)
        Vk = sqrt(V0 ** 2 + 2 * g * h)
        H = h + V0 ** 2 / (2 * g)
        vVk.delete(0, END)
        vH.delete(0, END)
        vV0.delete(0, END)
        vVk.insert(0, round(Vk * 1000) / 1000)
        vH.insert(0, round(H * 1000) / 1000)
        vV0.insert(0, round(V0 * 1000) / 1000)
    elif (hd and Vkd):
        if (Vk**2-2*g*h <0):
            mb.showerror("Ошибка", "Расчеты невзможны")
            stroim = False
        else:
            V0 = sqrt(Vk**2-2*g*h)
            H = h + V0 ** 2 / (2 * g)
            T = (V0 + sqrt(V0 ** 2 + 2 * g * h)) / g
            vT.delete(0, END)
            vH.delete(0, END)
            vV0.delete(0, END)
            vT.insert(0, round(T * 1000) / 1000)
            vH.insert(0, round(H * 1000) / 1000)
            vV0.insert(0, round(V0 * 1000) / 1000)
    elif (Hd and Td):
        V0 = T*g-sqrt(2*g*H)
        h = (2*g*H-V0**2)/(2*g)
        Vk = sqrt(V0**2+2*g*h)
        vVk.delete(0, END)
        vh.delete(0, END)
        vV0.delete(0, END)
        vVk.insert(0, round(Vk * 1000) / 1000)
        vh.insert(0, round(h * 1000) / 1000)
        vV0.insert(0, round(V0 * 1000) / 1000)
    elif (Td and Vkd):
        V0 = T*g-Vk
        h = (Vk**2-V0**2)/(2*g)
        H = h + V0 ** 2 / (2 * g)
        vH.delete(0, END)
        vh.delete(0, END)
        vV0.delete(0, END)
        vH.insert(0, round(H * 1000) / 1000)
        vh.insert(0, round(h * 1000) / 1000)
        vV0.insert(0, round(V0 * 1000) / 1000)
    else:
        vV0.delete(0, END)
        vh.delete(0, END)
        vH.delete(0, END)
        vT.delete(0, END)
        vVk.delete(0, END)
        vV0.insert(0, "Рассчеты")
        vH.insert(0, "Невозможны")
        vh.insert(0, "Введите")
        vT.insert(0, "Другие")
        vVk.insert(0, "Значения")
        stroim = False


    if (stroim):
        global k
        k = 190 / H
        grafic.create_line(10, 10, 10, 210, arrow=FIRST)
        grafic.create_line(10, 210, 395, 210, arrow=LAST)
        grafic.create_text(15, 6, text="y(м)")
        grafic.create_text(385, 200, text="x(м)")
        grafic.create_line(10, 210-h*k, 10 , 210 - 30-h*k, arrow=LAST)
        grafic.create_text(19, 210 - 30 - h*k, text="Vo")
        grafic.create_line(370, 10, 370, 40, arrow=LAST)
        grafic.create_text(361, 33, text="g")
        grafic.create_text(24, 210-h*k, text=str(round(h*1000)/1000))
        grafic.create_text(10, 220, text="0")
        grafic.create_text(17 + len(str(round(H * 100) / 100)) * 5, 200 - (H * k), text=str(round(H * 100) / 100))
        grafic.create_line(5, 210 - (H * k), 390, 210 - (H * k), dash=True)
        global i
        global telo
        telo = grafic.create_oval(10 - r, 210-h*k - r, 10 + r, 210-h*k + r, fill="#c00300")
        i = 0
        global xy, XY
        xy = Label(text="x=0.000 , y="+str(h), font="Cricket 12")
        xy.config(bd=20, bg='#F7DDC4', fg='#0C136F')
        xy.place(x=400, y=320)
        XY.append(xy)
        root.after(1, draw_vert_v_h)

def draw_vert_v_h():
    global i
    global telo
    global xy
    global stroim
    global h, k
    if (stroim):
        grafic.delete(telo)
        xy.destroy()
        x = T / 2000 * i
        y = h+ V0*x-g*x**2/2
        x1 = T / 2000 * (i + 1)
        y1 = h+ V0*x1 - g*x1**2/2
        telo = grafic.create_oval(10 - r, 210 - y1*k - r, 10 + r, 210 - y1*k + r, fill="#c00300")
        grafic.create_line(10, 210 - y*k, 10, 210 - y1*k, fill="#c00300")
        i+=1
        xy = Label(text="x=0.000"+ ", y=" + str(col_znak(y1, 3)), font="Cricket 12")
        xy.config(bd=20, bg='#F7DDC4', fg='#0C136F')
        xy.place(x=400, y=320)
        global vvod
        vvod.append(xy)
        if (i<2000):
            root.after(1, draw_vert_v_h)

def del_vert_v_h():
    vH.delete(0, END)
    vV0.delete(0, END)
    vT.delete(0, END)
    vVk.delete(0, END)
    vh.delete(0, END)
    global stroim, XY
    stroim = False
    for a in XY:
        a.destroy()
    grafic.delete("all")

def file_vert_v_h():
    colvo = 0
    n = 0
    with open('input.txt', "r") as file:
        st = file.readline()
        while st:
            colvo += 1
            st = st.rstrip('\n')
            if (colvo == 1):
                fV0 = st
                if (is_num(fV0)):
                    n += 1
            if (colvo == 2):
                fh = st
                if (is_num(fh)):
                    n += 1
            if (colvo == 3):
                fH = st
                if (is_num(fH)):
                    n += 1
            if (colvo == 4):
                fT = st
                if (is_num(fT)):
                    n += 1
            if (colvo == 5):
                fVk = st
                if (is_num(fVk)):
                    n += 1
            st = file.readline()
    if (colvo == 5) and (n == 2):
        vh.delete(0, END)
        vH.delete(0, END)
        vT.delete(0, END)
        vV0.delete(0, END)
        vVk.delete(0, END)
        if (is_num(fV0)):
            vV0.insert(0, str(fV0))
        if (is_num(fh)):
            vh.insert(0, str(fh))
        if (is_num(fH)):
            vL.insert(0, str(fH))
        if (is_num(fT)):
            vT.insert(0, str(fT))
        if (is_num(fVk)):
            vV0.insert(0, str(fVk))
        vvod_vert_v_h()
    else:
        mb.showerror("Ошибка", "Неверный формат входных данных")

def save_vert_v_h():
    vvod_vert_v_h(False)
    global stroim, XY
    stroim = False
    for a in XY:
        a.destroy()
    grafic.delete("all")
    if (is_num(vV0.get()) and is_num(vh.get())):
        now = datetime.datetime.now()
        cur_time = now.strftime("%d-%m-%Y(%H-%M-%S)") + ".txt"
        with open("saved_files.txt", "a") as file:
            file.write(cur_time+"\n")
        with open(cur_time, "w") as file:
            st = 'Бросок вертикально вверх с высоты  \n'
            file.write(st)
            st = "Vo (м/с) = " + str(vV0.get()) + '\n'
            file.write(st)
            st = "h (м) = " + str(vh.get()) + '\n'
            file.write(st)
            st = "H (м) = " + str(vH.get()) + '\n'
            file.write(st)
            st = "T (с) = " + str(vT.get()) + '\n'
            file.write(st)
            st = "Vk (м/с) = " + str(vVk.get()) + '\n'
            file.write(st)
            mb.showinfo(
                "Успешно",
                "Данные сохранены")

def vert_v_h():
    global vvod
    vvod = []
    grafic.place(x=257, y=70)

    l1 = Label(text="Введите любые \n два значения", font="Cricket 12")
    l1.config(bd=20, bg='#F7DDC4', fg='#0C136F')
    l1.grid(row=1, column=0, columnspan=2, rowspan=1)
    vvod.append(l1)

    l2 = Label(text="Бросок вертикально вверх с высоты", font="Cricket 18")
    l2.config(bd=20, bg='#F7DDC4', fg='#0C136F')
    l2.grid(row=0, column=0, columnspan=100, rowspan=1)
    vvod.append(l2)

    delete_main()
    global vV0
    vV0 = Entry(width=13)
    vV0.grid(row=2, column=2)
    vvod.append(vV0)

    bV0 = Label(text="Vo(м/с)   =", font="Cricket 10")
    bV0.place(x=75, y=152)
    bV0.config(bg='#F7DDC4', fg='#0C136F')
    vvod.append(bV0)

    global vh
    vh = Entry(width=13)
    vh.grid(row=3, column=2)
    vvod.append(vh)

    bh = Label(text="h(м)      =", font="Cricket 10")
    bh.place(x=83, y=175)
    bh.config(bg='#F7DDC4', fg='#0C136F')
    vvod.append(bh)

    global vH
    vH = Entry(width=13)
    vH.grid(row=4, column=2)
    vvod.append(vH)

    bH = Label(text="Hmax(м)       = ", font="Cricket 10")
    bH.place(x=52, y=197)
    bH.config(bg='#F7DDC4', fg='#0C136F')
    vvod.append(bH)

    global vT
    vT = Entry(width=13)
    vT.grid(row=5, column=2)
    vvod.append(vT)

    bT = Label(text="Tполёта(с)    = ", font="Cricket 10")
    bT.place(x=53, y=219)
    bT.config(bg='#F7DDC4', fg='#0C136F')
    vvod.append(bT)


    global vVk
    vVk = Entry(width=13)
    vVk.grid(row=6, column=2)
    vvod.append(vVk)

    bVk = Label(text="Vконечная(м/c)  = ", font="Cricket 10")
    bVk.place(x=31, y=244)
    bVk.config(bg='#F7DDC4', fg='#0C136F')
    vvod.append(bVk)

    bvvesti = Button(root, height=2, width=17)
    change_button(bvvesti, "Ввести значения")
    bvvesti.place(x=20, y=275)
    vvod.append(bvvesti)
    bvvesti.config(command=vvod_vert_v_h)

    bdel = Button(root, height=2, width=10)
    change_button(bdel, "Удалить\nзначения")
    bdel.place(x=163, y=275)
    vvod.append(bdel)
    bdel.config(command=del_vert_v_h)

    bopen = Button(root, height=5, width=30)
    change_button(bopen,
                  'Считать значения из файла \n(введите 2 значения, на \nместе остальных "_" в\nследующем порядке: V0, h, H, T, Vk \n в файл "input.txt" в столбик)')
    bopen.place(x=20, y=385)
    vvod.append(bopen)
    bopen.config(command=file_vert_v_h)

    bsave = Button(root, height=5, width=30)
    change_button(bsave, 'Сохранить значения\n в файл')
    bsave.place(x=300, y=385)
    vvod.append(bsave)
    bsave.config(command=save_vert_v_h)

    l3 = Label(text="ИЛИ", font="Cricket 12")
    l3.config(bd=20, bg='#F7DDC4', fg='#0C136F')
    l3.place(x=90, y=320)
    vvod.append(l3)


# вертикально вниз с высоты

def vvod_vert_vniz_h(x=True):
    grafic.delete("all")
    global V0, h, T, Vk
    V0 = vV0.get()
    h = vh.get()
    T = vT.get()
    Vk = vVk.get()
    col=0
    V0d = False
    hd = False
    Td = False
    Vkd = False
    global stroim
    stroim = x
    if (is_num(V0)):
        col += 1
        V0d = True
        V0 = float(V0)
    if (is_num(h)):
        col += 1
        hd = True
        h = float(h)
    if (is_num(T)):
        col += 1
        Td = True
        T = float(T)
    if (is_num(Vk)):
        col += 1
        Vkd = True
        Vk = float(Vk)
    if (V0d and Vkd):
        if (Vk < V0):
            mb.showerror("Неверные данные", "Рассчеты невозможны")
            stroim = False
        else:
            h = (Vk**2-V0**2)/(2*g)
            T = (-V0+sqrt(V0**2+2*g*h))/g
            vh.delete(0, END)
            vT.delete(0, END)
            vh.insert(0, round(h*1000)/1000)
            vT.insert(0, round(T*1000)/1000)
    elif (V0d and hd):
        T=(-V0+sqrt(V0**2+2*g*h))/g
        Vk=sqrt(V0**2+2*g*h)
        vVk.delete(0, END)
        vT.delete(0, END)
        vVk.insert(0, round(Vk * 1000) / 1000)
        vT.insert(0, round(T * 1000) / 1000)
    elif (V0d and Td):
        h = (g**2*(T+V0/g)**2-V0**2)/(2*g)
        Vk = sqrt(V0 ** 2 + 2 * g * h)
        vVk.delete(0, END)
        vh.delete(0, END)
        vVk.insert(0, round(Vk * 1000) / 1000)
        vh.insert(0, round(h * 1000) / 1000)
    elif (hd and Td):
        V0 = -1 * (T**2*g-2*h)/(2*T)
        Vk = sqrt(V0 ** 2 + 2 * g * h)
        vVk.delete(0, END)
        vV0.delete(0, END)
        vVk.insert(0, round(Vk * 1000) / 1000)
        vV0.insert(0, round(V0 * 1000) / 1000)
    elif (hd and Vkd):
        if (Vk**2-2*g*h <0):
            mb.showerror("Ошибка", "Расчеты невзможны")
            stroim = False
        else:
            V0 = sqrt(Vk**2-2*g*h)
            T=(-V0+sqrt(V0**2+2*g*h))/g
            vT.delete(0, END)
            vV0.delete(0, END)
            vT.insert(0, round(T * 1000) / 1000)
            vV0.insert(0, round(V0 * 1000) / 1000)
    elif (Td and Vkd):
        V0 = -(T*g-Vk)
        h = (Vk**2-V0**2)/(2*g)
        vh.delete(0, END)
        vV0.delete(0, END)
        vh.insert(0, round(h * 1000) / 1000)
        vV0.insert(0, round(V0 * 1000) / 1000)
    else:
        vV0.delete(0, END)
        vh.delete(0, END)
        vT.delete(0, END)
        vVk.delete(0, END)
        vV0.insert(0, "Рассчеты")
        vh.insert(0, "Невозможны")
        vVk.insert(0, "Введите")
        vT.insert(0, "Другое")
        stroim = False

    if (stroim):
        global k
        k = 190 / h
        H=h
        grafic.create_line(10, 10, 10, 210, arrow=FIRST)
        grafic.create_line(10, 210, 395, 210, arrow=LAST)
        grafic.create_text(15, 6, text="y(м)")
        grafic.create_text(385, 200, text="x(м)")
        grafic.create_line(10, 210-h*k, 10 , 210 - 30-h*k, arrow=LAST)
        grafic.create_text(19, 210 - 30 - h*k, text="Vo")
        grafic.create_line(370, 10, 370, 40, arrow=LAST)
        grafic.create_text(361, 33, text="g")
        grafic.create_text(24, 210-h*k, text=str(round(h*1000)/1000))
        grafic.create_text(10, 220, text="0")
        grafic.create_text(17 + len(str(round(H * 100) / 100)) * 5, 200 - (H * k), text=str(round(H * 100) / 100))
        grafic.create_line(5, 210 - (h * k), 390, 210 - (h * k), dash=True)
        global i
        global telo
        telo = grafic.create_oval(10 - r, 210-h*k - r, 10 + r, 210-h*k + r, fill="#c00300")
        i = 0
        global xy, XY
        xy = Label(text="x=0.000 , y="+str(h), font="Cricket 12")
        xy.config(bd=20, bg='#F7DDC4', fg='#0C136F')
        xy.place(x=400, y=320)
        XY.append(xy)
        root.after(1, draw_vert_vniz_h)

def draw_vert_vniz_h():
    global i
    global telo
    global xy, XY
    global stroim
    global h, k
    col = 2000
    if (stroim):
        grafic.delete(telo)
        xy.destroy()
        XY=[]
        x = T / col * i
        y = h - V0*x-g*x**2/2
        x1 = T / col * (i + 1)
        y1 = h - V0*x1 - g*x1**2/2
        telo = grafic.create_oval(10 - r, 210 - y1*k - r, 10 + r, 210 - y1*k + r, fill="#c00300")
        grafic.create_line(10, 210 - y*k, 10, 210 - y1*k, fill="#c00300")
        i+=1
        xy = Label(text="x=0.000"+ ", y=" + str(col_znak(y1, 3)), font="Cricket 12")
        xy.config(bd=20, bg='#F7DDC4', fg='#0C136F')
        xy.place(x=400, y=320)
        global vvod
        XY.append(xy)
        vvod.append(xy)
        if (i<col):
            root.after(1, draw_vert_vniz_h)

def del_vert_vniz_h():
    vV0.delete(0, END)
    vT.delete(0, END)
    vVk.delete(0, END)
    vh.delete(0, END)
    global stroim, XY
    stroim = False
    for a in XY:
        a.destroy()
    grafic.delete("all")

def file_vert_vniz_h():
    colvo = 0
    n = 0
    with open('input.txt', "r") as file:
        st = file.readline()
        while st:
            colvo += 1
            st = st.rstrip('\n')
            if (colvo == 1):
                fV0 = st
                if (is_num(fV0)):
                    n += 1
            if (colvo == 2):
                fh = st
                if (is_num(fh)):
                    n += 1
            if (colvo == 3):
                fVk = st
                if (is_num(fVk)):
                    n += 1
            if (colvo == 4):
                fT = st
                if (is_num(fT)):
                    n += 1
            st = file.readline()
    if (colvo == 4) and (n == 2):
        vh.delete(0, END)
        vT.delete(0, END)
        vV0.delete(0, END)
        vVk.delete(0, END)
        if (is_num(fV0)):
            vV0.insert(0, str(fV0))
        if (is_num(fh)):
            vh.insert(0, str(fh))
        if (is_num(fT)):
            vT.insert(0, str(fT))
        if (is_num(fVk)):
            vV0.insert(0, str(fVk))
        vvod_vert_vniz_h()
    else:
        mb.showerror("Ошибка", "Неверный формат входных данных")

def save_vert_vniz_h():
    vvod_vert_vniz_h(False)
    global stroim, XY
    stroim = False
    for a in XY:
        a.destroy()
    grafic.delete("all")
    if (is_num(vV0.get()) and is_num(vh.get())):
        now = datetime.datetime.now()
        cur_time = now.strftime("%d-%m-%Y(%H-%M-%S)") + ".txt"
        with open("saved_files.txt", "a") as file:
            file.write(cur_time+"\n")
        with open(cur_time, "w") as file:
            st = 'Бросок вертикально вниз с высоты  \n'
            file.write(st)
            st = "Vo (м/с) = " + str(vV0.get()) + '\n'
            file.write(st)
            st = "h (м) = " + str(vh.get()) + '\n'
            file.write(st)
            st = "Vk (м/с) = " + str(vVk.get()) + '\n'
            file.write(st)
            st = "T (с) = " + str(vT.get()) + '\n'
            file.write(st)

            mb.showinfo(
                "Успешно",
                "Данные сохранены")

def vert_vniz_h():
    global vvod
    vvod = []
    grafic.place(x=257, y=70)

    l1 = Label(text="Введите любые \n два значения", font="Cricket 12")
    l1.config(bd=20, bg='#F7DDC4', fg='#0C136F')
    l1.grid(row=1, column=0, columnspan=2, rowspan=1)
    vvod.append(l1)

    l2 = Label(text="Бросок вертикально вниз с высоты", font="Cricket 18")
    l2.config(bd=20, bg='#F7DDC4', fg='#0C136F')
    l2.grid(row=0, column=0, columnspan=100, rowspan=1)
    vvod.append(l2)

    delete_main()
    global vV0
    vV0 = Entry(width=13)
    vV0.grid(row=2, column=2)
    vvod.append(vV0)

    bV0 = Label(text="Vo(м/с)   =", font="Cricket 10")
    bV0.place(x=75, y=152)
    bV0.config(bg='#F7DDC4', fg='#0C136F')
    vvod.append(bV0)

    global vh
    vh = Entry(width=13)
    vh.grid(row=3, column=2)
    vvod.append(vh)

    bh = Label(text="h(м)      =", font="Cricket 10")
    bh.place(x=83, y=175)
    bh.config(bg='#F7DDC4', fg='#0C136F')
    vvod.append(bh)


    global vT
    vT = Entry(width=13)
    vT.grid(row=5, column=2)
    vvod.append(vT)

    bT = Label(text="Tполёта(с)    = ", font="Cricket 10")
    bT.place(x=53, y=219)
    bT.config(bg='#F7DDC4', fg='#0C136F')
    vvod.append(bT)


    global vVk
    vVk = Entry(width=13)
    vVk.grid(row=4, column=2)
    vvod.append(vVk)

    bVk = Label(text="Vконечная(м/c)  = ", font="Cricket 10")
    bVk.place(x=31, y=197)
    bVk.config(bg='#F7DDC4', fg='#0C136F')
    vvod.append(bVk)

    bvvesti = Button(root, height=2, width=17)
    change_button(bvvesti, "Ввести значения")
    bvvesti.place(x=20, y=275)
    vvod.append(bvvesti)
    bvvesti.config(command=vvod_vert_vniz_h)

    bdel = Button(root, height=2, width=10)
    change_button(bdel, "Удалить\nзначения")
    bdel.place(x=163, y=275)
    vvod.append(bdel)
    bdel.config(command=del_vert_vniz_h)

    bopen = Button(root, height=5, width=30)
    change_button(bopen,
                  'Считать значения из файла \n(введите 2 значения, на \nместе остальных "_" в\nследующем порядке: V0, h, Vk, T \n в файл "input.txt" в столбик)')
    bopen.place(x=20, y=385)
    vvod.append(bopen)
    bopen.config(command=file_vert_vniz_h)

    bsave = Button(root, height=5, width=30)
    change_button(bsave, 'Сохранить значения\n в файл')
    bsave.place(x=300, y=385)
    vvod.append(bsave)
    bsave.config(command=save_vert_vniz_h)

    l3 = Label(text="ИЛИ", font="Cricket 12")
    l3.config(bd=20, bg='#F7DDC4', fg='#0C136F')
    l3.place(x=90, y=320)
    vvod.append(l3)


# Под углом к горизонту с высоты h

def vvod_by_angle_h(x=True):
    grafic.delete("all")
    global V0
    global A
    global H
    global T
    global L
    global h
    h = vh.get()
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
    hd = False
    global stroim
    stroim = x
    if (is_num(V0)):
        col += 1
        V0d = True
        V0 = float(V0)
    if (is_num(h)):
        col += 1
        hd = True
        h = float(h)
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
    if (V0d and Ad and hd):
        if (A > -pi/2) and (A < pi/2):
            L = (V0**2*sin(A)*cos(A)+V0*cos(A)*sqrt(V0**2*sin(A)**2+2*g*h)) / g
            H = (V0**2*sin(A)**2+2*g*h)/(2 * g)
            T = (V0*sin(A)+sqrt(V0**2*sin(A)**2+2*g*h)) / g
            vL.delete(0, END)
            vH.delete(0, END)
            vT.delete(0, END)
            vL.insert(0, round(L*1000)/1000)
            vH.insert(0, round(H*1000)/1000)
            vT.insert(0, round(T*1000)/1000)
        else:
            stroim = False
            mb.showerror("Неверные данные", "Рассчеты невозможны")
    elif (V0d and hd and Hd):
        if (h <= H) and (V0 != 0):
            A=asin(sqrt(2*g*(H-h)/V0**2))
            L = (V0 ** 2 * sin(A) * cos(A) + V0 * cos(A) * sqrt(V0 ** 2 * sin(A) ** 2 + 2 * g * h)) / g
            T = (V0 * sin(A) + sqrt(V0 ** 2 * sin(A) ** 2 + 2 * g * h)) / g
            vL.delete(0, END)
            vA.delete(0, END)
            vT.delete(0, END)
            vL.insert(0, round(L * 1000) / 1000)
            vA.insert(0, round(A*180/pi * 1000) / 1000)
            vT.insert(0, round(T * 1000) / 1000)
        else:
            stroim = False
            mb.showerror("Неверные данные", "Рассчеты невозможны")
    elif (V0d and hd and Td):
        x=(T**2*g - 2*h)/ (2*T*V0)
        if (x>-1) and (x<1):
            A=asin(x)
            L = (V0 ** 2 * sin(A) * cos(A) + V0 * cos(A) * sqrt(V0 ** 2 * sin(A) ** 2 + 2 * g * h)) / g
            H = (V0**2*sin(A)**2+2*g*h)/(2 * g)
            vL.delete(0, END)
            vA.delete(0, END)
            vH.delete(0, END)
            vL.insert(0, round(L * 1000) / 1000)
            vA.insert(0, round(A * 180 / pi * 1000) / 1000)
            vH.insert(0, round(H * 1000) / 1000)
        else:
            stroim = False
            mb.showerror("Неверные данные", "Рассчеты невозможны")
    elif (V0d and hd and Ld):
        D = (V0**2+g*h)**2 - g**2*(h**2+L**2)
        if (D>0):
            T = sqrt((V0**2 + g*h + sqrt(D))/(g**2/2))
            if (L/(T*V0) > -1) and (L/(T*V0) < 1):
                A = acos(L/(T*V0))
                H = (V0 ** 2 * sin(A) ** 2 + 2 * g * h) / (2 * g)
                vT.delete(0, END)
                vA.delete(0, END)
                vH.delete(0, END)
                vT.insert(0, round(T * 1000) / 1000)
                vA.insert(0, round(A * 180 / pi * 1000) / 1000)
                vH.insert(0, round(H * 1000) / 1000)
            else:
                stroim = False
                mb.showerror("Неверные данные", "Рассчеты невозможны")
        else:
            stroim = False
            mb.showerror("Неверные данные", "Рассчеты невозможны")
    elif (hd and Ad and Hd):
        if (H>=h):
            V0 = sqrt((H-h)*2*g/sin(A)**2)
            L = (V0 ** 2 * sin(A) * cos(A) + V0 * cos(A) * sqrt(V0 ** 2 * sin(A) ** 2 + 2 * g * h)) / g
            T = (V0 * sin(A) + sqrt(V0 ** 2 * sin(A) ** 2 + 2 * g * h)) / g
            vT.delete(0, END)
            vA.delete(0, END)
            vL.delete(0, END)
            vT.insert(0, round(T * 1000) / 1000)
            vV0.insert(0, round(V0 * 1000) / 1000)
            vL.insert(0, round(L * 1000) / 1000)
        else:
            stroim = False
            mb.showerror("Неверные данные", "Рассчеты невозможны")
    elif (hd and Ad and Td):
        V0 = (T**2*g-2*h)/(2*T*sin(A))
        if (V0>0):
            L = (V0 ** 2 * sin(A) * cos(A) + V0 * cos(A) * sqrt(V0 ** 2 * sin(A) ** 2 + 2 * g * h)) / g
            H = (V0 ** 2 * sin(A) ** 2 + 2 * g * h) / (2 * g)
            vL.delete(0, END)
            vV0.delete(0, END)
            vH.delete(0, END)
            vL.insert(0, round(L * 1000) / 1000)
            vV0.insert(0, round(V0 * 1000) / 1000)
            vH.insert(0, round(H * 1000) / 1000)
        else:
            stroim = False
            mb.showerror("Неверные данные", "Рассчеты невозможны")
    elif (hd and Ad and Ld):
        x = L**2*g**2/(2*(L*g*sin(A)*cos(A) + g*h*cos(A)**2))
        if (x>0):
            V0 = sqrt(x)
            H = (V0 ** 2 * sin(A) ** 2 + 2 * g * h) / (2 * g)
            T = (V0 * sin(A) + sqrt(V0 ** 2 * sin(A) ** 2 + 2 * g * h)) / g
            vT.delete(0, END)
            vV0.delete(0, END)
            vH.delete(0, END)
            vT.insert(0, round(T * 1000) / 1000)
            vV0.insert(0, round(V0 * 1000) / 1000)
            vH.insert(0, round(H * 1000) / 1000)
        else:
            stroim = False
            mb.showerror("Неверные данные", "Рассчеты невозможны")
    elif (V0d and Ad and Hd):
        if (A<=0):
            h = H
            L = (V0 ** 2 * sin(A) * cos(A) + V0 * cos(A) * sqrt(V0 ** 2 * sin(A) ** 2 + 2 * g * h)) / g
            T = (V0 * sin(A) + sqrt(V0 ** 2 * sin(A) ** 2 + 2 * g * h)) / g
        else:
            h = H - V0**2*sin(A)**2/(2*g)
            L = (V0 ** 2 * sin(A) * cos(A) + V0 * cos(A) * sqrt(V0 ** 2 * sin(A) ** 2 + 2 * g * h)) / g
            T = (V0 * sin(A) + sqrt(V0 ** 2 * sin(A) ** 2 + 2 * g * h)) / g
    elif (V0d and Ad and Td):
        h = ((T*g-V0*sin(A))**2-V0**2*sin(A)**2)/(2*g)
        L = (V0 ** 2 * sin(A) * cos(A) + V0 * cos(A) * sqrt(V0 ** 2 * sin(A) ** 2 + 2 * g * h)) / g
        H = (V0 ** 2 * sin(A) ** 2 + 2 * g * h) / (2 * g)
        vL.delete(0, END)
        vH.delete(0, END)
        vh.delete(0, END)
        vL.insert(0, round(L * 1000) / 1000)
        vH.insert(0, round(H * 1000) / 1000)
        vh.insert(0, round(h * 1000) / 1000)
    elif (V0d and Ad and Ld):
        T = L/(V0*cos(A))
        h = ((T*g-V0*sin(A))**2-V0**2*sin(A)**2)/(2*g)
        H = (V0 ** 2 * sin(A) ** 2 + 2 * g * h) / (2 * g)
        vT.delete(0, END)
        vH.delete(0, END)
        vh.delete(0, END)
        vT.insert(0, round(T * 1000) / 1000)
        vH.insert(0, round(H * 1000) / 1000)
        vh.insert(0, round(h * 1000) / 1000)
    elif():
        
    else:
        vV0.delete(0, END)
        vA.delete(0, END)
        vT.delete(0, END)
        vL.delete(0, END)
        vh.delete(0, END)
        vH.delete(0, END)
        vh.insert(0,"Рассчеты")
        vV0.insert(0, "Невозможны")
        vA.insert(0, "Рассчеты")
        vH.insert(0, "Введите")
        vT.insert(0, "Другие")
        vL.insert(0, "Значения")
        stroim = False

    if (stroim):
        global k
        k = min(370 / L, 190 / H)
        grafic.create_line(10, 10, 10, 210, arrow=FIRST)
        grafic.create_line(10, 210, 395, 210, arrow=LAST)
        grafic.create_text(15, 6, text="y(м)")
        grafic.create_text(385, 200, text="x(м)")
        grafic.create_line(10, 210 - h*k, 10 + 30 * cos(A), 210 - h*k - 30 * sin(A), arrow=LAST)
        grafic.create_text(10 + 30 * cos(A) + 11, 210 - h*k - 30 * sin(A) + 5, text="Vo")
        grafic.create_line(30, 210 - h*k, 10 + 20 * cos(A), 210 - h*k - 20 * sin(A))
        grafic.create_line(10, 210 - h * k, 45, 210 - h * k, dash = True)
        grafic.create_text(35, 210 - h*k - 10 * sin(A) , text="A")
        grafic.create_line(370, 10, 370, 40, arrow=LAST)
        grafic.create_text(361, 33, text="g")
        grafic.create_text(10, 220, text="0")
        grafic.create_text(17+len(str(round(H * 100)/100))*5, 200 - (H * k), text=str(round(H * 100)/100))
        grafic.create_line(5, 210 - (H * k), 390, 210 - (H * k), dash=True)
        grafic.create_text(10 + L * k, 220, text=str(round(L * 100)/100))
        grafic.create_line(10 + L * k, 10, 10 + L * k, 215, dash=True)
        grafic.create_text(10 + (V0**2*sin(A)*cos(A)/g)*k, 220, text=str(round(V0**2*sin(A)*cos(A)/g * 100)/100))
        grafic.create_line(10 + (V0**2*sin(A)*cos(A)/g)*k, 10, 10 + (V0**2*sin(A)*cos(A)/g)*k, 215, dash=True)
        global i
        global telo
        global xy, XY
        xy = Label(text="x=0.000 , y=0.000", font="Cricket 12")
        xy.config(bd=20, bg='#F7DDC4', fg='#0C136F')
        xy.place(x= 400, y=320)
        XY.append(xy)
        telo = grafic.create_oval(10 - r, 210-h*k - r, 10 + r, 210-h*k + r, fill="#c00300")
        i=0
        root.after(10, draw_angle_by_h)

def draw_angle_by_h():
    global i
    global telo
    global xy, XY
    if (stroim):
        grafic.delete(telo)
        xy.destroy()
        XY=[]

        x = L / 2000 * i
        y = h + tan(A) * x - g / (2 * V0 ** 2 * cos(A) ** 2) * x ** 2
        x1 = L / 2000 * (i + 1)
        y1 = h + tan(A) * x1 - g / (2 * V0 ** 2 * cos(A) ** 2) * x1 ** 2
        telo = grafic.create_oval(((x1) * k + 10) - r, 220 - ((y1) * k + 10) - r, ((x1) * k + 10) + r, 220 - ((y1) * k + 10) + r, fill="#c00300")
        grafic.create_line((x) * k + 10, 220 - ((y) * k + 10), ((x1) * k + 10), 220 - ((y1) * k + 10), fill="#c00300")
        i+=1
        xy = Label(text="x="+str(col_znak(round(x*1000)/1000, 3))+", y="+str(col_znak(round(y*1000)/1000, 3)), font="Cricket 12")
        xy.config(bd=20, bg='#F7DDC4', fg='#0C136F')
        xy.place(x=400, y=320)
        XY.append(xy)
        global vvod
        vvod.append(xy)
        if (i<=2000):
            root.after(1, draw_angle_by_h)

def del_by_angle_h():
    vA.delete(0, END)
    vh.delete(0, END)
    vH.delete(0, END)
    vV0.delete(0, END)
    vT.delete(0, END)
    vL.delete(0, END)
    global stroim, XY
    stroim = False
    for a in XY:
        a.destroy()
    grafic.delete("all")

def file_by_angle_h():
    colvo = 0
    n = 0
    with open('input.txt', "r") as file:
        st = file.readline()
        while st:
            colvo+=1
            st=st.rstrip('\n')
            if (colvo==1):
                fh = st
                if (is_num(fh)):
                    n+=1
            if (colvo==2):
                fV0 = st
                if (is_num(fV0)):
                    n+=1
            if (colvo==3):
                fA = st
                if (is_num(fA)):
                    n+=1
            if (colvo==4):
                fH = st
                if (is_num(fH)):
                    n+=1
            if (colvo==5):
                fT = st
                if (is_num(fT)):
                    n+=1
            if (colvo==6):
                fL = st
                if (is_num(fL)):
                    n+=1
            st = file.readline()
    if (colvo==6) and (n==3):
        vh.delete(0, END)
        vL.delete(0, END)
        vH.delete(0, END)
        vT.delete(0, END)
        vV0.delete(0, END)
        vA.delete(0, END)
        if (is_num(fh)):
            vh.insert(0, str(fh))
        if (is_num(fV0)):
            vV0.insert(0, str(fV0))
        if (is_num(fA)):
            vA.insert(0, str(fA))
        if (is_num(fH)):
            vH.insert(0, str(fH))
        if (is_num(fT)):
            vT.insert(0, str(fT))
        if (is_num(fL)):
            vL.insert(0, str(fL))
        vvod_by_angle_h()

def save_by_angle_h():
    vvod_by_angle_zero(False)
    global stroim, XY
    stroim = False
    for a in XY:
        a.destroy()
    grafic.delete("all")
    if (is_num(vV0.get()) and is_num(vA.get())):
        now = datetime.datetime.now()
        cur_time = now.strftime("%d-%m-%Y(%H-%M-%S)") + ".txt "
        with open("saved_files.txt", "a") as file:
            file.write(cur_time+"\n")
        with open(cur_time, "w") as file:
            st = 'Бросок под углом к горизонту с высоты h \n'
            file.write(st)
            st = "h (м) = " + str(vh.get()) + '\n'
            file.write(st)
            st = "Vo (м/с) = " + str(vV0.get()) + '\n'
            file.write(st)
            st = "A (градусов) = " + str(vA.get()) + '\n'
            file.write(st)
            st = "H (м) = " + str(vH.get()) + '\n'
            file.write(st)
            st = "L (м) = " + str(vL.get()) + '\n'
            file.write(st)
            st = "T (с) = " + str(vT.get()) + '\n'
            file.write(st)
            mb.showinfo(
                "Успешно",
                "Данные сохранены")

def by_angle_h():
    global vvod
    vvod = []
    grafic.place(x=257, y=70)

    l1 = Label(text="Введите любые \n три значения", font="Cricket 12")
    l1.config(bd=20, bg='#F7DDC4', fg='#0C136F')
    l1.grid(row=1, column=0, columnspan=2, rowspan=1)
    vvod.append(l1)

    l2 = Label(text="Бросок под углом с земли", font="Cricket 18")
    l2.config(bd=20, bg='#F7DDC4', fg='#0C136F')
    l2.grid(row=0,  column=0, columnspan=100, rowspan=1)
    vvod.append(l2)

    delete_main()

    global vh
    vh = Entry(width=13)
    vh.place(x=163, y=134)
    vvod.append(vh)

    bh = Label(text="h        =", font="Cricket 10")
    bh.place(x=77, y=134)
    bh.config(bg='#F7DDC4', fg='#0C136F')
    vvod.append(bh)

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
    bvvesti.config(command=vvod_by_angle_h)

    bdel = Button(root, height=2, width=10)
    change_button(bdel, "Удалить\nзначения")
    bdel.place(x=163, y=275)
    vvod.append(bdel)
    bdel.config(command=del_by_angle_h)

    bopen = Button(root, height=5, width=30)
    change_button(bopen, 'Считать значения из файла \n(введите 2 значения, на \nместе остальных "_" в\nследующем порядке: h, V0, A, H, T, L \n в файл "input.txt" в столбик)' )
    bopen.place(x=20, y=385)
    vvod.append(bopen)
    bopen.config(command=file_by_angle_h)

    bsave = Button(root, height=5, width=30)
    change_button(bsave,'Сохранить значения\n в файл')
    bsave.place(x=300, y=385)
    vvod.append(bsave)
    bsave.config(command=save_by_angle_h)

    l3 = Label(text="ИЛИ", font="Cricket 12")
    l3.config(bd=20, bg='#F7DDC4', fg='#0C136F')
    l3.place(x=90, y=320)
    vvod.append(l3)



def start_window():  # Основное меню
    grafic.delete("all")
    grafic.place(x=100000, y=70)
    global stroim
    stroim = False
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
    b2.config(command=vert_zero)
    change_button(b2, "Бросок вертикально \n вверх с земли")


    b3 = Button(root, text="3",  width=25, height=6)
    b3.place(x=40, y=360)
    b3.config(command=hor_h)
    change_button(b3, "Бросок со скоростью, \n направленной горизонтально, \n с высоты ")


    b4 = Button(root, text="4",  width=25, height=6)
    b4.place(x=250, y=120)
    b4.config(command=by_angle_h)
    change_button(b4, "Бросок со скоростью, \n направленной под углом \n к горизонту, с высоты ")


    b5 = Button(root, text="5",  width=25, height=6)
    b5.place(x=250, y=240)
    b5.config(command=vert_v_h)
    change_button(b5, "Бросок с высоты со \n скоростью, направленной \nвертикально вверх")


    b6 = Button(root, text="6",  width=25, height=6)
    b6.place(x=250, y=360)
    b6.config(command=vert_vniz_h)
    change_button(b6, "Бросок с высоты со \n скоростью, направленной \nвертикально вниз")


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