from tkinter.ttk import Notebook

from pycreator_tkinter.Core.Widgets.EditorWidget import EditorWidget


class TabEditorWidget(Notebook):
    def __init__(self, parent):
        super(TabEditorWidget, self).__init__(parent)
        self.tabnames = []

    def add_tab(self, file):
        if file not in self.tabnames:
            self.add(EditorWidget(self, file), text=file)
            self.tabnames.append(file)

