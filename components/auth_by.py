from tkinter import BooleanVar, Label, Radiobutton, Frame,SOLID
from .token_field import init_token_field
from .credentials_fields import init_credentials






def init_auth_by_login(root, saved_conf:dict):



    def toggle_auth(*args):
        if auth_by_login.get():
            token_frame.grid_forget()
            credetials_frame.grid(row=2, column=0, columnspan=2)
        else:
            credetials_frame.grid_forget()
            token_frame.grid(row=2, column=0, columnspan=2)

    frame = Frame(root,borderwidth=1, relief=SOLID, pady=5)
    auth_by_login = BooleanVar(frame, value=saved_conf.get("auth_by_login", False))
    l = Label(frame, text="Авторизация в NTTM по:")
    login_btn = Radiobutton(frame, text="Логин и пароль", variable=auth_by_login, value=True)
    token_btn = Radiobutton(frame, text="Токену", variable=auth_by_login, value=False)
    l.grid(row=0)
    login_btn.grid(row=1, column=1)
    token_btn.grid(row=1, column=0)
    credetials_frame, login, passw = init_credentials(frame, saved_conf)
    token_frame, token = init_token_field(frame, saved_conf)
    auth_by_login.trace_add("write", toggle_auth)
    toggle_auth()
    return frame, {"auth_by_login":auth_by_login ,"login":login, "password":passw, "token": token}
