from tkinter import *
from math import sin, cos, pi, asin, acos, atan, sqrt, tan


root = Tk()
root.title("Movement of the body thrown at the angle to the horizon")
c = Canvas(root, bg='#F7DDC4', width=680, height=500)
root.geometry("680x500")
c.grid(row=0, column=0, columnspan=200, rowspan=70)


grafic = Canvas(root, bg='#D7E6FE', width=400, height=240)
grafic.place(x=257, y=20)

g=9.8

def draw():
    L=8.83
    V0=10
    A=pi/3
    H=3.82
    k=min(370/L, 190/H)
    grafic.create_line(10, 10, 10, 210, arrow=FIRST)
    grafic.create_line(10, 210, 395, 210, arrow=LAST)
    grafic.create_text(18, 13, text="y")
    grafic.create_text(391, 200, text="x")
    grafic.create_line(10, 210, 10+30*cos(A), 210-30*sin(A), arrow=LAST)
    grafic.create_text(10+30*cos(A)-2, 210-30*sin(A)-14, text="Vo")
    grafic.create_line(370, 10, 370, 40, arrow=LAST)
    grafic.create_text(361, 33, text="g")
    grafic.create_text(10, 220, text="0")
    grafic.create_text(27, 200-(H*k), text="Hmax")
    grafic.create_line(5, 210-(H*k), 390, 210-(H*k), dash=True)
    grafic.create_text(10+L*k, 220, text="Lmax")
    grafic.create_line(10+L*k, 10, 10+L*k, 215, dash=True)
    grafic.create_text(10 + (L * k)/2, 220, text="Lпод")
    grafic.create_line(10 + L* k/2, 10, 10 + L* k/2, 215, dash=True)
    for i in range(0, 1000):
        x=L/1000*i
        y= tan(A)*x - g/(2*V0**2*cos(A)**2) * x**2
        x1 = L/1000*(i+1)
        y1= tan(A)*x1 - g/(2*V0**2*cos(A)**2) * x1**2

        grafic.create_line((x)*k + 10, 220-((y)*k +10) , ((x1)*k +10) ,220-((y1)*k +10), fill="#000814")

draw()
root.mainloop()