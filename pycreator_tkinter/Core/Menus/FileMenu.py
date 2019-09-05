from tkinter import Menu
import os

from pycreator_tkinter.Core.Windows import AskText
from pycreator_core import FileSystem
from pycreator_tkinter.Core.Utils import save_code


class FileMenu(Menu):
    def __init__(self, window, menu):
        super(FileMenu, self).__init__(menu, tearoff=0)
        self.window = window

        self.ask = None  # Respect PEP8

        self.add_command(label="Ouvrir")
        self.add_command(label="Sauvegarder", command=self.save)
        self.add_command(label="Sauvegarder Sous", command=self.saveas)
        self.add_command(label="Nouveau", command=self.new)
        self.add_separator()
        self.add_command(label="Quitter", command=self.window.destroy)

    def save(self):
        selected = self.window.tabeditor.select()
        if selected:
            save_code(self.window, selected)

    def saveas(self):
        self.ask = AskText(self.window, "Nom du fichier", "Entrez le nom du fichier", self.validate_save)

    def validate_save(self):
        selected = self.window.tabeditor.select()
        if selected:
            save = self.ask.entry.get()
            if save != "":
                if "." in save:
                    save_code(self.window, selected, os.path.join(self.window.filesview.folder, save))
                else:
                    save_code(self.window, selected, os.path.join(self.window.filesview.folder, save+".py"))
                self.ask.destroy()
                self.window.filesview.update_items()

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

