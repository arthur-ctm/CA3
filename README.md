# CA3

I am using the same project as CA1 (this is way it is the same djangoproject name), I just added the accounts sytsmen. This is a simple web application built with Django that allows users to perform CRUD (Create, Read, Update, Delete) operations on a database of drivers and cars with an account system. In CA3 I added some tests.

# Tests 

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

  
# Security 

  I added `` < meta http-equiv= "X-XSS-Protection" content="1 ; mode=block" > `` in my base.html file

 
