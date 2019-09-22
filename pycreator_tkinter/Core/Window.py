import tkinter as tk
from tkinter.ttk import Style, Scrollbar

from pycreator_tkinter.Core.Widgets import FilesWidget, TabEditorWidget
from pycreator_tkinter.Core.Menus import FileMenu, ExecuteMenu, CodeMenu, ParametersMenu

from pycreator_core import Config, Analyser


class Window(tk.Tk):
    def __init__(self):
        super(Window, self).__init__()
        self.conf = Config()
        self.analyser = Analyser(self.conf)

        self.theme = None  # Respect PEP8
        self.set_theme(self.conf.get("gui.tkinter.theme", "default"))

        self.title("PyCreator")
        self.state("zoomed")

        self.menu = tk.Menu(self)
        self.filemenu = FileMenu(self, self.menu)
        self.executemenu = ExecuteMenu(self, self.menu)
        self.codemenu = CodeMenu(self, self.menu)
        self.parametersmenu = ParametersMenu(self, self.menu)
        self.filesview = FilesWidget(self)
        self.tabeditor = TabEditorWidget(self)
        self.sh = Scrollbar()
        self.sv = Scrollbar()

        self.setup_ui()
        self.bind_event()

        self.protocol("WM_DELETE_WINDOW", self.on_close)
        self.mainloop()

    def bind_event(self):
        self.bind_all("<Control-KeyPress-o>", self.filemenu.open_file)
        self.bind_all("<Control-KeyPress-n>", self.filemenu.new)
        self.bind_all("<Control-KeyPress-i>", self.parametersmenu.open_info)
        self.bind_all("<Control-KeyPress-p>", self.parametersmenu.open_parameters)
        self.bind_all("<Control-KeyPress-s>", self.filemenu.save)
        self.bind_all("<Control-KeyPress-d>", self.filemenu.open_folder)
        self.bind_all("<Alt-KeyPress-c>", self.executemenu.console)
        self.bind_all("<Control-KeyPress-t>", self.codemenu.indenter)
        self.bind_all("<Alt-KeyPress-t>", self.codemenu.desindenter)
        self.bind_all("<KeyPress-F5>", self.executemenu.execute)

    def setup_ui(self):
        self.menu.add_cascade(label="Fichier", menu=self.filemenu)
        self.menu.add_cascade(label="Executer", menu=self.executemenu)
        self.menu.add_cascade(label="Code", menu=self.codemenu)
        self.menu.add_cascade(label="Paramètres", menu=self.parametersmenu)

        self.config(menu=self.menu)
        self.sh.config(orient="horizontal")

        self.filesview.grid(row=0, column=0, rowspan=2, sticky="news")
        self.tabeditor.grid(row=0, column=1, sticky="news")
        self.sh.grid(row=1, column=1, sticky="news")
        self.sv.grid(row=0, column=2, rowspan=2, sticky="news")

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=5)

    def set_theme(self, theme):
        self.theme = theme
        Style().theme_use(theme)

    def on_close(self):
        self.conf.set("folder", self.filesview.folder)

        self.conf.set("gui.tkinter.theme", self.theme)
        self.conf.save()
        self.destroy()
