""" This file contains validation methods"""

from marshmallow.validate import *
import re

regex = r'^[a-zA-Z0-9_]+$'

def contains_digits(name):
    return any(char.isdigit() for char in name)


def validate_name(name):

    if not name:
        raise ValidationError("Name cannot be empty, please enter correct name and try one more time!")

    if not re.match(regex, name):
        raise ValidationError(f"Name cannot contain next symbols:{regex}, enter correct name and try again!")

    if contains_digits(name):
        raise ValidationError("Name should contain only letters, please enter correct name and try one more time!")

    if len(name) < 2 or len(name) > 30:
        raise ValidationError("Name cannot be shorter than 2 letters and longer than 30, please enter correct name and "
                              "try one more time!")


def validate_lastname(lastname):

    if not lastname:
        raise ValidationError("Lastname cannot be empty, please enter correct name and try one more time!")

    if not re.match(regex, lastname):
        raise ValidationError(f"Lastname cannot contain next symbols:{regex}, enter correct lastname and try again!")

    if contains_digits(lastname):
        raise ValidationError("Lastname should contain only letters, please enter correct name and try one more time!")

    if len(lastname) < 5 or len(lastname) > 30:
        raise ValidationError("Lastname cannot be shorter than 5 letters and longer than 30, please enter correct name"
                              " and try one more time!")


def validate_email(email):

    if not email:
        raise ValidationError("Email address cannot be empty, please enter correct email address and try one more time!")

    if len(email) > 254:
        raise ValidationError("Email address cannot be longer than 254, please enter correct email address and try"
                              " one more time!")

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        raise ValidationError("Email address format is invalid, please enter correct email address and try"
                              " one more time!")


def validate(name, lastname, email):
    return validate_name(name), validate_lastname(lastname), validate_email(email)


def validate_update(name, lastname):
    return validate_name(name), validate_lastname(lastname),
