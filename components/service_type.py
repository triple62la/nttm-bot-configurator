from tkinter import StringVar, SOLID, Label, Radiobutton, Frame


def init_service_type(root, saved_conf:dict):
    service_type = Frame(root, borderwidth=1, relief=SOLID)

    wifi_1 = "wifi_1.0"
    wifi_2 = "wifi_2.0"

    service_name = StringVar(value=saved_conf.get("service_type", "wifi_1.0"))
    service_header = Label(master=service_type, textvariable=service_name)
    wifi_1_btn = Radiobutton(service_type, text=wifi_1, value=wifi_1, variable=service_name)
    wifi_2_btn = Radiobutton(service_type, text=wifi_2, value=wifi_2, variable=service_name)
    l = Label(service_type, text="Выберите услугу:")
    l.grid(row=0, column=0)
    service_header.grid(row=0, column=1)
    wifi_1_btn.grid(row=1, column=0)
    wifi_2_btn.grid(row=1, column=1)
    return service_type, service_name
