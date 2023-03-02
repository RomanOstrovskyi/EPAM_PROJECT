"""tests for all endpoint in rest.view.py"""
from tests.test_endpoints.schemas.schemas import valid_schema, invalid_schema
from tests.test_endpoints.models import EmployerData, EmployeeData
from methods import AddEmployer, UpdateEmployer, DeleteEmployer, AddEmployee, UpdateEmployee, DeleteEmployee
from methods import is_employer_added_to_db, is_employee_added_to_db


class TestEmployer:
    """test for adding employer"""
    def test_add_employer_valid_data(self):
        body = EmployerData.valid_creation_data()
        response = AddEmployer().add_employer(body=body, schema=valid_schema)

        assert response.status_code == 200
        assert response.response_data.get("Message")
        assert is_employer_added_to_db(body)

    def test_add_employer_already_exist(self):
        body = EmployerData.already_exist()
        response = AddEmployer().add_employer(body=body, schema=invalid_schema)

        assert response.status_code == 400
        assert response.response_data.get("error")

    def test_add_employer_empty_data(self):
        body = EmployerData.empty_data()
        response = AddEmployer().add_employer(body=body, schema=invalid_schema)

        assert response.status_code == 400
        assert response.response_data.get("error")

    def test_add_employer_invalid_name(self):
        body = EmployerData.invalid_name()
        response = AddEmployer().add_employer(body=body, schema=invalid_schema)

        assert response.status_code == 400
        assert response.response_data.get("error")

    def test_add_employer_invalid_lastname(self):
        body = EmployerData.invalid_lastname()
        response = AddEmployer().add_employer(body=body, schema=invalid_schema)

        assert response.status_code == 400
        assert response.response_data.get("error")

    def test_add_employer_invalid_email(self):
        body = EmployerData.invalid_email()
        response = AddEmployer().add_employer(body=body, schema=invalid_schema)

        assert response.status_code == 400
        assert response.response_data.get("error")

    def test_add_employer_invalid_name_symbol(self):
        body = EmployerData.invalid_name_symbols()
        response = AddEmployer().add_employer(body=body, schema=invalid_schema)

        assert response.status_code == 400
        assert response.response_data.get("error")

    def test_add_employer_invalid_lastname_symbol(self):
        body = EmployerData.invalid_lastname_symbols()
        response = AddEmployer().add_employer(body=body, schema=invalid_schema)

        assert response.status_code == 400
        assert response.response_data.get("error")

    """test for updating employer"""
    def test_update_employer_valid_data(self):
        body = EmployerData.valid_update_data()
        response = UpdateEmployer().update_employer(body=body, schema=valid_schema)

        assert response.status_code == 200
        assert response.response_data.get("email") == "woodmaria@example.com"

    def test_update_employer_empty_data(self):
        body = EmployerData.empty_employer_data()
        response = UpdateEmployer().update_employer(body=body, schema=invalid_schema)

        assert response.status_code == 400
        assert response.response_data.get("error")

    def test_update_employer_invalid_name(self):
        body = EmployerData.invalid_update_name()
        response = UpdateEmployer().update_employer(body=body, schema=invalid_schema)

        assert response.status_code == 400
        assert response.response_data.get("error")

    def test_update_employer_invalid_lastname(self):
        body = EmployerData.invalid_update_lastname()
        response = UpdateEmployer().update_employer(body=body, schema=invalid_schema)

        assert response.status_code == 400
        assert response.response_data.get("error")

    def test_update_employer_invalid_name_symbol(self):
        body = EmployerData.invalid_update_name_symbols()
        response = UpdateEmployer().update_employer(body=body, schema=invalid_schema)

        assert response.status_code == 400
        assert response.response_data.get("error")

    def test_update_employer_invalid_lastname_symbol(self):
        body = EmployerData.invalid_update_lastname_symbols()
        response = UpdateEmployer().update_employer(body=body, schema=invalid_schema)

        assert response.status_code == 400
        assert response.response_data.get("error")

    """test for deleting employer"""
    def test_delete_employer_valid_data(self):
        body = EmployerData.valid_creation_data()
        response = AddEmployer().add_employer(body=body, schema=valid_schema)

        assert response.status_code == 200
        assert response.response_data.get("Message")

        response2 = DeleteEmployer().delete_employer(email=body["email"], schema=valid_schema)

        assert response2.status_code == 200
        assert response.response_data.get("Message")

    def test_delete_employer_invalid_data(self):

        email = "dontexist@dontexist.dontexist"
        response = DeleteEmployer().delete_employer(email=email, schema=valid_schema)

        assert response.status_code == 400
        assert response.response_data.get("error")


class TestEmployee:
    """test for adding employee"""

    def test_add_employee_valid_data(self):
        body = EmployeeData.valid_creation_data()
        response = AddEmployee().add_employee(body=body, schema=valid_schema)

        assert response.status_code == 200
        assert response.response_data.get("Message")
        assert is_employee_added_to_db(body)

    def test_add_employee_empty_data(self):
        body = EmployeeData.empty_creation_data()
        response = AddEmployee().add_employee(body=body, schema=valid_schema)

        assert response.status_code == 400
        assert response.response_data.get("error")

    def test_add_employee_invalid_name(self):
        body = EmployeeData.invalid_name_creation_data()
        response = AddEmployee().add_employee(body=body, schema=valid_schema)

        assert response.status_code == 400
        assert response.response_data.get("error")

    def test_add_employee_invalid_lastname(self):
        body = EmployeeData.invalid_lastname_creation_data()
        response = AddEmployee().add_employee(body=body, schema=valid_schema)

        assert response.status_code == 400
        assert response.response_data.get("error")

    def test_add_employee_invalid_email(self):
        body = EmployeeData.invalid_email_creation_data()
        response = AddEmployee().add_employee(body=body, schema=valid_schema)

        assert response.status_code == 400
        assert response.response_data.get("error")

    def test_add_employee_invalid_employer_id(self):
        body = EmployeeData.invalid_employer_id_creation_data()
        response = AddEmployee().add_employee(body=body, schema=valid_schema)

        assert response.status_code == 400
        assert response.response_data.get("error")

    def test_add_employee_already_exist(self):
        body = EmployeeData.already_exist_creation_data()
        response = AddEmployee().add_employee(body=body, schema=valid_schema)

        assert response.status_code == 400
        assert response.response_data.get("error")

    def test_add_employee_invalid_name_symbols(self):
        body = EmployeeData.invalid_name_symbols_data()
        response = AddEmployee().add_employee(body=body, schema=valid_schema)

        assert response.status_code == 400
        assert response.response_data.get("error")

    def test_add_employee_invalid_lastname_symbols(self):
        body = EmployeeData.invalid_lastname_symbols_data()
        response = AddEmployee().add_employee(body=body, schema=valid_schema)

        assert response.status_code == 400
        assert response.response_data.get("error")

    """test for updating employee"""

    def test_update_employee_valid_data(self):
        body = EmployeeData.valid_update_data()
        response = UpdateEmployee().update_employee(body=body, schema=valid_schema)

        assert response.status_code == 200
        assert response.response_data.get("email") == "olegarch@gmail.com"

    def test_update_employee_empty_data(self):
        body = EmployeeData.empty_update_data()
        response = UpdateEmployee().update_employee(body=body, schema=invalid_schema)

        assert response.status_code == 400
        assert response.response_data.get("error")

    def test_update_employee_invalid_name(self):
        body = EmployeeData.invalid_name_update_data()
        response = UpdateEmployee().update_employee(body=body, schema=invalid_schema)

        assert response.status_code == 400
        assert response.response_data.get("error")

    def test_update_employee_invalid_lastname(self):
        body = EmployeeData.invalid_lastname_update_data()
        response = UpdateEmployee().update_employee(body=body, schema=invalid_schema)

        assert response.status_code == 400
        assert response.response_data.get("error")

    def test_update_employee_invalid_employer_id(self):
        body = EmployeeData.invalid_employer_id_update_data()
        response = UpdateEmployee().update_employee(body=body, schema=invalid_schema)

        assert response.status_code == 400
        assert response.response_data.get("error")

    def test_update_employee_already_exist(self):
        body = EmployeeData.already_exist_update_data()
        response = UpdateEmployee().update_employee(body=body, schema=invalid_schema)

        assert response.status_code == 400
        assert response.response_data.get("error")

    def test_update_employee_invalid_name_symbols(self):
        body = EmployeeData.invalid_name_symbols_update_data()
        response = UpdateEmployee().update_employee(body=body, schema=invalid_schema)

        assert response.status_code == 400
        assert response.response_data.get("error")

    def test_update_employee_invalid_lastname_symbols(self):
        body = EmployeeData.invalid_lastname_symbols_update_data()
        response = UpdateEmployee().update_employee(body=body, schema=invalid_schema)

        assert response.status_code == 400
        assert response.response_data.get("error")

    """test for deleting employee"""

    def test_delete_employee_valid_data(self):
        body = EmployeeData.valid_creation_data()
        response = AddEmployee().add_employee(body=body, schema=valid_schema)

        assert response.status_code == 200
        assert response.response_data.get("Message")

        response2 = DeleteEmployee().delete_employee(email=body["email"], schema=valid_schema)

        assert response2.status_code == 200
        assert response.response_data.get("Message")

    def test_delete_employee_invalid_data(self):

        email = "dontexist@dontexist.dontexist"
        response = DeleteEmployee().delete_employee(email=email, schema=valid_schema)

        assert response.status_code == 400
        assert response.response_data.get("error")



