from converter import Converter
import tkinter as tk
from tkinter.filedialog import askopenfilename

if __name__ == "__main__":
    tk.Tk().withdraw()
    Converter.convert(askopenfilename())