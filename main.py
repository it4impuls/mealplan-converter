import sys
import os
import re
from _converter import Converter
from _menu_writer import MenuWriter

def sort_by_number(file_list):
    pattern = r'KW (\d+)\.pdf'
    
    def get_number(file_name):
        match = re.match(pattern, file_name)
        return int(match.group(1)) if match else 0
    
    sorted_list = sorted(file_list, key=get_number)
    return sorted_list

"""Bin mir noch nicht sicher ob wir eine Main hier benötigen!?!"""
if __name__ == "__main__":
    # os.getcwd() + "/test.pdf"
    """try:
        match sys.argv[1]:
            case x if not (os.getcwd() + x).endswith('.pdf'):
                print("Das ist keine PDF-Datei")
                
            case _:
                mw = Converter(os.getcwd()+"/"+ sys.argv[1])
                mw.convert()
    except IndexError:
        print("Sie haben kein Pfad angegeben")"""
    pdf_files = [f for f in os.listdir(os.getcwd()) if f.endswith('.pdf') and re.search(r"KW", f)]

    pdf_files = sort_by_number(pdf_files)
    print(pdf_files)
