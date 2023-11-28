from abc import ABC, abstractmethod


class ValidationError(Exception):
    """ Exception for validation error """


class Validator(ABC):
    """ Interface for validators """

    @abstractmethod
    def __init__(self, text: str):
        """ Force to implement __init__ method """

    @abstractmethod
    def is_valid(self) -> bool:
        """ Force to implement is_valid method """
