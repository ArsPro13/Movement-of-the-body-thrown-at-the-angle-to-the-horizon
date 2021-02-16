from tkinter import *



root = Tk()
root.title("Movement of the body thrown at the angle to the horizon")
c = Canvas(root, bg='#F7DDC4', width=680, height=500)
root.geometry("680x500")
c.grid(row=0, column=0, columnspan=100, rowspan=70)

b_home = Button(root)
vvod = []

def get_num(): # Получение числа из поля ввода
    pass

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
    b_home.place(x=635, y=458)
    b_home.config(command=start_window)

def by_angle_zero():  # Бросок под углом с земли
    global vvod
    delete_main()
    vvod = []
    vV0 = Entry(width=7)
    vV0.grid(row=0, column=0)
    vvod.append(vV0)

    bV0 = Button(root,  width=5, height=1)
    bV0.grid(row=0, column=1)
    change_button(bV0, "Vo")
    vvod.append(bV0)
    bV0.config(command=get_num)

    vA = Entry(width=7)
    vA.grid(row=1, column=0)
    vvod.append(vA)

    bA = Button(root, width=5, height=1)
    bA.grid(row=1, column=1)
    change_button(bA, "Угол")
    vvod.append(bA)
    bA.config(command=get_num)

    vH = Entry(width=7)
    vH.grid(row=2, column=0)
    vvod.append(vH)

    bH = Button(root, width=5, height=1)
    bH.grid(row=2, column=1)
    change_button(bH, "Hmax")
    vvod.append(bH)
    bH.config(command=get_num)

    vT = Entry(width=7)
    vT.grid(row=3, column=0)
    vvod.append(vT)

    bT = Button(root, width=5, height=1)
    bT.grid(row=3, column=1)
    change_button(bT, "Tпол.")
    vvod.append(bT)
    bT.config(command=get_num)

    vL = Entry(width=7)
    vL.grid(row=4, column=0)
    vvod.append(vL)

    bL = Button(root, width=5, height=1)
    bL.grid(row=4, column=1)
    change_button(bL, "Lпол.")
    vvod.append(bL)
    bL.config(command=get_num)

def start_window():  # Основное меню
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