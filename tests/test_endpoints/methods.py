"""This file contains methods that are used in tests"""
from .models import ResponseModel, Client
from jsonschema import validate
import logging
from connection import session
from epam_project.models.models import Employee, Employer
logger = logging.getLogger("test_endpoints")


def is_employer_added_to_db(body: dict):
    """This method is responsible for checking if an employer has been added to database"""

    email = body['email']
    employer = session.query(Employer).filter(Employer.email == email).first()

    if employer is None:
        return False

    return True


class AddEmployer:
    """This class responsible for calling add employer endpoint"""

    def __init__(self):
        """constructor"""
        self.client = Client()

    def add_employer(self, body: dict, schema: dict):
        """This method takes data and schema, send request to url and return response_model(status_code and data)"""

        name = body['name']
        lastname = body['lastname']
        email = body['email']
        date = body['date_of_birth']
        response = self.client.custom_request("POST", f'http://127.0.0.1:5000/api/add_employer?name={name}'
                                                      f'&lastname={lastname}&email={email}&date_of_birth={date}')

        validate(instance=response.json(), schema=schema)
        logger.info("response.text")
        return ResponseModel(status_code=response.status_code, response=response.json())


class GetEmployer:
    """This class responsible for calling get employer endpoint"""

    def __init__(self):
        """constructor"""
        self.client = Client()

    def get_employer_by_email(self, email: str, schema: dict):
        """This method takes schema, send request to url and return response_model(status_code and data)"""

        email_address = email

        response = self.client.custom_request("GET", f'http://127.0.0.1:5000/api/get_employer_by_email/{email_address}')

        validate(instance=response.json(), schema=schema)
        logger.info("response.text")
        return ResponseModel(status_code=response.status_code, response=response.json())

    def get_employers(self, schema: dict):
        """This method takes email and schema, send request to url and return response_model(status_code and data)"""

        response = self.client.custom_request("GET", f'http://127.0.0.1:5000/api/get_all_employers')

        validate(instance=response.json(), schema=schema)
        logger.info("response.text")
        return ResponseModel(status_code=response.status_code, response=response.json())

    def get_employer_by_date_of_birth(self, date_of_birth, schema: dict):
        """This method takes schema, send request to url and return response_model(status_code and data)"""

        date_of_birth = date_of_birth

        response = self.client.custom_request("GET", f'http://127.0.0.1:5000/api/get_employer_by_date_of_birth'
                                                     f'/{date_of_birth}')

        validate(instance=response.json(), schema=schema)
        logger.info("response.text")
        return ResponseModel(status_code=response.status_code, response=response.json())


class UpdateEmployer:
    """This class responsible for calling update employer endpoint"""

    def __init__(self):
        """constructor"""
        self.client = Client()

    def update_employer(self, body: dict, schema: dict):
        """This method takes data and schema, send request to url and return response_model(status_code and data)"""
        email = "woodmaria@example.com"
        response = self.client.custom_request("PUT", f'http://127.0.0.1:5000/api/update_employer/{email}', json=body)

        validate(instance=response.json(), schema=schema)
        logger.info("response.text")
        return ResponseModel(status_code=response.status_code, response=response.json())


class DeleteEmployer:
    """This class responsible for calling delete employer endpoint"""

    def __init__(self):
        """constructor"""
        self.client = Client()

    def delete_employer(self, email: str, schema: dict):
        """This method takes data and schema, send request to url and return response_model(status_code and data)"""
        response = self.client.custom_request("DELETE", f'http://127.0.0.1:5000/api/delete_employer/{email}')

        validate(instance=response.json(), schema=schema)
        logger.info("response.text")
        return ResponseModel(status_code=response.status_code, response=response.json())


class AddEmployee:
    """This class responsible for calling add employee endpoint"""

    def __init__(self):
        """constructor"""
        self.client = Client()

    def add_employee(self, body: dict, schema: dict):
        """This method takes data and schema, send request to url and return response_model(status_code and data)"""
        name = body['name']
        lastname = body['lastname']
        email = body['email']
        date = body['date_of_birth']
        employer_id = body['employer_id']

        response = self.client.custom_request("POST", f'http://127.0.0.1:5000/api/add_employee?name={name}'
                                                      f'&lastname={lastname}&email={email}'
                                                      f'&date_of_birth={date}&employer_id={employer_id}')

        validate(instance=response.json(), schema=schema)
        logger.info("response.text")
        return ResponseModel(status_code=response.status_code, response=response.json())


class GetEmployee:
    """This class responsible for calling get employee endpoint"""

    def __init__(self):
        """constructor"""
        self.client = Client()

    def get_employee_by_email(self, email: str, schema: dict):
        """This method takes schema, send request to url and return response_model(status_code and data)"""

        email_address = email

        response = self.client.custom_request("GET", f'http://127.0.0.1:5000/api/get_employee_by_email/{email_address}')

        validate(instance=response.json(), schema=schema)
        logger.info("response.text")
        return ResponseModel(status_code=response.status_code, response=response.json())

    def get_employees(self, schema: dict):
        """This method takes email and schema, send request to url and return response_model(status_code and data)"""

        response = self.client.custom_request("GET", f'http://127.0.0.1:5000/api/get_all_employees')

        validate(instance=response.json(), schema=schema)
        logger.info("response.text")
        return ResponseModel(status_code=response.status_code, response=response.json())

    def get_employee_by_date_of_birth(self, date_of_birth, schema: dict):
        """This method takes schema, send request to url and return response_model(status_code and data)"""

        date_of_birth = date_of_birth

        response = self.client.custom_request("GET", f'http://127.0.0.1:5000/api/get_employee_by_date_of_birth'
                                                     f'/{date_of_birth}')

        validate(instance=response.json(), schema=schema)
        logger.info("response.text")
        return ResponseModel(status_code=response.status_code, response=response.json())

    def get_employee_by_employer_id(self, employer_id: int, schema: dict):
        """This method takes schema, send request to url and return response_model(status_code and data)"""

        employer_id = employer_id

        response = self.client.custom_request("GET", f'http://127.0.0.1:5000/api/get_employees_by_employer_id'
                                                     f'/{employer_id}')

        validate(instance=response.json(), schema=schema)
        logger.info("response.text")
        return ResponseModel(status_code=response.status_code, response=response.json())


class UpdateEmployee:
    """This class responsible for calling update employee endpoint"""

    def __init__(self):
        """constructor"""
        self.client = Client()

    def update_employee(self, body: dict, schema: dict):
        """This method takes data and schema, send request to url and return response_model(status_code and data)"""
        email = "olegarch@gmail.com"
        response = self.client.custom_request("PUT", f'http://127.0.0.1:5000/api/update_employee/{email}', json=body)

        validate(instance=response.json(), schema=schema)
        logger.info("response.text")
        return ResponseModel(status_code=response.status_code, response=response.json())


class DeleteEmployee:
    """This class responsible for calling delete employee endpoint"""

    def __init__(self):
        """constructor"""
        self.client = Client()

    def delete_employee(self, email: str, schema: dict):
        """This method takes data and schema, send request to url and return response_model(status_code and data)"""
        response = self.client.custom_request("DELETE", f'http://127.0.0.1:5000/api/delete_employee/{email}')

        validate(instance=response.json(), schema=schema)
        logger.info("response.text")
        return ResponseModel(status_code=response.status_code, response=response.json())
