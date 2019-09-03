from tkinter import Menu
from pycreator_core import FileSystem
from pycreator_tkinter.Core.Windows import Console

class ExecuteMenu(Menu):
    def __init__(self, window, menu):
        super(ExecuteMenu, self).__init__(menu, tearoff=0)
        self.window = window

        self.add_command(label="Executer", command=self.execute)
        self.add_command(label="Débugguer")
        self.add_command(label="Console")

    def execute(self):
        selected = self.window.tabeditor.select()
        if selected:
            filename = self.window.tabeditor.tab(selected, 'text')
            editor = self.window.tabeditor.nametowidget(selected)
            text = editor.get('1.0', 'end')[:-1]
            if FileSystem.open(filename) != text:
                FileSystem.save(filename, text)
            top = Console(self.window, filename)


