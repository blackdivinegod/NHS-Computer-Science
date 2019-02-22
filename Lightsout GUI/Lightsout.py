from tkinter import *

li = Tk()
li.geometry("180x164")
li.title("Lightsout")

def b1_pressed():
    if b1.cget('bg') == 'blue':
        b1.config(bg='yellow')
    else:
        b1.config(bg='blue')
    if b2.cget('bg') == 'blue':
        b2.config(bg='yellow')
    else:
        b2.config(bg='blue')
    if b5.cget('bg') == 'blue':
        b5.config(bg='yellow')
    else:
        b5.config(bg='blue')

b1 = Button(li, text=" ", bg='blue', command=b1_pressed)
b1.grid()
b1.config(width = 5, height = 2)

def b2_pressed():
    if b2.cget('bg') == 'blue':
        b2.config(bg='yellow')
    else:
        b2.config(bg='blue')
    if b1.cget('bg') == 'blue':
        b1.config(bg='yellow')
    else:
        b1.config(bg='blue')

    if b6.cget('bg') == 'blue':
        b6.config(bg='yellow')
    else:
        b6.config(bg='blue')
    if b3.cget('bg') == 'blue':
        b3.config(bg='yellow')
    else:
        b3.config(bg='blue')
b2 = Button(li, text=" ", bg='blue', command=b2_pressed)
b2.grid()
b2.config(width = 5, height = 2)

def b3_pressed():
    if b3.cget('bg') == 'blue':
        b3.config(bg='yellow')
    else:
        b3.config(bg='blue')

    if b2.cget('bg') == 'blue':
        b2.config(bg='yellow')
    else:
        b2.config(bg='blue')
    if b7.cget('bg') == 'blue':
        b7.config(bg='yellow')
    else:
        b7.config(bg='blue')
    if b4.cget('bg') == 'blue':
        b4.config(bg='yellow')
    else:
        b4.config(bg='blue')
b3 = Button(li, text=" ", bg='blue', command=b3_pressed)
b3.grid()
b3.config(width = 5, height = 2)

def b4_pressed():
    if b4.cget('bg') == 'blue':
        b4.config(bg='yellow')
    else:
        b4.config(bg='blue')

    if b3.cget('bg') == 'blue':
        b3.config(bg='yellow')
    else:
        b3.config(bg='blue')
    if b8.cget('bg') == 'blue':
        b8.config(bg='yellow')
    else:
        b8.config(bg='blue')

b4 = Button(li, text=" ", bg='blue', command=b4_pressed)
b4.grid()
b4.config(width = 5, height = 2)

def b5_pressed():
    if b5.cget('bg') == 'blue':
        b5.config(bg='yellow')
    else:
        b5.config(bg='blue')
    if b6.cget('bg') == 'blue':
        b6.config(bg='yellow')
    else:
        b6.config(bg='blue')
    if b9.cget('bg') == 'blue':
        b9.config(bg='yellow')
    else:
        b9.config(bg='blue')
    if b1.cget('bg') == 'blue':
        b1.config(bg='yellow')
    else:
        b1.config(bg='blue')
b5 = Button(li, text=" ", bg='blue', command=b5_pressed)
b5.grid()
b5.config(width = 5, height = 2)

def b6_pressed():
    if b6.cget('bg') == 'blue':
        b6.config(bg='yellow')
    else:
        b6.config(bg='blue')

    if b7.cget('bg') == 'blue':
        b7.config(bg='yellow')
    else:
        b7.config(bg='blue')
    if b10.cget('bg') == 'blue':
        b10.config(bg='yellow')
    else:
        b10.config(bg='blue')
    if b5.cget('bg') == 'blue':
        b5.config(bg='yellow')
    else:
        b5.config(bg='blue')
    if b2.cget('bg') == 'blue':
        b2.config(bg='yellow')
    else:
        b2.config(bg='blue')
b6 = Button(li, text=" ", bg='blue', command=b6_pressed)
b6.grid()
b6.config(width = 5, height = 2)

def b7_pressed():
    if b7.cget('bg') == 'blue':
        b7.config(bg='yellow')
    else:
        b7.config(bg='blue')

    if b8.cget('bg') == 'blue':
        b8.config(bg='yellow')
    else:
        b8.config(bg='blue')
    if b11.cget('bg') == 'blue':
        b11.config(bg='yellow')
    else:
        b11.config(bg='blue')
    if b6.cget('bg') == 'blue':
        b6.config(bg='yellow')
    else:
        b6.config(bg='blue')
    if b3.cget('bg') == 'blue':
        b3.config(bg='yellow')
    else:
        b3.config(bg='blue')
b7 = Button(li, text=" ", bg='blue', command=b7_pressed)
b7.grid()
b7.config(width = 5, height = 2)

def b8_pressed():
    if b8.cget('bg') == 'blue':
        b8.config(bg='yellow')
    else:
        b8.config(bg='blue')

    if b7.cget('bg') == 'blue':
        b7.config(bg='yellow')
    else:
        b7.config(bg='blue')
    if b12.cget('bg') == 'blue':
        b12.config(bg='yellow')
    else:
        b12.config(bg='blue')
    if b4.cget('bg') == 'blue':
        b4.config(bg='yellow')
    else:
        b4.config(bg='blue')
b8 = Button(li, text=" ", bg='blue', command=b8_pressed)
b8.grid()
b8.config(width = 5, height = 2)

def b9_pressed():
    if b9.cget('bg') == 'blue':
        b9.config(bg='yellow')
    else:
        b9.config(bg='blue')
    if b13.cget('bg') == 'blue':
        b13.config(bg='yellow')
    else:
        b13.config(bg='blue')

    if b10.cget('bg') == 'blue':
        b10.config(bg='yellow')
    else:
        b10.config(bg='blue')
    if b5.cget('bg') == 'blue':
        b5.config(bg='yellow')
    else:
        b5.config(bg='blue')
b9 = Button(li, text=" ", bg='blue', command=b9_pressed)
b9.grid()
b9.config(width = 5, height = 2)

def b10_pressed():
    if b10.cget('bg') == 'blue':
        b10.config(bg='yellow')
    else:
        b10.config(bg='blue')
    if b9.cget('bg') == 'blue':
        b9.config(bg='yellow')
    else:
        b9.config(bg='blue')
    if b14.cget('bg') == 'blue':
        b14.config(bg='yellow')
    else:
        b14.config(bg='blue')
    if b6.cget('bg') == 'blue':
        b6.config(bg='yellow')
    else:
        b6.config(bg='blue')
    if b11.cget('bg') == 'blue':
        b11.config(bg='yellow')
    else:
        b11.config(bg='blue')
b10 = Button(li, text=" ", bg='blue', command=b10_pressed)
b10.grid()
b10.config(width = 5, height = 2)

def b11_pressed():
    if b11.cget('bg') == 'blue':
        b11.config(bg='yellow')
    else:
        b11.config(bg='blue')
    if b10.cget('bg') == 'blue':
        b10.config(bg='yellow')
    else:
        b10.config(bg='blue')

    if b15.cget('bg') == 'blue':
        b15.config(bg='yellow')
    else:
        b15.config(bg='blue')
    if b12.cget('bg') == 'blue':
        b12.config(bg='yellow')
    else:
        b12.config(bg='blue')
    if b7.cget('bg') == 'blue':
        b7.config(bg='yellow')
    else:
        b7.config(bg='blue')
b11 = Button(li, text=" ", bg='blue', command=b11_pressed)
b11.grid()
b11.config(width = 5, height = 2)

def b12_pressed():
    if b12.cget('bg') == 'blue':
        b12.config(bg='yellow')
    else:
        b12.config(bg='blue')

    if b11.cget('bg') == 'blue':
        b11.config(bg='yellow')
    else:
        b11.config(bg='blue')

    if b16.cget('bg') == 'blue':
        b16.config(bg='yellow')
    else:
        b16.config(bg='blue')
    if b8.cget('bg') == 'blue':
        b8.config(bg='yellow')
    else:
        b8.config(bg='blue')
b12 = Button(li, text=" ", bg='blue', command=b12_pressed)
b12.grid()
b12.config(width = 5, height = 2)

def b13_pressed():
    if b13.cget('bg') == 'blue':
        b13.config(bg='yellow')
    else:
        b13.config(bg='blue')

    if b9.cget('bg') == 'blue':
        b9.config(bg='yellow')
    else:
        b9.config(bg='blue')

    if b14.cget('bg') == 'blue':
        b14.config(bg='yellow')
    else:
        b14.config(bg='blue')

b13 = Button(li, text=" ", bg='blue', command=b13_pressed)
b13.grid()
b13.config(width = 5, height = 2)

def b14_pressed():
    if b14.cget('bg') == 'blue':
        b14.config(bg='yellow')
    else:
        b14.config(bg='blue')
    if b10.cget('bg') == 'blue':
        b10.config(bg='yellow')
    else:
        b10.config(bg='blue')
    if b15.cget('bg') == 'blue':
        b15.config(bg='yellow')
    else:
        b15.config(bg='blue')
    if b13.cget('bg') == 'blue':
        b13.config(bg='yellow')
    else:
        b13.config(bg='blue')
b14 = Button(li, text=" ", bg='blue', command=b14_pressed)
b14.grid()
b14.config(width = 5, height = 2)

def b15_pressed():
    if b15.cget('bg') == 'blue':
        b15.config(bg='yellow')
    else:
        b15.config(bg='blue')

    if b14.cget('bg') == 'blue':
        b14.config(bg='yellow')
    else:
        b14.config(bg='blue')

    if b11.cget('bg') == 'blue':
        b11.config(bg='yellow')
    else:
        b11.config(bg='blue')
    if b16.cget('bg') == 'blue':
        b16.config(bg='yellow')
    else:
        b16.config(bg='blue')
b15 = Button(li, text=" ", bg='blue', command=b15_pressed)
b15.grid()
b15.config(width = 5, height = 2)

def b16_pressed():
    if b16.cget('bg') == 'blue':
        b16.config(bg='yellow')
    else:
        b16.config(bg='blue')

    if b15.cget('bg') == 'blue':
        b15.config(bg='yellow')
    else:
        b15.config(bg='blue')

    if b12.cget('bg') == 'blue':
        b12.config(bg='yellow')
    else:
        b12.config(bg='blue')
b16 = Button(li, text=" ", bg='blue', command=b16_pressed)
b16.grid()
b16.config(width = 5, height = 2)

b1.grid(row=0, column=1)
b2.grid(row=1, column=1)
b3.grid(row=2, column=1)
b4.grid(row=3, column=1)
b5.grid(row=0, column=2)
b6.grid(row=1, column=2)
b7.grid(row=2, column=2)
b8.grid(row=3, column=2)
b9.grid(row=0, column=3)
b10.grid(row=1, column=3)
b11.grid(row=2, column=3)
b12.grid(row=3, column=3)
b13.grid(row=0, column=4)
b14.grid(row=1, column=4)
b15.grid(row=2, column=4)
b16.grid(row=3, column=4)

li.mainloop()
