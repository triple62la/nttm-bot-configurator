from tkinter import *
from .service_type import init_service_type
from .auth_by import init_auth_by_login
from .polling_interval import init_polling_spin
from .nttm_url import init_nttm_url

root = Tk()

x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.geometry(f"350x400+{int(x)}+{int(y)}")
root.title("bot config")

service_type, service_type_value = init_service_type(root)
service_type.pack(fill=X, anchor=NW, padx=10, pady=10)

auth_by_login, auth_by_login_value = init_auth_by_login(root)
auth_by_login.pack(fill=X, anchor=NW, padx=10, pady=10)

polling_int_spin, polling_int_value = init_polling_spin(root)
polling_int_spin.pack(anchor=NW, padx=10, pady=10)

nttm_url_frame, nttm_url_value = init_nttm_url(root)
nttm_url_frame.pack(anchor=NW, padx=10, pady=10)

confirm_button = Button(text="Сохранить")
confirm_button.pack(pady=10)

