"""view file, all endpoints related to employer and employee are located there"""
import requests
from flask import Blueprint, request, jsonify, render_template, redirect, url_for

endpoints_for_html = Blueprint('endpoints_for_html', __name__)


@endpoints_for_html.route('/info', methods=['GET'])
def info():
    """INFO endpoint"""
    return jsonify({"Message": "This is Epam project!"})


@endpoints_for_html.route('/get_all_employers', methods=['GET'])
def get_all_employers():
    """Endpoint responsible for retrieving all employers"""

    response = requests.get('http://127.0.0.1:5000/api/get_all_employers', timeout=30)

    if response.status_code == 200:
        employers = response.json()
        return render_template("employers.html", employers=employers)

    error_message = "Could not retrieve employers"
    return render_template('error.html', error_message=error_message)


@endpoints_for_html.route('/add_employer', methods=['GET', 'POST'])
def add_employer():
    """Endpoint responsible for adding employer"""
    if request.method == "POST":
        args = {
            'name': request.form['name'],
            'lastname': request.form['lastname'],
            'email': request.form['email'],
            'date_of_birth': request.form['date_of_birth']
        }

        name = args.get('name')
        lastname = args.get('lastname')
        email = args.get('email')
        date = args.get('date_of_birth')

        requests.post(f'http://127.0.0.1:5000/api/add_employer?name={name}&lastname={lastname}'
                      f'&email={email}&date_of_birth={date}', timeout=30)

        return redirect(url_for('endpoints_for_html.get_all_employers'))

    return render_template('add_employer.html')


@endpoints_for_html.route('/delete_employer', methods=['POST'])
def delete_employer():
    """Endpoint responsible for deleting employer"""

    email = request.form['email']

    response = requests.delete(f'http://127.0.0.1:5000/api/delete_employer/{email}', timeout=30)

    if response.status_code == 200:
        return redirect(url_for('endpoints_for_html.get_all_employers'))

    error_message = f"Could not delete employer with email = {email}"
    return render_template('error.html', error_message=error_message)


@endpoints_for_html.route('/get_employer_by_email', methods=['GET'])
def get_employer_by_email():
    """Endpoint responsible for getting employer by email address"""

    email = request.args.get("email")

    response = requests.get(f'http://127.0.0.1:5000/api/get_employer_by_email/{email}', timeout=30)

    if response.status_code == 200:
        employer = response.json()
        return render_template('employer.html', employer=employer)

    error_message = f"Could not retrieve employer with email {email}"
    return render_template('error.html', error_message=error_message)


@endpoints_for_html.route('/get_employer_by_date_of_birth', methods=['GET'])
def get_employer_by_date_of_birth():
    """Endpoint responsible for getting employer by email address"""

    date_of_birth = request.args.get("email")

    response = requests.get(f'http://127.0.0.1:5000/api/get_employer_by_date_of_birth/{date_of_birth}', timeout=30)

    if response.status_code == 200:
        employers = response.json()
        return render_template("employers.html", employers=employers)

    error_message = f"Could not retrieve employer with date of birth {date_of_birth}"
    return render_template('error.html', error_message=error_message)


@endpoints_for_html.route('/update_employer/<string:email>', methods=['GET'])
def update_employer(email):
    """Endpoint responsible for updating employer data by email address"""

    employer = requests.get(f'http://127.0.0.1:5000/api/get_employer_by_email/{email}', timeout=30)
    if employer is None:
        return render_template('error.html', message="Employer not found"), 404

    return render_template('update_employer.html', employer=employer, email=email)


@endpoints_for_html.route('/update_employer/<string:email>', methods=['POST'])
def update_employer_post(email):
    """Endpoint responsible for updating employer data by email address"""
    name = request.form.get('name')
    lastname = request.form.get('lastname')
    new_email = request.form.get('email')

    employer_data = {
        'name': name,
        'lastname': lastname,
        'email': new_email
    }

    response = requests.put(f'http://127.0.0.1:5000/api/update_employer/{email}', json=employer_data, timeout=30)

    if response.status_code == 200:
        if new_email:
            return redirect(url_for('endpoints_for_html.get_employer_by_email', email=new_email))
        return redirect(url_for('endpoints_for_html.get_employer_by_email', email=email))

    return render_template('error.html', message="Could not update employer"), response.status_code


# employees
@endpoints_for_html.route('/get_all_employees', methods=['GET'])
def get_all_employees():
    """Endpoint responsible for retrieving all employees"""

    response = requests.get('http://127.0.0.1:5000/api/get_all_employees', timeout=30)

    if response.status_code == 200:
        employees = response.json()
        return render_template("employees.html", employees=employees)

    return render_template('error.html', message="Could not get employees"), response.status_code


@endpoints_for_html.route('/get_employees_by_employer_id', methods=['GET'])
def get_employees_by_employer_id():
    """Endpoint responsible for retrieving all employees by their employer id"""

    employer_id = request.args.get("id")

    response = requests.get(f'http://127.0.0.1:5000/api/get_employees_by_employer_id/{employer_id}', timeout=30)

    if response.status_code == 200:
        employees = response.json()
        return render_template("employer_employees.html", employees=employees)

    error_message = f"Could not retrieve employees with employer_id = {employer_id}"
    return render_template('error.html', error_message=error_message)


@endpoints_for_html.route('/delete_employee', methods=['POST'])
def delete_employee():
    """Endpoint responsible for deleting employee"""

    email = request.form["email"]

    response = requests.delete(f'http://127.0.0.1:5000/api/delete_employee/{email}', timeout=30)

    if response.status_code == 200:
        return redirect(url_for('endpoints_for_html.get_all_employees'))

    error_message = f"Could not delete employee with email = {email}"
    return render_template('error.html', error_message=error_message)


@endpoints_for_html.route('/get_employee_by_email', methods=['GET'])
def get_employee_by_email():
    """Endpoint responsible for getting employee by email address"""

    email = request.args.get("email")

    response = requests.get(f'http://127.0.0.1:5000/api/get_employee_by_email/{email}', timeout=30)

    if response.status_code == 200:
        employee = response.json()
        return render_template('employee.html', employee=employee)

    error_message = f"Could not retrieve employee with email {email}"
    return render_template('error.html', error_message=error_message)


@endpoints_for_html.route('/get_employee_by_date_of_birth', methods=['GET'])
def get_employee_by_date_of_birth():
    """Endpoint responsible for getting employee by email address"""

    date_of_birth = request.args.get("email")

    response = requests.get(f'http://127.0.0.1:5000/api/get_employee_by_date_of_birth/{date_of_birth}', timeout=30)

    if response.status_code == 200:
        employees = response.json()
        return render_template("employees.html", employees=employees)

    error_message = f"Could not retrieve employer with date of birth {date_of_birth}"
    return render_template('error.html', error_message=error_message)


@endpoints_for_html.route('/add_employee', methods=['GET', 'POST'])
def add_employee():
    """Endpoint responsible for adding employee"""
    if request.method == "POST":
        args = {
            'name': request.form['name'],
            'lastname': request.form['lastname'],
            'email': request.form['email'],
            'date_of_birth': request.form['date_of_birth'],
            'employer_id': request.form['employer_id'],
        }

        name = args.get('name')
        lastname = args.get('lastname')
        email = args.get('email')
        date = args.get('date_of_birth')
        employer_id = args.get('employer_id')

        response = requests.post(f'http://127.0.0.1:5000/api/add_employee?name={name}&lastname={lastname}'
                                 f'&email={email}&date_of_birth={date}&employer_id={employer_id}', timeout=30)

        if response.status_code == 200:
            redirect(url_for('endpoints_for_html.get_all_employees'))
        else:
            error_message = f"Could not add employee with employer id = {employer_id}"
            return render_template('error.html', error_message=error_message)

    return render_template('add_employee.html')


@endpoints_for_html.route('/update_employee/<string:email>', methods=['GET'])
def update_employee(email):
    """Endpoint responsible for updating employee data by email address"""

    employee = requests.get(f'http://127.0.0.1:5000/api/get_employee_by_email/{email}', timeout=30)
    if employee is None:
        return render_template('error.html', message="Employee not found"), 404

    return render_template('update_employee.html', employee=employee, email=email)


@endpoints_for_html.route('/update_employee/<string:email>', methods=['POST'])
def update_employee_post(email):
    """Endpoint responsible for updating employee data by email address"""
    name = request.form.get('name')
    lastname = request.form.get('lastname')
    new_email = request.form.get('email')
    employer_id = request.form.get('employer_id')

    employee_data = {
        'name': name,
        'lastname': lastname,
        'email': new_email,
        'employer_id': employer_id,
    }

    response = requests.put(f'http://127.0.0.1:5000/api/update_employee/{email}', json=employee_data, timeout=30)

    if response.status_code == 200:
        if new_email:
            return redirect(url_for('endpoints_for_html.get_employee_by_email', email=new_email))
        return redirect(url_for('endpoints_for_html.get_employee_by_email', email=email))

    return render_template('error.html', message="Could not update employee"), response.status_code
