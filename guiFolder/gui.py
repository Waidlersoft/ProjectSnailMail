from tkinter import *

class gui():
    def start():
        root = Tk()
        root_dict = root.__dict__
        print(root_dict['master'])
        return root