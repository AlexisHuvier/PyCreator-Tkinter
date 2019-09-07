from tkinter import Toplevel, Text
from pycreator_core import execute_file, History
from threading import Thread


class Console(Toplevel):
    def __init__(self, window, file=None):
        super(Console, self).__init__(window)
        self.window = window
        self.history = History()

        self.text = Text(self)
        self.text.pack()

        if file is not None:
            p = Thread(target=self.execute, args=(file,))
            p.start()
        else:
            self.text.insert('1.0', ">>> ")

    def execute(self, file):
        execute_file(file, self.write)
        self.text.insert('end', ">>> ")

    def write(self, data):
        self.text.insert('end', data)
