import tkinter as tk



class Window(tk.Tk):
    def __init__(self):
        super(Window, self).__init__()
        self.title("PyCreator")
        self.state("zoomed")

        self.create_ui()

        self.mainloop()

    def create_ui(self):
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=4)
