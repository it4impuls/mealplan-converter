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

if __name__ == "__main__":
    pdf_files = [f for f in os.listdir(os.getcwd()) if f.endswith('.pdf') and re.search(r"KW", f)]
    pdf_files = sort_by_number(pdf_files)
    for f in pdf_files:
        Converter(os.getcwd()+ "/"+ f).convert()
