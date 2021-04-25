from tkinter import *
from math import sin, cos, pi, asin, acos, atan, sqrt, tan
import datetime
from tkinter import messagebox as mb
from tkinter import filedialog as fd

root = Tk()
root.title("Движение тела, брошенного под углом к горизонту")
root.resizable(width=False, height=False)

light_theme = True

label_bg_color = '#F7DDC4'
label_text_color = '#0C136F'

button_passive_bg_color = '#79A9F1'
button_passive_fg_color = '#ffffff'
button_active_bg_color = '#99BEF4'
button_active_fg_color = '#ffffff'

graph_x = 380
graph_y = 110


c = Canvas(root, bg='#F7DDC4', width=830, height=650)
root.geometry("830x650")
c.grid(row=0, column=0, columnspan=200, rowspan=70)

grafic = Canvas(root, bg='#D7E6FE', width=400, height=240)
stroim1=True
b_home = Button(root)
vvod = []
g = 9.81

files=[]
BB=[]
cifr = "1234567890.-"
r = 4

telo=''
XY=[]

def change_theme():
    global light_theme
    global main_buttons
    global label_bg_color
    global label_text_color
    global button_passive_bg_color
    global button_passive_fg_color
    global button_active_bg_color
    global button_active_fg_color

    light_theme = not light_theme

    if light_theme:
        label_bg_color = '#F7DDC4'
        label_text_color = '#0C136F'
        button_passive_bg_color = '#79A9F1'
        button_passive_fg_color = '#ffffff'
        button_active_bg_color = '#99BEF4'
        button_active_fg_color = '#ffffff'
    else:
        label_bg_color = 'gray'
        label_text_color = 'red'
        button_passive_bg_color = 'purple'
        button_passive_fg_color = 'blue'
        button_active_bg_color = 'yellow'
        button_active_fg_color = 'green'

    for a in main_buttons:
        a.destroy()

    start_window()

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
    global light_theme

    b1['text'] = st
    b1['bg'] = button_passive_bg_color
    b1['activebackground'] = button_active_bg_color
    b1['fg'] = button_passive_fg_color
    b1['activeforeground'] = button_active_fg_color
        

def delete_main():  # Переход от главного окна к побочному
    global main_buttons
    c.delete("all")
    for a in main_buttons:
        a.destroy()

    global b_home
    b_home = Button(root, height=3, width=7)
    change_button(b_home, 'HOME')
    b_home.place(x=750, y=572)
    b_home.config(command=start_window)


# Под углом к горизонту с земли
def vvod_by_angle_zero(x=True):
    grafic.delete("all")
    global V0
    global A
    for a in XY:
        a.destroy()
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
    flag = True
    if (is_num(V0)):
        col += 1
        V0d = True
        V0 = float(V0)
        if (V0 <= 0):
            flag = False
    if (is_num(A)):
        col += 1
        Ad = True
        A = float(A)
        A = A * pi / 180
        if (A <= 0) or (A >= pi / 2):
            flag = False
    if (is_num(H)):
        col += 1
        Hd = True
        H = float(H)
        if (H <= 0):
            flag = False
    if (is_num(T)):
        col += 1
        Td = True
        T = float(T)
        if (T <= 0):
            flag = False
    if (is_num(L)):
        col += 1
        Ld = True
        L = float(L)
        if (L <= 0):
            flag = False
    if (flag):
        if (V0d and Ad):
            try:
                L = (V0 ** 2) * sin(2 * A) / g
                H = (V0 ** 2) * (sin(A) ** 2) / (2 * g)
                T = 2 * V0 * sin(A) / g
                vL.delete(0, END)
                vH.delete(0, END)
                vT.delete(0, END)
                vL.insert(0, round(L * 1000) / 1000)
                vH.insert(0, round(H * 1000) / 1000)
                vT.insert(0, round(T * 1000) / 1000)
            except:
                mb.showerror("Неверные данные", "Расчёты невозможны")
                stroim = False
        elif (V0d and Ld):
            try:
                A = asin((L*g)/(V0**2)) / 2
                H = (V0 ** 2) * (sin(A) ** 2) / (2 * g)
                T = 2 * V0 * sin(A) / g
                vA.delete(0, END)
                vH.delete(0, END)
                vT.delete(0, END)
                vA.insert(0, round(A*180/pi*1000)/1000)
                vH.insert(0, round(H*1000)/1000)
                vT.insert(0, round(T*1000)/1000)
            except:
                mb.showerror("Неверные данные", "Расчёты невозможны")
                stroim = False
        elif (V0d and Hd):
            try:
                A = asin(sqrt(H*2*g/V0**2))
                L=V0**2 * sin(2*A) / g
                T = 2 * V0 * sin(A) / g
                vA.delete(0, END)
                vL.delete(0, END)
                vT.delete(0, END)
                vA.insert(0, round(A * 180 / pi * 1000) / 1000)
                vL.insert(0, round(L * 1000) / 1000)
                vT.insert(0, round(T * 1000) / 1000)
            except:
                mb.showerror("Неверные данные", "Расчёты невозможны")
                stroim = False
        elif (V0d and Td):
            try:
                A = asin(T*g/(2*V0))
                L = V0 ** 2 * sin(2 * A)  / g
                H = (V0 ** 2) * (sin(A) ** 2) / (2 * g)
                vA.delete(0, END)
                vL.delete(0, END)
                vH.delete(0, END)
                vA.insert(0, round(A*180/pi*1000)/1000)
                vL.insert(0, round(L*1000)/1000)
                vH.insert(0, round(H*1000)/1000)
            except:
                mb.showerror("Неверные данные", "Расчёты невозможны")
                stroim = False
        elif (Ad and Ld):
            try:
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
            except:
                mb.showerror("Неверные данные", "Расчёты невозможны")
                stroim = False
        elif (Ad and Hd):
            try:
                V0 = sqrt(H*2*g/(sin(A))**2)
                T = 2 * V0 * sin(A) / g
                L = V0 ** 2 * sin(2 * A) ** 2 / g
                vV0.delete(0, END)
                vL.delete(0, END)
                vT.delete(0, END)
                vV0.insert(0, round(V0*1000)/1000)
                vL.insert(0, round(L*1000)/1000)
                vT.insert(0, round(T*1000)/1000)
            except:
                mb.showerror("Неверные данные", "Расчёты невозможны")
                stroim = False
        elif (Ad and Td):
            try:
                V0 = T*g/(2*sin(A))
                L = V0 ** 2 * sin(2 * A)  / g
                H = (V0 ** 2) * (sin(A) ** 2) / (2 * g)
                vV0.delete(0, END)
                vL.delete(0, END)
                vH.delete(0, END)
                vV0.insert(0, round(V0 * 1000) / 1000)
                vL.insert(0, round(L * 1000) / 1000)
                vH.insert(0, round(H * 1000) / 1000)
            except:
                mb.showerror("Неверные данные", "Расчёты невозможны")
                stroim = False
        elif (Td and Ld):
            try:
                A = atan(g*T**2/(2*L))
                V0 = T*g/(2*sin(A))
                H = (V0 ** 2) * (sin(A) ** 2) / (2 * g)
                vV0.delete(0, END)
                vA.delete(0, END)
                vH.delete(0, END)
                vV0.insert(0, round(V0*1000)/1000)
                vA.insert(0, round(A*180/pi*1000)/1000)
                vH.insert(0, round(H*1000)/1000)
            except:
                mb.showerror("Неверные данные", "Расчёты невозможны")
                stroim = False
        elif (Hd and Ld):
            try:
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
            except:
                mb.showerror("Неверные данные", "Расчёты невозможны")
                stroim = False
        else:
            mb.showerror("Неверные данные", "Расчёты невозможны")
            stroim = False

        if (stroim):
                global k
                global graph_x
                global graph_y
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
                global xy
                xy = Label(text="x=0.000 , y=0.000", font="Cricket 12")
                xy.config(bd=20, bg=label_bg_color, fg=label_text_color)
                xy.place(x=graph_x+175, y=graph_y+350)
                XY.append(xy)
                telo = grafic.create_oval(10 - r, 210 - r, 10 + r, 210 + r, fill="#c00300")
                i=0
                root.after(10, draw_angle_by_zero)

    else:
        mb.showerror("Неверные данные", "Расчёты невозможны")
        stroim = False

def draw_angle_by_zero():
    global i
    global telo
    global xy, XY
    if (stroim):
        grafic.delete(telo)
        xy.destroy()
        XY=[]

        x = L / 2000 * i
        y = tan(A) * x - g / (2 * V0 ** 2 * cos(A) ** 2) * x ** 2
        x1 = L / 2000 * (i + 1)
        y1 = tan(A) * x1 - g / (2 * V0 ** 2 * cos(A) ** 2) * x1 ** 2
        telo = grafic.create_oval(((x1) * k + 10) - r, 220 - ((y1) * k + 10) - r, ((x1) * k + 10) + r, 220 - ((y1) * k + 10) + r, fill="#c00300")
        grafic.create_line((x) * k + 10, 220 - ((y) * k + 10), ((x1) * k + 10), 220 - ((y1) * k + 10), fill="#c00300")
        i+=1
        xy = Label(text="x="+str(col_znak(round(x*1000)/1000, 3))+", y="+str(col_znak(round(y*1000)/1000, 3)), font="Cricket 12")
        xy.config(bd=20, bg=label_bg_color, fg=label_text_color)
        xy.place(x=graph_x+120, y=graph_y+250)
        XY.append(xy)
        global vvod
        vvod.append(xy)
        if (i<=2000):
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
        f_name = fd.asksaveasfilename(filetypes=(("TXT files", "*.txt"),))
        with open(f_name, "w") as file:
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
    f_name = fd.askopenfilename()
    with open(f_name, "r") as file:
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
    else:
        mb.showerror("Ошибка", "Неверный формат входных данных")

def by_angle_zero():  # Бросок под углом с земли
    global vvod
    vvod = []
    grafic.place(x=graph_x, y=graph_y)

    l1 = Label(text="Введите любые два значения", font="Cricket 16")
    l1.config(bd=20, bg=label_bg_color, fg=label_text_color)
    l1.place(x=20, y=70)
    vvod.append(l1)

    l2 = Label(text="Бросок под углом с земли", font="Cricket 23")
    l2.config(bd=20, bg=label_bg_color, fg=label_text_color)
    l2.place(x=20, y=10)
    vvod.append(l2)

    delete_main()
    global vV0
    vV0= Entry(width=13)
    vV0.place(x=150, y=152)
    vvod.append(vV0)

    bV0 = Label(text="Vo (м/c) =", font="Cricket 10")
    bV0.place(x=64, y=152)
    bV0.config(bg=label_bg_color, fg=label_text_color)
    vvod.append(bV0)

    global vA
    vA= Entry(width=13)
    vA.place(x=150, y=175)
    vvod.append(vA)

    bA = Label(text="Угол (В градусах) = ", font="Cricket 10")
    bA.place(x=5, y=175)
    bA.config(bg=label_bg_color, fg=label_text_color)
    vvod.append(bA)

    global vH
    vH = Entry(width=13)
    vH.place(x=150, y=197)
    vvod.append(vH)

    bH = Label(text="Hmax (м)   = ", font="Cricket 10")
    bH.place(x=49, y=197)
    bH.config(bg=label_bg_color, fg=label_text_color)
    vvod.append(bH)

    global vT
    vT = Entry(width=13)
    vT.place(x=150, y=219)
    vvod.append(vT)

    bT = Label(text="Tполёта (с) = ", font="Cricket 10")
    bT.place(x=46, y=219)
    bT.config(bg=label_bg_color, fg=label_text_color)
    vvod.append(bT)

    global vL
    vL = Entry(width=13)
    vL.place(x=150, y=244)
    vvod.append(vL)

    bL = Label(text="Lполёта (с) = ", font="Cricket 10")
    bL.place(x=46, y=244)
    bL.config(bg=label_bg_color, fg=label_text_color)
    vvod.append(bL)

    bvvesti = Button(root, height=2, width=17)
    change_button(bvvesti, "Ввести значения")
    bvvesti.place(x=20, y=300)
    vvod.append(bvvesti)
    bvvesti.config(command=vvod_by_angle_zero)

    bdel = Button(root, height=2, width=10)
    change_button(bdel, "Удалить\nзначения")
    bdel.place(x=163, y=300)
    vvod.append(bdel)
    bdel.config(command=del_by_angle_zero)

    bopen = Button(root, height=6, width=27, font=('Cricket', 10))
    change_button(bopen, 'Считать значения из файла \n(введите 2 значения, на \nместе остальных "_" в\nследующем порядке: V0, A, H, T, L \n в файл "input.txt" в столбик)')
    bopen.place(x=30, y=425)
    vvod.append(bopen)
    bopen.config(command=file_by_angle_zero)

    bsave = Button(root, height=6, width=27, font=('Cricket', 10))
    change_button(bsave,'Сохранить значения\n в файл')
    bsave.place(x=350, y=425)
    vvod.append(bsave)
    bsave.config(command=save_by_angle_zero)

    l3 = Label(text="ИЛИ", font="Cricket 12")
    l3.config(bd=20, bg=label_bg_color, fg=label_text_color)
    l3.place(x=100, y=350)
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
    for a in XY:
        a.destroy()
    Ad = True
    A = pi/2
    Hd = False
    Td = False
    global stroim
    stroim = x
    flag = True
    if (is_num(V0)):
        col += 1
        V0d = True
        V0 = float(V0)
        if (V0 <= 0):
            flag = False
    if (is_num(H)):
        col += 1
        Hd = True
        H = float(H)
        if (H <= 0):
            flag = False
    if (is_num(T)):
        col += 1
        Td = True
        T = float(T)
        if (T <= 0):
            flag = False
    if (flag):
        if (V0d and Ad):
            try:
                H = (V0 ** 2) * (sin(A) ** 2) / (2 * g)
                T = 2 * V0 * sin(A) / g
                vH.delete(0, END)
                vT.delete(0, END)
                vH.insert(0, round(H * 1000) / 1000)
                vT.insert(0, round(T * 1000) / 1000)
            except:
                mb.showerror("Неверные данные", "Расчёты невозможны")
                stroim = False
        elif (Ad and Hd):
            try:
                V0 = sqrt(H * 2 * g / (sin(A)) ** 2)
                T = 2 * V0 * sin(A) / g
                vV0.delete(0, END)
                vT.delete(0, END)
                vV0.insert(0, round(V0 * 1000) / 1000)
                vT.insert(0, round(T * 1000) / 1000)
            except:
                mb.showerror("Неверные данные", "Расчёты невозможны")
                stroim = False
        elif (Ad and Td):
            try:
                V0 = T * g / (2 * sin(A))
                H = (V0 ** 2) * (sin(A) ** 2) / (2 * g)
                vV0.delete(0, END)
                vH.delete(0, END)
                vV0.insert(0, round(V0 * 1000) / 1000)
                vH.insert(0, round(H * 1000) / 1000)
            except:
                mb.showerror("Неверные данные", "Расчёты невозможны")
                stroim = False
        else:
            vV0.delete(0, END)
            vT.delete(0, END)
            vH.delete(0, END)
            mb.showerror("Неверные данные", "Расчёты невозможны")
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
            global xy
            xy = Label(text="x=0.000 , y=0.000", font="Cricket 12")
            xy.config(bd=20, bg=label_bg_color, fg=label_text_color)
            xy.place(x=graph_x+120, y=graph_y+250)
            XY.append(xy)
            root.after(10, draw_vert_zero)
            
    else:
        vV0.delete(0, END)
        vT.delete(0, END)
        vH.delete(0, END)
        mb.showerror("Неверные данные", "Расчёты невозможны")
        stroim = False

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
        xy.config(bd=20, bg=label_bg_color, fg=label_text_color)
        xy.place(x=graph_x+120, y=graph_y+250)
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
    f_name = fd.askopenfilename()
    with open(f_name, "r") as file:
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
    else:
        mb.showerror("Ошибка", "Неверный формат входных данных")

def save_vert_zero():
    vvod_vert_zero(False)
    global stroim, XY
    stroim = False
    for a in XY:
        a.destroy()
    grafic.delete("all")
    if (is_num(vV0.get()) and is_num(vT.get())):
        f_name = fd.asksaveasfilename(filetypes=(("TXT files", "*.txt"),))
        with open(f_name, "w") as file:
            st = 'Бросок вертикально вверх с земли \n'
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
    grafic.place(x=graph_x, y=graph_y)

    l1 = Label(text="Введите любое значение", font="Cricket 16")
    l1.config(bd=20, bg=label_bg_color, fg=label_text_color)
    l1.place(x=20, y=70)
    vvod.append(l1)

    l2 = Label(text="Бросок вертикально вверх с земли", font="Cricket 23")
    l2.config(bd=20, bg=label_bg_color, fg=label_text_color)
    l2.place(x=20, y=10)
    vvod.append(l2)

    delete_main()
    global vV0
    vV0= Entry(width=13)
    vV0.place(x=164, y=152)
    vvod.append(vV0)

    bV0 = Label(text="Vo (м/с)   =", font="Cricket 10")
    bV0.place(x=76, y=152)
    bV0.config(bg=label_bg_color, fg=label_text_color)
    vvod.append(bV0)


    global vH
    vH = Entry(width=13)
    vH.place(x=164, y=197)
    vvod.append(vH)

    bH = Label(text="Hmax (м)      = ", font="Cricket 10")
    bH.place(x=56, y=197)
    bH.config(bg=label_bg_color, fg=label_text_color)
    vvod.append(bH)

    global vT
    vT = Entry(width=13)
    vT.place(x=164, y=174)
    vvod.append(vT)

    bT = Label(text="Tполёта (с)    = ", font="Cricket 10")
    bT.place(x=53, y=174)
    bT.config(bg=label_bg_color, fg=label_text_color)
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

    bopen = Button(root, height=5, width=30, font=('Cricket', 10))
    change_button(bopen, 'Считать значения из файла \n(введите 1 значение, на \nместе остальных "_" в\nследующем порядке: V0, H, T \n в файл "input.txt" в столбик)' )
    bopen.place(x=30, y=425)
    vvod.append(bopen)
    bopen.config(command=file_vert_zero)

    bsave = Button(root, height=5, width=30, font=('Cricket', 10))
    change_button(bsave,'Сохранить значения\n в файл')
    bsave.place(x=350, y=425)
    vvod.append(bsave)
    bsave.config(command=save_vert_zero)

    l3 = Label(text="ИЛИ", font="Cricket 12")
    l3.config(bd=20, bg=label_bg_color, fg=label_text_color)
    l3.place(x=90, y=350)
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
    for a in XY:
        a.destroy()
    V0d = False
    hd = False
    Td = False
    Ld = False
    flag = True
    stroim = True
    if (is_num(V0)):
        col += 1
        V0d = True
        V0 = float(V0)
        if (V0 <= 0):
            flag = False
    if (is_num(h)):
        col += 1
        hd = True
        h = float(h)
        if (h<= 0):
            flag = False
    if (is_num(T)):
        col += 1
        Td = True
        T = float(T)
        if (T<=0):
            flag = False
    if (is_num(L)):
        col += 1
        Ld = True
        L = float(L)
        if (L<=0):
            flag = False
    if (flag):
        if (V0d and hd):
            try:
                T = sqrt(2*h/g)
                L = V0*T
                vL.delete(0, END)
                vT.delete(0, END)
                vL.insert(0, round(L * 1000) / 1000)
                vT.insert(0, round(T * 1000) / 1000)
            except:
                mb.showerror("Неверные данные", "Расчёты невозможны")
                stroim = False
        elif (V0d and Td):
            try:
                h = T**2 * g/2
                L = V0*T
                vL.delete(0, END)
                vh.delete(0, END)
                vL.insert(0, round(L * 1000) / 1000)
                vh.insert(0, round(h * 1000) / 1000)
            except:
                mb.showerror("Неверные данные", "Расчёты невозможны")
                stroim = False
        elif (Ld and hd):
            try:
                V0 = L*sqrt(g/(2*h))
                T = sqrt(2 * h / g)
                vV0.delete(0, END)
                vT.delete(0, END)
                vV0.insert(0, round(V0 * 1000) / 1000)
                vT.insert(0, round(T * 1000) / 1000)
            except:
                mb.showerror("Неверные данные", "Расчёты невозможны")
                stroim = False
        elif (Td and Ld):
            try:
                V0 = L/T
                h=g*T**2 / 2
                vV0.delete(0, END)
                vh.delete(0, END)
                vV0.insert(0, round(V0 * 1000) / 1000)
                vh.insert(0, round(h * 1000) / 1000)
            except:
                mb.showerror("Неверные данные", "Расчёты невозможны")
                stroim = False
        elif (V0d and Ld):
            try:
                h = g/2 * (L/V0)**2
                T = sqrt(2 * h / g)
                vT.delete(0, END)
                vh.delete(0, END)
                vT.insert(0, round(T * 1000) / 1000)
                vh.insert(0, round(h * 1000) / 1000)
            except:
                mb.showerror("Неверные данные", "Расчёты невозможны")
                stroim = False
        else:
            vV0.delete(0, END)
            vh.delete(0, END)
            vL.delete(0, END)
            vT.delete(0, END)
            mb.showerror("Неверные данные", "Расчёты невозможны")
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
            xy.config(bd=20, bg=label_bg_color, fg=label_text_color)
            xy.place(x=graph_x+120, y=graph_y+250)
            telo = grafic.create_oval(10 - r, 210 - h*k - r, 10 + r, 210 - h*k  + r, fill="#c00300")
            i = 0
            XY.append(xy)
            root.after(10, draw_hor_h)
    else:
        vV0.delete(0, END)
        vh.delete(0, END)
        vL.delete(0, END)
        vT.delete(0, END)
        mb.showerror("Неверные данные", "Расчёты невозможны")
        stroim = False

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
        xy.config(bd=20, bg=label_bg_color, fg=label_text_color)
        xy.place(x=graph_x+120, y=graph_y+250)
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
    f_name = fd.askopenfilename()
    with open(f_name, "r") as file:
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
        f_name = fd.asksaveasfilename(filetypes=(("TXT files", "*.txt"),))
        with open(f_name, "w") as file:
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
    grafic.place(x=graph_x, y=graph_y)

    l1 = Label(text="Введите любые два значения", font="Cricket 16")
    l1.config(bd=20, bg=label_bg_color, fg=label_text_color)
    l1.place(x=20, y=70)
    vvod.append(l1)

    l2 = Label(text="Бросок горизонтально с высоты", font="Cricket 23")
    l2.config(bd=20, bg=label_bg_color, fg=label_text_color)
    l2.place(x=20, y=10)
    vvod.append(l2)

    delete_main()
    global vV0
    vV0 = Entry(width=13)
    vV0.place(x=164, y=152)
    vvod.append(vV0)

    bV0 = Label(text="Vo(м/с)      =", font="Cricket 10")
    bV0.place(x=76, y=152)
    bV0.config(bg=label_bg_color, fg=label_text_color)
    vvod.append(bV0)

    global vh
    vh = Entry(width=13)
    vh.place(x=164, y=175)
    vvod.append(vh)

    bh = Label(text="Начальная высота (м)  = ", font="Cricket 10")
    bh.place(x=4, y=175)
    bh.config(bg=label_bg_color, fg=label_text_color)
    vvod.append(bh)

    global vL
    vL = Entry(width=13)
    vL.place(x=164, y=197)
    vvod.append(vL)

    bL = Label(text="       L(м)        =", font="Cricket 10")
    bL.place(x=60, y=197)
    bL.config(bg=label_bg_color, fg=label_text_color)
    vvod.append(bL)

    global vT
    vT = Entry(width=13)
    vT.place(x=164, y=219)
    vvod.append(vT)

    bT = Label(text="Tполёта(с)       = ", font="Cricket 10")
    bT.place(x=54, y=219)
    bT.config(bg=label_bg_color, fg=label_text_color)
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

    bopen = Button(root, height=5, width=30, font=('Cricket', 10))
    change_button(bopen,
                  'Считать значения из файла \n(введите 2 значения, на \nместе остальных "_" в\nследующем порядке: V0, h, L, T \n в файл "input.txt" в столбик)')
    bopen.place(x=30, y=425)
    vvod.append(bopen)
    bopen.config(command=file_hor_h)

    bsave = Button(root, height=5, width=30, font=('Cricket', 10))
    change_button(bsave, 'Сохранить значения\n в файл')
    bsave.place(x=350, y=425)
    vvod.append(bsave)
    bsave.config(command=save_hor_h)

    l3 = Label(text="ИЛИ", font="Cricket 12")
    l3.config(bd=20, bg=label_bg_color, fg=label_text_color)
    l3.place(x=90, y=350)
    vvod.append(l3)


# вертикально вверх с высоты
def vvod_vert_v_h(x=True):
    grafic.delete("all")
    global V0, h, H, T, Vk
    V0 = vV0.get()
    h = vh.get()
    for a in XY:
        a.destroy()
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
    flag = True
    if (is_num(V0)):
        col += 1
        V0d = True
        V0 = float(V0)
        if (V0 <= 0):
            flag = False
    if (is_num(h)):
        col += 1
        hd = True
        h = float(h)
        if (h <= 0):
            flag = False
    if (is_num(H)):
        col += 1
        Hd = True
        H = float(H)
        if (H <= 0):
            flag = False
    if (is_num(T)):
        col += 1
        Td = True
        T = float(T)
        if (T <= 0):
            flag = False
    if (is_num(Vk)):
        col += 1
        Vkd = True
        Vk = float(Vk)
        if (Vk <= 0):
            flag = False
    if (flag):
        if (V0d and Vkd):
            if (Vk < V0):
                mb.showerror("Неверные данные", "Расчёты невозможны")
                stroim = False
            else:
                try:
                    h = (Vk**2-V0**2)/(2*g)
                    H = h + V0**2/(2*g)
                    T = (V0+sqrt(V0**2+2*g*h))/g
                    vh.delete(0, END)
                    vH.delete(0, END)
                    vT.delete(0, END)
                    vh.insert(0, round(h*1000)/1000)
                    vH.insert(0, round(H*1000)/1000)
                    vT.insert(0, round(T*1000)/1000)
                except:
                    mb.showerror("Неверные данные", "Расчёты невозможны")
                    stroim = False
        elif (V0d and hd):
            try:
                T=(V0+sqrt(V0**2+2*g*h))/g
                H = h + V0 ** 2 / (2 * g)
                Vk=sqrt(V0**2+2*g*h)
                vVk.delete(0, END)
                vH.delete(0, END)
                vT.delete(0, END)
                vVk.insert(0, round(Vk * 1000) / 1000)
                vH.insert(0, round(H * 1000) / 1000)
                vT.insert(0, round(T * 1000) / 1000)
            except:
                mb.showerror("Неверные данные", "Расчёты невозможны")
                stroim = False
        elif (V0d and Hd):
            try:
                h = H-V0**2/(2*g)
                T = (V0 + sqrt(V0 ** 2 + 2 * g * h)) / g
                Vk = sqrt(V0 ** 2 + 2 * g * h)
                vVk.delete(0, END)
                vh.delete(0, END)
                vT.delete(0, END)
                vVk.insert(0, round(Vk * 1000) / 1000)
                vh.insert(0, round(h * 1000) / 1000)
                vT.insert(0, round(T * 1000) / 1000)
            except:
                mb.showerror("Неверные данные", "Расчёты невозможны")
                stroim = False
        elif (V0d and Td):
            try:
                h = (g**2*(T-V0/g)**2-V0**2)/(2*g)
                H = h + V0 ** 2 / (2 * g)
                Vk = sqrt(V0 ** 2 + 2 * g * h)
                vVk.delete(0, END)
                vh.delete(0, END)
                vH.delete(0, END)
                vVk.insert(0, round(Vk * 1000) / 1000)
                vh.insert(0, round(h * 1000) / 1000)
                vH.insert(0, round(H * 1000) / 1000)
            except:
                mb.showerror("Неверные данные", "Расчёты невозможны")
                stroim = False
        elif (hd and Hd):
            if (H-h<0):
                mb.showerror("Ошибка",  "Расчеты невозможны")
                stroim = False
            else:
                try:
                    V0 = sqrt((H - h) * 2 * g)
                    T = (V0 + sqrt(V0 ** 2 + 2 * g * h)) / g
                    Vk = sqrt(V0 ** 2 + 2 * g * h)
                    vVk.delete(0, END)
                    vT.delete(0, END)
                    vV0.delete(0, END)
                    vVk.insert(0, round(Vk * 1000) / 1000)
                    vT.insert(0, round(T * 1000) / 1000)
                    vV0.insert(0, round(V0 * 1000) / 1000)
                except:
                    mb.showerror("Неверные данные", "Расчёты невозможны")
                    stroim = False
        elif (hd and Td):
            try:
                V0 = (T**2*g-2*h)/(2*T)
                Vk = sqrt(V0 ** 2 + 2 * g * h)
                H = h + V0 ** 2 / (2 * g)
                vVk.delete(0, END)
                vH.delete(0, END)
                vV0.delete(0, END)
                vVk.insert(0, round(Vk * 1000) / 1000)
                vH.insert(0, round(H * 1000) / 1000)
                vV0.insert(0, round(V0 * 1000) / 1000)
            except:
                mb.showerror("Неверные данные", "Расчёты невозможны")
                stroim = False
        elif (hd and Vkd):
            if (Vk**2-2*g*h <0):
                mb.showerror("Ошибка", "Расчеты невзможны")
                stroim = False
            else:
                try:
                    V0 = sqrt(Vk**2-2*g*h)
                    H = h + V0 ** 2 / (2 * g)
                    T = (V0 + sqrt(V0 ** 2 + 2 * g * h)) / g
                    vT.delete(0, END)
                    vH.delete(0, END)
                    vV0.delete(0, END)
                    vT.insert(0, round(T * 1000) / 1000)
                    vH.insert(0, round(H * 1000) / 1000)
                    vV0.insert(0, round(V0 * 1000) / 1000)
                except:
                    mb.showerror("Неверные данные", "Расчёты невозможны")
                    stroim = False
        elif (Hd and Td):
            try:
                V0 = T*g-sqrt(2*g*H)
                h = (2*g*H-V0**2)/(2*g)
                Vk = sqrt(V0**2+2*g*h)
                vVk.delete(0, END)
                vh.delete(0, END)
                vV0.delete(0, END)
                vVk.insert(0, round(Vk * 1000) / 1000)
                vh.insert(0, round(h * 1000) / 1000)
                vV0.insert(0, round(V0 * 1000) / 1000)
            except:
                mb.showerror("Неверные данные", "Расчёты невозможны")
                stroim = False
        elif (Td and Vkd):
            try:
                V0 = T*g-Vk
                h = (Vk**2-V0**2)/(2*g)
                H = h + V0 ** 2 / (2 * g)
                vH.delete(0, END)
                vh.delete(0, END)
                vV0.delete(0, END)
                vH.insert(0, round(H * 1000) / 1000)
                vh.insert(0, round(h * 1000) / 1000)
                vV0.insert(0, round(V0 * 1000) / 1000)
            except:
                mb.showerror("Неверные данные", "Расчёты невозможны")
                stroim = False
        else:
            vV0.delete(0, END)
            vh.delete(0, END)
            vH.delete(0, END)
            vT.delete(0, END)
            vVk.delete(0, END)
            mb.showerror("Неверные данные", "Расчёты невозможны")
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
            global xy
            xy = Label(text="x=0.000 , y="+str(h), font="Cricket 12")
            xy.config(bd=20, bg=label_bg_color, fg=label_text_color)
            xy.place(x=graph_x+120, y=graph_y+250)
            XY.append(xy)
            root.after(1, draw_vert_v_h)
    else:
        vV0.delete(0, END)
        vh.delete(0, END)
        vH.delete(0, END)
        vT.delete(0, END)
        vVk.delete(0, END)
        mb.showerror("Неверные данные", "Расчёты невозможны")
        stroim = False

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
        xy.config(bd=20, bg=label_bg_color, fg=label_text_color)
        xy.place(x=graph_x+120, y=graph_y+250)
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
    f_name = fd.askopenfilename()
    with open(f_name, "r") as file:
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
        f_name = fd.asksaveasfilename(filetypes=(("TXT files", "*.txt"),))
        with open(f_name, "w") as file:
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
    grafic.place(x=graph_x, y=graph_y)

    l1 = Label(text="Введите любые два значения", font="Cricket 16")
    l1.config(bd=20, bg=label_bg_color, fg=label_text_color)
    l1.place(x=20, y=70)
    vvod.append(l1)

    l2 = Label(text="Бросок вертикально вверх с высоты", font="Cricket 23")
    l2.config(bd=20, bg=label_bg_color, fg=label_text_color)
    l2.place(x=20, y=10)
    vvod.append(l2)

    delete_main()
    global vV0
    vV0 = Entry(width=13)
    vV0.place(x=164, y=152)
    vvod.append(vV0)

    bV0 = Label(text="Vo(м/с)   =", font="Cricket 10")
    bV0.place(x=75, y=152)
    bV0.config(bg=label_bg_color, fg=label_text_color)
    vvod.append(bV0)

    global vh
    vh = Entry(width=13)
    vh.place(x=164, y=175)
    vvod.append(vh)

    bh = Label(text="h(м)      =", font="Cricket 10")
    bh.place(x=83, y=175)
    bh.config(bg=label_bg_color, fg=label_text_color)
    vvod.append(bh)

    global vH
    vH = Entry(width=13)
    vH.place(x=164, y=197)
    vvod.append(vH)

    bH = Label(text="Hmax(м)       = ", font="Cricket 10")
    bH.place(x=52, y=197)
    bH.config(bg=label_bg_color, fg=label_text_color)
    vvod.append(bH)

    global vT
    vT = Entry(width=13)
    vT.place(x=164, y=219)
    vvod.append(vT)

    bT = Label(text="Tполёта(с)    = ", font="Cricket 10")
    bT.place(x=53, y=219)
    bT.config(bg=label_bg_color, fg=label_text_color)
    vvod.append(bT)


    global vVk
    vVk = Entry(width=13)
    vVk.place(x=164, y=244)
    vvod.append(vVk)

    bVk = Label(text="Vконечная(м/c)  = ", font="Cricket 10")
    bVk.place(x=31, y=244)
    bVk.config(bg=label_bg_color, fg=label_text_color)
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

    bopen = Button(root, height=5, width=30, font=('Cricket', 10))
    change_button(bopen,
                  'Считать значения из файла \n(введите 2 значения, на \nместе остальных "_" в\nследующем порядке: V0, h, H, T, Vk \n в файл "input.txt" в столбик)')
    bopen.place(x=30, y=425)
    vvod.append(bopen)
    bopen.config(command=file_vert_v_h)

    bsave = Button(root, height=5, width=30, font=('Cricket', 10))
    change_button(bsave, 'Сохранить значения\n в файл')
    bsave.place(x=350, y=425)
    vvod.append(bsave)
    bsave.config(command=save_vert_v_h)

    l3 = Label(text="ИЛИ", font="Cricket 12")
    l3.config(bd=20, bg=label_bg_color, fg=label_text_color)
    l3.place(x=90, y=350)
    vvod.append(l3)


# вертикально вниз с высоты

def vvod_vert_vniz_h(x=True):
    grafic.delete("all")
    global V0, h, T, Vk
    V0 = vV0.get()
    global XY
    for a in XY:
        a.destroy()
    h = vh.get()
    T = vT.get()
    Vk = vVk.get()
    col=0
    V0d = False
    hd = False
    Td = False
    Vkd = False
    global stroim
    flag = True
    stroim = x
    if (is_num(V0)):
        col += 1
        V0d = True
        V0 = float(V0)
        if (V0 < 0):
            flag = False
    if (is_num(h)):
        col += 1
        hd = True
        h = float(h)
        if (h < 0):
            flag = False
    if (is_num(T)):
        col += 1
        Td = True
        T = float(T)
        if (T < 0):
            flag = False
    if (is_num(Vk)):
        col += 1
        Vkd = True
        Vk = float(Vk)
        if (Vk < 0):
            flag = False
    if (flag):
        if (V0d and Vkd):
            if (Vk < V0):
                mb.showerror("Неверные данные", "Расчёты невозможны")
                stroim = False
            else:
                try:
                    h = (Vk**2-V0**2)/(2*g)
                    T = (-V0+sqrt(V0**2+2*g*h))/g
                    vh.delete(0, END)
                    vT.delete(0, END)
                    vh.insert(0, round(h*1000)/1000)
                    vT.insert(0, round(T*1000)/1000)
                except:
                    mb.showerror("Неверные данные", "Расчёты невозможны")
                    stroim = False
        elif (V0d and hd):
            try:
                T=(-V0+sqrt(V0**2+2*g*h))/g
                Vk=sqrt(V0**2+2*g*h)
                vVk.delete(0, END)
                vT.delete(0, END)
                vVk.insert(0, round(Vk * 1000) / 1000)
                vT.insert(0, round(T * 1000) / 1000)
            except:
                mb.showerror("Неверные данные", "Расчёты невозможны")
                stroim = False
        elif (V0d and Td):
            try:
                h = (g**2*(T+V0/g)**2-V0**2)/(2*g)
                Vk = sqrt(V0 ** 2 + 2 * g * h)
                vVk.delete(0, END)
                vh.delete(0, END)
                vVk.insert(0, round(Vk * 1000) / 1000)
                vh.insert(0, round(h * 1000) / 1000)
            except:
                mb.showerror("Неверные данные", "Расчёты невозможны")
                stroim = False
        elif (hd and Td):
            try:
                V0 = -1 * (T**2*g-2*h)/(2*T)
                Vk = sqrt(V0 ** 2 + 2 * g * h)
                vVk.delete(0, END)
                vV0.delete(0, END)
                vVk.insert(0, round(Vk * 1000) / 1000)
                vV0.insert(0, round(V0 * 1000) / 1000)
            except:
                mb.showerror("Неверные данные", "Расчёты невозможны")
                stroim = False
        elif (hd and Vkd):
            if (Vk**2-2*g*h <0):
                mb.showerror("Ошибка", "Расчеты невзможны")
                stroim = False
            else:
                try:
                    V0 = sqrt(Vk**2-2*g*h)
                    T=(-V0+sqrt(V0**2+2*g*h))/g
                    vT.delete(0, END)
                    vV0.delete(0, END)
                    vT.insert(0, round(T * 1000) / 1000)
                    vV0.insert(0, round(V0 * 1000) / 1000)
                except:
                    mb.showerror("Неверные данные", "Расчёты невозможны")
                    stroim = False
        elif (Td and Vkd):
            try:
                V0 = -(T*g-Vk)
                h = (Vk**2-V0**2)/(2*g)
                vh.delete(0, END)
                vV0.delete(0, END)
                vh.insert(0, round(h * 1000) / 1000)
                vV0.insert(0, round(V0 * 1000) / 1000)
            except:
                mb.showerror("Неверные данные", "Расчёты невозможны")
                stroim = False
        else:
            vV0.delete(0, END)
            vh.delete(0, END)
            vT.delete(0, END)
            vVk.delete(0, END)
            mb.showerror("Неверные данные", "Расчёты невозможны")
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
            global xy
            xy = Label(text="x=0.000 , y="+str(h), font="Cricket 12")
            xy.config(bd=20, bg=label_bg_color, fg=label_text_color)
            xy.place(x=graph_x+120, y=graph_y+250)
            XY.append(xy)
            root.after(1, draw_vert_vniz_h)
    else:
        vV0.delete(0, END)
        vh.delete(0, END)
        vT.delete(0, END)
        vVk.delete(0, END)
        mb.showerror("Неверные данные", "Расчёты невозможны")
        stroim = False

def draw_vert_vniz_h():
    global i
    global telo
    global xy, XY
    global stroim
    global h, k
    col = 1000
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
        xy.config(bd=20, bg=label_bg_color, fg=label_text_color)
        xy.place(x=graph_x+120, y=graph_y+250)
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
    f_name = fd.askopenfilename()
    with open(f_name, "r") as file:
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
        f_name = fd.asksaveasfilename(filetypes=(("TXT files", "*.txt"),))
        with open(f_name, "w") as file:
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
    grafic.place(x=graph_x, y=graph_y)

    l1 = Label(text="Введите любые два значения", font="Cricket 16")
    l1.config(bd=20, bg=label_bg_color, fg=label_text_color)
    l1.place(x=20, y=70)
    vvod.append(l1)

    l2 = Label(text="Бросок вертикально вниз с высоты", font="Cricket 23")
    l2.config(bd=20, bg=label_bg_color, fg=label_text_color)
    l2.place(x=20, y=10)
    vvod.append(l2)

    delete_main()
    global vV0
    vV0 = Entry(width=13)
    vV0.place(x=164, y=152)
    vvod.append(vV0)

    bV0 = Label(text="Vo(м/с)   =", font="Cricket 10")
    bV0.place(x=75, y=152)
    bV0.config(bg=label_bg_color, fg=label_text_color)
    vvod.append(bV0)

    global vh
    vh = Entry(width=13)
    vh.place(x=164, y=175)
    vvod.append(vh)

    bh = Label(text="h(м)      =", font="Cricket 10")
    bh.place(x=83, y=175)
    bh.config(bg=label_bg_color, fg=label_text_color)
    vvod.append(bh)


    global vT
    vT = Entry(width=13)
    vT.place(x=164, y=219)
    vvod.append(vT)

    bT = Label(text="Tполёта(с)    = ", font="Cricket 10")
    bT.place(x=53, y=219)
    bT.config(bg=label_bg_color, fg=label_text_color)
    vvod.append(bT)


    global vVk
    vVk = Entry(width=13)
    vVk.place(x=164, y=197)
    vvod.append(vVk)

    bVk = Label(text="Vконечная(м/c)  = ", font="Cricket 10")
    bVk.place(x=31, y=197)
    bVk.config(bg=label_bg_color, fg=label_text_color)
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

    bopen = Button(root, height=5, width=30, font=('Cricket', 10))
    change_button(bopen,
                  'Считать значения из файла \n(введите 2 значения, на \nместе остальных "_" в\nследующем порядке: V0, h, Vk, T \n в файл "input.txt" в столбик)')
    bopen.place(x=30, y=425)
    vvod.append(bopen)
    bopen.config(command=file_vert_vniz_h)

    bsave = Button(root, height=5, width=30, font=('Cricket', 10))
    change_button(bsave, 'Сохранить значения\n в файл')
    bsave.place(x=350, y=425)
    vvod.append(bsave)
    bsave.config(command=save_vert_vniz_h)

    l3 = Label(text="ИЛИ", font="Cricket 12")
    l3.config(bd=20, bg=label_bg_color, fg=label_text_color)
    l3.place(x=90, y=350)
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
    global XY
    for a in XY:
        a.destroy()
    global V0, h, A, B, T, L
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
    flag = True
    global stroim
    stroim = x
    if (is_num(V0)):
        col += 1
        V0d = True
        V0 = float(V0)
        if (V0 <= 0):
            flag = False
    if (is_num(h)):
        col += 1
        hd = True
        h = float(h)
        if (h <= 0):
            flag = False
    if (is_num(A)):
        col += 1
        Ad = True
        A = float(A)
        A = A * pi / 180
    if (is_num(H)):
        col += 1
        Hd = True
        H = float(H)
        if (H <= 0):
            flag = False
    if (is_num(T)):
        col += 1
        Td = True
        T = float(T)
        if (T <= 0):
            flag = False
    if (is_num(L)):
        col += 1
        Ld = True
        L = float(L)
        if (L <= 0):
            flag = False
    if (flag):
        if (V0d and Ad and hd):
            if (A > -pi/2) and (A < pi/2):
                try:
                    L = (V0**2*sin(A)*cos(A)+V0*cos(A)*sqrt(V0**2*sin(A)**2+2*g*h)) / g
                    H = (V0**2*sin(A)**2+2*g*h)/(2 * g)
                    T = (V0*sin(A)+sqrt(V0**2*sin(A)**2+2*g*h)) / g
                    vL.delete(0, END)
                    vH.delete(0, END)
                    vT.delete(0, END)
                    vL.insert(0, round(L*1000)/1000)
                    vH.insert(0, round(H*1000)/1000)
                    vT.insert(0, round(T*1000)/1000)
                except:
                    mb.showerror("Неверные данные", "Расчёты невозможны")
                    stroim = False
            else:
                stroim = False
                mb.showerror("Неверные данные", "Расчёты невозможны")
        elif (V0d and hd and Hd):
            if (h <= H) and (V0 != 0):
                try:
                    A=asin(sqrt(2*g*(H-h)/V0**2))
                    L = (V0 ** 2 * sin(A) * cos(A) + V0 * cos(A) * sqrt(V0 ** 2 * sin(A) ** 2 + 2 * g * h)) / g
                    T = (V0 * sin(A) + sqrt(V0 ** 2 * sin(A) ** 2 + 2 * g * h)) / g
                    vL.delete(0, END)
                    vA.delete(0, END)
                    vT.delete(0, END)
                    vL.insert(0, round(L * 1000) / 1000)
                    vA.insert(0, round(A*180/pi * 1000) / 1000)
                    vT.insert(0, round(T * 1000) / 1000)
                except:
                    mb.showerror("Неверные данные", "Расчёты невозможны")
                    stroim = False
            else:
                stroim = False
                mb.showerror("Неверные данные", "Расчёты невозможны")
        elif (V0d and hd and Td):
            x=(T**2*g - 2*h)/ (2*T*V0)
            if (x>-1) and (x<1):
                try:
                    A=asin(x)
                    L = (V0 ** 2 * sin(A) * cos(A) + V0 * cos(A) * sqrt(V0 ** 2 * sin(A) ** 2 + 2 * g * h)) / g
                    H = (V0**2*sin(A)**2+2*g*h)/(2 * g)
                    vL.delete(0, END)
                    vA.delete(0, END)
                    vH.delete(0, END)
                    vL.insert(0, round(L * 1000) / 1000)
                    vA.insert(0, round(A * 180 / pi * 1000) / 1000)
                    vH.insert(0, round(H * 1000) / 1000)
                except:
                    mb.showerror("Неверные данные", "Расчёты невозможны")
                    stroim = False
            else:
                stroim = False
                mb.showerror("Неверные данные", "Расчёты невозможны")
        elif (V0d and hd and Ld):
            D = (V0**2+g*h)**2 - g**2*(h**2+L**2)
            if (D>0):
                T = sqrt((V0**2 + g*h + sqrt(D))/(g**2/2))
                if (L/(T*V0) > -1) and (L/(T*V0) < 1):
                    try:
                        A = acos(L/(T*V0))
                        H = (V0 ** 2 * sin(A) ** 2 + 2 * g * h) / (2 * g)
                        vT.delete(0, END)
                        vA.delete(0, END)
                        vH.delete(0, END)
                        vT.insert(0, round(T * 1000) / 1000)
                        vA.insert(0, round(A * 180 / pi * 1000) / 1000)
                        vH.insert(0, round(H * 1000) / 1000)
                    except:
                        mb.showerror("Неверные данные", "Расчёты невозможны")
                        stroim = False
                else:
                    stroim = False
                    mb.showerror("Неверные данные", "Расчёты невозможны")
            else:
                stroim = False
                mb.showerror("Неверные данные", "Расчёты невозможны")
        elif (hd and Ad and Hd):
            if (H>=h):
                try:
                    V0 = sqrt((H-h)*2*g/sin(A)**2)
                    L = (V0 ** 2 * sin(A) * cos(A) + V0 * cos(A) * sqrt(V0 ** 2 * sin(A) ** 2 + 2 * g * h)) / g
                    T = (V0 * sin(A) + sqrt(V0 ** 2 * sin(A) ** 2 + 2 * g * h)) / g
                    vT.delete(0, END)
                    vA.delete(0, END)
                    vL.delete(0, END)
                    vT.insert(0, round(T * 1000) / 1000)
                    vV0.insert(0, round(V0 * 1000) / 1000)
                    vL.insert(0, round(L * 1000) / 1000)
                except:
                    mb.showerror("Неверные данные", "Расчёты невозможны")
                    stroim = False
            else:
                stroim = False
                mb.showerror("Неверные данные", "Расчёты невозможны")
        elif (hd and Ad and Td):
            V0 = (T**2*g-2*h)/(2*T*sin(A))
            if (V0>0):
                try:
                    L = (V0 ** 2 * sin(A) * cos(A) + V0 * cos(A) * sqrt(V0 ** 2 * sin(A) ** 2 + 2 * g * h)) / g
                    H = (V0 ** 2 * sin(A) ** 2 + 2 * g * h) / (2 * g)
                    vL.delete(0, END)
                    vV0.delete(0, END)
                    vH.delete(0, END)
                    vL.insert(0, round(L * 1000) / 1000)
                    vV0.insert(0, round(V0 * 1000) / 1000)
                    vH.insert(0, round(H * 1000) / 1000)
                except:
                    mb.showerror("Неверные данные", "Расчёты невозможны")
                    stroim = False
            else:
                stroim = False
                mb.showerror("Неверные данные", "Расчёты невозможны")
        elif (hd and Ad and Ld):
            x = L**2*g**2/(2*(L*g*sin(A)*cos(A) + g*h*cos(A)**2))
            if (x>0):
                try:
                    V0 = sqrt(x)
                    H = (V0 ** 2 * sin(A) ** 2 + 2 * g * h) / (2 * g)
                    T = (V0 * sin(A) + sqrt(V0 ** 2 * sin(A) ** 2 + 2 * g * h)) / g
                    vT.delete(0, END)
                    vV0.delete(0, END)
                    vH.delete(0, END)
                    vT.insert(0, round(T * 1000) / 1000)
                    vV0.insert(0, round(V0 * 1000) / 1000)
                    vH.insert(0, round(H * 1000) / 1000)
                except:
                    mb.showerror("Неверные данные", "Расчёты невозможны")
                    stroim = False
            else:
                stroim = False
                mb.showerror("Неверные данные", "Расчёты невозможны")
        elif (V0d and Ad and Hd):
            try:
                if (A<=0):
                    h = H
                    L = (V0 ** 2 * sin(A) * cos(A) + V0 * cos(A) * sqrt(V0 ** 2 * sin(A) ** 2 + 2 * g * h)) / g
                    T = (V0 * sin(A) + sqrt(V0 ** 2 * sin(A) ** 2 + 2 * g * h)) / g
                else:
                    h = H - V0**2*sin(A)**2/(2*g)
                    L = (V0 ** 2 * sin(A) * cos(A) + V0 * cos(A) * sqrt(V0 ** 2 * sin(A) ** 2 + 2 * g * h)) / g
                    T = (V0 * sin(A) + sqrt(V0 ** 2 * sin(A) ** 2 + 2 * g * h)) / g
                vL.delete(0, END)
                vT.delete(0, END)
                vh.delete(0, END)
                vL.insert(0, round(L * 1000) / 1000)
                vT.insert(0, round(T * 1000) / 1000)
                vh.insert(0, round(h * 1000) / 1000)
            except:
                mb.showerror("Неверные данные", "Расчёты невозможны")
                stroim = False
        elif (V0d and Ad and Td):
            try:
                h = ((T*g-V0*sin(A))**2-V0**2*sin(A)**2)/(2*g)
                L = (V0 ** 2 * sin(A) * cos(A) + V0 * cos(A) * sqrt(V0 ** 2 * sin(A) ** 2 + 2 * g * h)) / g
                H = (V0 ** 2 * sin(A) ** 2 + 2 * g * h) / (2 * g)
                vL.delete(0, END)
                vH.delete(0, END)
                vh.delete(0, END)
                vL.insert(0, round(L * 1000) / 1000)
                vH.insert(0, round(H * 1000) / 1000)
                vh.insert(0, round(h * 1000) / 1000)
            except:
                mb.showerror("Неверные данные", "Расчёты невозможны")
                stroim = False
        elif (V0d and Ad and Ld):
            try:
                T = L/(V0*cos(A))
                h = ((T*g-V0*sin(A))**2-V0**2*sin(A)**2)/(2*g)
                H = (V0 ** 2 * sin(A) ** 2 + 2 * g * h) / (2 * g)
                vT.delete(0, END)
                vH.delete(0, END)
                vh.delete(0, END)
                vT.insert(0, round(T * 1000) / 1000)
                vH.insert(0, round(H * 1000) / 1000)
                vh.insert(0, round(h * 1000) / 1000)
            except:
                mb.showerror("Неверные данные", "Расчёты невозможны")
                stroim = False
        elif (Ad and Hd and Td):
            try:
                V0 = (g*T - sqrt(2*g*H))/g
                h = H - V0**2*sin(A)**2/(2*g)
                L = V0*cos(A)*T
                vV0.delete(0, END)
                vL.delete(0, END)
                vh.delete(0, END)
                vV0.insert(0, round(V0 * 1000) / 1000)
                vL.insert(0, round(L * 1000) / 1000)
                vh.insert(0, round(h * 1000) / 1000)
            except:
                mb.showerror("Неверные данные", "Расчёты невозможны")
                stroim = False
        elif (Ad and Hd and Ld):
            try:
                D = (cos(A)*sqrt(2*g*H))**2 + 4*L*sin(A)*cos(A)*g
                V0 = max((-1*cos(A)*sqrt(2*g*H) + sqrt(D))/(2*sin(A)*cos(A)), (-1*cos(A)*sqrt(2*g*H) - sqrt(D))/(2*sin(A)*cos(A)))
                h = H - V0 ** 2 * sin(A) ** 2 / (2 * g)
                T = L/(V0 * cos(A))
                vV0.delete(0, END)
                vT.delete(0, END)
                vh.delete(0, END)
                vV0.insert(0, round(V0 * 1000) / 1000)
                vT.insert(0, round(T * 1000) / 1000)
                vh.insert(0, round(h * 1000) / 1000)
            except:
                mb.showerror("Неверные данные", "Расчёты невозможны")
                stroim = False
        elif (Td and Ld and Hd):
            try:
                A = atan(T*(T*g- sqrt(2*g*H))/L)
                V0 = L/(T*cos(A))
                h = H - V0**2 * sin(A)**2/(2*g)
                vh.delete(0, END)
                vA.delete(0, END)
                vV0.delete(0, END)
                vh.insert(0, round(h * 1000) / 1000)
                vA.insert(0, round(A * 180 / pi * 1000) / 1000)
                vV0.insert(0, round(H * 1000) / 1000)
            except:
                mb.showerror("Неверные данные", "Расчёты невозможны")
                stroim = False
        elif (hd and Td and Ld):
            V0 =sqrt((L**2 + (g*T**2/2 - h)**2)/T**2)
            x = L/(V0*T)
            if (x>-1) and (x<1):
                try:
                    A = acos(x)
                    H = (V0 ** 2 * sin(A) ** 2 + 2 * g * h) / (2 * g)
                    vH.delete(0, END)
                    vA.delete(0, END)
                    vV0.delete(0, END)
                    vH.insert(0, round(H * 1000) / 1000)
                    vA.insert(0, round(A * 180 / pi * 1000) / 1000)
                    vV0.insert(0, round(H * 1000) / 1000)
                except:
                    mb.showerror("Неверные данные", "Расчёты невозможны")
                    stroim = False
            else:
                stroim = False
                mb.showerror("Неверные данные", "Расчёты невозможны")
        elif (V0d and Hd and Td):
            x = (T*g-sqrt(2*g*H))/V0
            if (x>-1)and (x<1):
                try:
                    A = asin(x)
                    h = H - (V0**2*sin(A)**2)/(2*g)
                    L =T*V0*cos(A)
                    vH.delete(0, END)
                    vA.delete(0, END)
                    vL.delete(0, END)
                    vH.insert(0, round(H * 1000) / 1000)
                    vA.insert(0, round(A * 180 / pi * 1000) / 1000)
                    vL.insert(0, round(L * 1000) / 1000)
                except:
                    mb.showerror("Неверные данные", "Расчёты невозможны")
                    stroim = False
            else:
                stroim = False
                mb.showerror("Неверные данные", "Расчёты невозможны")
        elif (V0d and Hd and Td):
            x = (T*g - sqrt(2*g*H))/V0
            if (x>-1)and(x<1):
                try:
                    A = asin(x)
                    h = H - V0**2*sin(A)**2/(2*g)
                    L = V0*cos(A)*T
                    vh.delete(0, END)
                    vA.delete(0, END)
                    vL.delete(0, END)
                    vh.insert(0, round(h * 1000) / 1000)
                    vA.insert(0, round(A * 180 / pi * 1000) / 1000)
                    vL.insert(0, round(L * 1000) / 1000)
                except:
                    mb.showerror("Неверные данные", "Расчёты невозможны")
                    stroim = False
            else:
                stroim = False
                mb.showerror("Неверные данные", "Расчёты невозможны")
        elif (Ad and Td and Ld):
            V0 = L/(T*cos(A))
            H = (T*g - V0*sin(A))**2/(2*g)
            h = H - V0**2*sin(A)**2/(2*g)
            vV0.delete(0, END)
            vh.delete(0, END)
            vH.delete(0, END)
            vV0.insert(0, round(V0 * 1000) / 1000)
            vH.insert(0, round(H * 1000) / 1000)
            vh.insert(0, round(h * 1000) / 1000)
        else:
            vV0.delete(0, END)
            vA.delete(0, END)
            vT.delete(0, END)
            vL.delete(0, END)
            vh.delete(0, END)
            vH.delete(0, END)
            mb.showerror("Неверные данные", "Расчёты невозможны")        
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
            global xy
            xy = Label(text="x=0.000 , y=0.000", font="Cricket 12")
            xy.config(bd=20, bg=label_bg_color, fg=label_text_color)
            xy.place(x= 400, y=320)
            XY.append(xy)
            telo = grafic.create_oval(10 - r, 210-h*k - r, 10 + r, 210-h*k + r, fill="#c00300")
            i=0
            root.after(10, draw_angle_by_h)
    else:
        vV0.delete(0, END)
        vA.delete(0, END)
        vT.delete(0, END)
        vL.delete(0, END)
        vh.delete(0, END)
        vH.delete(0, END)
        mb.showerror("Неверные данные", "Расчёты невозможны")
        stroim = False

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
        xy.config(bd=20, bg=label_bg_color, fg=label_text_color)
        xy.place(x=graph_x+120, y=graph_y+250)
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
    f_name = fd.askopenfilename()
    with open(f_name, "r") as file:
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
    else:
        mb.showerror("Ошибка", "Неверный формат входных данных")

def save_by_angle_h():
    vvod_by_angle_h(False)
    global stroim, XY
    stroim = False
    for a in XY:
        a.destroy()
    grafic.delete("all")
    if (is_num(vV0.get()) and is_num(vA.get())):
        f_name = fd.asksaveasfilename(filetypes=(("TXT files", "*.txt"),))
        with open(f_name, "w") as file:
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
    grafic.place(x=graph_x, y=graph_y)

    l1 = Label(text="Введите любые три значения", font="Cricket 16")
    l1.config(bd=20, bg=label_bg_color, fg=label_text_color)
    l1.place(x=20, y=70)
    vvod.append(l1)

    l2 = Label(text="Бросок под углом к горизонту с высоты", font="Cricket 20")
    l2.config(bd=20, bg=label_bg_color, fg=label_text_color)
    l2.place(x=20, y=10)
    vvod.append(l2)

    delete_main()

    global vh
    vh = Entry(width=13)
    vh.place(x=164, y=150)
    vvod.append(vh)

    bh = Label(text="h (м)    =", font="Cricket 10")
    bh.place(x=70, y=150)
    bh.config(bg=label_bg_color, fg=label_text_color)
    vvod.append(bh)

    global vV0
    vV0= Entry(width=13)
    vV0.place(x=164, y=175)
    vvod.append(vV0)

    bV0 = Label(text="Vo (м/c)  =", font="Cricket 10")
    bV0.place(x=70, y=175)
    bV0.config(bg=label_bg_color, fg=label_text_color)
    vvod.append(bV0)

    global vA
    vA= Entry(width=13)
    vA.place(x=164, y=201)
    vvod.append(vA)

    bA = Label(text="Угол (В градусах)  = ", font="Cricket 10")
    bA.place(x=17, y=201)
    bA.config(bg=label_bg_color, fg=label_text_color)
    vvod.append(bA)

    global vH
    vH = Entry(width=13)
    vH.place(x=164, y=223)
    vvod.append(vH)

    bH = Label(text="Hmax (м)    = ", font="Cricket 10")
    bH.place(x=61, y=223)
    bH.config(bg=label_bg_color, fg=label_text_color)
    vvod.append(bH)

    global vT
    vT = Entry(width=13)
    vT.place(x=164, y=248)
    vvod.append(vT)

    bT = Label(text="Tполёта (с)  = ", font="Cricket 10")
    bT.place(x=58, y=248)
    bT.config(bg=label_bg_color, fg=label_text_color)
    vvod.append(bT)

    global vL
    vL = Entry(width=13)
    vL.place(x=164, y=275)
    vvod.append(vL)

    bL = Label(text="Lполёта (м)   = ", font="Cricket 10")
    bL.place(x=52, y=275)
    bL.config(bg=label_bg_color, fg=label_text_color)
    vvod.append(bL)

    bvvesti = Button(root, height=2, width=17)
    change_button(bvvesti, "Ввести значения")
    bvvesti.place(x=20, y=330)
    vvod.append(bvvesti)
    bvvesti.config(command=vvod_by_angle_h)

    bdel = Button(root, height=2, width=10)
    change_button(bdel, "Удалить\nзначения")
    bdel.place(x=163, y=330)
    vvod.append(bdel)
    bdel.config(command=del_by_angle_h)

    bopen = Button(root, height=5, width=30, font=('Cricket', 10))
    change_button(bopen, 'Считать значения из файла \n(введите 2 значения, на \nместе остальных "_" в\nследующем порядке: h, V0, A, H, T, L \n в файл "input.txt" в столбик)' )
    bopen.place(x=30, y=450)
    vvod.append(bopen)
    bopen.config(command=file_by_angle_h)

    bsave = Button(root, height=5, width=30, font=('Cricket', 10))
    change_button(bsave,'Сохранить значения\n в файл')
    bsave.place(x=350, y=450)
    vvod.append(bsave)
    bsave.config(command=save_by_angle_h)

    l3 = Label(text="ИЛИ", font="Cricket 12")
    l3.config(bd=20, bg=label_bg_color, fg=label_text_color)
    l3.place(x=90, y=380)
    vvod.append(l3)


# Под углом с движущегося тела

def vvod_by_angle_h_move(x=True):
    grafic.delete("all")
    global V0
    global Vdop
    global A
    global H
    global T
    global L
    global h
    global XY
    for a in XY:
        a.destroy()
    global V0, h, A, B, T, L, Vdop
    h = vh.get()
    V0 = vV0.get()
    A = vA.get()
    H = vH.get()
    T = vT.get()
    L = vL.get()
    Vdop = vVdop.get()
    col=0
    V0d = False
    Ad = False
    Hd = False
    Td = False
    Ld = False
    hd = False
    Vdopd = False
    flag = True
    global stroim
    stroim = x
    if (is_num(V0)):
        col += 1
        V0d = True
        V0 = float(V0)
        if (V0 <= 0):
            flag = False
    if (is_num(h)):
        col += 1
        hd = True
        h = float(h)
        if (h <= 0):
            flag = False
    if (is_num(A)):
        col += 1
        Ad = True
        A = float(A)
        A = A * pi / 180
    if (is_num(H)):
        col += 1
        Hd = True
        H = float(H)
        if (H <= 0):
            flag = False
    if (is_num(T)):
        col += 1
        Td = True
        T = float(T)
        if (T <= 0):
            flag = False
    if (is_num(L)):
        col += 1
        Ld = True
        L = float(L)
        if (L <= 0):
            flag = False
    if (is_num(Vdop)):
        col += 1
        Vdopd = True
        Vdop = float(Vdop)
        if (Vdop <= 0):
            flag = False
    if (flag):
        if (V0d and Ad and hd and Vdopd):
            if (A > -pi/2) and (A < pi/2):
                try:
                    T = (V0*sin(A)+sqrt(V0**2*sin(A)**2+2*g*h)) / g
                    L = (V0*cos(A) + Vdop)*T
                    H = (V0**2*sin(A)**2 + 2*g*h)/(2*g)
                    vL.delete(0, END)
                    vH.delete(0, END)
                    vT.delete(0, END)
                    vL.insert(0, round(L*1000)/1000)
                    vH.insert(0, round(H*1000)/1000)
                    vT.insert(0, round(T*1000)/1000)
                except:
                    mb.showerror("Неверные данные", "Расчёты невозможны")
                    stroim = False
            else:
                stroim = False
                mb.showerror("Неверные данные", "Расчёты невозможны")
        elif (V0d and Ad and Hd and Vdopd): # 15
            if (A > -pi/2) and (A < pi/2):
                try:
                    h = H - (V0 ** 2 * sin(A) ** 2) / (2 * g)
                    T = (V0*sin(A)+sqrt(V0**2*sin(A)**2+2*g*h)) / g
                    L = (V0*cos(A) + Vdop)*T
                    vL.delete(0, END)
                    vh.delete(0, END)
                    vT.delete(0, END)
                    vL.insert(0, round(L*1000)/1000)
                    vh.insert(0, round(h*1000)/1000)
                    vT.insert(0, round(T*1000)/1000)
                except:
                    mb.showerror("Неверные данные", "Расчёты невозможны")
                    stroim = False
            else:
                stroim = False
                mb.showerror("Неверные данные", "Расчёты невозможны")
        elif (V0d and Ad and Td and Vdopd): # 16
            if (A > -pi/2) and (A < pi/2):
                try:
                    H = ((T - (V0 * sin(A)) / g) ** 2 * g) / 2
                    h = H - (V0 ** 2 * sin(A) ** 2) / (2 * g)
                    L = (V0*cos(A) + Vdop)*T
                    vH.delete(0, END)
                    vh.delete(0, END)
                    vL.delete(0, END)
                    vH.insert(0, round(H*1000)/1000)
                    vh.insert(0, round(h*1000)/1000)
                    vL.insert(0, round(L*1000)/1000)
                except:
                    mb.showerror("Неверные данные", "Расчёты невозможны")
                    stroim = False
            else:
                stroim = False
                mb.showerror("Неверные данные", "Расчёты невозможны")
        elif (V0d and Ad and Ld and Vdopd): # 17
            if (A > -pi/2) and (A < pi/2):
                try:
                    T = L / (V0 * cos(A) + Vdop)
                    H = ((T - (V0 * sin(A)) / g) ** 2 * g) / 2
                    h = H - (V0 ** 2 * sin(A) ** 2) / (2 * g)
                    vh.delete(0, END)
                    vH.delete(0, END)
                    vT.delete(0, END)
                    vH.insert(0, round(H*1000)/1000)
                    vh.insert(0, round(h*1000)/1000)
                    vT.insert(0, round(T*1000)/1000)
                except:
                    mb.showerror("Неверные данные", "Расчёты невозможны")
                    stroim = False
            else:
                stroim = False
                mb.showerror("Неверные данные", "Расчёты невозможны")
        elif (V0d and hd and Hd and Vdopd): # 18
            try:
                A = asin((sqrt((H - h) * 2 * g)) / V0)
                T = (V0*sin(A)+sqrt(V0**2*sin(A)**2+2*g*h)) / g
                L = (V0*cos(A) + Vdop)*T
                vA.delete(0, END)
                vL.delete(0, END)
                vT.delete(0, END)
                vA.insert(0, round(A*1000)/1000)
                vL.insert(0, round(L*1000)/1000)
                vT.insert(0, round(T*1000)/1000)
            except:
                mb.showerror("Неверные данные", "Расчёты невозможны")
                stroim = False
        elif (V0d and Td and hd and Vdopd): # 19
            try:
                A = asin((T**2 - 2*h) / (2*T*V0))
                H = h + (((V0**2)*(sin(A)**2)) / (2*g))
                L = (V0*cos(A) + Vdop)*T
                vA.delete(0, END)
                vL.delete(0, END)
                vH.delete(0, END)
                vA.insert(0, round(A*1000)/1000)
                vL.insert(0, round(L*1000)/1000)
                vH.insert(0, round(H*1000)/1000)
            except:
                mb.showerror("Неверные данные", "Расчёты невозможны")
                stroim = False
        elif (V0d and Td and Hd and Vdopd): # 20
            try:
                A = asin(((T - sqrt((2 * H) / g)) * g) / Vdop) 
                h = H - ((V0**2*sin(A)**2) / (2*g))
                L = (V0*cos(A) + Vdop)*T
                vA.delete(0, END)
                vL.delete(0, END)
                vh.delete(0, END)
                vA.insert(0, round(A*1000)/1000)
                vL.insert(0, round(L*1000)/1000)
                vh.insert(0, round(h*1000)/1000)
            except:
                mb.showerror("Неверные данные", "Расчёты невозможны")
                stroim = False
        elif (V0d and Td and Ld and Vdopd): # 21
            try:
                A = acos((L - Vdop * T) / (V0*T))
                H = (((T - (V0*sin(A))/g))**2*g) / 2 
                h = H - (V0**2*sin(A)**2) / (2*g)
                vA.delete(0, END)
                vh.delete(0, END)
                vH.delete(0, END)
                vA.insert(0, round(A*1000)/1000)
                vh.insert(0, round(h*1000)/1000)
                vH.insert(0, round(H*1000)/1000)
            except:
                mb.showerror("Неверные данные", "Расчёты невозможны")
                stroim = False
        elif (V0d and Ad and hd and Ld): # 22
            if (A > -pi/2) and (A < pi/2):
                try:
                    H = h + ((V0**2)*(sin(A)**2)) / (2*g)
                    T = (V0*sin(A) + sqrt(2*H*g)) / g 
                    Vdop = L/T - V0*cos(A)
                    vVdop.delete(0, END)
                    vH.delete(0, END)
                    vT.delete(0, END)
                    vVdop.insert(0, round(Vdop*1000)/1000)
                    vH.insert(0, round(H*1000)/1000)
                    vT.insert(0, round(T*1000)/1000)
                except:
                    mb.showerror("Неверные данные", "Расчёты невозможны")
                    stroim = False
            else:
                stroim = False
                mb.showerror("Неверные данные", "Расчёты невозможны")
        elif (V0d and Ad and Hd and Ld): # 23
            if (A > -pi/2) and (A < pi/2):
                try:
                    h = H - (V0**2*sin(A)**2) / (2*g)
                    T = (V0*sin(A) + sqrt(2*H*g)) / g
                    Vdop = L/T - V0*cos(A)
                    vL.delete(0, END)
                    vh.delete(0, END)
                    vVdop.delete(0, END)
                    vL.insert(0, round(L*1000)/1000)
                    vh.insert(0, round(h*1000)/1000)
                    vVdop.insert(0, round(Vdop*1000)/1000)
                except Exception as e:
                    mb.showerror("Неверные данные", "Расчёты невозможны")
                    stroim = False
            else:
                stroim = False
                mb.showerror("Неверные данные", "Расчёты невозможны")
        elif (V0d and Ad and Td and Ld): # 24
            if (A > -pi/2) and (A < pi/2):
                try:
                    H = (((T - (V0*sin(A))/g))**2*g) / 2 
                    h = H - (V0**2*sin(A)**2) / (2*g)
                    Vdop = L/T - V0*cos(A)
                    vVdop.delete(0, END)
                    vH.delete(0, END)
                    vh.delete(0, END)
                    vVdop.insert(0, round(Vdop*1000)/1000)
                    vH.insert(0, round(H*1000)/1000)
                    vh.insert(0, round(h*1000)/1000)
                except:
                    mb.showerror("Неверные данные", "Расчёты невозможны")
                    stroim = False
            else:
                stroim = False
                mb.showerror("Неверные данные", "Расчёты невозможны")
        elif (V0d and hd and Hd and Ld): # 25
            try:
                A = asin((sqrt((H - h) * 2 * g)) / V0)
                T = (V0*sin(A) + sqrt(2*H*g)) / g
                Vdop = L/T - V0*cos(A)
                vA.delete(0, END)
                vT.delete(0, END)
                vVdop.delete(0, END)
                vA.insert(0, round(A*1000)/1000)
                vT.insert(0, round(T*1000)/1000)
                vVdop.insert(0, round(Vdop*1000)/1000)
            except:
                mb.showerror("Неверные данные", "Расчёты невозможны")
                stroim = False
        elif (V0d and hd and Td and Ld): # 26
            try:
                A = asin((T**2*g - 2*h) / (2*T*V0))
                H = h + ((V0**2*sin(A)**2) / (2*g))
                Vdop = L/T - V0*cos(A)
                vA.delete(0, END)
                vH.delete(0, END)
                vVdop.delete(0, END)
                vA.insert(0, round(A*1000)/1000)
                vH.insert(0, round(H*1000)/1000)
                vVdop.insert(0, round(Vdop*1000)/1000)
            except:
                mb.showerror("Неверные данные", "Расчёты невозможны")
                stroim = False
        elif (V0d and Td and Hd and Ld): # 27
            try:
                A = asin(((T - sqrt((2 * H) / g)) * g) / V0) 
                h = H - (V0**2*sin(A)**2) / (2*g)
                Vdop = L/T - V0*cos(A)
                vA.delete(0, END)
                vH.delete(0, END)
                vVdop.delete(0, END)
                vA.insert(0, round(A*1000)/1000)
                vH.insert(0, round(H*1000)/1000)
                vVdop.insert(0, round(Vdop*1000)/1000)
            except Exception as e:
                print(e)
                mb.showerror("Неверные данные", "Расчёты невозможны")
                stroim = False
        elif (hd and Ad and Hd and Vdopd): # 28
            if (A > -pi/2) and (A < pi/2):
                try:
                    V0 = sqrt(2*g*(H-h)) / sin(A)
                    T = (V0*sin(A) + sqrt(2*H*g)) / g
                    L = (V0*cos(A) + Vdop) * T
                    vV0.delete(0, END)
                    vT.delete(0, END)
                    vL.delete(0, END)
                    vV0.insert(0, round(V0*1000)/1000)
                    vT.insert(0, round(T*1000)/1000)
                    vL.insert(0, round(L*1000)/1000)
                except:
                    mb.showerror("Неверные данные", "Расчёты невозможны")
                    stroim = False
            else:
                stroim = False
                mb.showerror("Неверные данные", "Расчёты невозможны")
        elif (Td and Ad and hd and Vdopd): # 29
            if (A > -pi/2) and (A < pi/2):
                try:
                    V0 = (T**2*g - 2*h) / (2*T*sin(A))
                    H = h + ((V0**2*sin(A)**2) / (2*g))
                    L = (V0*cos(A) + Vdop) * T
                    vV0.delete(0, END)
                    vH.delete(0, END)
                    vL.delete(0, END)
                    vV0.insert(0, round(V0*1000)/1000)
                    vH.insert(0, round(H*1000)/1000)
                    vL.insert(0, round(L*1000)/1000)
                except:
                    mb.showerror("Неверные данные", "Расчёты невозможны")
                    stroim = False
            else:
                stroim = False
                mb.showerror("Неверные данные", "Расчёты невозможны")
        elif (Ld and Ad and hd and Vdopd): # 30
            if (A > -pi/2) and (A < pi/2):
                try:
                    V0 = (-L*sin(A)*Vdop - 2*h*Vdop*cos(A) + sqrt((L*Vdop*sin(A) + 2*h*Vdop*cos(A))**2 - (L*sin(2*A) + 2*h*cos(A)**2)*(2*h*Vdop**2 - L**2*g))) / (L*sin(2*A) + 2*h*cos(A)**2)
                    H = h + ((V0**2*sin(A)**2) / (2*g))
                    T = (V0*sin(A) + sqrt(2*H*g)) / g
                    vV0.delete(0, END)
                    vH.delete(0, END)
                    vT.delete(0, END)
                    vV0.insert(0, round(V0*1000)/1000)
                    vH.insert(0, round(H*1000)/1000)
                    vT.insert(0, round(T*1000)/1000)
                except:
                    mb.showerror("Неверные данные", "Расчёты невозможны")
                    stroim = False
            else:
                stroim = False
                mb.showerror("Неверные данные", "Расчёты невозможны")
        elif (Td and Ad and Hd and Vdopd): # 31
            if (A > -pi/2) and (A < pi/2):
                try:
                    V0 = (T*g + sqrt(2*H*g)) / sin(A)
                    h = H - (V0**2*sin(A)**2) / (2*g)
                    L = (V0*cos(A) + Vdop)*T
                    vV0.delete(0, END)
                    vh.delete(0, END)
                    vL.delete(0, END)
                    vV0.insert(0, round(V0*1000)/1000)
                    vh.insert(0, round(h*1000)/1000)
                    vL.insert(0, round(L*1000)/1000)
                except:
                    mb.showerror("Неверные данные", "Расчёты невозможны")
                    stroim = False
            else:
                stroim = False
                mb.showerror("Неверные данные", "Расчёты невозможны")
        elif (Ld and Ad and Hd and Vdopd): # 32
            if (A > -pi/2) and (A < pi/2):
                try:
                    V0 = (-Vdop*sin(A) - sqrt(2*H/g)*g*cos(A) + sqrt((Vdop*sin(A) + sqrt(2*H/g)*g*cos(A))**2 - 2*sin(2*A)*(4*sqrt(2*H/g)*g - L*g))) / sin(2*A)
                    h = H - ((V0**2*sin(A)**2) / (2*g))
                    T = (V0*sin(A) + sqrt(2*H*g)) / g
                    vV0.delete(0, END)
                    vh.delete(0, END)
                    vT.delete(0, END)
                    vV0.insert(0, round(V0*1000)/1000)
                    vh.insert(0, round(h*1000)/1000)
                    vT.insert(0, round(T*1000)/1000)
                except:
                    mb.showerror("Неверные данные", "Расчёты невозможны")
                    stroim = False
            else:
                stroim = False
                mb.showerror("Неверные данные", "Расчёты невозможны")
        elif (Ld and Ad and Td and Vdopd): # 33
            if (A > -pi/2) and (A < pi/2):
                try:
                    V0 = (L/T - Vdop) / cos(A)
                    H = (g*((T - (V0*sin(A))/g))**2) / 2 
                    h = H - (V0**2*sin(A)**2) / (2*g)
                    vV0.delete(0, END)
                    vH.delete(0, END)
                    vh.delete(0, END)
                    vV0.insert(0, round(V0*1000)/1000)
                    vH.insert(0, round(H*1000)/1000)
                    vh.insert(0, round(h*1000)/1000)
                except:
                    mb.showerror("Неверные данные", "Расчёты невозможны")
                    stroim = False
            else:
                stroim = False
                mb.showerror("Неверные данные", "Расчёты невозможны")
        elif (Ld and hd and Hd and Vdopd): # 34
            try:
                A = acos((g*L - sqrt(2*H*g)*Vdop)/(2*g*sqrt(H*(H-h))))
                V0 = sqrt(2*g*(H-h)) / sin(A)
                T = (V0*sin(A) + sqrt(2*H*g)) / g
                vA.delete(0, END)
                vV0.delete(0, END)
                vT.delete(0, END)
                vA.insert(0, round(A*1000)/1000)
                vV0.insert(0, round(V0*1000)/1000)
                vT.insert(0, round(T*1000)/1000)
            except Exception as e:
                print(e)
                mb.showerror("Неверные данные", "Расчёты невозможны")
                stroim = False
        elif (Vdopd and hd and Td and Ld): # 35
            try:
                A = atan((g*T**2 - 2*h)/(2*(L - Vdop*T)))
                V0 = (L/T -Vdop) / cos(A)
                H = h + (V0**2 * sin(A)**2)
                vA.delete(0, END)
                vV0.delete(0, END)
                vH.delete(0, END)
                vA.insert(0, round(A*1000)/1000)
                vV0.insert(0, round(V0*1000)/1000)
                vH.insert(0, round(H*1000)/1000)
            except:
                mb.showerror("Неверные данные", "Расчёты невозможны")
                stroim = False
        else:
            vV0.delete(0, END)
            vA.delete(0, END)
            vT.delete(0, END)
            vL.delete(0, END)
            vh.delete(0, END)
            vH.delete(0, END)
            vVdop.delete(0, END)
            mb.showerror("Неверные данные", "Расчёты невозможны")
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
            t1 = V0*sin(A)/g
            grafic.create_line(10 + t1*k * (V0*cos(A) + Vdop), 10, 10 + t1*k * (V0*cos(A) + Vdop), 215, dash=True)
            global i
            global telo
            global xy
            xy = Label(text="x=0.000 , y=0.000", font="Cricket 12")
            xy.config(bd=20, bg=label_bg_color, fg=label_text_color)
            xy.place(x= 400, y=320)
            XY.append(xy)
            telo = grafic.create_oval(10 - r, 210-h*k - r, 10 + r, 210-h*k + r, fill="#c00300")
            i=0
            global telo1
            telo1 = grafic.create_rectangle(10-8, 210-3-h*k, 10+8, 210+3-h*k, fill="#00003d")
            root.after(10, draw_angle_by_h_move)
    else:
        vV0.delete(0, END)
        vA.delete(0, END)
        vT.delete(0, END)
        vL.delete(0, END)
        vh.delete(0, END)
        vH.delete(0, END)
        vVdop.delete(0, END)
        mb.showerror("Неверные данные", "Расчёты невозможны")
        stroim = False

def del_by_angle_h_move():
    vA.delete(0, END)
    vh.delete(0, END)
    vH.delete(0, END)
    vV0.delete(0, END)
    vT.delete(0, END)
    vL.delete(0, END)
    vVdop.delete(0, END)
    global stroim, XY
    stroim = False
    for a in XY:
        a.destroy()
    grafic.delete("all")

def draw_angle_by_h_move():
    global i
    global telo, telo1
    global xy, XY
    if (stroim):
        grafic.delete(telo)
        grafic.delete(telo1)
        xy.destroy()
        XY=[]
        x = L / 2000 * i
        t = x/(V0*cos(A) + Vdop)
        y = h + V0*sin(A)*t - g*t**2/2
        x1 = L / 2000 * (i + 1)
        t1 = x1 / (V0 * cos(A) + Vdop)
        y1 = h + V0 * sin(A) * t1 - g * t1 ** 2 / 2
        telo = grafic.create_oval(((x1) * k + 10) - r, 220 - ((y1) * k + 10) - r, ((x1) * k + 10) + r, 220 - ((y1) * k + 10) + r, fill="#c00300")
        telo1 = grafic.create_rectangle(10 - 15 + t1*(Vdop), 210 - 3 - h * k, 10 + 15+ t1*(Vdop), 210 + 3 - h * k, fill="#00003d")
        grafic.create_line((x) * k + 10, 220 - ((y) * k + 10), ((x1) * k + 10), 220 - ((y1) * k + 10), fill="#c00300")
        i+=1
        xy = Label(text="x="+str(col_znak(round(x*1000)/1000, 3))+", y="+str(col_znak(round(y*1000)/1000, 3)), font="Cricket 12")
        xy.config(bd=20, bg=label_bg_color, fg=label_text_color)
        xy.place(x=graph_x+120, y=graph_y+250)
        XY.append(xy)
        global vvod
        vvod.append(xy)
        if (i<=2000):
            root.after(1, draw_angle_by_h_move)

def file_by_angle_h_move():
    colvo = 0
    n = 0
    f_name = fd.askopenfilename()
    with open(f_name, "r") as file:
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
                fVdop = st
                if (is_num(fVdop)):
                    n+=1
            st = file.readline()
    if (colvo==4) and (n==4):
        vh.delete(0, END)
        vL.delete(0, END)
        vH.delete(0, END)
        vT.delete(0, END)
        vV0.delete(0, END)
        vVdop.delete(0, END)
        vA.delete(0, END)
        if (is_num(fh)):
            vh.insert(0, str(fh))
        if (is_num(fV0)):
            vV0.insert(0, str(fV0))
        if (is_num(fA)):
            vA.insert(0, str(fA))
        if (is_num(fVdop)):
            vVdop.insert(0, str(fVdop))
        vvod_by_angle_h_move()
    else:
        mb.showerror("Ошибка", "Неверный формат входных данных")

def save_by_angle_h_move():
    vvod_by_angle_h_move(False)
    global stroim, XY
    stroim = False
    for a in XY:
        a.destroy()
    grafic.delete("all")
    if (is_num(vV0.get()) and is_num(vA.get())):
        f_name = fd.asksaveasfilename(filetypes=(("TXT files", "*.txt"),))
        with open(f_name, "w") as file:
            st = 'Бросок под углом к горизонту с учетом ветра \n'
            file.write(st)
            st = "h (м) = " + str(vh.get()) + '\n'
            file.write(st)
            st = "Vo (м/с) = " + str(vV0.get()) + '\n'
            file.write(st)
            st = "Vплатформы (м/с) = " + str(vVdop.get()) + '\n'
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

def by_angle_h_move():
    global vvod
    vvod = []
    grafic.place(x=graph_x, y=graph_y)

    l1 = Label(text="Введите любые четыре значения", font="Cricket 16")
    l1.config(bd=20, bg=label_bg_color, fg=label_text_color)
    l1.place(x=7, y=70)
    vvod.append(l1)

    l2 = Label(text="Бросок под углом к горизонту с движущегося тела на высоте", font="Cricket 18")
    l2.config(bd=20, bg=label_bg_color, fg=label_text_color)
    l2.place(x=7, y=10)
    vvod.append(l2)

    delete_main()

    global vh
    vh = Entry(width=13)
    vh.place(x=172, y=128)
    vvod.append(vh)

    bh = Label(text="h (м)        =", font="Cricket 10")
    bh.place(x=84, y=128)
    bh.config(bg=label_bg_color, fg=label_text_color)
    vvod.append(bh)

    global vV0
    vV0= Entry(width=13)
    vV0.place(x=172, y=152)
    vvod.append(vV0)

    bV0 = Label(text="Vo (м/с)     =", font="Cricket 10")
    bV0.place(x=76, y=152)
    bV0.config(bg=label_bg_color, fg=label_text_color)
    vvod.append(bV0)

    global vA
    vA= Entry(width=13)
    vA.place(x=172, y=175)
    vvod.append(vA)

    bA = Label(text="Угол (В градусах)      = ", font="Cricket 10")
    bA.place(x=13, y=175)
    bA.config(bg=label_bg_color, fg=label_text_color)
    vvod.append(bA)

    global vVdop
    vVdop = Entry(width=13)
    vVdop.place(x=172, y=198)
    vvod.append(vVdop)

    bVdop = Label(text="Vdop (м/с)       = ", font="Cricket 10")
    bVdop.place(x=54 , y=198)
    bVdop.config(bg=label_bg_color, fg=label_text_color)
    vvod.append(bVdop)

    global vH
    vH = Entry(width=13)
    vH.place(x=172, y=221)
    vvod.append(vH)

    bH = Label(text="Hmax (м)    = ", font="Cricket 10")
    bH.place(x=73, y=221)
    bH.config(bg=label_bg_color, fg=label_text_color)
    vvod.append(bH)

    global vT
    vT = Entry(width=13)
    vT.place(x=172, y=243)
    vvod.append(vT)

    bT = Label(text="Tполёта (с)  = ", font="Cricket 10")
    bT.place(x=71, y=243)
    bT.config(bg=label_bg_color, fg=label_text_color)
    vvod.append(bT)

    global vL
    vL = Entry(width=13)
    vL.place(x=172, y=266)
    vvod.append(vL)

    bL = Label(text="Lполёта (м)  = ", font="Cricket 10")
    bL.place(x=70, y=266)
    bL.config(bg=label_bg_color, fg=label_text_color)
    vvod.append(bL)

    bvvesti = Button(root, height=2, width=17)
    change_button(bvvesti, "Ввести значения")
    bvvesti.place(x=20, y=303)
    vvod.append(bvvesti)
    bvvesti.config(command=vvod_by_angle_h_move)

    bdel = Button(root, height=2, width=10)
    change_button(bdel, "Удалить\nзначения")
    bdel.place(x=163, y=303)
    vvod.append(bdel)
    bdel.config(command=del_by_angle_h_move)

    bopen = Button(root, height=5, width=30, font=('Cricket', 10))
    change_button(bopen, 'Считать значения из файла \n(введите 4 значения\n в следующем порядке: h, V0, A, \nVплатформы в файл "input.txt"\n в столбик)' )
    bopen.place(x=30, y=420)
    vvod.append(bopen)
    bopen.config(command=file_by_angle_h_move)

    bsave = Button(root, height=5, width=30, font=('Cricket', 10))
    change_button(bsave,'Сохранить значения\n в файл')
    bsave.place(x=350, y=420)
    vvod.append(bsave)
    bsave.config(command=save_by_angle_h_move)

    l3 = Label(text="ИЛИ", font="Cricket 12", height=1)
    l3.config(bd=12, bg=label_bg_color, fg=label_text_color)
    l3.place(x=90, y=360)
    vvod.append(l3)

# Под углом с высоты под углом к горизонту с учетом ветра

def vvod_by_angle_h_wind(x=True):
    grafic.delete("all")
    global V0 # начальная скорость
    global Vdop # скорость ветра
    global A # angle
    global H # макс. высота
    global T # время
    global L # дальность
    global h # начальная высота
    global XY
    for a in XY:
        a.destroy()
    global V0, h, A, B, T, L, Vdop
    h = vh.get()
    V0 = vV0.get()
    A = vA.get()
    H = vH.get()
    T = vT.get()
    L = vL.get()
    Vdop = vVdop.get()
    col=0
    V0d = False
    Ad = False
    Hd = False
    Td = False
    Ld = False
    hd = False
    Vdopd = False
    flag = True
    global stroim
    stroim = x
    if (is_num(V0)):
        col += 1
        V0d = True
        V0 = float(V0)
        if (V0 <= 0):
            flag = False
    if (is_num(h)):
        col += 1
        hd = True
        h = float(h)
        if (h <= 0):
            flag = False
    if (is_num(A)):
        col += 1
        Ad = True
        A = float(A)
        A = A * pi / 180
    if (is_num(H)):
        col += 1
        Hd = True
        H = float(H)
        if (H <= 0):
            flag = False
    if (is_num(T)):
        col += 1
        Td = True
        T = float(T)
        if (T <= 0):
            flag = False
    if (is_num(L)):
        col += 1
        Ld = True
        L = float(L)
        if (L <= 0):
            flag = False
    if (is_num(Vdop)):
        col += 1
        Vdopd = True
        Vdop = float(Vdop)
        if (Vdop <= 0):
            flag = False
    if (flag):
        if (V0d and Ad and hd and Vdopd):
            if (A > -pi/2) and (A < pi/2):
                try:
                    T = (V0*sin(A)+sqrt(V0**2*sin(A)**2+2*g*h)) / g
                    L = (V0*cos(A) + Vdop)*T
                    H = (V0**2*sin(A)**2 + 2*g*h)/(2*g)
                    vL.delete(0, END)
                    vH.delete(0, END)
                    vT.delete(0, END)
                    vL.insert(0, round(L*1000)/1000)
                    vH.insert(0, round(H*1000)/1000)
                    vT.insert(0, round(T*1000)/1000)
                except:
                    mb.showerror("Неверные данные", "Расчёты невозможны")
                    stroim = False
            else:
                stroim = False
                mb.showerror("Неверные данные", "Расчёты невозможны")
        elif (V0d and Ad and Hd and Vdopd): # 15
            if (A > -pi/2) and (A < pi/2):
                try:
                    h = H - (V0 ** 2 * sin(A) ** 2) / (2 * g)
                    T = (V0*sin(A)+sqrt(V0**2*sin(A)**2+2*g*h)) / g
                    L = (V0*cos(A) + Vdop)*T
                    vL.delete(0, END)
                    vh.delete(0, END)
                    vT.delete(0, END)
                    vL.insert(0, round(L*1000)/1000)
                    vh.insert(0, round(h*1000)/1000)
                    vT.insert(0, round(T*1000)/1000)
                except:
                    mb.showerror("Неверные данные", "Расчёты невозможны")
                    stroim = False
            else:
                stroim = False
                mb.showerror("Неверные данные", "Расчёты невозможны")
        elif (V0d and Ad and Td and Vdopd): # 16
            if (A > -pi/2) and (A < pi/2):
                try:
                    H = ((T - (V0 * sin(A)) / g) ** 2 * g) / 2
                    h = H - (V0 ** 2 * sin(A) ** 2) / (2 * g)
                    L = (V0*cos(A) + Vdop)*T
                    vH.delete(0, END)
                    vh.delete(0, END)
                    vL.delete(0, END)
                    vH.insert(0, round(H*1000)/1000)
                    vh.insert(0, round(h*1000)/1000)
                    vL.insert(0, round(L*1000)/1000)
                except:
                    mb.showerror("Неверные данные", "Расчёты невозможны")
                    stroim = False
            else:
                stroim = False
                mb.showerror("Неверные данные", "Расчёты невозможны")
        elif (V0d and Ad and Ld and Vdopd): # 17
            if (A > -pi/2) and (A < pi/2):
                try:
                    T = L / (V0 * cos(A) + Vdop)
                    H = ((T - (V0 * sin(A)) / g) ** 2 * g) / 2
                    h = H - (V0 ** 2 * sin(A) ** 2) / (2 * g)
                    vh.delete(0, END)
                    vH.delete(0, END)
                    vT.delete(0, END)
                    vH.insert(0, round(H*1000)/1000)
                    vh.insert(0, round(h*1000)/1000)
                    vT.insert(0, round(T*1000)/1000)
                except:
                    mb.showerror("Неверные данные", "Расчёты невозможны")
                    stroim = False
            else:
                stroim = False
                mb.showerror("Неверные данные", "Расчёты невозможны")
        elif (V0d and hd and Hd and Vdopd): # 18
            try:
                A = asin((sqrt((H - h) * 2 * g)) / V0)
                T = (V0*sin(A)+sqrt(V0**2*sin(A)**2+2*g*h)) / g
                L = (V0*cos(A) + Vdop)*T
                vA.delete(0, END)
                vL.delete(0, END)
                vT.delete(0, END)
                vA.insert(0, round(A*1000)/1000)
                vL.insert(0, round(L*1000)/1000)
                vT.insert(0, round(T*1000)/1000)
            except:
                mb.showerror("Неверные данные", "Расчёты невозможны")
                stroim = False
        elif (V0d and Td and hd and Vdopd): # 19
            try:
                A = asin((T**2 - 2*h) / (2*T*V0))
                H = h + (((V0**2)*(sin(A)**2)) / (2*g))
                L = (V0*cos(A) + Vdop)*T
                vA.delete(0, END)
                vL.delete(0, END)
                vH.delete(0, END)
                vA.insert(0, round(A*1000)/1000)
                vL.insert(0, round(L*1000)/1000)
                vH.insert(0, round(H*1000)/1000)
            except:
                mb.showerror("Неверные данные", "Расчёты невозможны")
                stroim = False
        elif (V0d and Td and Hd and Vdopd): # 20
            try:
                A = asin(((T - sqrt((2 * H) / g)) * g) / Vdop) 
                h = H - ((V0**2*sin(A)**2) / (2*g))
                L = (V0*cos(A) + Vdop)*T
                vA.delete(0, END)
                vL.delete(0, END)
                vh.delete(0, END)
                vA.insert(0, round(A*1000)/1000)
                vL.insert(0, round(L*1000)/1000)
                vh.insert(0, round(h*1000)/1000)
            except Exception as e:
                print(e)
                mb.showerror("Неверные данные", "Расчёты невозможны")
                stroim = False
        elif (V0d and Td and Ld and Vdopd): # 21
            try:
                A = acos((L - Vdop * T) / (V0*T))
                H = (((T - (V0*sin(A))/g))**2*g) / 2 
                h = H - (V0**2*sin(A)**2) / (2*g)
                vA.delete(0, END)
                vh.delete(0, END)
                vH.delete(0, END)
                vA.insert(0, round(A*1000)/1000)
                vh.insert(0, round(h*1000)/1000)
                vH.insert(0, round(H*1000)/1000)
            except:
                mb.showerror("Неверные данные", "Расчёты невозможны")
                stroim = False
        elif (V0d and Ad and hd and Ld): # 22
            if (A > -pi/2) and (A < pi/2):
                try:
                    H = h + ((V0**2)*(sin(A)**2)) / (2*g)
                    T = (V0*sin(A) + sqrt(2*H*g)) / g 
                    Vdop = L/T - V0*cos(A)
                    vVdop.delete(0, END)
                    vH.delete(0, END)
                    vT.delete(0, END)
                    vVdop.insert(0, round(Vdop*1000)/1000)
                    vH.insert(0, round(H*1000)/1000)
                    vT.insert(0, round(T*1000)/1000)
                except:
                    mb.showerror("Неверные данные", "Расчёты невозможны")
                    stroim = False
            else:
                stroim = False
                mb.showerror("Неверные данные", "Расчёты невозможны")
        elif (V0d and Ad and Hd and Ld): # 23
            if (A > -pi/2) and (A < pi/2):
                try:
                    h = H - (V0**2*sin(A)**2) / (2*g)
                    T = (V0*sin(A) + sqrt(2*H*g)) / g
                    Vdop = L/T - V0*cos(A)
                    vL.delete(0, END)
                    vh.delete(0, END)
                    vVdop.delete(0, END)
                    vL.insert(0, round(L*1000)/1000)
                    vh.insert(0, round(h*1000)/1000)
                    vVdop.insert(0, round(Vdop*1000)/1000)
                except Exception as e:
                    mb.showerror("Неверные данные", "Расчёты невозможны")
                    stroim = False
            else:
                stroim = False
                mb.showerror("Неверные данные", "Расчёты невозможны")
        elif (V0d and Ad and Td and Ld): # 24
            if (A > -pi/2) and (A < pi/2):
                try:
                    H = (((T - (V0*sin(A))/g))**2*g) / 2 
                    h = H - (V0**2*sin(A)**2) / (2*g)
                    Vdop = L/T - V0*cos(A)
                    vVdop.delete(0, END)
                    vH.delete(0, END)
                    vh.delete(0, END)
                    vVdop.insert(0, round(Vdop*1000)/1000)
                    vH.insert(0, round(H*1000)/1000)
                    vh.insert(0, round(h*1000)/1000)
                except:
                    mb.showerror("Неверные данные", "Расчёты невозможны")
                    stroim = False
            else:
                stroim = False
                mb.showerror("Неверные данные", "Расчёты невозможны")
        elif (V0d and hd and Hd and Ld): # 25
            try:
                A = asin((sqrt((H - h) * 2 * g)) / V0)
                T = (V0*sin(A) + sqrt(2*H*g)) / g
                Vdop = L/T - V0*cos(A)
                vA.delete(0, END)
                vT.delete(0, END)
                vVdop.delete(0, END)
                vA.insert(0, round(A*1000)/1000)
                vT.insert(0, round(T*1000)/1000)
                vVdop.insert(0, round(Vdop*1000)/1000)
            except:
                mb.showerror("Неверные данные", "Расчёты невозможны")
                stroim = False
        elif (V0d and hd and Td and Ld): # 26
            try:
                A = asin((T**2*g - 2*h) / (2*T*V0))
                H = h + ((V0**2*sin(A)**2) / (2*g))
                Vdop = L/T - V0*cos(A)
                vA.delete(0, END)
                vH.delete(0, END)
                vVdop.delete(0, END)
                vA.insert(0, round(A*1000)/1000)
                vH.insert(0, round(H*1000)/1000)
                vVdop.insert(0, round(Vdop*1000)/1000)
            except:
                mb.showerror("Неверные данные", "Расчёты невозможны")
                stroim = False
        elif (V0d and Td and Hd and Ld): # 27
            try:
                A = asin(((T - sqrt((2 * H) / g)) * g) / V0) 
                h = H - (V0**2*sin(A)**2) / (2*g)
                Vdop = L/T - V0*cos(A)
                vA.delete(0, END)
                vH.delete(0, END)
                vVdop.delete(0, END)
                vA.insert(0, round(A*1000)/1000)
                vH.insert(0, round(H*1000)/1000)
                vVdop.insert(0, round(Vdop*1000)/1000)
            except Exception as e:
                print(e)
                mb.showerror("Неверные данные", "Расчёты невозможны")
                stroim = False
        elif (hd and Ad and Hd and Vdopd): # 28
            if (A > -pi/2) and (A < pi/2):
                try:
                    V0 = sqrt(2*g*(H-h)) / sin(A)
                    T = (V0*sin(A) + sqrt(2*H*g)) / g
                    L = (V0*cos(A) + Vdop) * T
                    vV0.delete(0, END)
                    vT.delete(0, END)
                    vL.delete(0, END)
                    vV0.insert(0, round(V0*1000)/1000)
                    vT.insert(0, round(T*1000)/1000)
                    vL.insert(0, round(L*1000)/1000)
                except:
                    mb.showerror("Неверные данные", "Расчёты невозможны")
                    stroim = False
            else:
                stroim = False
                mb.showerror("Неверные данные", "Расчёты невозможны")
        elif (Td and Ad and hd and Vdopd): # 29
            if (A > -pi/2) and (A < pi/2):
                try:
                    V0 = (T**2*g - 2*h) / (2*T*sin(A))
                    H = h + ((V0**2*sin(A)**2) / (2*g))
                    L = (V0*cos(A) + Vdop) * T
                    vV0.delete(0, END)
                    vH.delete(0, END)
                    vL.delete(0, END)
                    vV0.insert(0, round(V0*1000)/1000)
                    vH.insert(0, round(H*1000)/1000)
                    vL.insert(0, round(L*1000)/1000)
                except:
                    mb.showerror("Неверные данные", "Расчёты невозможны")
                    stroim = False
            else:
                stroim = False
                mb.showerror("Неверные данные", "Расчёты невозможны")
        elif (Ld and Ad and hd and Vdopd): # 30
            if (A > -pi/2) and (A < pi/2):
                try:
                    V0 = (-L*sin(A)*Vdop - 2*h*Vdop*cos(A) + sqrt((L*Vdop*sin(A) + 2*h*Vdop*cos(A))**2 - (L*sin(2*A) + 2*h*cos(A)**2)*(2*h*Vdop**2 - L**2*g))) / (L*sin(2*A) + 2*h*cos(A)**2)
                    H = h + ((V0**2*sin(A)**2) / (2*g))
                    T = (V0*sin(A) + sqrt(2*H*g)) / g
                    vV0.delete(0, END)
                    vH.delete(0, END)
                    vT.delete(0, END)
                    vV0.insert(0, round(V0*1000)/1000)
                    vH.insert(0, round(H*1000)/1000)
                    vT.insert(0, round(T*1000)/1000)
                except:
                    mb.showerror("Неверные данные", "Расчёты невозможны")
                    stroim = False
            else:
                stroim = False
                mb.showerror("Неверные данные", "Расчёты невозможны")
        elif (Td and Ad and Hd and Vdopd): # 31
            if (A > -pi/2) and (A < pi/2):
                try:
                    V0 = (T*g + sqrt(2*H*g)) / sin(A)
                    h = H - (V0**2*sin(A)**2) / (2*g)
                    L = (V0*cos(A) + Vdop)*T
                    vV0.delete(0, END)
                    vh.delete(0, END)
                    vL.delete(0, END)
                    vV0.insert(0, round(V0*1000)/1000)
                    vh.insert(0, round(h*1000)/1000)
                    vL.insert(0, round(L*1000)/1000)
                except:
                    mb.showerror("Неверные данные", "Расчёты невозможны")
                    stroim = False
            else:
                stroim = False
                mb.showerror("Неверные данные", "Расчёты невозможны")
        elif (Ld and Ad and Hd and Vdopd): # 32
            if (A > -pi/2) and (A < pi/2):
                try:
                    V0 = (-Vdop*sin(A) - sqrt(2*H/g)*g*cos(A) + sqrt((Vdop*sin(A) + sqrt(2*H/g)*g*cos(A))**2 - 2*sin(2*A)*(4*sqrt(2*H/g)*g - L*g))) / sin(2*A)
                    h = H - ((V0**2*sin(A)**2) / (2*g))
                    T = (V0*sin(A) + sqrt(2*H*g)) / g
                    vV0.delete(0, END)
                    vh.delete(0, END)
                    vT.delete(0, END)
                    vV0.insert(0, round(V0*1000)/1000)
                    vh.insert(0, round(h*1000)/1000)
                    vT.insert(0, round(T*1000)/1000)
                except:
                    mb.showerror("Неверные данные", "Расчёты невозможны")
                    stroim = False
            else:
                stroim = False
                mb.showerror("Неверные данные", "Расчёты невозможны")
        elif (Ld and Ad and Td and Vdopd): # 33
            if (A > -pi/2) and (A < pi/2):
                try:
                    V0 = (L/T - Vdop) / cos(A)
                    H = (g*((T - (V0*sin(A))/g))**2) / 2 
                    h = H - (V0**2*sin(A)**2) / (2*g)
                    vV0.delete(0, END)
                    vH.delete(0, END)
                    vh.delete(0, END)
                    vV0.insert(0, round(V0*1000)/1000)
                    vH.insert(0, round(H*1000)/1000)
                    vh.insert(0, round(h*1000)/1000)
                except:
                    mb.showerror("Неверные данные", "Расчёты невозможны")
                    stroim = False
            else:
                stroim = False
                mb.showerror("Неверные данные", "Расчёты невозможны")
        elif (Ld and hd and Hd and Vdopd): # 34
            try:
                A = acos((g*L - sqrt(2*H*g)*Vdop)/(2*g*sqrt(H*(H-h))))
                V0 = sqrt(2*g*(H-h)) / sin(A)
                T = (V0*sin(A) + sqrt(2*H*g)) / g
                vA.delete(0, END)
                vV0.delete(0, END)
                vT.delete(0, END)
                vA.insert(0, round(A*1000)/1000)
                vV0.insert(0, round(V0*1000)/1000)
                vT.insert(0, round(T*1000)/1000)
            except Exception as e:
                print(e)
                mb.showerror("Неверные данные", "Расчёты невозможны")
                stroim = False
        elif (Vdopd and hd and Td and Ld): # 35
            try:
                A = atan((g*T**2 - 2*h)/(2*(L - Vdop*T)))
                V0 = (L/T -Vdop) / cos(A)
                H = h + (V0**2 * sin(A)**2)
                vA.delete(0, END)
                vV0.delete(0, END)
                vH.delete(0, END)
                vA.insert(0, round(A*1000)/1000)
                vV0.insert(0, round(V0*1000)/1000)
                vH.insert(0, round(H*1000)/1000)
            except:
                mb.showerror("Неверные данные", "Расчёты невозможны")
                stroim = False
        else:
            vV0.delete(0, END)
            vA.delete(0, END)
            vT.delete(0, END)
            vL.delete(0, END)
            vh.delete(0, END)
            vH.delete(0, END)
            mb.showerror("Неверные данные", "Расчёты невозможны")
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
            t1 = V0*sin(A)/g
            grafic.create_line(10 + t1*k * (V0*cos(A) + Vdop), 10, 10 + t1*k * (V0*cos(A) + Vdop), 215, dash=True)
            global i
            global telo
            global xy
            xy = Label(text="x=0.000 , y=0.000", font="Cricket 12")
            xy.config(bd=20, bg=label_bg_color, fg=label_text_color)
            xy.place(x=graph_x+120, y=graph_y+250)
            XY.append(xy)
            telo = grafic.create_oval(10 - r, 210-h*k - r, 10 + r, 210-h*k + r, fill="#c00300")
            i=0
            global telo1
            telo1 = grafic.create_line(10-8, 210 - h * k, 10 + 8, 210 - h * k, arrow=LAST)
            root.after(10, draw_angle_by_h_wind)
    else:
        vV0.delete(0, END)
        vA.delete(0, END)
        vT.delete(0, END)
        vL.delete(0, END)
        vh.delete(0, END)
        vH.delete(0, END)
        vVdop.delete(0, END)
        mb.showerror("Неверные данные", "Расчёты невозможны")
        stroim = False

def del_by_angle_h_wind():
    vA.delete(0, END)
    vh.delete(0, END)
    vH.delete(0, END)
    vV0.delete(0, END)
    vT.delete(0, END)
    vL.delete(0, END)
    vVdop.delete(0, END)
    global stroim, XY
    stroim = False
    for a in XY:
        a.destroy()
    grafic.delete("all")

def draw_angle_by_h_wind():
    global i
    global telo, telo1
    global xy, XY
    if (stroim):
        grafic.delete(telo)
        grafic.delete(telo1)
        xy.destroy()
        XY=[]
        x = L / 2000 * i
        t = x/(V0*cos(A) + Vdop)
        y = h + V0*sin(A)*t - g*t**2/2
        x1 = L / 2000 * (i + 1)
        t1 = x1 / (V0 * cos(A) + Vdop)
        y1 = h + V0 * sin(A) * t1 - g * t1 ** 2 / 2
        telo = grafic.create_oval(((x1) * k + 10) - r, 220 - ((y1) * k + 10) - r, ((x1) * k + 10) + r, 220 - ((y1) * k + 10) + r, fill="#c00300")
        telo1 = grafic.create_line(10 - 8 + t1*(Vdop), 210 - h * k, 10 + 8 + t1*(Vdop), 210 - h * k, arrow=LAST)
        grafic.create_line((x) * k + 10, 220 - ((y) * k + 10), ((x1) * k + 10), 220 - ((y1) * k + 10), fill="#c00300")
        i+=1
        xy = Label(text="x="+str(col_znak(round(x*1000)/1000, 3))+", y="+str(col_znak(round(y*1000)/1000, 3)), font="Cricket 12")
        xy.config(bd=20, bg=label_bg_color, fg=label_text_color)
        xy.place(x=graph_x+120, y=graph_y+250)
        XY.append(xy)
        global vvod
        vvod.append(xy)
        if (i<=2000):
            root.after(1, draw_angle_by_h_wind)

def file_by_angle_h_wind():
    colvo = 0
    n = 0
    f_name = fd.askopenfilename()
    with open(f_name, "r") as file:
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
                fVdop = st
                if (is_num(fVdop)):
                    n+=1
            st = file.readline()
    if (colvo==4) and (n==4):
        vh.delete(0, END)
        vL.delete(0, END)
        vH.delete(0, END)
        vT.delete(0, END)
        vV0.delete(0, END)
        vVdop.delete(0, END)
        vA.delete(0, END)
        if (is_num(fh)):
            vh.insert(0, str(fh))
        if (is_num(fV0)):
            vV0.insert(0, str(fV0))
        if (is_num(fA)):
            vA.insert(0, str(fA))
        if (is_num(fVdop)):
            vVdop.insert(0, str(fVdop))
        vvod_by_angle_h_wind()
    else:
        mb.showerror("Ошибка", "Неверный формат входных данных")

def save_by_angle_h_wind():
    vvod_by_angle_zero(False)
    global stroim, XY
    stroim = False
    for a in XY:
        a.destroy()
    grafic.delete("all")
    if (is_num(vV0.get()) and is_num(vA.get())):
        f_name = fd.asksaveasfilename(filetypes=(("TXT files", "*.txt"),))
        with open(f_name, "w") as file:
            st = 'Бросок под углом к горизонту с движущейся платформы \n'
            file.write(st)
            st = "h (м) = " + str(vh.get()) + '\n'
            file.write(st)
            st = "Vo (м/с) = " + str(vV0.get()) + '\n'
            file.write(st)
            st = "Vплатформы (м/с) = " + str(vVdop.get()) + '\n'
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

def by_angle_h_wind():
    global vvod
    vvod = []
    grafic.place(x=graph_x, y=graph_y)

    l1 = Label(text="Введите любые четыре значения", font="Cricket 16")
    l1.config(bd=20, bg=label_bg_color, fg=label_text_color)
    l1.place(x=7, y=70)
    vvod.append(l1)

    l2 = Label(text="Бросок под углом к горизонту с высоты с учетом ветра", font="Cricket 23")
    l2.config(bd=20, bg=label_bg_color, fg=label_text_color)
    l2.place(x=7, y=10)
    vvod.append(l2)

    delete_main()

    global vh
    vh = Entry(width=13)
    vh.place(x=172, y=128)
    vvod.append(vh)

    bh = Label(text="h (м)        =", font="Cricket 10")
    bh.place(x=84, y=128)
    bh.config(bg=label_bg_color, fg=label_text_color)
    vvod.append(bh)

    global vV0
    vV0= Entry(width=13)
    vV0.place(x=172, y=152)
    vvod.append(vV0)

    bV0 = Label(text="Vo (м/с)     =", font="Cricket 10")
    bV0.place(x=76, y=152)
    bV0.config(bg=label_bg_color, fg=label_text_color)
    vvod.append(bV0)

    global vA
    vA= Entry(width=13)
    vA.place(x=172, y=176)
    vvod.append(vA)

    bA = Label(text="Угол (В градусах)      = ", font="Cricket 10")
    bA.place(x=13, y=176)
    bA.config(bg=label_bg_color, fg=label_text_color)
    vvod.append(bA)

    global vVdop
    vVdop = Entry(width=13)
    vVdop.place(x=172, y=199)
    vvod.append(vVdop)

    bVdop = Label(text="Vdop (м/с)       = ", font="Cricket 10")
    bVdop.place(x=54 , y=199)
    bVdop.config(bg=label_bg_color, fg=label_text_color)
    vvod.append(bVdop)

    global vH
    vH = Entry(width=13)
    vH.place(x=172, y=224)
    vvod.append(vH)

    bH = Label(text="Hmax (м)    = ", font="Cricket 10")
    bH.place(x=73, y=224)
    bH.config(bg=label_bg_color, fg=label_text_color)
    vvod.append(bH)

    global vT
    vT = Entry(width=13)
    vT.place(x=172, y=248)
    vvod.append(vT)

    bT = Label(text="Tполёта (с)  = ", font="Cricket 10")
    bT.place(x=70, y=248)
    bT.config(bg=label_bg_color, fg=label_text_color)
    vvod.append(bT)

    global vL
    vL = Entry(width=13)
    vL.place(x=172, y=271)
    vvod.append(vL)

    bL = Label(text="Lполёта (м)  = ", font="Cricket 10")
    bL.place(x=68, y=271)
    bL.config(bg=label_bg_color, fg=label_text_color)
    vvod.append(bL)

    bvvesti = Button(root, height=2, width=17)
    change_button(bvvesti, "Ввести значения")
    bvvesti.place(x=20, y=303)
    vvod.append(bvvesti)
    bvvesti.config(command=vvod_by_angle_h_wind)

    bdel = Button(root, height=2, width=10)
    change_button(bdel, "Удалить\nзначения")
    bdel.place(x=163, y=303)
    vvod.append(bdel)
    bdel.config(command=del_by_angle_h_wind)

    bopen = Button(root, height=5, width=30, font=('Cricket', 10))
    change_button(bopen, 'Считать значения из файла \n(введите 4 значения\n в следующем порядке: h, V0, A, \nVплатформы в файл "input.txt"\n в столбик)' )
    bopen.place(x=30, y=420)
    vvod.append(bopen)
    bopen.config(command=file_by_angle_h_wind)

    bsave = Button(root, height=5, width=30, font=('Cricket', 10))
    change_button(bsave,'Сохранить значения\n в файл')
    bsave.place(x=350, y=420)
    vvod.append(bsave)
    bsave.config(command=save_by_angle_h_wind)

    l3 = Label(text="ИЛИ", font="Cricket 12", height=1)
    l3.config(bd=12, bg=label_bg_color, fg=label_text_color)
    l3.place(x=90, y=360)
    vvod.append(l3)


# Под углом к горизонту с земли к наклонной плоскости

def vvod_dop(x=True):
    grafic.delete("all")
    global XY
    for a in XY:
        a.destroy()
    global V0, h, A, B, T, L
    V0 = vV0.get()
    h = vh.get()
    A = vA.get()
    B = vB.get()
    col=0
    V0d = False
    hd = False
    Td = False
    Vkd = False
    global stroim
    flag = True
    stroim = x
    if (is_num(V0)):
        col += 1
        V0d = True
        V0 = float(V0)
        if (V0 < 0):
            flag = False
    if (is_num(h)):
        col += 1
        hd = True
        h = float(h)
        if (h < 0):
            flag = False
    if (is_num(A)):
        col += 1
        Ad = True
        A = float(A)
        if (A<=-90)or(A>=90):
            flag = False
        A = A * pi / 180
    if (is_num(B)):
        col += 1
        Bd = True
        B = float(B)
        if (B <= 0)or(B>=90):
            flag = False
        B = B * pi / 180
    if (flag):
        if (V0d and hd and Ad and Bd):
            D = (tan(A)-tan(B))**2 + 2*g*h/(V0**2*cos(A)**2)
            L = ((tan(A)-tan(B) + sqrt(D)))/(g/(V0**2 * cos(A)**2))
            T = L/(V0*cos(A))
            vLx.delete(0, END)
            vLpl.delete(0, END)
            vT.delete(0, END)
            vLx.insert(0, round(L * 1000) / 1000)
            vT.insert(0, round(T * 1000) / 1000)
            vLpl.insert(0, round(L/cos(B) * 1000) / 1000)

            
        else:
            vV0.delete(0, END)
            vh.delete(0, END)
            vT.delete(0, END)
            vVk.delete(0, END)
            mb.showerror("Неверные данные", "Расчёты невозможны")
            stroim = False

        if (stroim):
            global k
            k = min(190 / (h + V0**2*sin(A)**2/(2*g)), 380/L)
            H=h
            grafic.create_line(10, 10, 10, 210, arrow=FIRST)
            grafic.create_line(10, 210, 395, 210, arrow=LAST)
            grafic.create_text(15, 6, text="y(м)")
            grafic.create_text(385, 200, text="x(м)")
            grafic.create_line(10, 210-h*k, 10 , 210 - 30-h*k, arrow=LAST)
            grafic.create_text(19, 210 - 30 - h*k, text="Vo")
            grafic.create_line(390, 10, 390, 40, arrow=LAST)
            grafic.create_polygon([10, 210], [370, 210-370*tan(B)], [370, 210], fill='#048B22', outline='#044412')
            grafic.create_text(376, 33, text="g")
            grafic.create_text(24, 210-h*k, text=str(round(h*1000)/1000))
            grafic.create_text(10, 220, text="0")
            grafic.create_text(17 + len(str(round(H * 100) / 100)) * 5, 200 - (H * k), text=str(round(H * 100) / 100))
            grafic.create_line(5, 210 - (h * k), 390, 210 - (h * k), dash=True)
            global i
            global telo
            telo = grafic.create_oval(10 - r, 210-h*k - r, 10 + r, 210-h*k + r, fill="#c00300")
            i = 0
            global xy
            xy = Label(text="x=0.000 , y="+str(h), font="Cricket 12")
            xy.config(bd=20, bg=label_bg_color, fg=label_text_color)
            xy.place(x=graph_x+120, y=graph_y+250)
            XY.append(xy)
            root.after(1, draw_angle_by_h)
    else:
        vV0.delete(0, END)
        vh.delete(0, END)
        vT.delete(0, END)
        vVk.delete(0, END)
        mb.showerror("Неверные данные", "Расчёты невозможны")
        stroim = False

def del_dop():
    vh.delete(0, END)
    vT.delete(0, END)
    vV0.delete(0, END)
    vA.delete(0, END)
    vB.delete(0, END)
    vLx.delete(0, END)
    vLpl.delete(0, END)
    global stroim, XY
    stroim = False
    for a in XY:
        a.destroy()
    grafic.delete("all")

def file_dop():
    colvo = 0
    n = 0
    f_name = fd.askopenfilename()
    with open(f_name, "r") as file:
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
                fB = st
                if (is_num(fB)):
                    n+=1
            st = file.readline()
    if (colvo==4) and (n==4):
        vh.delete(0, END)
        vB.delete(0, END)
        vV0.delete(0, END)
        vA.delete(0, END)
        if (is_num(fh)):
            vh.insert(0, str(fh))
        if (is_num(fV0)):
            vV0.insert(0, str(fV0))
        if (is_num(fA)):
            vA.insert(0, str(fA))
        if (is_num(fB)):
            vB.insert(0, str(fB))
        vvod_dop()
    else:
        mb.showerror("Ошибка", "Неверный формат входных данных")

def save_dop():
    vvod_dop(False)
    global stroim, XY
    stroim = False
    for a in XY:
        a.destroy()
    grafic.delete("all")
    if (is_num(vV0.get()) and is_num(vA.get())):
        f_name = fd.asksaveasfilename(filetypes=(("TXT files", "*.txt"),))
        with open(f_name, "w") as file:
            st = 'Бросок под углом А к горизонту с высоты h на плоскость под углом B \n'
            file.write(st)
            st = "h (м) = " + str(vh.get()) + '\n'
            file.write(st)
            st = "Vo (м/с) = " + str(vV0.get()) + '\n'
            file.write(st)
            st = "A (градусов) = " + str(vA.get()) + '\n'
            file.write(st)
            st = "B (градусов) = " + str(vB.get()) + '\n'
            file.write(st)
            st = "T (с) = " + str(vT.get()) + '\n'
            file.write(st)
            st = "L по оси ох (м) = " + str(vLx.get()) + '\n'
            file.write(st)
            st = "L по плоскости (м) = " + str(vLpl.get()) + '\n'
            file.write(st)
            mb.showinfo(
                "Успешно",
                "Данные сохранены")

def dop():
    global vvod
    vvod = []
    grafic.place(x=graph_x, y=graph_y)

    l1 = Label(text="Введите значения A, B, Vo, h", font="Cricket 14")
    l1.config(bd=20, bg=label_bg_color, fg=label_text_color)
    l1.place(x=20, y=55)
    vvod.append(l1)

    l2 = Label(text="Бросок под углом А к горизонту с высоты на наклонную плоскость под углом B (0°; 90°)", font="Cricket 14")
    l2.config(bd=20, bg=label_bg_color, fg=label_text_color)
    l2.place(x=20, y=10)
    vvod.append(l2)

    delete_main()

    global vh
    vh = Entry(width=13)
    vh.place(x=163, y=116)
    vvod.append(vh)

    bh = Label(text="h (м)    =", font="Cricket 10")
    bh.place(x=82, y=116)
    bh.config(bg=label_bg_color, fg=label_text_color)
    vvod.append(bh)

    global vV0
    vV0= Entry(width=13)
    vV0.place(x=163, y=138)
    vvod.append(vV0)

    bV0 = Label(text="Vo (м/c)  =", font="Cricket 10")
    bV0.place(x=70, y=138)
    bV0.config(bg=label_bg_color, fg=label_text_color)
    vvod.append(bV0)

    global vA
    vA= Entry(width=13)
    vA.place(x=163, y=160)
    vvod.append(vA)

    bA = Label(text="A (В градусах)  = ", font="Cricket 10")
    bA.place(x=29, y=160)
    bA.config(bg=label_bg_color, fg=label_text_color)
    vvod.append(bA)

    global vB
    vB = Entry(width=13)
    vB.place(x=163, y=182)
    vvod.append(vB)

    bB = Label(text="B (В градусах)  = ", font="Cricket 10")
    bB.place(x=29, y=182)
    bB.config(bg=label_bg_color, fg=label_text_color)
    vvod.append(bB)

    global vT
    vT = Entry(width=13)
    vT.place(x=163, y=204)
    vvod.append(vT)

    bT = Label(text="T (c)  = ", font="Cricket 10")
    bT.place(x=92, y=204)
    bT.config(bg=label_bg_color, fg=label_text_color)
    vvod.append(bT)

    global vLx
    vLx = Entry(width=13)
    vLx.place(x=163, y=226)
    vvod.append(vLx)

    bLx = Label(text="Lx (м)  = ", font="Cricket 10")
    bLx.place(x=83, y=226)
    bLx.config(bg=label_bg_color, fg=label_text_color)
    vvod.append(bLx)

    global vLpl
    vLpl = Entry(width=13)
    vLpl.place(x=163, y=248)
    vvod.append(vLpl)

    bLpl = Label(text="Lна плоскости (м)  = ", font="Cricket 10")
    bLpl.place(x=12, y=248)
    bLpl.config(bg=label_bg_color, fg=label_text_color)
    vvod.append(bLpl)

    bvvesti = Button(root, height=2, width=17)
    change_button(bvvesti, "Ввести значения")
    bvvesti.place(x=20, y=300)
    vvod.append(bvvesti)
    bvvesti.config(command=vvod_dop)

    bdel = Button(root, height=2, width=10)
    change_button(bdel, "Удалить\nзначения")
    bdel.place(x=163, y=300)
    vvod.append(bdel)
    bdel.config(command=del_dop)

    bopen = Button(root, height=5, width=30, font=('Cricket', 10))
    change_button(bopen, 'Считать значения из файла \n(введите 4 значения \n в следующем порядке: h, V0, A, B \n в файл "input.txt" в столбик)' )
    bopen.place(x=30, y=425)
    vvod.append(bopen)
    bopen.config(command=file_dop)

    bsave = Button(root, height=5, width=30, font=('Cricket', 10))
    change_button(bsave, 'Сохранить значения\n в файл')
    bsave.place(x=350, y=425)
    vvod.append(bsave)
    bsave.config(command=save_dop)

    l3 = Label(text="ИЛИ", font="Cricket 12")
    l3.config(bd=20, bg=label_bg_color, fg=label_text_color)
    l3.place(x=90, y=350)
    vvod.append(l3)


# теория
def delete_th():
        c.delete("all")
        for a in vvod:
            a.destroy()

def th_by_angle_zero():
    delete_th()
    global BB
    l0 = Label(text="Бросок тела под углом к горизонту с земли", font="Cricket 18")
    l0.place(x=75, y=10)
    l0.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l0)
    l1 = Label(text="Vy(t) = Vo*sinA - gt - скорость по оси оу через t секунд полёта", font="Cricket 14")
    l1.place(x=10, y=80)
    l1.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l1)
    l2 = Label(text="Vx(t) = Vo*cosA - скорость по оси ох через t секунд полёта", font="Cricket 14")
    l2.place(x=10, y=130)
    l2.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l2)
    l3 = Label(text="y(t) = Vo*sinA*t - g*t^2/2 - координата по оси оу через t секунд полёта", font="Cricket 14")
    l3.place(x=10, y=180)
    l3.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l3)
    l4 = Label(text="x(t) = xo + Vo*cosA*t - координата по оси ох через t секунд полёта", font="Cricket 14")
    l4.place(x=10, y=230)
    l4.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l4)
    l5 = Label(text="Hmax = Vo^2*(sinA)^2/(2*g) - максимальная высота полёта", font="Cricket 14")
    l5.place(x=10, y=280)
    l5.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l5)
    l6 = Label(text="Lmax = Vo^2*sin(2A)/g - дальность полёта", font="Cricket 14")
    l6.place(x=10, y=320)
    l6.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l6)
    l7 = Label(text="Tполёта = 2*Vo*sinA/g - время полёта", font="Cricket 14")
    l7.place(x=10, y=370)
    l7.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l7)
    l8 = Label(text="Траектория движения тела, брошенного под углом к горизонту - парабола", font="Cricket 14")
    l8.place(x=10, y=420)
    l8.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l8)

def th_vert_v_zero():
    delete_th()
    global BB
    l0 = Label(text="Бросок тела вертикально вверх с земли", font="Cricket 18")
    l0.place(x=75, y=10)
    l0.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l0)
    l1 = Label(text="Vy(t) = Vo - gt - скорость по оси оу через t секунд полёта", font="Cricket 14")
    l1.place(x=10, y=80)
    l1.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l1)
    l2 = Label(text="Vx(t) = 0 - скорость по оси ох через t секунд полёта", font="Cricket 14")
    l2.place(x=10, y=130)
    l2.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l2)
    l3 = Label(text="y(t) = Vo*t - g*t^2/2 - координата по оси оу через t секунд полёта", font="Cricket 14")
    l3.place(x=10, y=180)
    l3.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l3)
    l4 = Label(text="x(t) = xo - координата по оси ох через t секунд полёта", font="Cricket 14")
    l4.place(x=10, y=230)
    l4.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l4)
    l5 = Label(text="Hmax = Vo^2*/(2*g) - максимальная высота полёта", font="Cricket 14")
    l5.place(x=10, y=275)
    l5.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l5)
    l6 = Label(text="Lmax = 0 - дальность полёта", font="Cricket 14")
    l6.place(x=10, y=320)
    l6.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l6)
    l7 = Label(text="Tполёта = 2*Vo/g - время полёта", font="Cricket 14")
    l7.place(x=10, y=370)
    l7.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l7)
    l8 = Label(text="Траектория движения тела, брошенного вертикально вверх - прямая линия", font="Cricket 14")
    l8.place(x=10, y=420)
    l8.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l8)

def th_hor():
    delete_th()
    global BB
    l0 = Label(text="Бросок тела горизонтально с высоты h", font="Cricket 18")
    l0.place(x=75, y=10)
    l0.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l0)
    l1 = Label(text="Vy(t) = - gt - скорость по оси оу через t секунд полёта", font="Cricket 14")
    l1.place(x=10, y=80)
    l1.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l1)
    l2 = Label(text="Vx(t) = Vo - скорость по оси ох через t секунд полёта", font="Cricket 14")
    l2.place(x=10, y=130)
    l2.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l2)
    l3 = Label(text="y(t) = h - g*t^2/2 - координата по оси оу через t секунд полёта", font="Cricket 14")
    l3.place(x=10, y=180)
    l3.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l3)
    l4 = Label(text="x(t) = xo + Vo*t - координата по оси ох через t секунд полёта", font="Cricket 14")
    l4.place(x=10, y=230)
    l4.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l4)
    l5 = Label(text="Hmax = h - максимальная высота полёта", font="Cricket 14")
    l5.place(x=10, y=280)
    l5.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l5)
    l6 = Label(text="Lmax = Vo*sqrt(2h/g) - дальность полёта", font="Cricket 14")
    l6.place(x=10, y=320)
    l6.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l6)
    l7 = Label(text="Tполёта = sqrt(2h/g) - время полёта", font="Cricket 14")
    l7.place(x=10, y=370)
    l7.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l7)
    l8 = Label(text="Траектория движения тела, брошенного горизонтально с высоты \nh - парабола", font="Cricket 14")
    l8.place(x=10, y=420)
    l8.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l8)

def th_angle_h():
    delete_th()
    global BB
    l0 = Label(text="Бросок тела под углом к горизонту с высоты h", font="Cricket 18")
    l0.place(x=75, y=10)
    l0.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l0)
    l1 = Label(text="Vy(t) = Vo*sinA - gt - скорость по оси оу через t секунд полёта", font="Cricket 14")
    l1.place(x=10, y=80)
    l1.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l1)
    l2 = Label(text="Vx(t) = Vo*cosA - скорость по оси ох через t секунд полёта", font="Cricket 14")
    l2.place(x=10, y=130)
    l2.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l2)
    l3 = Label(text="y(t) = h + Vo*sinA*t - g*t^2/2 - координата по оси оу через t секунд полёта", font="Cricket 14")
    l3.place(x=10, y=180)
    l3.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l3)
    l4 = Label(text="x(t) = xo + Vo*cosA*t - координата по оси ох через t секунд полёта", font="Cricket 14")
    l4.place(x=10, y=230)
    l4.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l4)
    l5 = Label(text="Hmax = (V0^2 * (sin(A))^2 + 2 * g * h) / (2 * g) - максимальная высота полёта", font="Cricket 14")
    l5.place(x=10, y=280)
    l5.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l5)
    l6 = Label(text="Lmax = (V0^2*sin(A)*cos(A)+V0*cos(A)*sqrt(V0^2*(sin(A))^2+2*g*h))/g - дальность полёта", font="Cricket 14")
    l6.place(x=10, y=320)
    l6.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l6)
    l7 = Label(text="Tполёта = (V0 * sin(A) + sqrt(V0^2 * (sin(A))^2 + 2 * g * h)) / g - время полёта", font="Cricket 14")
    l7.place(x=10, y=370)
    l7.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l7)
    l8 = Label(text="Траектория движения тела, брошенного под углом к горизонту с высоты - \nпарабола", font="Cricket 14")
    l8.place(x=10, y=420)
    l8.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l8)

def th_vert_vniz():
    delete_th()
    global BB
    l0 = Label(text="Бросок тела вертикально вниз с высоты h", font="Cricket 18")
    l0.place(x=75, y=10)
    l0.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l0)
    l1 = Label(text="Vy(t) = -Vo - gt - скорость по оси оу через t секунд полёта", font="Cricket 14")
    l1.place(x=10, y=80)
    l1.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l1)
    l2 = Label(text="Vx(t) = 0 - скорость по оси ох через t секунд полёта", font="Cricket 14")
    l2.place(x=10, y=130)
    l2.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l2)
    l3 = Label(text="y(t) = h - Vo*t - g*t^2/2 - координата по оси оу через t секунд полёта", font="Cricket 14")
    l3.place(x=10, y=180)
    l3.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l3)
    l4 = Label(text="x(t) = xo - координата по оси ох через t секунд полёта", font="Cricket 14")
    l4.place(x=10, y=230)
    l4.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l4)
    l5 = Label(text="Hmax = h - максимальная высота полёта", font="Cricket 14")
    l5.place(x=10, y=275)
    l5.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l5)
    l6 = Label(text="Lmax = 0 - дальность полёта", font="Cricket 14")
    l6.place(x=10, y=320)
    l6.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l6)
    l7 = Label(text="Tполёта = (-V0+sqrt(V0^2+2*g*h))/g - время полёта", font="Cricket 14")
    l7.place(x=10, y=370)
    l7.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l7)
    l8 = Label(text="Траектория движения тела, брошенного вертикально вниз с высоты \nh - прямая линия", font="Cricket 14")
    l8.place(x=10, y=420)
    l8.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l8)

def th_vert_vverh():
    delete_th()
    global BB
    l0 = Label(text="Бросок тела вертикально вверх с высоты h", font="Cricket 18")
    l0.place(x=75, y=10)
    l0.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l0)
    l1 = Label(text="Vy(t) = Vo - gt - скорость по оси оу через t секунд полёта", font="Cricket 14")
    l1.place(x=10, y=80)
    l1.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l1)
    l2 = Label(text="Vx(t) = 0 - скорость по оси ох через t секунд полёта", font="Cricket 14")
    l2.place(x=10, y=130)
    l2.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l2)
    l3 = Label(text="y(t) = h + Vo*t - g*t^2/2 - координата по оси оу через t секунд полёта", font="Cricket 14")
    l3.place(x=10, y=180)
    l3.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l3)
    l4 = Label(text="x(t) = xo - координата по оси ох через t секунд полёта", font="Cricket 14")
    l4.place(x=10, y=230)
    l4.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l4)
    l5 = Label(text="Hmax = h + V0^2/(2*g) - максимальная высота полёта", font="Cricket 14")
    l5.place(x=10, y=275)
    l5.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l5)
    l6 = Label(text="Lmax = 0 - дальность полёта", font="Cricket 14")
    l6.place(x=10, y=320)
    l6.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l6)
    l7 = Label(text="Tполёта = (V0+sqrt(V0^2+2*g*h))/g - время полёта", font="Cricket 14")
    l7.place(x=10, y=370)
    l7.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l7)
    l8 = Label(text="Траектория движения тела, брошенного вертикально вверх с высоты \nh - прямая линия", font="Cricket 14")
    l8.place(x=10, y=420)
    l8.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l8)

def th_dop():
    delete_th()
    global BB
    l0 = Label(text="Бросок тела под углом к горизонту с высоты h а наклонную плоскость\n под углом B", font="Cricket 15")
    l0.place(x=5, y=10)
    l0.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l0)
    l1 = Label(text="Vy(t) = Vo*sinA - gt - скорость по оси оу через t секунд полёта", font="Cricket 14")
    l1.place(x=10, y=80)
    l1.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l1)
    l2 = Label(text="Vx(t) = Vo*cosA - скорость по оси ох через t секунд полёта", font="Cricket 14")
    l2.place(x=10, y=130)
    l2.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l2)
    l3 = Label(text="y(t) = h + Vo*sinA*t - g*t^2/2 - координата по оси оу через t секунд полёта", font="Cricket 14")
    l3.place(x=10, y=180)
    l3.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l3)
    l4 = Label(text="x(t) = xo + Vo*cosA*t - координата по оси ох через t секунд полёта", font="Cricket 14")
    l4.place(x=10, y=230)
    l4.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l4)
    l6 = Label(text="Lx = ((tan(A)-tan(B)+sqrt(D)))/(g/(V0^2*cos(A)^2)) - дальность полёта по оси ох",
               font="Cricket 14")
    l6.place(x=10, y=320)
    l6.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l6)
    l7 = Label(text="Tполёта = L/(V0*cos(A)) - время полёта",
               font="Cricket 14")
    l7.place(x=10, y=270)
    l7.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l7)
    l5 = Label(text="Lпл. = (((tan(A)-tan(B)+sqrt(D)))/(g/(V0^2*cos(A)^2)))/cos(A) - дальность полёта по плоскости",
               font="Cricket 14")
    l5.place(x=10, y=370)
    l5.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l5)
    l8 = Label(text="Траектория движения тела, брошенного под углом к горизонту с высоты - \nпарабола",
               font="Cricket 14")
    l8.place(x=10, y=420)
    l8.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l8)

def th_angle_h_wind():
    delete_th()
    global BB
    l0 = Label(text="Бросок тела под углом к горизонту с высоты h с учетом ветра", font="Cricket 18")
    l0.place(x=10, y=10)
    l0.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l0)
    l1 = Label(text="Vy(t) = Vo*sinA - gt - скорость по оси оу через t секунд полёта", font="Cricket 14")
    l1.place(x=10, y=80)
    l1.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l1)
    l2 = Label(text="Vx(t) = Vo*cosA + Vdop - скорость по оси ох через t секунд полёта", font="Cricket 14")
    l2.place(x=10, y=130)
    l2.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l2)
    l3 = Label(text="y(t) = h + Vo*sinA*t - g*t^2/2 - координата по оси оу через t секунд полёта", font="Cricket 14")
    l3.place(x=10, y=180)
    l3.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l3)
    l4 = Label(text="x(t) = xo + (Vo*cosA+Vdop)*t - координата по оси ох через t секунд полёта", font="Cricket 14")
    l4.place(x=10, y=230)
    l4.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l4)
    l5 = Label(text="Hmax = (V0^2 * (sin(A))^2 + 2 * g * h) / (2 * g) - максимальная высота полёта", font="Cricket 14")
    l5.place(x=10, y=280)
    l5.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l5)
    l6 = Label(text="Lmax = (V0*sin(A)+sqrt(V0^2*(sin(A))^2+2*g*h))/g * (Vo*cosA+Vdop) - дальность полёта", font="Cricket 14")
    l6.place(x=10, y=320)
    l6.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l6)
    l7 = Label(text="Tполёта = (V0 * sin(A) + sqrt(V0^2 * (sin(A))^2 + 2 * g * h)) / g - время полёта", font="Cricket 14")
    l7.place(x=10, y=370)
    l7.config(bd=14, bg=label_bg_color, fg=label_text_color)
    BB.append(l7)
    l8 = Label(text="Траектория движения тела, брошенного под углом к горизонту с \n высоты с учемом ветра - парабола", font="Cricket 14")
    l8.place(x=10, y=410)
    l8.config(bd=14, bg=label_bg_color, fg=label_text_color)
    BB.append(l8)

def th_angle_h_move():
    delete_th()
    global BB
    l0 = Label(text="Бросок тела под углом к горизонту с движущейся платформы на высоте h", font="Cricket 16")
    l0.place(x=10, y=10)
    l0.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l0)
    l1 = Label(text="Vy(t) = Vo*sinA - gt - скорость по оси оу через t секунд полёта", font="Cricket 14")
    l1.place(x=10, y=80)
    l1.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l1)
    l2 = Label(text="Vx(t) = Vo*cosA + Vdop - скорость по оси ох через t секунд полёта", font="Cricket 14")
    l2.place(x=10, y=130)
    l2.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l2)
    l3 = Label(text="y(t) = h + Vo*sinA*t - g*t^2/2 - координата по оси оу через t секунд полёта", font="Cricket 14")
    l3.place(x=10, y=180)
    l3.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l3)
    l4 = Label(text="x(t) = xo + (Vo*cosA+Vdop)*t - координата по оси ох через t секунд полёта", font="Cricket 14")
    l4.place(x=10, y=230)
    l4.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l4)
    l5 = Label(text="Hmax = (V0^2 * (sin(A))^2 + 2 * g * h) / (2 * g) - максимальная высота полёта", font="Cricket 14")
    l5.place(x=10, y=280)
    l5.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l5)
    l6 = Label(text="Lmax = (V0*sin(A)+sqrt(V0^2*(sin(A))^2+2*g*h))/g * (Vo*cosA+Vdop) - дальность полёта", font="Cricket 14")
    l6.place(x=10, y=320)
    l6.config(bd=20, bg=label_bg_color, fg=label_text_color)
    BB.append(l6)
    l7 = Label(text="Tполёта = (V0 * sin(A) + sqrt(V0^2 * (sin(A))^2 + 2 * g * h)) / g - время полёта", font="Cricket 14")
    l7.place(x=10, y=370)
    l7.config(bd=14, bg=label_bg_color, fg=label_text_color)
    BB.append(l7)
    l8 = Label(text="Траектория движения тела, брошенного под углом к горизонту с \nплатформы - парабола", font="Cricket 14")
    l8.place(x=10, y=410)
    l8.config(bd=14, bg=label_bg_color, fg=label_text_color)
    BB.append(l8)

def theory():
    delete_main()
    global vvod
    vvod = []
    for a in vvod:
        a.destroy()
    lth = Label(text="Теория", font="Cricket 25")
    lth.config(bd=20, bg=label_bg_color, fg=label_text_color)
    lth.place(x=345, y=21)
    vvod.append(lth)

    lx = Label(text="Выберите раздел,\n по которому хотите \nузнать больше:", font="Cricket 14")
    lx.config(bd=20, bg=label_bg_color, fg=label_text_color)
    #lx.place(x=33, y=111)
    vvod.append(lx)

    b1 = Button(root, width=21, height=4, font=('Cricket', 14))
    b1.place(x=40, y=120)
    change_button(b1, "Бросок под углом \n с земли")
    vvod.append(b1)
    b1.config(command=th_by_angle_zero)

    b2 = Button(root, width=21, height=4, font=('Cricket', 14))
    b2.place(x=40, y=270)
    change_button(b2, "Бросок вертикально \n вверх с земли")
    vvod.append(b2)
    b2.config(command=th_vert_v_zero)

    b3 = Button(root, width=21, height=4, font=('Cricket', 14))
    b3.place(x=40, y=420)
    change_button(b3, "Бросок со скоростью, \n направленной \nгоризонтально, с высоты ")
    vvod.append(b3)
    b3.config(command=th_hor)

    b4 = Button(root, width=21, height=4, font=('Cricket', 14))
    b4.place(x=295, y=120)
    change_button(b4, "Бросок со скоростью, \n направленной под углом \n к горизонту, с высоты ")
    vvod.append(b4)
    b4.config(command=th_angle_h)

    b5 = Button(root, width=21, height=4, font=('Cricket', 14))
    b5.place(x=295, y=270)
    change_button(b5, "Бросок с высоты со \n скоростью, направленной \nвертикально вверх")
    vvod.append(b5)
    b5.config(command=th_vert_vverh)

    b6 = Button(root, width=21, height=4, font=('Cricket', 14))
    b6.place(x=295, y=420)
    change_button(b6, "Бросок с высоты со \n скоростью, направленной \nвертикально вниз")
    vvod.append(b6)
    b6.config(command=th_vert_vniz)

    b7 = Button(root, width=21, height=4, font=('Cricket', 14))
    b7.place(x=550, y=120)
    change_button(b7, "Бросок под углом А к \nгоризонту с высоты h\n на наклонную плоскость\n под углом B")
    vvod.append(b7)
    b7.config(command=th_dop)

    b8 = Button(root, width=21, height=4, font=('Cricket', 14))
    b8.place(x=550, y=270)
    change_button(b8, "Бросок под углом А к \nгоризонту c движущейся \nплатформы на высоте h")
    vvod.append(b8)
    b8.config(command=th_angle_h_move)

    b9 = Button(root, width=21, height=4, font=('Cricket', 14))
    b9.place(x=550, y=420)
    change_button(b9, "Бросок под углом А к \nгоризонту c высоты \nс учетом ветра")
    vvod.append(b9)
    b9.config(command=th_angle_h_wind)

def saved_files():
    f_name = fd.askopenfilename()
    f = open(f_name, "r")
    global vV0, vA, vh, vVdop
    st = f.readline().strip()
    if (st.find('Бросок под углом к горизонту с земли')!=-1):
        while (st):
            st = f.readline().strip()
            if (st.find('Vo') != -1):
                global V0
                V0 = float(st[10:])

            if (st.find('A (градусов)') != -1):
                global A
                A = float(st[14:])
        by_angle_zero()
        vV0.insert(0, V0)
        vA.insert(0, A)
        vvod_by_angle_zero()
    elif (st.find('Бросок вертикально вверх с земли')!=-1):
        while (st):
            st = f.readline().strip()
            if (st.find('Vo') != -1):
                V0 = float(st[10:])
        vert_zero()
        vV0.insert(0, V0)
        vvod_vert_zero()
    elif (st.find('Бросок горизонтально с высоты')!=-1):
        while (st):
            st = f.readline().strip()
            if (st.find('Vo (м/с)') != -1):
                V0 = float(st[10:])
            if (st.find('h (м)') != -1):
                h = float(st[7:])
        hor_h()
        vV0.insert(0, V0)
        vh.insert(0, h)
        vvod_hor_h()
    elif (st.find('Бросок под углом к горизонту с высоты h')!=-1):
        while (st):
            st = f.readline().strip()
            if (st.find('Vo (м/с)') != -1):
                V0 = float(st[10:])
            if (st.find('h (м)') != -1):
                h = float(st[7:])
            if (st.find('A (градусов)') != -1):
                A = float(st[14:])
        by_angle_h()
        vV0.insert(0, V0)
        vh.insert(0, h)
        vA.insert(0, A)
        vvod_by_angle_h()
    elif (st.find('Бросок вертикально вверх с высоты')!=-1):
        while (st):
            st = f.readline().strip()
            if (st.find('Vo (м/с)') != -1):
                V0 = float(st[10:])
            if (st.find('h (м)') != -1):
                h = float(st[7:])
        vert_v_h()
        vV0.insert(0, V0)
        vh.insert(0, h)
        vvod_vert_v_h()
    elif (st.find('Бросок вертикально вниз с высоты')!=-1):
        while (st):
            st = f.readline().strip()
            if (st.find('Vo (м/с)') != -1):
                V0 = float(st[10:])
            if (st.find('h (м)') != -1):
                h = float(st[7:])
        vert_vniz_h()
        vV0.insert(0, V0)
        vh.insert(0, h)
        vvod_vert_vniz_h()
    elif (st.find('Бросок под углом А к горизонту с высоты h на плоскость под углом B')!=-1):
        while (st):
            st = f.readline().strip()
            if (st.find('Vo (м/с)') != -1):
                V0 = float(st[10:])
            if (st.find('h (м)') != -1):
                h = float(st[7:])
            if (st.find('A (градусов)') != -1):
                A = float(st[14:])
            if (st.find('B (градусов)') != -1):
                B = float(st[14:])
        dop()
        global vB
        vV0.insert(0, V0)
        vh.insert(0, h)
        vA.insert(0, A)
        vB.insert(0, B)
        vvod_dop()
    elif (st.find('Бросок под углом к горизонту с движущейся платформы')!=-1):
        while (st):
            st = f.readline().strip()
            if (st.find('Vo (м/с)') != -1):
                V0 = float(st[10:])
            if (st.find('h (м)') != -1):
                h = float(st[7:])
            if (st.find('A (градусов)') != -1):
                A = float(st[14:])
            if (st.find('Vплатформы (м/с) = ') != -1):
                Vdop = float(st[19:])
        by_angle_h_move()
        vV0.insert(0, V0)
        vh.insert(0, h)
        vA.insert(0, A)
        vVdop.insert(0, Vdop)
        vvod_by_angle_h_move()

def start_window():  # Основное меню
    grafic.delete("all")
    global BB
    for a in BB:
        a.destroy()
    grafic.place(x=100000, y=70)
    global stroim
    stroim = False
    b_home.destroy()
    c.create_text(415, 60, text="Движение тела, брошенного под углом к горизонту", font=('Cricket', 23), fill=label_text_color)
    
    c['bg'] = label_bg_color

    for a in vvod:
        a.destroy()

    b1 = Button(root, text="1", width=21, height=4, font=('Cricket', 14))
    b1.place(x=40, y=120)
    b1.config(command = by_angle_zero)
    change_button(b1, "Бросок под углом \n с земли")


    b2 = Button(root, text="2", width=21, height=4, font=('Cricket', 14))
    b2.place(x=40, y=240)
    b2.config(command=vert_zero)
    change_button(b2, "Бросок вертикально \n вверх с земли")


    b3 = Button(root, text="3", width=21, height=4, font=('Cricket', 14))
    b3.place(x=40, y=360)
    b3.config(command=hor_h)
    change_button(b3, "Бросок со скоростью, \n направленной \nгоризонтально, с высоты ")


    b4 = Button(root, text="4", width=21, height=4, font=('Cricket', 14))
    b4.place(x=295, y=120)
    b4.config(command=by_angle_h)
    change_button(b4, "Бросок со скоростью, \n направленной под углом \n к горизонту, с высоты ")


    b5 = Button(root, text="5", width=21, height=4, font=('Cricket', 14))
    b5.place(x=295, y=240)
    b5.config(command=vert_v_h)
    change_button(b5, "Бросок с высоты \nвертикально вверх")


    b6 = Button(root, text="6", width=21, height=4, font=('Cricket', 14))
    b6.place(x=550, y=240)
    b6.config(command=vert_vniz_h)
    change_button(b6, "Бросок с высоты \nвертикально вниз")

    b10 = Button(root, text="6", width=21, height=4, font=('Cricket', 14))
    b10.place(x=550, y=360)
    b10.config(command=by_angle_h_move)
    change_button(b10, "Бросок под углом \nс движущегося тела\n на высоте")

    b11 = Button(root, text="6", width=21, height=4, font=('Cricket', 14))
    b11.place(x=295, y=360)
    b11.config(command=by_angle_h_wind)
    change_button(b11, "Бросок под углом \nс учетом ветра")

    b7 = Button(root, text="7", width=21, height=4, font=('Cricket', 14))
    b7.place(x=550, y=120)
    change_button(b7, "Бросок под углом А к \nгоризонту с высоты h на \nнаклонную плоскость\n под углом B")
    b7.config(command=dop)

    b8 = Button(root, text="8", width=21, height=4, font=('Cricket', 14))
    b8.place(x=295, y=480)
    change_button(b8, "СОХРАНЕННЫЕ \n РЕЗУЛЬТАТЫ")
    b8.config(command=saved_files)

    b9 = Button(root, text="9", width=21, height=4, font=('Cricket', 14))
    b9.place(x=40, y=480)
    change_button(b9, "ТЕОРИЯ")
    b9.config(command=theory)

    b12 = Button(root, text="bruh", width=21, height=4, font=('Cricket', 14))
    b12.place(x=550, y=480)
    change_button(b12, "СМЕНА ТЕМЫ")
    b12.config(command=change_theme)

    global main_buttons
    main_buttons = {b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12}

start_window()

root.mainloop()