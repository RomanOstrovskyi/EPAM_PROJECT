""" File responsible for adding testing data to database """
from datetime import datetime
import os
import sys
script_dir = os.path.dirname(os.path.abspath(__file__))

connection_path = os.path.join(script_dir, '..', '..', 'connection.py')
sys.path.append(os.path.dirname(connection_path))
from connection import session

models_path = os.path.join(script_dir, '..', 'models', 'models.py')
sys.path.append(os.path.dirname(models_path))
from epam_project.models.models import Employer, Employee

DATE_STR = '2003-11-26'
DATE_OBJ = datetime.strptime(DATE_STR, '%Y-%m-%d')


def add_employers():
    """ This methods adds three employers to database """

    if session.query(Employer).filter(Employer.email == "woodmaria@example.com").count():
        pass
    else:
        name = "Maria"
        lastname = "Woods"
        email = "woodmaria@example.com"
        date_of_birth = DATE_OBJ

        employer = Employer(name=name, lastname=lastname, email=email, date_of_birth=date_of_birth)

        session.add(employer)
        session.commit()

    if session.query(Employer).filter(Employer.email == "romaostrovskiy616@gmail.com").count():
        pass
    else:
        name = "Roman"
        lastname = "Ostrovskyi"
        email = "romaostrovskiy616@gmail.com"
        date_of_birth = DATE_OBJ

        employer = Employer(name=name, lastname=lastname, email=email, date_of_birth=date_of_birth)

        session.add(employer)
        session.commit()

    if session.query(Employer).filter(Employer.email == "vbartkiv@gmail.com").count():
        pass
    else:
        name = "Valeriy"
        lastname = "Bartkiv"
        email = "vbartkiv@gmail.com"
        date_of_birth = DATE_OBJ

        employer = Employer(name=name, lastname=lastname, email=email, date_of_birth=date_of_birth)

        session.add(employer)
        session.commit()

    return True


def add_employees():
    """ This methods adds three employees to database """

    if session.query(Employee).filter(Employee.email == "Ivantsiv@gmail.com1").count():
        pass
    else:
        name = "Ivan"
        lastname = "Ivantsiv"
        email = "Ivantsiv@gmail.com1"
        date_of_birth = DATE_OBJ

        employee = Employee(name=name, lastname=lastname, email=email, date_of_birth=date_of_birth, employer_id=3)

        session.add(employee)
        session.commit()

    if session.query(Employee).filter(Employee.email == "GigaChad@gmail.com").count():
        pass
    else:
        name = "Giga"
        lastname = "Chad"
        email = "GigaChad@gmail.com"
        date_of_birth = DATE_OBJ

        employee = Employee(name=name, lastname=lastname, email=email, date_of_birth=date_of_birth, employer_id=3)

        session.add(employee)
        session.commit()

    if session.query(Employee).filter(Employee.email == "olegarch@gmail.com").count():
        pass
    else:
        name = "Oleg"
        lastname = "Olegarch"
        email = "olegarch@gmail.com"
        date_of_birth = DATE_OBJ

        employee = Employee(name=name, lastname=lastname, email=email, date_of_birth=date_of_birth, employer_id=3)

        session.add(employee)
        session.commit()

    return True


print(add_employers())
print(add_employees())
