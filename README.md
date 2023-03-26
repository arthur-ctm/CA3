# CA3

I am using the same project as CA1 (this is way it is the same djangoproject name), I just added the accounts sytsmen. This is a simple web application built with Django that allows users to perform CRUD (Create, Read, Update, Delete) operations on a database of drivers and cars with an account system. In CA3 I added some tests.

# Developing process 

Create login, sign-in, logout, and change password views: Create views for login, sign-in, logout, and change password operations in the app's views.py file.

Define URL patterns for authentication views: Define URL patterns for the authentication views in the app's urls.py file.

Create templates for authentication views: Create HTML templates for the authentication views.

Add authentication middleware: Add authentication middleware to the project's settings.py file.

Add login and logout URLs to your navigation menu: Add links to the login and logout views in your app's navigation menu.

I didn't use the email sent system because it didn't work for me. If you want to change your password you have to go to your profile and click on "Change password".

# Purpose 

The purpose of the application would be to help manage and organize data related to F1 cars and drivers, making it easier for users to access and manipulate this information as needed. Allowing users to perform basic CRUD (Create, Read, Update, Delete) and create accounts, change password, signin, login, logout.


# Tests 



Files:

cars/tests.py

Contains tests for the Car and Driver models in the project.
The Car model tests ensure that the model can be created and deleted successfully, and that the correct data is saved to the database.
The Driver model tests ensure that the model can be created and deleted successfully, and that the correct data is saved to the database.

accounts/tests.py

Contains tests for the views in the project.
The tests ensure that the login, logout, signup, and change password views are working correctly.
The tests check that the correct templates are being used, and that the correct HTTP response codes are returned.
The tests also check that the views are redirecting to the correct URLs after successful completion.
The tests are conducted with valid and invalid form data to ensure that the views are robust to incorrect user input.
Dependencies:

Django
Django REST framework
Python
How to run the tests:

Ensure that all necessary dependencies are installed.
Navigate to the project directory in the command line.
Run the command "python manage.py test" to run all tests in the project.
To run individual tests, use the command "python manage.py test <app_name>.<test_file_name>.<TestCaseName>.<test_method_name>". For example, to run the test_model_creation test in test_models.py, use the command "python manage.py test cars.test_models.CarTestCase.test_model_creation".
