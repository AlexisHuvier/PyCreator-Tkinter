from tkinter.ttk import Notebook

from pycreator_tkinter.Core.Widgets.EditorWidget import EditorWidget


class TabEditorWidget(Notebook):
    def __init__(self, window):
        super(TabEditorWidget, self).__init__(window)
        self.window = window
        self.tabnames = []

    def remove_tab(self, file):
        for i in self.tabs():
            if self.tab(i, "text") == file:
                self.forget(i)

    def add_tab(self, file):
        if file not in self.tabnames:
            self.add(EditorWidget(self, file), text=file)
            self.tabnames.append(file)
            self.select(self.tabs()[-1])

