"""Module for checking email"""
from abc import ABC, abstractmethod
import re


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


class AtSignValidator(Validator):
    """ Validator that checks if email contains one @ sign """

    def __init__(self, email: str):
        self.email = email

    def is_valid(self) -> bool:
        """ Checks if email is valid

        Raises:
            ValidationError: email is not valid because it does not pass the criteria:
                            * Email must contain only one "@" symbol. (and must contain at least that one)
        Returns:
            bool: there is only one 'at sign'

        """
        if self.email.count("@") == 1:
            return True
        raise ValidationError('Invalid email. Email must contain one "@" sign')


class LengthOfTextBeforeAtSign(Validator):
    """ Validator that checks if email value before "@" sign is valid """

    def __init__(self, email: str):
        self.email = email

    def is_valid(self) -> bool:
        """ Checks if email is valid

        Raises:
            ValidationError: email is not valid because it does not pass the criteria:
                            * The part before "@" must be at least 1 character long.
        Returns:
            bool: text before "@" is at least 1 char long

        """
        if len(self.email.split("@")[0]) > 0:
            return True
        raise ValidationError('Invalid email. Email name before "@" must contain at least one character')


class LengthOfTextBetweenAtSignAndDot(Validator):
    """ Validator that checks if email value between "@" and "." is valid """

    def __init__(self, email: str):
        self.email = email

    def is_valid(self) -> bool:
        """ Checks if email is valid

        Raises:
            ValidationError: email is not valid because it does not pass the criteria:
                            * The part between "@" and "." must be at least 1 character long.
        Returns:
            bool: text between "@" and "." is at least 1 char long

        """
        if len(self.email.split("@")[1].split(".")[0]) > 0:
            return True
        raise ValidationError('Invalid email. Email name between "@" and "." must contain at least one character')


class LengthOfTextAfterLastDot(Validator):
    """ Validator that checks if email value after last "." is valid """

    def __init__(self, email: str):
        self.email = email

    def is_valid(self) -> bool:
        """ Checks if email is valid

        Raises:
            ValidationError: email is not valid because it does not pass the criteria:
                            * The part after last "." must contain between 1 and 4 characters
        Returns:
            bool: text after last "." contains between 1 and 4 characters

        """
        if 0 < len(self.email.split(".")[-1]) < 5:
            return True
        raise ValidationError('Invalid email. Email text after the last "." should contain between 1 and 4 characters')


class TextAfterLastDot(Validator):
    """ Validator that checks if email value after last "." is valid """

    def __init__(self, email: str):
        self.email = email

    def is_valid(self) -> bool:
        """ Checks if email is valid

        Raises:
            ValidationError: email is not valid because it does not pass the criteria:
                            * The part after last "." must contain only letters and/or digits
        Returns:
            bool: text after last "." contains letters and/or digits

        """
        pattern = re.compile("^[a-zA-Z0-9]+$")
        if bool(pattern.match(self.email.split(".")[-1])):
            return True
        raise ValidationError('Invalid email. Email text after the last "." should contain only letters and/or digits')


class EmailValidator(Validator):
    """ Validator to check if text is strong enough as a password"""

    def __init__(self, email: str):
        self.email = email
        self.validators = [
            AtSignValidator,
            LengthOfTextBeforeAtSign,
            LengthOfTextBetweenAtSignAndDot,
            LengthOfTextAfterLastDot,
            TextAfterLastDot
        ]

    def is_valid(self) -> bool:
        """ Checks if email is valid

        Returns:
          bool: returns True if passes all the validators requirements

        """
        validation_list = []
        for new_validator in self.validators:
            validator = new_validator(self.email)
            validation_list.append(validator.is_valid())
        return all(validation_list)
