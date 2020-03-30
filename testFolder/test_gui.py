import syspath
from guiFolder.gui import gui

def test_gui():
    root = gui.start()
    root_dict= root.__dict__
    assert root_dict['master'] is not False
    assert root_dict['children'] is not False
