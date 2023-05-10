""" Module. """
import os
import logging
import xlsxwriter
import re

class MenuWriter:
    row = 1 # Zeile
    cols = 0 # Spalte

    def __init__(self, table):
        self.__table = table

    def create_xlsx(self):
        workbook = xlsxwriter.Workbook('new_menu.xlsx')
        worksheet = workbook.add_worksheet()

        worksheet.write(0, 0, "Datum")
        worksheet.write(0, 1, "Vollkost")
        worksheet.write(0, 2, "Vegetarisch")

        # print(self.__table.columns)
        
        for c in range(1, len(self.__table.columns)):
            for r in range(0, len(self.__table)-1):
                match r:
                    case 0 if re.search(r"\b(?:0?[1-9]|[1-2][0-9]|3[0-1])\.(?:0?[1-9]|1[0-2])\.\d{4}\b", self.__table[c][r]):
                        worksheet.write(self.row, self.cols, self.__table[c][r].split(",")[1].strip())
                        self.cols += 1
                    case 1:
                        # GV entfernen
                        # Rundeklammern um Allergene setzten
                        # Komma nach den Allergene setzten außer nachdem letzten Eintrag
                        worksheet.write(self.row, self.cols, self.__table[c][r])
                        self.cols += 1
                    case 2:
                        # Das gleiche wie in case nur in eine andere Zelle schreiben
                        worksheet.write(self.row, self.cols, self.__table[c][r])
                        self.row += 1
                        self.cols = 0
                
                    
        
        # Erste freie Zeile im Worksheet
        # print(worksheet.dim_colmax + 1)

        workbook.close()
        
    


if __name__ == "__main__":
    logger = logging.getLogger()
    logging.basicConfig(
        format='%(asctime)s %(levelname)s: %(message)s',
        level=logging.DEBUG
    )
