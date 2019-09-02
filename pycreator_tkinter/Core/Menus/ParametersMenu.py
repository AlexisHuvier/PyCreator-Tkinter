from tkinter import Menu


class ParametersMenu(Menu):
    def __init__(self, window, menu):
        super(ParametersMenu, self).__init__(menu, tearoff=0)
        self.window = window

        self.add_command(label="Thèmes")
        self.add_command(label="Addons")
        self.add_command(label="Paramètres")
        self.add_separator()
        self.add_command(label="A Propos")
