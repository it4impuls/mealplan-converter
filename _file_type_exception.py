class FileTypeException(Exception):
    def __init__(self, message="The file has not the correct type"):
        self.message = message
        super().__init__(self.message)
