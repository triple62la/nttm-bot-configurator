from tkinter import Frame, Text, Label, Button, BooleanVar

enabled = {"state": "normal", "background": "white"}
disabled = {"state": "disabled", "background": "#e3e3e3"}


def init_bot_token(root, saved_conf:dict):
    def toggle_field_lock():
        if is_locked.get():
            text.config(**enabled)
        else:
            text.config(**disabled)

        is_locked.set(not is_locked.get())

    frame = Frame(root)
    is_locked = BooleanVar(frame, True)
    Label(frame, text="Токен тлг бота").grid(row=0, column=0)
    text = Text(frame, width=22, height=3, padx=5, pady=3)
    text.insert("1.0", saved_conf.get("bot_token", ""))
    text.config(**disabled)
    text.grid(row=0, column=1)
    Button(frame, text="Разблок.", command=toggle_field_lock).grid(row=0, column=2)
    return frame, text
