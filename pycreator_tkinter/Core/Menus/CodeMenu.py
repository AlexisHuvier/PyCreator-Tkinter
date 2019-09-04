from tkinter import Menu


class CodeMenu(Menu):
    def __init__(self, window, menu):
        super(CodeMenu, self).__init__(menu, tearoff=0)
        self.window = window

        self.add_command(label="Informations")
        self.add_separator()
        self.add_command(label="Indenter")
        self.add_command(label="Désindenter")
        self.add_command(label="Reformater")
        self.add_command(label="Commenter")
        self.add_command(label="Décommenter")
        self.add_separator()
        self.add_command(label="Espaces -> Tabs")
        self.add_command(label="Tabs -> Espaces")
