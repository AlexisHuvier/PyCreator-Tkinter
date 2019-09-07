from tkinter import Toplevel, Text
from pycreator_core import execute_file, History


class Console(Toplevel):
    def __init__(self, window, file=None):
        super(Console, self).__init__(window)
        self.window = window
        self.history = History()

        self.text = Text(self)
        self.text.pack()

        if file is not None:
            execute_file(file, self.write)
            self.text.insert('end', ">>> ")
        else:
            self.text.insert('1.0', ">>> ")

    def write(self, data):
        self.text.insert('end', data)
