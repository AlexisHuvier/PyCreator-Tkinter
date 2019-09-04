from tkinter import Toplevel, Text
from pycreator_core import execute_file, FileSystem, History


class Console(Toplevel):
    def __init__(self, window, file=None):
        super(Console, self).__init__(window)
        self.window = window
        self.history = History()

        self.text = Text(self)
        self.text.pack()

        if file is not None:
            self.text.insert('1.0', execute_file(file, FileSystem.open(file)))
            self.text.insert('end', "\n>>>")
        else:
            self.text.insert('1.0', ">>>")
