"""tests for all endpoint in rest.view.py"""
from tests.test_endpoints.schemas.schemas import valid_schema, invalid_schema, valid_get_schema,\
    valid_get_by_email_date_of_birth_schema
from tests.test_endpoints.models import EmployerData, EmployeeData
from .methods import AddEmployer, GetEmployer, UpdateEmployer, DeleteEmployer, AddEmployee,\
    UpdateEmployee, DeleteEmployee, GetEmployee
from .methods import is_employer_added_to_db
import epam_project.rest.view


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

    """test for getting employer/employers"""
    def test_get_all_employers(self):
        response = GetEmployer().get_employers(schema=valid_get_schema)

        assert response.status_code == 200

    def test_get_employer_by_email(self):
        email = "romaostrovskiy616@gmail.com"
        response = GetEmployer().get_employer_by_email(email=email, schema=valid_get_by_email_date_of_birth_schema)

        assert response.status_code == 200
        assert response.response_data.get("email") == email

    def test_get_employer_by_non_existent_email(self):
        email = "non-existent@gmail.com"
        response = GetEmployer().get_employer_by_email(email=email, schema=invalid_schema)

        assert response.status_code == 404
        assert response.response_data.get("Message")

    def test_get_employer_by_date_of_birth(self):
        date_of_birth = "2003-11-26"
        response = GetEmployer().get_employer_by_date_of_birth(date_of_birth=date_of_birth, schema=valid_get_schema)

        assert response.status_code == 200

    def test_get_employer_by_date_of_birth_dont_exist(self):
        date_of_birth = "2004-11-27"
        response = GetEmployer().get_employer_by_date_of_birth(date_of_birth=date_of_birth, schema=invalid_schema)

        assert response.status_code == 404
        assert response.response_data.get("message")

    def test_get_employer_by_date_of_birth_invalid_format(self):
        date_of_birth = "2004-11-272"
        response = GetEmployer().get_employer_by_date_of_birth(date_of_birth=date_of_birth, schema=invalid_schema)

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

    """test for getting employee/employees"""
    def test_get_all_employees(self):
        response = GetEmployee().get_employees(schema=valid_get_schema)

        assert response.status_code == 200

    def test_get_employee_by_email(self):
        email = "Ivantsiv@gmail.com1"
        response = GetEmployee().get_employee_by_email(email=email, schema=valid_get_by_email_date_of_birth_schema)

        assert response.status_code == 200
        assert response.response_data.get("email") == email

    def test_get_employee_by_non_existent_email(self):
        email = "non-existent@gmail.com"
        response = GetEmployee().get_employee_by_email(email=email, schema=invalid_schema)

        assert response.status_code == 404
        assert response.response_data.get("Message")

    def test_get_employee_by_date_of_birth(self):
        date_of_birth = "2003-11-26"
        response = GetEmployee().get_employee_by_date_of_birth(date_of_birth=date_of_birth, schema=valid_get_schema)

        assert response.status_code == 200

    def test_get_employee_by_date_of_birth_dont_exist(self):
        date_of_birth = "2004-11-27"
        response = GetEmployee().get_employee_by_date_of_birth(date_of_birth=date_of_birth, schema=invalid_schema)

        assert response.status_code == 404
        assert response.response_data.get("message")

    def test_get_employee_by_date_of_birth_invalid_format(self):
        date_of_birth = "2004-11-272"
        response = GetEmployee().get_employee_by_date_of_birth(date_of_birth=date_of_birth, schema=invalid_schema)

        assert response.status_code == 400
        assert response.response_data.get("error")

    def test_get_employee_by_employer_id(self):
        employer_id = 3
        response = GetEmployee().get_employee_by_employer_id(employer_id=employer_id, schema=valid_get_schema)

        assert response.status_code == 200

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



