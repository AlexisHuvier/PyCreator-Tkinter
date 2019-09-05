from tkinter import ttk, TclError
import os

from pycreator_core import FileSystem


class FilesWidget(ttk.Treeview):
    def __init__(self, window):
        super(FilesWidget, self).__init__(window, show="tree")
        self.window = window
        self.bind("<Double-1>", self.double_click)
        self.folder = self.window.conf.get("folder", "")
        if self.folder == "":
            self.folder = "."
        self.update_items(self.folder)

    def double_click(self, event):
        liste = []
        item = self.selection()[0]
        liste.append(self.item(item, "text"))
        while self.parent(item) != '':
            item = self.parent(item)
            liste.append(self.item(item, "text"))
        liste.reverse()
        file = os.path.join(*liste)
        if os.path.isfile(os.path.join(self.folder, file)):
            self.window.tabeditor.add_tab(os.path.join(self.folder, file))
    
    def update_items(self, directory=None, parent='', delete=False):
        if directory is None:
            directory = self.folder
        if delete:
            self.delete(*self.get_children())

        files = FileSystem.list_files(directory)
        for k, v in files.items():
            if k != "__pycache__":
                try:
                    self.insert(parent, 'end', parent+k, text=k)
                except TclError:
                    pass
                if v is not None:
                    self.update_items(os.path.join(directory, k), parent+k)
