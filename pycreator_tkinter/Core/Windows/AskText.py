from tkinter import Label, Entry, Button, Toplevel


class AskText(Toplevel):
    def __init__(self, window, titre, message, command):
        super(AskText, self).__init__(window)
        self.window = window

        self.label = Label(self, text=message)
        self.entry = Entry(self)
        self.button = Button(self, text="Valider", command=command)

        self.label.pack()
        self.entry.pack()
        self.button.pack()

        self.title(titre)
