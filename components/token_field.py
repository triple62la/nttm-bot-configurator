from tkinter import Text,  Frame, Label


def init_token_field(root, saved_conf:dict):
    frame = Frame(root)
    token_l = Label(frame, text="Токен из NTTM")
    # token_field = Text(frame)
    # token_field.config(width=30, height=5)
    token_l.grid(row=1, column=0)
    # token_field.grid(row=1, column=1)
    return frame
