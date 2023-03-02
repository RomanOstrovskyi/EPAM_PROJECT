""" This file contains validation methods"""

from marshmallow.validate import *
import re


def validate_name(name):

    if not name:
        raise ValidationError("Name cannot be empty, please enter correct name and try one more time!")

    if not isinstance(name, str) and not name.isalpha():
        raise ValidationError("Name should contain only letters, please enter correct name and try one more time!")

    if len(name) < 2 or len(name) > 30:
        raise ValidationError("Name cannot be shorter than 2 letters and longer than 30, please enter correct name and "
                              "try one more time!")


def validate_lastname(name):

    if not name:
        raise ValidationError("Lastname cannot be empty, please enter correct name and try one more time!")

    if not isinstance(name, str) and not name.isalpha():
        raise ValidationError("Lastname should contain only letters, please enter correct name and try one more time!")

    if len(name) < 5 or len(name) > 30:
        raise ValidationError("Lastname cannot be shorter than 5 letters and longer than 30, please enter correct name"
                              " and try one more time!!")


def validate_email(email):

    if not email:
        raise ValidationError("Email address cannot be empty, please enter correct email address and try one more time!")

    if not isinstance(email, str):
        raise ValidationError("Email address should contain only letters, please enter correct email address and try"
                              " one more time!")

    if len(email) > 254:
        raise ValidationError("Email address cannot be longer than 254, please enter correct email address and try"
                              " one more time!")

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        raise ValidationError("Email address format is invalid, please enter correct email address and try"
                              " one more time!")


def validate(name, lastname, email):
    return validate_name(name), validate_lastname(lastname), validate_email(email)
