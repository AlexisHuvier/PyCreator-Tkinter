from tkinter import Text, INSERT, LEFT, RIGHT

from pycreator_core import FileSystem


class EditorWidget(Text):
    def __init__(self, parent, file):
        super(EditorWidget, self).__init__(parent)
        self.parent = parent
        self.file = file
        self.insert('1.0', FileSystem.open(self.file))
        self.config(tabs=('1c', '2c'))
        self.bind('<Key>', self.text_changed)

    def text_changed(self, e):
        self.mark_gravity(INSERT, LEFT)
        self.insert("insert", self.parent.window.analyser.update_code(e.char))
        self.mark_gravity(INSERT, RIGHT)
        self.parent.tab(self, text=self.file+"*")
