from tkinter import Toplevel
from tkinter.ttk import Label

import pycreator_tkinter
import pycreator_core


class Informations(Toplevel):
    def __init__(self, window):
        super(Informations, self).__init__(window)
        self.window = window

        title = Label(self, text="Informations")
        author = Label(self, text="Auteur : LavaPower")
        version = Label(self, text="Version PyCreator-Tkinter : " + pycreator_tkinter.__version__)
        versioncore = Label(self, text="Version PyCreator-Core : " + pycreator_core.__version__)

        title.pack(padx=10, pady=10)
        author.pack(padx=10, pady=5)
        version.pack(padx=10, pady=5)
        versioncore.pack(padx=10, pady=5)

        self.title("PyCreator - Informations")
