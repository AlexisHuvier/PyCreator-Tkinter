from tkinter import Menu

from pycreator_tkinter.Core.Windows import Informations, Themes


class ParametersMenu(Menu):
    def __init__(self, window, menu):
        super(ParametersMenu, self).__init__(menu, tearoff=0)
        self.window = window

        self.add_command(label="Thèmes", command=self.open_theme)
        self.add_command(label="Addons")
        self.add_command(label="Paramètres")
        self.add_separator()
        self.add_command(label="A Propos", command=self.open_info)

    def open_info(self, evt=None):  # Can be use by events
        Informations(self.window)

    def open_theme(self):
        Themes(self.window)

