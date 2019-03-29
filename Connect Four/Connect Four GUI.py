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

def column_1():
    if frame_6.cget('bg') == 'gray87':
        frame_6.config(bg='red')
    elif frame_5.cget('bg') == 'gray87':
        frame_5.config(bg='red')
    elif frame_4.cget('bg') == 'gray87':
        frame_4.config(bg='red')
    elif frame_3.cget('bg') == 'gray87':
        frame_3.config(bg='red')
    elif frame_2.cget('bg') == 'gray87':
        frame_2.config(bg='red')
    elif frame_1.cget('bg') == 'gray87':
        frame_1.config(bg='red')


def callback_1(event):
    if frame_1.cget('bg') == 'red':
        frame_1.config(bg=turn)
    else:
        frame_1.config(bg=turn)
    toggle()

frame_1 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_1.bind("<Button-1>", callback_1)
frame_1.grid(row=1, column=1)

def callback_2(event):
    if frame_2.cget('bg') == 'red':
        frame_2.config(bg=turn)
    else:
        frame_2.config(bg=turn)
    toggle()


frame_2 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_2.bind("<Button-1>", callback_2)
frame_2.grid(row=2, column=1)

def callback_3(event):
    if frame_3.cget('bg') == 'red':
        frame_3.config(bg=turn)
    else:
        frame_3.config(bg=turn)
    toggle()

frame_3= Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_3.bind("<Button-1>", callback_3)
frame_3.grid(row=3, column=1)

def callback_4(event):
    if frame_4.cget('bg') == 'red':
        frame_4.config(bg=turn)
    else:
        frame_4.config(bg=turn)
    toggle()

frame_4 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_4.bind("<Button-1>", callback_4)
frame_4.grid(row=4, column=1)

def callback_5(event):
    if frame_5.cget('bg') == 'red':
        frame_5.config(bg=turn)
    else:
        frame_5.config(bg=turn)
    toggle()

frame_5 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_5.bind("<Button-1>", callback_5)
frame_5.grid(row=5, column=1)

def callback_6(event):
    if frame_6.cget('bg') == 'red':
        frame_6.config(bg=turn)
    else:
        frame_6.config(bg=turn)
    toggle()

frame_6 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_6.bind("<Button-1>", callback_6)
frame_6.grid(row=6, column=1)


def callback_7(event):
    if frame_7.cget('bg') == 'red':
        frame_7.config(bg=turn)
    else:
        frame_7.config(bg=turn)
    toggle()

frame_7 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_7.bind("<Button-1>", callback_7)
frame_7.grid(row=1, column=2)

def callback_8(event):
    if frame_8.cget('bg') == 'red':
        frame_8.config(bg=turn)
    else:
        frame_8.config(bg=turn)
    toggle()

frame_8 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_8.bind("<Button-1>", callback_8)
frame_8.grid(row=2, column=2)

def callback_9(event):
    if frame_9.cget('bg') == 'red':
        frame_9.config(bg=turn)
    else:
        frame_9.config(bg=turn)
    toggle()

frame_9 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_9.bind("<Button-1>", callback_9)
frame_9.grid(row=3, column=2)

def callback_10(event):
    if frame_10.cget('bg') == 'red':
        frame_10.config(bg=turn)
    else:
        frame_10.config(bg=turn)
    toggle()

frame_10 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_10.bind("<Button-1>", callback_10)
frame_10.grid(row=4, column=2)

def callback_11(event):
    if frame_11.cget('bg') == 'red':
        frame_11.config(bg=turn)
    else:
        frame_11.config(bg=turn)
    toggle()

frame_11 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_11.bind("<Button-1>", callback_11)
frame_11.grid(row=5, column=2)

def callback_12(event):
    if frame_12.cget('bg') == 'red':
        frame_12.config(bg=turn)
    else:
        frame_12.config(bg=turn)
    toggle()

frame_12 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_12.bind("<Button-1>", callback_12)
frame_12.grid(row=6, column=2)

def callback_13(event):
    if frame_13.cget('bg') == 'red':
        frame_13.config(bg=turn)
    else:
        frame_13.config(bg=turn)
    toggle()

frame_13 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_13.bind("<Button-1>", callback_13)
frame_13.grid(row=1, column=3)

def callback_14(event):
    if frame_14.cget('bg') == 'red':
        frame_14.config(bg=turn)
    else:
        frame_14.config(bg=turn)
    toggle()

frame_14 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_14.bind("<Button-1>", callback_14)
frame_14.grid(row=2, column=3)

def callback_15(event):
    if frame_15.cget('bg') == 'red':
        frame_15.config(bg=turn)
    else:
        frame_15.config(bg=turn)
    toggle()

frame_15 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_15.bind("<Button-1>", callback_15)
frame_15.grid(row=3, column=3)

def callback_16(event):
    if frame_16.cget('bg') == 'red':
        frame_16.config(bg=turn)
    else:
        frame_16.config(bg=turn)
    toggle()

frame_16 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_16.bind("<Button-1>", callback_16)
frame_16.grid(row=4, column=3)

def callback_17(event):
    if frame_17.cget('bg') == 'red':
        frame_17.config(bg=turn)
    else:
        frame_17.config(bg=turn)
    toggle()

frame_17 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_17.bind("<Button-1>", callback_17)
frame_17.grid(row=5, column=3)

def callback_19(event):
    if frame_19.cget('bg') == 'red':
        frame_19.config(bg=turn)
    else:
        frame_19.config(bg=turn)
    toggle()

frame_19 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_19.bind("<Button-1>", callback_19)
frame_19.grid(row=6, column=3)

def callback_20(event):
    if frame_20.cget('bg') == 'red':
        frame_20.config(bg=turn)
    else:
        frame_20.config(bg=turn)
    toggle()

frame_20 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_20.bind("<Button-1>", callback_20)
frame_20.grid(row=1, column=4)

def callback_21(event):
    if frame_21.cget('bg') == 'red':
        frame_21.config(bg=turn)
    else:
        frame_21.config(bg=turn)
    toggle()

frame_21 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_21.bind("<Button-1>", callback_21)
frame_21.grid(row=2, column=4)

def callback_22(event):
    if frame_22.cget('bg') == 'red':
        frame_22.config(bg=turn)
    else:
        frame_22.config(bg=turn)
    toggle()

frame_22 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_22.bind("<Button-1>", callback_22)
frame_22.grid(row=3, column=4)

def callback_23(event):
    if frame_23.cget('bg') == 'red':
        frame_23.config(bg=turn)
    else:
        frame_23.config(bg=turn)
    toggle()

frame_23 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_23.bind("<Button-1>", callback_23)
frame_23.grid(row=4, column=4)

def callback_24(event):
    if frame_24.cget('bg') == 'red':
        frame_24.config(bg=turn)
    else:
        frame_24.config(bg=turn)
    toggle()

frame_24 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_24.bind("<Button-1>", callback_24)
frame_24.grid(row=5, column=4)

def callback_25(event):
    if frame_25.cget('bg') == 'red':
        frame_25.config(bg=turn)
    else:
        frame_25.config(bg=turn)
    toggle()

frame_25 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_25.bind("<Button-1>", callback_25)
frame_25.grid(row=6, column=4)

def callback_26(event):
    if frame_26.cget('bg') == 'red':
        frame_26.config(bg=turn)
    else:
        frame_26.config(bg=turn)
    toggle()

frame_26 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_26.bind("<Button-1>", callback_26)
frame_26.grid(row=1, column=5)

def callback_27(event):
    if frame_27.cget('bg') == 'red':
        frame_27.config(bg=turn)
    else:
        frame_27.config(bg=turn)
    toggle()

frame_27 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_27.bind("<Button-1>", callback_27)
frame_27.grid(row=2, column=5)

def callback_28(event):
    if frame_28.cget('bg') == 'red':
        frame_28.config(bg=turn)
    else:
        frame_28.config(bg=turn)
    toggle()

frame_28 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_28.bind("<Button-1>", callback_28)
frame_28.grid(row=3, column=5)

def callback_29(event):
    if frame_29.cget('bg') == 'red':
        frame_29.config(bg=turn)
    else:
        frame_29.config(bg=turn)
    toggle()

frame_29 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_29.bind("<Button-1>", callback_29)
frame_29.grid(row=4, column=5)

def callback_30(event):
    if frame_30.cget('bg') == 'red':
        frame_30.config(bg=turn)
    else:
        frame_30.config(bg=turn)
    toggle()

frame_30 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_30.bind("<Button-1>", callback_30)
frame_30.grid(row=5, column=5)

def callback_31(event):
    if frame_31.cget('bg') == 'red':
        frame_31.config(bg=turn)
    else:
        frame_31.config(bg=turn)
    toggle()

frame_31 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_31.bind("<Button-1>", callback_31)
frame_31.grid(row=6, column=5)

def callback_32(event):
    if frame_32.cget('bg') == 'red':
        frame_32.config(bg=turn)
    else:
        frame_32.config(bg=turn)
    toggle()

frame_32 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_32.bind("<Button-1>", callback_32)
frame_32.grid(row=1, column=6)

def callback_33(event):
    if frame_33.cget('bg') == 'red':
        frame_33.config(bg=turn)
    else:
        frame_33.config(bg=turn)
    toggle()

frame_33 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_33.bind("<Button-1>", callback_33)
frame_33.grid(row=2, column=6)

def callback_34(event):
    if frame_34.cget('bg') == 'red':
        frame_34.config(bg=turn)
    else:
        frame_34.config(bg=turn)
    toggle()

frame_34 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_34.bind("<Button-1>", callback_34)
frame_34.grid(row=3, column=6)

def callback_35(event):
    if frame_35.cget('bg') == 'red':
        frame_35.config(bg=turn)
    else:
        frame_35.config(bg=turn)
    toggle()

frame_35 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_35.bind("<Button-1>", callback_35)
frame_35.grid(row=4, column=6)

def callback_36(event):
    if frame_36.cget('bg') == 'red':
        frame_36.config(bg=turn)
    else:
        frame_36.config(bg=turn)
    toggle()

frame_36 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_36.bind("<Button-1>", callback_36)
frame_36.grid(row=5, column=6)

def callback_37(event):
    if frame_37.cget('bg') == 'red':
        frame_37.config(bg=turn)
    else:
        frame_37.config(bg=turn)
    toggle()

frame_37 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_37.bind("<Button-1>", callback_37)
frame_37.grid(row=6, column=6)

def callback_38(event):
    if frame_38.cget('bg') == 'red':
        frame_38.config(bg=turn)
    else:
        frame_38.config(bg=turn)
    toggle()

frame_38 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_38.bind("<Button-1>", callback_38)
frame_38.grid(row=1, column=7)

def callback_39(event):
    if frame_39.cget('bg') == 'red':
        frame_39.config(bg=turn)
    else:
        frame_39.config(bg=turn)
    toggle()

frame_39 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_39.bind("<Button-1>", callback_39)
frame_39.grid(row=1, column=7)

def callback_40(event):
    if frame_40.cget('bg') == 'red':
        frame_40.config(bg=turn)
    else:
        frame_40.config(bg=turn)
    toggle()

frame_40 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_40.bind("<Button-1>", callback_40)
frame_40.grid(row=2, column=7)

def callback_41(event):
    if frame_41.cget('bg') == 'red':
        frame_41.config(bg=turn)
    else:
        frame_41.config(bg=turn)
    toggle()

frame_41 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_41.bind("<Button-1>", callback_41)
frame_41.grid(row=3, column=7)

def callback_42(event):
    if frame_42.cget('bg') == 'red':
        frame_42.config(bg=turn)
    else:
        frame_42.config(bg=turn)
    toggle()

frame_42 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_42.bind("<Button-1>", callback_42)
frame_42.grid(row=4, column=7)

def callback_43(event):
    if frame_43.cget('bg') == 'red':
        frame_43.config(bg=turn)
    else:
        frame_43.config(bg=turn)
    toggle()

frame_43 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_43.bind("<Button-1>", callback_43)
frame_43.grid(row=5, column=7)

def callback_44(event):
    if frame_44.cget('bg') == 'red':
        frame_44.config(bg=turn)
    else:
        frame_44.config(bg=turn)
    toggle()

frame_44 = Frame(cf, width=100, height=100, bd=20, relief=SUNKEN, background='gray87')
frame_44.bind("<Button-1>", callback_44)
frame_44.grid(row=6, column=7)

cf.mainloop()