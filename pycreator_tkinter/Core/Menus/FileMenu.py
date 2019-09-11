from tkinter import Menu, filedialog
import os

from pycreator_tkinter.Core.Windows import AskText
from pycreator_core import FileSystem
from pycreator_tkinter.Core.Utils import save_code


class FileMenu(Menu):
    def __init__(self, window, menu):
        super(FileMenu, self).__init__(menu, tearoff=0)
        self.window = window

        self.ask = None  # Respect PEP8

        self.add_command(label="Ouvrir Dossier", command=self.open_folder)
        self.add_command(label="Ouvrir Fichier", command=self.open_file)
        self.add_separator()
        self.add_command(label="Sauvegarder", command=self.save)
        self.add_command(label="Sauvegarder Sous", command=self.saveas)
        self.add_command(label="Supprimer", command=self.delete_file)
        self.add_command(label="Nouveau", command=self.new)
        self.add_separator()
        self.add_command(label="Quitter", command=self.window.destroy)

    def open_folder(self):
        directory = filedialog.askdirectory(title="Choisissez le dossier")
        if directory != "":
            self.window.filesview.folder = directory
            self.window.filesview.update_items(delete=True)

    def open_file(self):
        file = filedialog.askopenfilename(title="Choisissez le fichier", defaultextension='.py',
                                          filetypes=[('Fichier Python', '.py')])
        if file != "":
            self.window.tabeditor.add_tab(file)

    def delete_file(self):
        if len(self.window.filesview.selection()):
            item = self.window.filesview.item(self.window.filesview.selection()[0], "text")
            file = os.path.join(self.window.filesview.folder, item)
            os.remove(file)
            if file in self.window.tabeditor.tabnames:
                self.window.tabeditor.remove_tab(file)
            self.window.filesview.update_items(delete=True)

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

