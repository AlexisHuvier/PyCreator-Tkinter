from pycreator_core import FileSystem


def save_code(window, selected, filename=None):
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
