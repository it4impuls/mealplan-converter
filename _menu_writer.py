""" Module. """
import os
import logging


class MenuWriter:

    def __init__(self, table):
        self.__table = table

    def create_xlsx(self):
        pass


if __name__ == "__main__":
    logger = logging.getLogger()
    logging.basicConfig(
        format='%(asctime)s %(levelname)s: %(message)s',
        level=logging.DEBUG
    )
