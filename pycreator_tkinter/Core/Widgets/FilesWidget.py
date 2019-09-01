from tkinter import ttk
import os

from pycreator_core import FileSystem


class FilesWidget(ttk.Treeview):
    def __init__(self, window):
        super(FilesWidget, self).__init__(window, show="tree")
        self.update_items(".")
    
    def update_items(self, directory, parent=''):
        files = FileSystem.list_files(directory)
        for k, v in files.items():
            if k != "__pycache__":
                self.insert(parent, 'end', parent+k, text=k)
                if v is not None:
                    self.update_items(os.path.join(directory, k), parent+k)
