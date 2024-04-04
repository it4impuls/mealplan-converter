import sys
import os
import re
import pandas as pd
from _menu_writer import MenuWriter
from _menu_reader_pdf import MenuReaderPDF

def sort_by_number(file_list):
    pattern = r'KW (\d+)\.pdf'
    def get_number(file_name):
        match = re.match(pattern, file_name)
        return int(match.group(1)) if match else 0
    sorted_list = sorted(file_list, key=get_number)
    return sorted_list

def merge_xlsx_files():
    pass


if __name__ == "__main__":
    pdf_files = sort_by_number([f for f in os.listdir(os.getcwd()) if f.endswith('.pdf') and re.search(r"KW", f)])
    for f in pdf_files:
        MenuWriter(MenuReaderPDF(os.getcwd()+ "/"+ f).get_table(), f.split('.')[0]).create_xlsx()
    xlsx_files = sort_by_number([f for f in os.listdir(os.getcwd()) if f.endswith('.xlsx') and re.search(r"KW", f)])
    readed_xlsx_files = []
    for x in xlsx_files:
        readed_xlsx_files.append(pd.read_excel(os.getcwd()+ "/"+ x))
    pd.concat(readed_xlsx_files).to_excel('new_merged_menu.xlsx', index=False)
    for df in xlsx_files:
        os.remove(os.getcwd()+ "/"+ df)
