""" This file contains validation methods"""
import datetime
import re
from marshmallow.validate import ValidationError

REGEX = r'^[a-zA-Z0-9_]+$'


def contains_digits(name):
    """ Method responsible for checking if string contains digits """
    return any(char.isdigit() for char in name)


def validate_name(name):
    """ Method responsible for name validation """
    if not name:
        raise ValidationError("Name cannot be empty, please enter correct name and try one more time!")

    if not re.match(REGEX, name):
        raise ValidationError(f"Name cannot contain next symbols:{REGEX}, enter correct name and try again!")

    if contains_digits(name):
        raise ValidationError("Name should contain only letters, please enter correct name and try one more time!")

    if len(name) < 2 or len(name) > 30:
        raise ValidationError("Name cannot be shorter than 2 letters and longer than 30, please enter correct name and "
                              "try one more time!")


def validate_lastname(lastname):
    """ Method responsible for lastname validation """
    if not lastname:
        raise ValidationError("Lastname cannot be empty, please enter correct name and try one more time!")

    if not re.match(REGEX, lastname):
        raise ValidationError(f"Lastname cannot contain next symbols:{REGEX}, enter correct lastname and try again!")

    if contains_digits(lastname):
        raise ValidationError("Lastname should contain only letters, please enter correct name and try one more time!")

    if len(lastname) < 2 or len(lastname) > 30:
        raise ValidationError("Lastname cannot be shorter than 2 letters and longer than 30, please enter correct name"
                              " and try one more time!!")


def validate_email(email):
    """ Method responsible for email validation """

    if not email:
        raise ValidationError("Email address cannot be empty, please enter correct email address and try one "
                              "more time!")

    if len(email) > 254:
        raise ValidationError("Email address cannot be longer than 254, please enter correct email address and try"
                              " one more time!")

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        raise ValidationError("Email address format is invalid, please enter correct email address and try"
                              " one more time!")


def validate_date(date):
    """ Method responsible for date validation """
    date_parts = date.split('-')
    if len(date_parts) != 3:
        raise ValidationError("Invalid date format. Please use YYYY-MM-DD.")

    try:
        birth_date = datetime.date(int(date_parts[0]), int(date_parts[1]), int(date_parts[2]))
    except ValueError as exc:
        raise ValidationError("Invalid date format. Please use YYYY-MM-DD.") from exc

    return birth_date


def validate(name, lastname, email):
    """ Method responsible for validation while creating employer or employee """
    return validate_name(name), validate_lastname(lastname), validate_email(email)


def validate_update(name, lastname):
    """ Method responsible for validation while updating employer or employee """
    return validate_name(name), validate_lastname(lastname)
