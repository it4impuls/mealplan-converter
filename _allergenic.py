"""
Diese Klasse soll sich um die Allgene kümmern
"""
import os
import logging


class Allergenic:
    def __init__(self, allergenic_string):
        self.__allergenic_string = allergenic_string


if __name__ == "__main__":
    logger = logging.getLogger()
    logging.basicConfig(
        format='%(asctime)s %(levelname)s: %(message)s',
        level=logging.DEBUG
    )

    logging.info("Datei: %s wurde ausgeführt", os.path.basename(__file__))
