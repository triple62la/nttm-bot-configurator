from tkinter import Entry, StringVar, Label, Frame


def init_credentials(root):
    frame = Frame(root, pady=5)
    login_l = Label(frame, text="Логин NTTM")
    login = StringVar(frame, value="")
    login_input = Entry(frame, textvariable=login, width=25)
    login_l.grid(row=0, column=0)
    login_input.grid(row=0, column=1)
    passw = StringVar(frame, value="")
    passw_l = Label(frame, text="Пароль NTTM")
    passw_input = Entry(frame,textvariable=passw, show="*", width=25)
    passw_l.grid(row=1, column=0)
    passw_input.grid(row=1, column=1)
    return frame, login, passw
