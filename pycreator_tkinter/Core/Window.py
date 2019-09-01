import tkinter as tk

from pycreator_tkinter.Core.Widgets.FilesWidget import FilesWidget
from pycreator_tkinter.Core.Widgets.TabEditorWidget import TabEditorWidget


class Window(tk.Tk):
    def __init__(self):
        super(Window, self).__init__()
        self.title("PyCreator")
        self.state("zoomed")

        self.filesview = FilesWidget(self)
        self.tabeditor = TabEditorWidget(self)

        self.setup_ui()

        self.mainloop()

    def setup_ui(self):
        self.filesview.grid(row=0, column=0, sticky='nesw')
        self.tabeditor.grid(row=0, column=1, sticky='nesw')

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=4)
