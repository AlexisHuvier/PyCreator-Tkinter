from tkinter import Text, INSERT, LEFT, RIGHT, IntVar
from tkinter.font import Font

from pycreator_core import FileSystem, get_completion, get_snippet


class EditorWidget(Text):
    def __init__(self, parent, file):
        super(EditorWidget, self).__init__(parent, undo=True)
        self.parent = parent

        self.file = file
        self.insert('1.0', FileSystem.open(self.file))

        self.config(tabs=('1c', '2c'))
        self.tags = {
            'Keyword': {"foreground": "#0000FF"},
            "Operator": {"foreground": "#FF0000"},
            "Brace": {"foreground": "#808080"},
            "String": {"foreground": "#FF00FF"},
            "String2": {"foreground": "#800080"},
            "Comment": {"foreground": "#777777", "font": Font(font=self["font"], slant="italic")},
            "Self": {"foreground": "#000000", "font": Font(font=self["font"], slant="italic")},
            "Numbers": {"foreground": "#00FF00"}
        }
        self.setup_hightlighter()
        self.apply_hightlighter()
        self.bind('<KeyPress>', self.key_pressed)
        self.bind('<Alt-KeyPress-s>', self.snippet)
        self.bind('<Alt-KeyPress-a>', self.autocompletion)
        self.bind('<<Modified>>', self.changed)

    def autocompletion(self, evt):
        code = self.get("insert linestart", "insert lineend")
        if len(get_completion(code.split(" ")[-1])):
            self.delete("insert linestart", "insert lineend")
            self.insert("insert lineend", " ".join(code.split(" ")[:-1]))
            self.add_code(get_completion(code.split(" ")[-1])[0])
            self.mark_set("insert", "insert lineend")

    def snippet(self, evt):
        code = self.get("insert linestart", "insert lineend")
        self.delete("insert linestart", "insert lineend")
        self.insert("insert lineend", " ".join(code.split(" ")[:-1]))
        self.add_code(get_snippet(code.split(" ")[-1]))
        self.mark_set("insert", "insert lineend")

    def key_pressed(self, e):
        self.add_code(self.parent.window.analyser.update_code(e.char))

    def changed(self, value=None):
        flag = self.edit_modified()
        if flag:
            self.apply_hightlighter()
        self.edit_modified(False)

    def add_code(self, code):
        self.parent.tab(self, text=self.file + "*")
        self.mark_gravity(INSERT, LEFT)
        self.insert("insert", code)
        self.mark_gravity(INSERT, RIGHT)

    def setup_hightlighter(self):
        for k, v in self.tags.items():
            self.tag_config(k, **v)

    def apply_hightlighter(self):
        for i in self.tags.keys():
            self.tag_remove(i, "1.0", "end")

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
