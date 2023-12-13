from tkinter import Text,  Frame, Label, scrolledtext


def init_token_field(root, saved_conf:dict):
    frame = Frame(root, pady=5)
    token_l = Label(frame, text="Токен из NTTM")
    token_field = scrolledtext.ScrolledText(frame)
    token_field.insert(1.0, saved_conf.get("nttm_token", ""))
    token_field.config(width=30, height=5)
    token_l.grid(row=1, column=0)
    token_field.grid(row=1, column=1)
    return frame, token_field
