from flask import Blueprint, request, jsonify
from connection import session
from epam_project.models.models import Employer, Employee
from epam_project.service.services import create_employer_sv, update_employer_sv, create_employee_sv, update_employee_sv

endpoints = Blueprint('endpoints', __name__)


@endpoints.route('/info', methods=['GET'])
def info():
    return jsonify({"Message": "This is Epam project!"})


""" Endpoints for employer"""


@endpoints.route('/add_employer/', methods=['POST'])
def add_employer():
    args = request.args

    if len(args) == 0:
        raise Exception("Arguments is empty!")

    employer = create_employer_sv(args)

    if session.query(Employer).filter(Employer.email == f'{employer.email}').count():
        raise Exception("Employer with this email already exist.")

    if session.query(Employee).filter(Employee.email == f'{employer.email}').count():
        raise Exception("If you are an employee, you can't be an employer simultaneously.")

    session.add(employer)
    session.commit()

    return jsonify({"Message": "Employer successfully created!"}), 200


@endpoints.route('/get_all_employers', methods=['GET'])
def get_all_employers():

    result = []

    employers = session.query(Employer).all()

    if not employers:
        return {"Message": 'There are no employers.'}, 200

    for employer in employers:
        employer = employer.__dict__
        del employer['_sa_instance_state']
        result.append(employer)

    return jsonify(result)


@endpoints.route('/get_employer_by_email/<string:email>', methods=['GET'])
def get_employer_by_email(email):

    if len(email) == 0:
        raise Exception("You didnt enter an email address!")

    employer = (session.query(Employer).filter_by(email=email).first())

    if not employer:
        return {"Message": 'There is no employer with this email address.'}, 200

    employer = employer.__dict__
    del employer['_sa_instance_state']

    return jsonify(employer)


@endpoints.route('/update_employer/<string:email>', methods=['PUT'])
def update_employer(email):

    employer = session.query(Employer).filter_by(email=email).first()
    if not employer:
        raise Exception("There is no employer with such email address!")

    data = request.json

    update_employer_sv(data, employer)

    session.commit()

    employer = session.query(Employer).filter_by(email=email).first()
    employer = employer.__dict__
    del employer['_sa_instance_state']

    return jsonify(employer)


@endpoints.route('/delete_employer/<string:email>', methods=['DELETE'])
def delete_employer(email):

    employer = session.query(Employer).filter_by(email=email).first()
    if not employer:
        raise Exception("There is no employer with such email address!")

    session.delete(employer)
    session.commit()

    return jsonify("The employer has been successfully deleted!")


""" Endpoints for employee"""


@endpoints.route('/add_employee', methods=['POST'])
def add_employee():

    args = request.args

    if len(args) == 0:
        raise Exception("Arguments is empty!")

    employee = create_employee_sv(args)

    if session.query(Employee).filter(Employee.email == f'{employee.email}').count():
        raise Exception("Employee with this email already exist.")

    if session.query(Employer).filter(Employer.email == f'{employee.email}').count():
        raise Exception("If you are an employer, you can't be an employee simultaneously.")

    session.add(employee)
    session.commit()

    return jsonify({"Message": "Employee successfully created!"}), 200


@endpoints.route('/get_all_employees', methods=['GET'])
def get_all_employees():

    result = []

    employees = session.query(Employee).all()

    if not employees:
        return {"Message": 'There are no employees.'}, 200

    for employee in employees:
        employee = employee.__dict__
        del employee['_sa_instance_state']
        result.append(employee)

    return jsonify(result)


@endpoints.route('/get_employees_by_employer_id/<string:id>', methods=['GET'])
def get_employees_by_employer_id(id):

    result = []

    employees = session.query(Employee).filter(Employee.employer_id == id).all()

    if not employees:
        return {"Message": 'There are no employees by that employer id.'}, 200

    for employee in employees:
        employee = employee.__dict__
        del employee['_sa_instance_state']
        result.append(employee)

    return jsonify(result)


@endpoints.route('/update_employee/<string:email>', methods=['PUT'])
def update_employee(email):

    employee = session.query(Employee).filter_by(email=email).first()

    if not employee:
        raise Exception("There is no employee with such email address!")

    data = request.json

    update_employee_sv(data, employee)

    session.commit()

    employee = session.query(Employee).filter_by(email=email).first()
    employee = employee.__dict__
    del employee['_sa_instance_state']

    return jsonify(employee)


@endpoints.route('/delete_employee/<string:email>', methods=['DELETE'])
def delete_employee(email):

    employee = session.query(Employee).filter_by(email=email).first()
    if not employee:
        raise Exception("There is no employer with such email address!")

    session.delete(employee)
    session.commit()

    return jsonify("The employee has been successfully deleted!")
