from tkinter import Toplevel
from tkinter.ttk import Label, Entry, Button
import webbrowser
from pycreator_core import get_doc, get_help


class Documentation(Toplevel):
    def __init__(self, window):
        super(Documentation, self).__init__(window)
        self.title("PyEngine - Documentatition")

        title = Label(self, text="Documentation")
        self.e = Entry(self)
        offline = Button(self, text="Hors Ligne", command=self.v_offline)
        online = Button(self, text="En Ligne", command=self.v_online)
        self.info = Label(self, text="")

        title.pack(padx=10, pady=10)
        self.e.pack(padx=10, pady=5)
        offline.pack(padx=10, pady=5)
        online.pack(padx=10, pady=5)
        self.info.pack(padx=10, pady=10)

    def v_online(self):
        if self.e.get() != "":
            webbrowser.open(get_doc(self.e.get()))

    def v_offline(self):
        if self.e.get() != "":
            self.info.config(text="")
            get_help(self.e.get(), self.write_return)

    def write_return(self, text):
        self.info.config(text=self.info["text"]+text)
