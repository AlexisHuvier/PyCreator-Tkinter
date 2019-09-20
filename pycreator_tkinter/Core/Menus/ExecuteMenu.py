from tkinter import Menu
from pycreator_tkinter.Core.Windows import Console
from pycreator_tkinter.Core.Utils import save_code


class ExecuteMenu(Menu):
    def __init__(self, window, menu):
        super(ExecuteMenu, self).__init__(menu, tearoff=0)
        self.window = window

        self.add_command(label="Executer", command=self.execute)
        self.add_command(label="Débugguer")
        self.add_command(label="Console", command=self.console)

    def console(self, evt=None):  # Can be used by events
        Console(self.window)

    def execute(self, evt=None):  # Can be used by events
        selected = self.window.tabeditor.select()
        if selected:
            Console(self.window, save_code(self.window))


