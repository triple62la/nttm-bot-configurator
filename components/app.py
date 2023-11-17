import json
import sys
from tkinter import Tk, messagebox, X, NW, Button
from .utils import SAVED_CONFIG
from .service_type import init_service_type
from .auth_by import init_auth_by_login
from .polling_interval import init_polling_spin
from .nttm_url import init_nttm_url
from .bot_token import init_bot_token


def create_config_dict():
    return {
        "service_type": service_type_value.get(),
        "auth_by_login": auth_data["auth_by_login"].get(),
        "login": auth_data["login"].get(),
        "password": auth_data["password"].get(),
        "polling_interval": polling_int_value.get(),
        "nttm_url": nttm_url_value.get(),
        "bot_token": bot_token_field.get("1.0", "end").rstrip("\n")
            }

def save_config():
    try:
        data = create_config_dict()
        with open("config.json", "w") as f:
            f.write(json.dumps(data))
        messagebox.showinfo("Успех","Конфиг-файл успешно сохранен.Запустите bot.exe для начала работы")
        root.destroy()
    except Exception as e:
        messagebox.showerror("OopsyWhoopsy", f"При сохранении настроек произошла ошибка: {e}")


root = Tk()


x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.geometry(f"350x450+{int(x)}+{int(y)}")
root.title("bot config")

service_type, service_type_value = init_service_type(root, SAVED_CONFIG)
service_type.pack(fill=X, anchor=NW, padx=10, pady=10)

auth_by_login, auth_data = init_auth_by_login(root, SAVED_CONFIG)
auth_by_login.pack(fill=X, anchor=NW, padx=10, pady=10)

polling_int_spin, polling_int_value = init_polling_spin(root, SAVED_CONFIG)
polling_int_spin.pack(anchor=NW, padx=10, pady=10)

nttm_url_frame, nttm_url_value = init_nttm_url(root, SAVED_CONFIG)
nttm_url_frame.pack(anchor=NW, padx=10, pady=10)

bot_token_frame, bot_token_field = init_bot_token(root, SAVED_CONFIG)
bot_token_frame.pack()

confirm_button = Button(text="Сохранить", command=save_config)
confirm_button.pack(pady=10)

