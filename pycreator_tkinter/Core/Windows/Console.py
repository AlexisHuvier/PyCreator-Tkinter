from tkinter import Toplevel, Text
from pycreator_core import Interpreter, History
from threading import Thread


class Console(Toplevel):
    def __init__(self, window, file=None):
        super(Console, self).__init__(window)
        self.window = window
        self.history = History()
        self.interpreter = Interpreter(self.write)

        self.text = Text(self)
        self.text.pack()

        if file is not None:
            p = Thread(target=self.execute, args=(file,))
            p.start()
        else:
            self.text.insert('1.0', ">>> ")

        self.bind("<KeyPress-Return>", self.enter)

    def enter(self, evt):
        code = self.text.get("1.0", "end").split(">>> ")[-1].replace("\n\n", "")
        self.interpreter.execute_interactive(code)
        self.text.insert('end', ">>> ")

    def execute(self, file):
        self.interpreter.execute_file(file)
        self.text.insert('end', ">>> ")

    def write(self, data):
        self.text.insert('end', data)
