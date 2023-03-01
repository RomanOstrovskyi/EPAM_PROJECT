""" This file contains additional methods for endpoints"""
from epam_project.models.models import Employer, Employee
from epam_project.service.validation import validate

""" This method is necessary to create an employer"""
def create_employer_sv(data):
    name = data.get("name").capitalize()
    lastname = data.get("lastname").capitalize()
    email = data.get("email")
    date_of_birth = data.get("date_of_birth")

    validate(name, lastname, email)

    employer = Employer(name=name, lastname=lastname, email=email, date_of_birth=date_of_birth)

    return employer


""" This method is necessary to update an employer"""
def update_employer_sv(data, employer):
    new_name = data.get('name').capitalize()
    new_lastname = data.get('lastname').capitalize()
    new_email = data.get('email')

    validate(new_name, new_lastname, new_email)

    if new_name:
        employer.name = new_name
    if new_lastname:
        employer.lastname = new_lastname
    if new_email:
        employer.email = new_email


""" This method is necessary to create an employee"""
def create_employee_sv(data):
    name = data.get("name").capitalize()
    lastname = data.get("lastname").capitalize()
    email = data.get("email")
    date_of_birth = data.get("date_of_birth")
    employer_id = data.get("employer_id")

    validate(name, lastname, email)

    employee = Employee(name=name, lastname=lastname, email=email, date_of_birth=date_of_birth, employer_id=employer_id)

    return employee


""" This method is necessary to update an employee"""
def update_employee_sv(data, employee):
    new_name = data.get('name').capitalize()
    new_lastname = data.get('lastname').capitalize()
    new_email = data.get('email')
    new_employer_id = data.get('employer_id')

    validate(new_name, new_lastname, new_email)

    if new_name:
        employee.name = new_name
    if new_lastname:
        employee.lastname = new_lastname
    if new_email:
        employee.email = new_email
    if new_employer_id:
        employee.employer_id = new_employer_id
