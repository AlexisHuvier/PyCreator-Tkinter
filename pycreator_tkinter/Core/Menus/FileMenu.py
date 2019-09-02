from tkinter import Menu


class FileMenu(Menu):
    def __init__(self, window, menu):
        super(FileMenu, self).__init__(menu, tearoff=0)
        self.window = window

        self.add_command(label="Ouvrir")
        self.add_command(label="Sauvegarder")
        self.add_command(label="Sauvegarder Sous")
        self.add_command(label="Nouveau")
        self.add_separator()
        self.add_command(label="Quitter")
