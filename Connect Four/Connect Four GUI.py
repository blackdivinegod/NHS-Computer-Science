from tkinter import *

cf = Tk()
cf.geometry("700x600")
cf.title("Connect Four")
cf.configure(background='blue')

turn = 'red'

def toggle():
    global turn
    if turn=='red':
        turn ='yellow'
    else:
        turn = 'red'

def column_1(event):
    global turn

    if frame_6.cget('bg') == 'gray87':
        frame_6.config(bg=turn)
        toggle()
    elif frame_5.cget('bg') == 'gray87':
        frame_5.config(bg=turn)
        toggle()
    elif frame_4.cget('bg') == 'gray87':
        frame_4.config(bg=turn)
        toggle()
    elif frame_3.cget('bg') == 'gray87':
        frame_3.config(bg=turn)
        toggle()
    elif frame_2.cget('bg') == 'gray87':
        frame_2.config(bg=turn)
        toggle()
    elif frame_1.cget('bg') == 'gray87':
        frame_1.config(bg=turn)
        toggle()

frame_1 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_1.bind("<Button-1>", column_1)
frame_1.grid(row=1, column=1)

frame_2 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_2.bind("<Button-1>", column_1)
frame_2.grid(row=2, column=1)

frame_3= Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_3.bind("<Button-1>", column_1)
frame_3.grid(row=3, column=1)

frame_4 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_4.bind("<Button-1>", column_1)
frame_4.grid(row=4, column=1)

frame_5 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_5.bind("<Button-1>", column_1)
frame_5.grid(row=5, column=1)

frame_6 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_6.bind("<Button-1>", column_1)
frame_6.grid(row=6, column=1)

def column_2(event):
    global turn

    if frame_12.cget('bg') == 'gray87':
        frame_12.config(bg=turn)
        toggle()
    elif frame_11.cget('bg') == 'gray87':
        frame_11.config(bg=turn)
        toggle()
    elif frame_10.cget('bg') == 'gray87':
        frame_10.config(bg=turn)
        toggle()
    elif frame_9.cget('bg') == 'gray87':
        frame_9.config(bg=turn)
        toggle()
    elif frame_8.cget('bg') == 'gray87':
        frame_8.config(bg=turn)
        toggle()
    elif frame_7.cget('bg') == 'gray87':
        frame_7.config(bg=turn)
        toggle()

frame_7 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_7.bind("<Button-1>", column_2)
frame_7.grid(row=1, column=2)

frame_8 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_8.bind("<Button-1>", column_2)
frame_8.grid(row=2, column=2)

frame_9 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_9.bind("<Button-1>", column_2)
frame_9.grid(row=3, column=2)

frame_10 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_10.bind("<Button-1>", column_2)
frame_10.grid(row=4, column=2)

frame_11 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_11.bind("<Button-1>", column_2)
frame_11.grid(row=5, column=2)

frame_12 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_12.bind("<Button-1>", column_2)
frame_12.grid(row=6, column=2)

def column_3(event):
    global turn

    if frame_18.cget('bg') == 'gray87':
        frame_18.config(bg=turn)
        toggle()
    elif frame_17.cget('bg') == 'gray87':
        frame_17.config(bg=turn)
        toggle()
    elif frame_16.cget('bg') == 'gray87':
        frame_16.config(bg=turn)
        toggle()
    elif frame_15.cget('bg') == 'gray87':
        frame_15.config(bg=turn)
        toggle()
    elif frame_14.cget('bg') == 'gray87':
        frame_14.config(bg=turn)
        toggle()
    elif frame_13.cget('bg') == 'gray87':
        frame_13.config(bg=turn)
        toggle()

frame_13 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_13.bind("<Button-1>", column_3)
frame_13.grid(row=1, column=3)

frame_14 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_14.bind("<Button-1>", column_3)
frame_14.grid(row=2, column=3)

frame_15 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_15.bind("<Button-1>", column_3)
frame_15.grid(row=3, column=3)

frame_16 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_16.bind("<Button-1>", column_3)
frame_16.grid(row=4, column=3)

frame_17 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_17.bind("<Button-1>", column_3)
frame_17.grid(row=5, column=3)

frame_18 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_18.bind("<Button-1>", column_3)
frame_18.grid(row=6, column=3)

def column_4(event):
    global turn

    if frame_24.cget('bg') == 'gray87':
        frame_24.config(bg=turn)
        toggle()
    elif frame_23.cget('bg') == 'gray87':
        frame_23.config(bg=turn)
        toggle()
    elif frame_22.cget('bg') == 'gray87':
        frame_22.config(bg=turn)
        toggle()
    elif frame_21.cget('bg') == 'gray87':
        frame_21.config(bg=turn)
        toggle()
    elif frame_20.cget('bg') == 'gray87':
        frame_20.config(bg=turn)
        toggle()
    elif frame_19.cget('bg') == 'gray87':
        frame_19.config(bg=turn)
        toggle()

frame_19 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_19.bind("<Button-1>", column_4)
frame_19.grid(row=1, column=4)

frame_20 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_20.bind("<Button-1>", column_4)
frame_20.grid(row=2, column=4)

frame_21 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_21.bind("<Button-1>", column_4)
frame_21.grid(row=3, column=4)

frame_22 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_22.bind("<Button-1>", column_4)
frame_22.grid(row=4, column=4)

frame_23 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_23.bind("<Button-1>", column_4)
frame_23.grid(row=5, column=4)

frame_24 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_24.bind("<Button-1>", column_4)
frame_24.grid(row=6, column=4)

def column_5(event):
    global turn

    if frame_30.cget('bg') == 'gray87':
        frame_30.config(bg=turn)
        toggle()
    elif frame_29.cget('bg') == 'gray87':
        frame_29.config(bg=turn)
        toggle()
    elif frame_28.cget('bg') == 'gray87':
        frame_28.config(bg=turn)
        toggle()
    elif frame_27.cget('bg') == 'gray87':
        frame_27.config(bg=turn)
        toggle()
    elif frame_26.cget('bg') == 'gray87':
        frame_26.config(bg=turn)
        toggle()
    elif frame_25.cget('bg') == 'gray87':
        frame_25.config(bg=turn)
        toggle()

frame_25 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_25.bind("<Button-1>", column_5)
frame_25.grid(row=1, column=5)

frame_26 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_26.bind("<Button-1>", column_5)
frame_26.grid(row=2, column=5)

frame_27 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_27.bind("<Button-1>", column_5)
frame_27.grid(row=3, column=5)

frame_28 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_28.bind("<Button-1>", column_5)
frame_28.grid(row=4, column=5)

frame_29 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_29.bind("<Button-1>", column_5)
frame_29.grid(row=5, column=5)

frame_30 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_30.bind("<Button-1>", column_5)
frame_30.grid(row=6, column=5)

def column_6(event):
    global turn

    if frame_36.cget('bg') == 'gray87':
        frame_36.config(bg=turn)
        toggle()
    elif frame_35.cget('bg') == 'gray87':
        frame_35.config(bg=turn)
        toggle()
    elif frame_34.cget('bg') == 'gray87':
        frame_34.config(bg=turn)
        toggle()
    elif frame_33.cget('bg') == 'gray87':
        frame_33.config(bg=turn)
        toggle()
    elif frame_32.cget('bg') == 'gray87':
        frame_32.config(bg=turn)
        toggle()
    elif frame_31.cget('bg') == 'gray87':
        frame_31.config(bg=turn)
        toggle()

frame_31 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_31.bind("<Button-1>", column_6)
frame_31.grid(row=1, column=6)

frame_32 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_32.bind("<Button-1>", column_6)
frame_32.grid(row=2, column=6)

frame_33 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_33.bind("<Button-1>", column_6)
frame_33.grid(row=3, column=6)

frame_34 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_34.bind("<Button-1>", column_6)
frame_34.grid(row=4, column=6)

frame_35 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_35.bind("<Button-1>", column_6)
frame_35.grid(row=5, column=6)

frame_36 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_36.bind("<Button-1>", column_6)
frame_36.grid(row=6, column=6)

def column_7(event):
    global turn

    if frame_42.cget('bg') == 'gray87':
        frame_42.config(bg=turn)
        toggle()
    elif frame_41.cget('bg') == 'gray87':
        frame_41.config(bg=turn)
        toggle()
    elif frame_40.cget('bg') == 'gray87':
        frame_40.config(bg=turn)
        toggle()
    elif frame_39.cget('bg') == 'gray87':
        frame_39.config(bg=turn)
        toggle()
    elif frame_38.cget('bg') == 'gray87':
        frame_38.config(bg=turn)
        toggle()
    elif frame_37.cget('bg') == 'gray87':
        frame_37.config(bg=turn)
        toggle()

frame_37 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_37.bind("<Button-1>", column_7)
frame_37.grid(row=1, column=7)

frame_38 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_38.bind("<Button-1>", column_7)
frame_38.grid(row=2, column=7)

frame_39 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_39.bind("<Button-1>", column_7)
frame_39.grid(row=3, column=7)

frame_40 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_40.bind("<Button-1>", column_7)
frame_40.grid(row=4, column=7)

frame_41 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_41.bind("<Button-1>", column_7)
frame_41.grid(row=5, column=7)

frame_42 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_42.bind("<Button-1>", column_7)
frame_42.grid(row=6, column=7)

cf.mainloop()
