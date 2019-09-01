from tkinter.ttk import Notebook
import os

from pycreator_tkinter.Core.Widgets.EditorWidget import EditorWidget


class TabEditorWidget(Notebook):
    def __init__(self, parent):
        super(TabEditorWidget, self).__init__(parent)

    def add_tab(self, file):
        self.add(EditorWidget(self, file), text=os.path.basename(file))

