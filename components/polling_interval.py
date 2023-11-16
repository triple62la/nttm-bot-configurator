from tkinter import Label, Spinbox, Frame, StringVar

FROM = 10
TO = 40


def init_polling_spin(root):

    frame = Frame(root)
    l = Label(frame, text="Интервал опроса NTTM")
    value = StringVar(frame, "10")
    spin = Spinbox(frame, from_=FROM, to=TO, textvariable=value, width=5,state="readonly")
    l.grid(row=0, column=0)
    spin.grid(row=0, column=1)

    return frame, value
