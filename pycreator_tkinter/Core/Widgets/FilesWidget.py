from tkinter import ttk
import os

from pycreator_core import FileSystem


class FilesWidget(ttk.Treeview):
    def __init__(self, window):
        super(FilesWidget, self).__init__(window, show="tree")
        self.window = window
        self.bind("<Double-1>", self.double_click)
        self.update_items(".")

    def double_click(self, event):
        liste = []
        item = self.selection()[0]
        liste.append(self.item(item, "text"))
        while self.parent(item) != '':
            item = self.parent(item)
            liste.append(self.item(item, "text"))
        liste.reverse()
        file = os.path.join(*liste)
        if os.path.isfile(file):
            self.window.tabeditor.add_tab(file)
    
    def update_items(self, directory, parent=''):
        files = FileSystem.list_files(directory)
        for k, v in files.items():
            if k != "__pycache__":
                self.insert(parent, 'end', parent+k, text=k)
                if v is not None:
                    self.update_items(os.path.join(directory, k), parent+k)
