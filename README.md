# Catalystcounter
### This project implements a web application that allows users to upload large CSV files and filter the data, providing a count of matching records.

# Features
User authentication and registration.
Chunk-based file upload for large files (1GB+).
Database storage of uploaded data using Django default sqlite.
A user-friendly query builder for filtering data using various criteria.
API endpoint to return the count of records matching the applied filter.

# Technologies
**Django**: Framework for building the web application.

**Bootstrap**: Framework for styling the user interface.

**Django-all-auth**: For user authentication and registration.

**Django Rest Framework**: For creating the API endpoint.

# Installation
Install Python 3.6 or higher.

Clone the repository: git clone <repository URL>

Navigate to the project directory: cd catalyst-count

**Install dependencies:**
pip install Django==3.2.12  

pip install django-allauth==0.51.0  # for user authentication and registration

pip install django-crispy-forms==1.14.0  # for form rendering (optional)

pip install bootstrap4==1.1.2  # for Bootstrap 4 styling

pip install djangorestframework==3.13.1  

**Create superuser to see database using command**: python manage.py createsuperuser

DEBUG: Set to True for development mode, False for production.

ALLOWED_HOSTS: A list of allowed hostnames.


**Create the database**: python manage.py makemigrations python manage.py migrate

**Run the server**: python manage.py runserver

# Usage
Open the application in your web browser.
Log in or register a new account.
Upload a CSV file using the upload data page.
Use the query builder to filter the data.
View the count of matching records.

# Contributing
Contributions are welcome! Please submit a pull request with your changes.

