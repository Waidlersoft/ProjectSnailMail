import syspath
from guiFolder.gui import gui

def test_gui():
    assert gui.start()

def test_create_root():
    root = gui.create_root()
    root_dict= root.__dict__
    assert root_dict['master'] is not False
    assert root_dict['children'] is not False

def test_add_elements():
    label = gui.add_elements(gui.create_root()).__dict__
    print(label)
    assert isinstance(label, dict)