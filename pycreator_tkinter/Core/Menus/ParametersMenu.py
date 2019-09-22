import sys
from tkinter import Menu, TkVersion, TclVersion
from tkinter.ttk import __version__

import pycreator_core

import pycreator_tkinter
from pycreator_tkinter.Core.Windows import TextWindow, Themes, Parameters


class ParametersMenu(Menu):
    def __init__(self, window, menu):
        super(ParametersMenu, self).__init__(menu, tearoff=0)
        self.window = window

        self.add_command(label="Thèmes", command=self.open_theme)
        self.add_command(label="Addons")
        self.add_command(label="Paramètres", command=self.open_parameters)
        self.add_separator()
        self.add_command(label="A Propos", command=self.open_info)

    def open_parameters(self, evt=None):  # Can be use by events
        Parameters(self.window)

    def open_info(self, evt=None):  # Can be use by events
        v = str(sys.version_info.major) + "." + str(sys.version_info.minor) + "." + str(sys.version_info.micro)
        TextWindow(self.window, "PyEngine - A Propos", "A Propos", (
            "Auteur : LavaPower", "Version PyCreator-Tkinter : " + pycreator_tkinter.__version__,
            "Version PyCreator-Core : " + pycreator_core.__version__, "Version Tkinter : " + str(TkVersion),
            "Version Ttk : " + __version__, "Version Tcl : " + str(TclVersion), "Version Python : " + v
        ))

    def open_theme(self):
        Themes(self.window)

