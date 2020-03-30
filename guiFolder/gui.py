from tkinter import *

class gui():
    def start():
        root = gui.create_root()
        complete_gui = gui.add_elements(root)
        gui.build_gui(complete_gui)
        root.mainloop()
        return True

    def create_root():
        root = Tk()
        return root

    def add_elements(root):
        Text = Label(root,text="Hello")
        return Text

    def build_gui(complete_gui):
        complete_gui.pack()