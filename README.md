# EPAM_PROJECT
<a href='https://coveralls.io/github/RomanOstrovskyi/EPAM_PROJECT?branch=travis_ci'><img src='https://coveralls.io/repos/github/RomanOstrovskyi/EPAM_PROJECT/badge.svg?branch=travis_ci' alt='Coverage Status' /></a>
[![Flask](https://img.shields.io/badge/flask-blue.svg)](https://flask.palletsprojects.com/)
[![MySQL](https://img.shields.io/badge/mysql-blue.svg)](https://www.mysql.com/)
[![Pylint](https://img.shields.io/badge/pylint-blue.svg)](https://www.pylint.org/)

This is  **Flask-based** application, created for companies that need to track all **employer**s and **employees**! 

## Instalation
**To run the application locally, follow these steps:**
1. Clone github repository:
```
> git clone https://github.com/RomanOstrovskyi/EPAM_PROJECT.git
```
2. Create a virtual environment:
  ```
  > cd EPAM_PROJECT
  > python3 -m venv venv:
  ```
3. Activate virtual environment:
  ```
  > source venv/bin/activate
  ```
4. Install the required dependencies:
  ```
  > pip install -r requirements.txt
  ```
5. Set up the database:

  **First of all, configure confige.py file:**
  ```
  1 SERVER = 'Enter your value'(str)
  2 PORT = Enter your value(int)
  3 USERNAME = 'Enter your value'(str)
  4 PASSWORD = 'Enter your value'(str)
  5 DB = 'Enter your value'(str)
  6 SECRET_KEY = 'Enter your value'(str)
  ```
  **Secondly, run following file to create tables in your database(Migration):**
  ```
  >python epam_project/migrations/my_migration.py
  ```
6. Start application:
  ```
  > python main.py
  ```
  You can also run Python WSGI HTTP Server Gunicorn, for this run the following command:
  ```
  > gunicorn <name of the Python file containing your Flask application>:main
  ```
  
## Usage
To use the application, open a web browser and navigate to http://localhost:5000. To get data or create a new employer, use the following links:
 1. http://localhost:5000/get_all_employers - if you want to retrieve all employers from a database.
 2. http://localhost:5000/add_employer - if you want to add new employer to a database.
 3. http://localhost:5000/delete_employer - if you want to delete an employer from a database.
 
There are only examples of how to use this application, you can find the rest of the links in the documentation folder

## Contributing
Contributions to the EPAM_PROJECT repository are welcome! To contribute, please follow these steps:

  1.Fork the repository.
  
  2.Create a new branch for your changes:
  ```
  >git checkout -b my-new-feature
  ```
  3.Make your changes and commit them:
  ```
  >git commit -am 'Add some feature'
  ```
  4.Push your changes to your fork:
  ```
  >git push origin my-new-feature
  ```
  5.Create a new pull request on the main repository
  
## Credits
**This project was created by [Roman Ostrovskyi](https://github.com/RomanOstrovskyi) as part of the EPAM Python Course.**




