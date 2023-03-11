"""Data for tests and classes for sending requests"""
from faker import Faker
import requests
from datetime import datetime


fake = Faker()

date_str = '2003-11-26'
date_obj = datetime.strptime(date_str, '%Y-%m-%d')


class EmployerData:

    """Data for creation"""
    @staticmethod
    def valid_creation_data():

        name = fake.first_name()
        lastname = fake.last_name()
        email = fake.email()

        return {"name": name, "lastname": lastname, "email": email, "date_of_birth": date_obj}

    @staticmethod
    def already_exist():
        name = fake.first_name()
        lastname = fake.last_name()
        email = "woodmaria@example.com"

        return {"name": name, "lastname": lastname, "email": email, "date_of_birth": date_obj}

    @staticmethod
    def empty_data():
        name = ""
        lastname = ""
        email = ""

        return {"name": name, "lastname": lastname, "email": email, "date_of_birth": ""}

    @staticmethod
    def invalid_name():
        name = "a3252352342"
        lastname = fake.last_name()
        email = fake.email()

        return {"name": name, "lastname": lastname, "email": email, "date_of_birth": date_obj}

    @staticmethod
    def invalid_lastname():
        name = fake.first_name()
        lastname = "a3252d352342"
        email = fake.email()

        return {"name": name, "lastname": lastname, "email": email, "date_of_birth": date_obj}

    @staticmethod
    def invalid_email():
        name = fake.first_name()
        lastname = fake.last_name()
        email = "romaost@rovskiy616@gmailcom"

        return {"name": name, "lastname": lastname, "email": email, "date_of_birth": date_obj}

    @staticmethod
    def invalid_name_symbols():
        name = "asdawdwadas@sdadcom"
        lastname = fake.last_name()
        email = "asdawdwadas@sdad.com"

        return {"name": name, "lastname": lastname, "email": email, "date_of_birth": date_obj}

    @staticmethod
    def invalid_lastname_symbols():
        name = fake.first_name()
        lastname = "asdawdwadas@sdadcom"
        email = "asdawdwadas@sdad.com"

        return {"name": name, "lastname": lastname, "email": email, "date_of_birth": date_obj}

    """Data for updating"""
    @staticmethod
    def valid_update_data():
        name = fake.first_name()
        lastname = fake.last_name()

        return {"name": name, "lastname": lastname}

    @staticmethod
    def empty_employer_data():
        name = ""
        lastname = ""

        return {"name": name, "lastname": lastname}

    @staticmethod
    def invalid_update_name():
        name = "a3252352342"
        lastname = fake.last_name()

        return {"name": name, "lastname": lastname}

    @staticmethod
    def invalid_update_lastname():
        name = fake.first_name()
        lastname = "a3252d352342"

        return {"name": name, "lastname": lastname}

    @staticmethod
    def invalid_update_name_symbols():
        name = "asdawdwadas@sdadcom"
        lastname = fake.last_name()

        return {"name": name, "lastname": lastname}

    @staticmethod
    def invalid_update_lastname_symbols():
        name = fake.first_name()
        lastname = "asdawdwadas@sdadcom"

        return {"name": name, "lastname": lastname}


class EmployeeData:
    """Data for creation"""

    @staticmethod
    def valid_creation_data():

        name = fake.first_name()
        lastname = fake.last_name()
        email = fake.email()

        return {"name": name, "lastname": lastname, "email": email, "date_of_birth": date_obj, "employer_id": 3}

    @staticmethod
    def empty_creation_data():
        return {"name": "", "lastname": "", "email": "", "date_of_birth": "", "employer_id": ""}

    @staticmethod
    def invalid_name_creation_data():
        name = "namewqeqweqwe2342"
        lastname = fake.last_name()
        email = fake.email()

        return {"name": name, "lastname": lastname, "email": email, "date_of_birth": date_obj, "employer_id": 3}

    @staticmethod
    def invalid_lastname_creation_data():
        name = fake.first_name()
        lastname = "namewqeqweqwe2342"
        email = fake.email()

        return {"name": name, "lastname": lastname, "email": email, "date_of_birth": date_obj, "employer_id": 3}

    @staticmethod
    def invalid_email_creation_data():
        name = fake.first_name()
        lastname = fake.last_name()
        email = "roma@ostrovskiy616@gmail@com"

        return {"name": name, "lastname": lastname, "email": email, "date_of_birth": date_obj, "employer_id": 3}

    @staticmethod
    def invalid_employer_id_creation_data():
        name = fake.first_name()
        lastname = fake.last_name()
        email = fake.email()

        return {"name": name, "lastname": lastname, "email": email, "date_of_birth": date_obj, "employer_id": 999}

    @staticmethod
    def already_exist_creation_data():
        name = fake.first_name()
        lastname = fake.last_name()
        email = "Ivantsiv@gmail.com1"

        return {"name": name, "lastname": lastname, "email": email, "date_of_birth": date_obj, "employer_id": 3}

    @staticmethod
    def invalid_name_symbols_data():
        name = "namewqeqweqwe@"
        lastname = fake.last_name()
        email = fake.email()

        return {"name": name, "lastname": lastname, "email": email, "date_of_birth": date_obj, "employer_id": 3}

    @staticmethod
    def invalid_lastname_symbols_data():
        name = "namewqeqweqwe@"
        lastname = fake.last_name()
        email = fake.email()

        return {"name": name, "lastname": lastname, "email": email, "date_of_birth": date_obj, "employer_id": 3}

    """Data for updating"""

    @staticmethod
    def valid_update_data():
        name = fake.first_name()
        lastname = fake.last_name()

        return {"name": name, "lastname": lastname, "employer_id": 2}

    @staticmethod
    def empty_update_data():

        return {"name": "", "lastname": "", "employer_id": ""}

    @staticmethod
    def invalid_name_update_data():
        name = "namewqeqweqwe2342"
        lastname = fake.last_name()
        email = fake.email()

        return {"name": name, "lastname": lastname, "email": email}

    @staticmethod
    def invalid_lastname_update_data():
        name = fake.first_name()
        lastname = "namewqeqweqwe2342"
        email = fake.email()

        return {"name": name, "lastname": lastname, "email": email}

    @staticmethod
    def invalid_employer_id_update_data():
        name = fake.first_name()
        lastname = fake.last_name()

        return {"name": name, "lastname": lastname, "employer_id": 999}

    @staticmethod
    def already_exist_update_data():
        name = fake.first_name()
        lastname = fake.last_name()

        return {"name": name, "lastname": lastname, "email": "GigaChad@gmail.com"}

    @staticmethod
    def invalid_name_symbols_update_data():
        name = "namewqeqweqwe@"
        lastname = fake.last_name()

        return {"name": name, "lastname": lastname}

    @staticmethod
    def invalid_lastname_symbols_update_data():
        name = fake.first_name()
        lastname = "namewqeqweqwe@"

        return {"name": name, "lastname": lastname}


class ResponseModel:

    def __init__(self, status_code: int, response: dict = None):
        self.status_code = status_code
        self.response_data = response


class Client:
    @staticmethod
    def custom_request(method: str, url, **kwargs):
        return requests.request(method, url, **kwargs)
