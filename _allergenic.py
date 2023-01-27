"""
Diese Klasse soll sich um die Allgene kümmern
"""
import os
import logging
import re

from _exceptions import AllergenicException


class Allergenic:
    def __init__(self, allergenic_string):
        self.__allergenic_string = self.__validate_allergenics(allergenic_string)
        self.__allergenic_dict = self.__build_dict()
        # print(self.__allergenic_dict)


    def __validate_allergenics(self, allergenic_string):
        match allergenic_string:
            case None:
                raise AllergenicException
        tmp_al = allergenic_string.split("Allergene:")
        for i in range(len(tmp_al)):
            if i == 1:
                return tmp_al[i]

    def get_allgernics(self):
        return self.__allergenic_dict

    def __build_dict(self):
        allergenic_dict = dict()
        # match = re.findall(r'(?<=\()(.*?)(?=;)', self.__allergenic_string)
        self.__allergenic_string.replace("[* Kennzeichnung gesetzlich vorgegeben]", ";")
        match = re.findall(r'(?s)(?<=\()(.*?)(?=;)', self.__allergenic_string)
        for entry in match:
            tmp = entry.split(")")
            for x in tmp[1]:
                if x == "*":
                    tmp[1] = tmp[1].replace("*", "")
            allergenic_dict.update({tmp[0]: tmp[1].strip()})
        return allergenic_dict


if __name__ == "__main__":
    logger = logging.getLogger()
    logging.basicConfig(
        format='%(asctime)s %(levelname)s: %(message)s',
        level=logging.DEBUG
    )

    logging.info("Datei: %s wurde ausgeführt", os.path.basename(__file__))
