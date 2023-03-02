from models import ResponseModel, Client
from jsonschema import validate
import logging
from connection import session
from epam_project.models.models import Employee, Employer
logger = logging.getLogger("test_endpoints")


def is_employer_added_to_db(body: dict):

    email = body['email']
    employer = session.query(Employer).filter(Employer.email == email).first()

    if employer is None:
        return False

    return True


def is_employee_added_to_db(body: dict):

    email = body['email']
    employee = session.query(Employee).filter(Employee.email == email).first()

    if employee is None:
        return False

    return True


class AddEmployer:

    def __init__(self):
        self.client = Client()

    def add_employer(self, body: dict, schema: dict):

        name = body['name']
        lastname = body['lastname']
        email = body['email']
        date = body['date_of_birth']
        response = self.client.custom_request("POST", f'http://127.0.0.1:5000/add_employer?name={name}'
                                                      f'&lastname={lastname}&email={email}&date_of_birth={date}')

        validate(instance=response.json(), schema=schema)
        logger.info("response.text")
        return ResponseModel(status_code=response.status_code, response=response.json())


class UpdateEmployer:

    def __init__(self):
        self.client = Client()

    def update_employer(self, body: dict, schema: dict):
        email = "woodmaria@example.com"
        response = self.client.custom_request("PUT", f'http://127.0.0.1:5000/update_employer/{email}', json=body)

        validate(instance=response.json(), schema=schema)
        logger.info("response.text")
        return ResponseModel(status_code=response.status_code, response=response.json())


class DeleteEmployer:

    def __init__(self):
        self.client = Client()

    def delete_employer(self, email: str, schema: dict):
        response = self.client.custom_request("DELETE", f'http://127.0.0.1:5000/delete_employer/{email}')

        validate(instance=response.json(), schema=schema)
        logger.info("response.text")
        return ResponseModel(status_code=response.status_code, response=response.json())


class AddEmployee:

    def __init__(self):
        self.client = Client()

    def add_employee(self, body: dict, schema: dict):

        name = body['name']
        lastname = body['lastname']
        email = body['email']
        date = body['date_of_birth']
        employer_id = body['employer_id']

        response = self.client.custom_request("POST", f'http://127.0.0.1:5000/add_employee?name={name}'
                                                      f'&lastname={lastname}&email={email}'
                                                      f'&date_of_birth={date}&employer_id={employer_id}')

        validate(instance=response.json(), schema=schema)
        logger.info("response.text")
        return ResponseModel(status_code=response.status_code, response=response.json())


class UpdateEmployee:

    def __init__(self):
        self.client = Client()

    def update_employee(self, body: dict, schema: dict):
        email = "olegarch@gmail.com"
        response = self.client.custom_request("PUT", f'http://127.0.0.1:5000/update_employee/{email}', json=body)

        validate(instance=response.json(), schema=schema)
        logger.info("response.text")
        return ResponseModel(status_code=response.status_code, response=response.json())


class DeleteEmployee:

    def __init__(self):
        self.client = Client()

    def delete_employee(self, email: str, schema: dict):
        response = self.client.custom_request("DELETE", f'http://127.0.0.1:5000/delete_employee/{email}')

        validate(instance=response.json(), schema=schema)
        logger.info("response.text")
        return ResponseModel(status_code=response.status_code, response=response.json())