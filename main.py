from _converter import Converter
from tkinter.filedialog import askopenfilename
from _menu_writer import MenuWriter

"""Bin mir noch nicht sicher ob wir eine Main hier benötigen!?!"""
if __name__ == "__main__":
    mw = Converter("test.pdf")
    mw.convert()
