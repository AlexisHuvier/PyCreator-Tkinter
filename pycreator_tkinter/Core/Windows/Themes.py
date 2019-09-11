from tkinter import Toplevel, StringVar

from tkinter.ttk import Label, OptionMenu, Button, Style


class Themes(Toplevel):
    def __init__(self, window):
        super(Themes, self).__init__(window)

        self.window = window
        self.title("PyCreator - Themes")

        title = Label(self, text="Choisissez le thème")
        liste_themes = [self.window.theme]
        for i in Style().theme_names():
            if i not in liste_themes:
                liste_themes.append(i)
        self.v = StringVar()
        self.v.set(liste_themes[0])
        om = OptionMenu(self, self.v, *liste_themes)
        b = Button(self, text="Valider", command=self.validate)

        title.pack(padx=10, pady=10)
        om.pack(padx=10, pady=5)
        b.pack(padx=10, pady=5)

    def validate(self):
        self.window.set_theme(self.v.get())
        self.destroy()
