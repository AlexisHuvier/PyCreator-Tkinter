from tkinter import Toplevel, TkVersion, TclVersion
from tkinter.ttk import Label, __version__

import pycreator_tkinter
import pycreator_core
import sys


class Informations(Toplevel):
    def __init__(self, window):
        super(Informations, self).__init__(window)
        self.window = window

        title = Label(self, text="Informations")
        author = Label(self, text="Auteur : LavaPower")
        version = Label(self, text="Version PyCreator-Tkinter : " + pycreator_tkinter.__version__)
        versioncore = Label(self, text="Version PyCreator-Core : " + pycreator_core.__version__)
        versiontkinter = Label(self, text="Version Tkinter : " + str(TkVersion))
        versionttk = Label(self, text="Version Ttk : " + __version__)
        versiontcl = Label(self, text="Version Tcl : " + str(TclVersion))
        v = str(sys.version_info.major) + "." + str(sys.version_info.minor) + "." + str(sys.version_info.micro)
        versionpython = Label(self, text="Version Python : " + v)

        title.pack(padx=10, pady=10)
        author.pack(padx=10, pady=5)
        version.pack(padx=10, pady=5)
        versioncore.pack(padx=10, pady=5)
        versiontkinter.pack(padx=10, pady=5)
        versionttk.pack(padx=10, pady=5)
        versiontcl.pack(padx=10, pady=5)
        versionpython.pack(padx=10, pady=5)

        self.title("PyCreator - Informations")
