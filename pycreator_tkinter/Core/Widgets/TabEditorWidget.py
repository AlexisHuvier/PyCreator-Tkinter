from tkinter.ttk import Notebook

from pycreator_tkinter.Core.Widgets.EditorWidget import EditorWidget
from pycreator_tkinter.Core.Utils import get_editor


class TabEditorWidget(Notebook):
    def __init__(self, window):
        super(TabEditorWidget, self).__init__(window)
        self.window = window
        self.tabnames = []
        self.enable_traversal()
        self.bind("<<NotebookTabChanged>>", self.change_tab)

    def change_tab(self, evt):
        exist, editor = get_editor(self.window)
        if exist:
            editor.config(yscrollcommand=self.window.sv.set, xscrollcommand=self.window.sh.set)
            self.window.sh.config(command=editor.xview)
            self.window.sv.config(command=editor.yview)

    def remove_tab(self, file):
        for i in self.tabs():
            if self.tab(i, "text") == file:
                self.forget(i)

    def add_tab(self, file):
        if file not in self.tabnames:
            self.add(EditorWidget(self, file), text=file, sticky="NSEW")
            self.tabnames.append(file)
            self.select(self.tabs()[-1])

