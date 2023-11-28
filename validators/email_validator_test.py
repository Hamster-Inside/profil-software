import pytest
from .email_validator import AtSignValidator, ValidationError, LengthOfTextBeforeAtSign, \
    LengthOfTextBetweenAtSignAndDot, LengthOfTextAfterLastDot, TextAfterLastDot, EmailValidator


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


def test_length_of_text_before_at_sign_positive():
    # given
    validator = LengthOfTextBeforeAtSign('H@gmail.com')

    # when
    result = validator.is_valid()

    # then
    assert result is True


def test_length_of_text_before_at_sign_negative():
    # given
    validator = LengthOfTextBeforeAtSign('@home.com')

    # when
    with pytest.raises(ValidationError) as error:
        validator.is_valid()

        # then
        assert 'Invalid email. Email name before "@" must contain at least one character' in str(error.value)


def test_length_of_text_between_at_sign_and_dot_positive():
    # given
    validator = LengthOfTextBetweenAtSignAndDot('Kokos@G.com')

    # when
    result = validator.is_valid()

    # then
    assert result is True


def test_length_of_text_between_at_sign_and_dot_negative():
    # given
    validator = LengthOfTextBetweenAtSignAndDot('Home@.com')

    # when
    with pytest.raises(ValidationError) as error:
        validator.is_valid()

        # then
        assert 'Invalid email. Email name between "@" and "." must contain at least one character' in str(error.value)


def test_length_of_text_after_last_dot_positive():
    # given
    validator = LengthOfTextBetweenAtSignAndDot('Kokos@Gmail.com')

    # when
    result = validator.is_valid()

    # then
    assert result is True


def test_length_of_text_after_last_dot_too_short_negative():
    # given
    validator = LengthOfTextAfterLastDot('Home@Help.')

    # when
    with pytest.raises(ValidationError) as error:
        validator.is_valid()

        # then
        assert 'Invalid email. Email text after the last "." should contain between 1 and 4 characters' in str(
            error.value)


def test_length_of_text_after_last_dot_too_long_negative():
    # given
    validator = LengthOfTextAfterLastDot('Home@Help.kokos')

    # when
    with pytest.raises(ValidationError) as error:
        validator.is_valid()

        # then
        assert 'Invalid email. Email text after the last "." should contain between 1 and 4 characters' in str(
            error.value)


def test_text_after_last_dot_positive():
    # given
    validator = TextAfterLastDot('Kokos@Gmail.com')

    # when
    result = validator.is_valid()

    # then
    assert result is True


def test_text_after_last_dot_special_signs_negative():
    # given
    validator = TextAfterLastDot('Home@Help.c&m')

    # when
    with pytest.raises(ValidationError) as error:
        validator.is_valid()

        # then
        assert 'Invalid email. Email text after the last "." should contain only letters and/or digits' in str(
            error.value)


def test_email_validation_positive():
    # given
    validator = EmailValidator('Kokos@Gmail.com')

    # when
    result = validator.is_valid()

    # then
    assert result is True


def test_email_validation_negative():
    # given
    validator = EmailValidator('Home@Help.c&m')

    # when
    with pytest.raises(ValidationError) as error:
        validator.is_valid()

        # then
        assert 'Invalid email. Email text after the last "." should contain only letters and/or digits' in str(
            error.value)
