from tkinter import Text

from pycreator_core import FileSystem


class EditorWidget(Text):
    def __init__(self, parent, file):
        super(EditorWidget, self).__init__(parent)
        self.parent = parent
        self.file = file
        self.insert('1.0', FileSystem.open(self.file))
