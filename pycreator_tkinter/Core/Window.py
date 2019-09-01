import tkinter as tk

from pycreator_tkinter.Core.Widgets.FilesWidget import FilesWidget


class Window(tk.Tk):
    def __init__(self):
        super(Window, self).__init__()
        self.title("PyCreator")
        self.state("zoomed")

        self.create_ui()

        self.mainloop()

    def create_ui(self):
        filesview = FilesWidget(self)
        filesview.grid(row=0, column=0, sticky='nesw')

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=4)
