from tkinter import Menu
import os

from pycreator_tkinter.Core.Windows import AskText
from pycreator_core import FileSystem


class FileMenu(Menu):
    def __init__(self, window, menu):
        super(FileMenu, self).__init__(menu, tearoff=0)
        self.window = window

        self.ask = None  # Respect PEP8

        self.add_command(label="Ouvrir")
        self.add_command(label="Sauvegarder")
        self.add_command(label="Sauvegarder Sous")
        self.add_command(label="Nouveau", command=self.new)
        self.add_separator()
        self.add_command(label="Quitter")

    def new(self):
        self.ask = AskText(self.window, "Nom du fichier", "Entrez le nom du fichier", self.validate_new)

    def validate_new(self):
        new = self.ask.entry.get()
        if new != "":
            if "." in new:
                FileSystem.save(os.path.join(self.window.filesview.folder, new), "")
            else:
                FileSystem.save(os.path.join(self.window.filesview.folder, new+".py"), "")
            self.ask.destroy()
            self.window.filesview.update_items()

