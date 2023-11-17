from tkinter import Entry, Label, Frame, Radiobutton, StringVar


def init_nttm_url(root, saved_conf:dict):

    def other_input_enable():
        other_input.config(state="normal")
        other_input.focus_set()

    def other_input_disable():
        other_input.config(state="disabled")

    frame = Frame(root)
    Label(frame, text="Адрес NTTM:").grid(row=0, column=0)
    url = StringVar(frame, value=saved_conf.get("nttm_url", 'http://www.ttm.rt.ru'))
    url_lbl = Label(frame, textvariable=url)
    url_lbl.grid(row=0, column=1, columnspan=2)
    ttm_btn = Radiobutton(frame, text='ttm.rt.ru', value='http://www.ttm.rt.ru', variable=url, command=other_input_disable)
    ttm_btn.grid(row=1, column=0)
    vdi_btn = Radiobutton(frame, text="VDI", value='http://192.168.68.56', variable=url, command=other_input_disable)
    vdi_btn.grid(row=1, column=1)
    other_btn = Radiobutton(frame, text="Другое", value=saved_conf.get("nttm_url", 'http://'), variable=url, command=other_input_enable)
    other_btn.grid(row=1, column=2)
    other_input = Entry(frame, textvariable=url, state="disabled")
    other_input.grid(row=2, column=2, columnspan=3)
    return frame, url
