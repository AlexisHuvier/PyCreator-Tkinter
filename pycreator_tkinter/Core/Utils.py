from pycreator_core import FileSystem
from tkinter import IntVar, TclError


def get_editor(window):
    selected = window.tabeditor.select()
    if selected:
        return True, window.tabeditor.nametowidget(selected)
    else:
        return False, None


def save_code(window, filename=None):
    selected = window.tabeditor.select()
    if selected:
        if filename is None:
            changed = False
            filename = window.tabeditor.tab(selected, 'text')
        else:
            changed = True
        editor = window.tabeditor.nametowidget(selected)
        text = editor.get('1.0', 'end')[:-1]
        filename = filename.replace("*", "")
        if not changed:
            window.tabeditor.tab(selected, text=filename)
        FileSystem.save(filename, text)
        return filename


def replace_code(window, from_str, to_str):
    exist, editor = get_editor(window)
    if exist:
        nbm_char = IntVar()
        last_pos = "1.0"
        while 1:
            last_pos = editor.search(from_str, index=last_pos, stopindex='end', regexp=True, count=nbm_char)
            if last_pos == "":
                break
            editor.delete(last_pos, "%s + %d chars" % (last_pos, nbm_char.get()))
            editor.insert(last_pos, to_str)
            last_pos = "%s + 1 chars" % last_pos


def add_begin_code(window, txt):
    exist, editor = get_editor(window)
    if exist:
        try:
            line = "1.0"
            while editor.compare(line, '<', 'sel.first linestart'):
                liste = line.split(".")
                liste[0] = int(liste[0]) + 1
                line = str(liste[0]) + ".0"
            while editor.compare(line, '<=', 'sel.last linestart'):
                editor.insert(line, txt)
                liste = line.split(".")
                liste[0] = int(liste[0]) + 1
                line = str(liste[0]) + ".0"
        except TclError:
            editor.insert('insert linestart', txt)


def remove_begin_code(window, txt):
    exist, editor = get_editor(window)
    if exist:
        nmb_char = IntVar()
        try:
            editor.get('sel.first linestart')
        except TclError:
            begin = 'insert linestart'
            end = 'insert'
        else:
            begin = 'sel.first linestart'
            end = 'sel.last'
        line = "1.0"
        while editor.compare(line, '<', begin):
            liste = line.split(".")
            liste[0] = int(liste[0]) + 1
            line = str(liste[0]) + ".0"
        last_pos = line
        while 1:
            last_pos = editor.search(txt, index=last_pos, stopindex=end, regexp=True, count=nmb_char)
            if last_pos == "":
                break
            editor.delete(last_pos, "%s + %d chars" % (last_pos, nmb_char.get()))
            last_pos = "%s + 1 chars" % last_pos
