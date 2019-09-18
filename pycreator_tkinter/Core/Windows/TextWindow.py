from tkinter import Toplevel
from tkinter.ttk import Label


class TextWindow(Toplevel):
    def __init__(self, window, title, titletext, texts):
        super(TextWindow, self).__init__(window)
        self.title(title)
        title = Label(self, text=titletext)
        title.pack(padx=10, pady=10)
        for i in texts:
            label = Label(self, text=i)
            label.pack(padx=10, pady=5)
