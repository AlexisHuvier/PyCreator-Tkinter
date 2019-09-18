from tkinter import Menu
import os.path

from pycreator_tkinter.Core.Utils import replace_code, add_begin_code, remove_begin_code
from pycreator_tkinter.Core.Windows import Documentation, TextWindow


class CodeMenu(Menu):
    def __init__(self, window, menu):
        super(CodeMenu, self).__init__(menu, tearoff=0)
        self.window = window

        self.add_command(label="Informations", command=self.information)
        self.add_command(label="Documentation", command=self.documentation)
        self.add_separator()
        self.add_command(label="Indenter", command=self.indenter)
        self.add_command(label="Désindenter", command=self.desindenter)
        self.add_command(label="Reformater")
        self.add_command(label="Commenter", command=self.comment)
        self.add_command(label="Décommenter", command=self.decomment)
        self.add_separator()
        self.add_command(label="Espaces -> Tabs", command=self.spacestotabs)
        self.add_command(label="Tabs -> Espaces", command=self.tabstospaces)

    def information(self):
        selected = self.window.tabeditor.select()
        if selected:
            filename = self.window.tabeditor.tab(selected, 'text')
            filename = filename.replace("*", "")
            infos = self.window.analyser.information_file(filename)
            TextWindow(self.window, "PyEngine - Information", "Information sur "+os.path.basename(filename), (
                "Nombre de lignes : " + str(len(infos["lines"])),
                "Nombre de commentaires : " + str(len(infos["comments"])),
                "Variables (" + str(len(infos["variables"])) + ") : " + ", ".join(infos["variables"])
            ))

    def documentation(self):
        Documentation(self.window)

    def indenter(self, evt=None):  # Can be use by events
        add_begin_code(self.window, "\t")

    def desindenter(self, evt=None):  # Can be use by events
        remove_begin_code(self.window, "\t")

    def comment(self):
        add_begin_code(self.window, "#")

    def decomment(self):
        remove_begin_code(self.window, "#")

    def spacestotabs(self):
        replace_code(self.window, "    ", "\t")

    def tabstospaces(self):
        replace_code(self.window, "\t", "    ")
