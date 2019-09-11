from tkinter import Text, INSERT, LEFT, RIGHT, IntVar
from tkinter.font import Font

from pycreator_core import FileSystem


class EditorWidget(Text):
    def __init__(self, parent, file):
        super(EditorWidget, self).__init__(parent)
        self.parent = parent
        self.file = file
        self.insert('1.0', FileSystem.open(self.file))

        self.config(tabs=('1c', '2c'))
        self.setup_hightlighter()
        self.apply_hightlighter()
        self.bind('<Key>', self.key_pressed)
        self.bind('<<Modified>>', self.changed)

    def key_pressed(self, e):
        self.mark_gravity(INSERT, LEFT)
        self.insert("insert", self.parent.window.analyser.update_code(e.char))
        self.mark_gravity(INSERT, RIGHT)

    def changed(self, value=None):
        flag = self.edit_modified()
        if flag:
            self.apply_hightlighter()

            self.parent.tab(self, text=self.file + "*")
        self.edit_modified(False)

    def setup_hightlighter(self):
        self.tag_config('Keyword', foreground="#0000FF")
        self.tag_config("Operator", foreground="#FF0000")
        self.tag_config("Brace", foreground="#808080")
        self.tag_config("String", foreground="#FF00FF")
        self.tag_config("String2", foreground="#800080")
        self.tag_config("Comment", foreground="#C8C8C8", font=Font(font=self["font"], slant="italic"))
        self.tag_config("Self", foreground="#000000", font=Font(font=self["font"], slant="italic"))
        self.tag_config("Numbers", foreground="#00FF00")

    def apply_hightlighter(self):
        numb_char = IntVar()
        last_pos = "1.0"
        while 1:
            last_pos = self.search(r'#[^\n]*', index=last_pos, stopindex='end', regexp=True, count=numb_char)
            if last_pos == "":
                break
            self.tag_add('Comment', last_pos, "%s + %d chars" % (last_pos, numb_char.get()))
            last_pos = "%s + 1 chars" % last_pos
        last_pos = "1.0"
        while 1:
            last_pos = self.search("self", index=last_pos, stopindex='end', regexp=True, count=numb_char)
            if last_pos == "":
                break
            self.tag_add('Self', last_pos, "%s + %d chars" % (last_pos, numb_char.get()))
            last_pos = "%s + 1 chars" % last_pos
        for mot in ['".*"', "'.*'"]:
            last_pos = "1.0"
            while 1:
                last_pos = self.search(mot, index=last_pos, stopindex='end', regexp=True, count=numb_char)
                if last_pos == "":
                    break
                self.tag_add('String', last_pos, "%s + %d chars" % (last_pos, numb_char.get()))
                last_pos = "%s + 1 chars" % last_pos
        for mot in ['""".*"""', "'''.*'''"]:
            last_pos = "1.0"
            while 1:
                last_pos = self.search(mot, index=last_pos, stopindex='end', regexp=True, count=numb_char)
                if last_pos == "":
                    break
                self.tag_add('String2', last_pos, "%s + %d chars" % (last_pos, numb_char.get()))
                last_pos = "%s + 1 chars" % last_pos
        for mot in ['{', '}', '(', ')', '[', ']', ]:
            last_pos = "1.0"
            while 1:
                last_pos = self.search(mot, index=last_pos, stopindex='end', regexp=0, count=numb_char)
                if last_pos == "":
                    break
                self.tag_add('Brace', last_pos, "%s + %d chars" % (last_pos, numb_char.get()))
                last_pos = "%s + 1 chars" % last_pos
        for mot in ['=', '==', '!=', '<', '<=', '>', '>=', '+', '-', '*', '/', '//', '%', '**', '+=', '-=', '*=',
                    '/=', '%=', '^', '|', '&', '~', '>>', '<<']:
            last_pos = "1.0"
            while 1:
                last_pos = self.search(mot, index=last_pos, stopindex='end', regexp=0, count=numb_char)
                if last_pos == "":
                    break
                self.tag_add('Operator', last_pos, "%s + %d chars" % (last_pos, numb_char.get()))
                last_pos = "%s + 1 chars" % last_pos
        for mot in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
            last_pos = "1.0"
            while 1:
                last_pos = self.search(mot, index=last_pos, stopindex='end', regexp=0, count=numb_char)
                if last_pos == "":
                    break
                self.tag_add('Numbers', last_pos, "%s + %d chars" % (last_pos, numb_char.get()))
                last_pos = "%s + 1 chars" % last_pos
        for mot in ['and', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'exec',
                    'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'not', 'or', 'pass',
                    'print', 'raise', 'return', 'try', 'while', 'yield', 'None', 'True', 'False']:
            last_pos = "1.0"
            while 1:
                last_pos = self.search(mot, index=last_pos, stopindex='end', regexp=0, count=numb_char)
                if last_pos == "":
                    break
                self.tag_add('Keyword', last_pos, "%s + %d chars" % (last_pos, numb_char.get()))
                last_pos = "%s + 1 chars" % last_pos
