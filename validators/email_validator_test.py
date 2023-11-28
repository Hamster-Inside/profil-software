import pytest
from .email_validator import AtSignValidator, ValidationError


def test_email_at_sign_positive():
    # given
    validator = AtSignValidator('kokos@gmail.com')

    # when
    result = validator.is_valid()

    # then
    assert result is True


def test_email_at_sign_no_sign_negative():
    # given
    validator = AtSignValidator('ananas.kokos.com')

    # when
    with pytest.raises(ValidationError) as error:
        validator.is_valid()

    # then
        assert 'Invalid email. Email must contain one "@" sign' in str(error.value)


def test_email_at_sign_too_much_signs_negative():
    # given
    validator = AtSignValidator('ananas@kokos@kokos.com')

    # when
    with pytest.raises(ValidationError) as error:
        validator.is_valid()

    # then
        assert 'Invalid email. Email must contain one "@" sign' in str(error.value)


