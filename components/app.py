import json
import os
from tkinter import Tk, messagebox, X, NW, Button
from .utils import SAVED_CONFIG, validate_config, validate_token, format_token
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
        "nttm_token": format_token(auth_data["token"].get("1.0", "end")),
        "polling_interval": int(polling_int_value.get()),
        "nttm_url": nttm_url_value.get(),
        "bot_token": bot_token_field.get("1.0", "end").rstrip()
    }


def save_config(data):
    try:
        with open("config.json", "w") as f:
            f.write(json.dumps(data))
    except Exception as e:
        messagebox.showerror("OopsyWhoopsy", f"При сохранении настроек произошла ошибка: {e}")


def validate(config):
    conf_validation = validate_config(config)
    if config["auth_by_login"]:
        return conf_validation
    else:
        token_validation = validate_token(config.get("nttm_token"))
        return conf_validation if not conf_validation["is_valid"] else token_validation



def on_save_click():
    try:
        data = create_config_dict()
        validation = validate(data)
        if not validation["is_valid"]:
            messagebox.showwarning("Внимание", validation["message"])
            return
        save_config(data)
        messagebox.showinfo("Успешно", f"Файл конфигурации успешно сохранен.  {validation.get('message', '')}")
    except Exception as e:
        messagebox.showerror("OopsyWhoopsy", f"Произошла ошибка: {e}")


def on_start_click():
    try:
        data = create_config_dict()
        validation = validate(data)
        if not validation["is_valid"]:
            messagebox.showwarning("Внимание", validation["message"])
            return
        save_config(data)
        os.startfile("bot.exe")
        root.destroy()
    except Exception as e:
        messagebox.showerror("OopsyWhoopsy", f"Произошла ошибка: {e}")


root = Tk()

x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.geometry(f"370x550+{int(x)}+{int(y) - 200}")
root.title("bot launcher")

service_type, service_type_value = init_service_type(root, SAVED_CONFIG)
service_type.pack(fill=X, anchor=NW, padx=10, pady=10)

auth_by_login, auth_data = init_auth_by_login(root, SAVED_CONFIG)
auth_by_login.pack(fill=X, anchor=NW, padx=10, pady=10)

polling_int_spin, polling_int_value = init_polling_spin(root, SAVED_CONFIG)
polling_int_spin.pack(anchor=NW, padx=10, pady=10)

nttm_url_frame, nttm_url_value = init_nttm_url(root, SAVED_CONFIG)
nttm_url_frame.pack(anchor=NW, padx=10, pady=10)

bot_token_frame, bot_token_field = init_bot_token(root, SAVED_CONFIG)
bot_token_frame.pack(anchor=NW, padx=10, pady=10)

save_btn = Button(text="Сохранить конфиг", command=on_save_click)
save_btn.pack(pady=5)
confirm_button = Button(text="Сохранить и запустить бота", command=on_start_click)
confirm_button.pack(pady=5)
