from tkinter import Toplevel, IntVar
from tkinter.ttk import Label, Checkbutton, Button


class Parameters(Toplevel):
    def __init__(self, window):
        super(Parameters, self).__init__(window)
        self.window = window

        title = Label(self, text="Paramètres")
        self.usespace = IntVar()
        check_usespace = Checkbutton(self, text="Espace préféré", variable=self.usespace)
        valide = Button(self, text="Valider", command=self.validate)

        title.grid(row=0, column=0, padx=10, pady=10)
        check_usespace.grid(row=1, column=0, padx=10, pady=5)
        valide.grid(row=2, column=0, padx=10, pady=5)

        self.setup_ui()

    def setup_ui(self):
        if self.window.conf.get("use_spaces", True):
            self.usespace.set(1)
        else:
            self.usespace.set(0)

    def validate(self):
        if self.usespace.get() == 1:
            self.window.conf.set("use_spaces", True)
        else:
            self.window.conf.set("use_spaces", False)

        self.destroy()
