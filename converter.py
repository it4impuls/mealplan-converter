import camelot
import tkinter as tk
from tkinter.filedialog import askopenfilename



class Converter:

    def convert(input):
        try:
            tables = camelot.read_pdf(input)
            print(tables[0])
            raise Exception("Sorry")
        except(FileNotFoundError):
            raise Exception("File Not found!")

if __name__ == "__main__":
    tk.Tk().withdraw()
    print(askopenfilename())
    # Converter.convert("'" + askopenfilename() + "'")