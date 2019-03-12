from tkinter import*

cl = Tk()
cl.geometry('240x490')
cl.title('Calculator')

cl = Entry(cl)
cl.grid()
cl.focus_set()

def b1_pressed():
     cl.get()

b = Button(cl, text=" ", width=10, command=b1_pressed)
b.grid(row=4, column=1)




cl.mainloop()
