""" Custom Exceptions module """


class CustomError(Exception):
    """ Base class for custom exceptions """

    def __init__(self, message, code=None, params=None):
        super().__init__(message, code, params)
        self.message = message
        self.code = code
        self.params = params


class InvalidFileException(CustomError):
    """ Base class for invalid file """
