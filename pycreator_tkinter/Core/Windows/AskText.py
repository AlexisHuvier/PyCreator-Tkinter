from tkinter import Toplevel
from tkinter.ttk import Label, Entry, Button


class AskText(Toplevel):
    def __init__(self, window, titre, message, command):
        super(AskText, self).__init__(window)
        self.window = window

        self.label = Label(self, text=message)
        self.entry = Entry(self)
        self.button = Button(self, text="Valider", command=command)

        self.label.pack(padx=10, pady=10)
        self.entry.pack(padx=10, pady=7)
        self.button.pack(padx=10, pady=7)

        self.title(titre)
