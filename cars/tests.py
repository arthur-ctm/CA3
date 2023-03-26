from django.test import TestCase

# Create your tests here.


from django.test import TestCase
from .models import Car, Driver


class CarTestCase(TestCase):
    def setUp(self):
        # Set up any test data you need here
        driver = Driver.objects.create(number=22, last_name='Deep', first_name='Johnny', age=34)
        Car.objects.create(safety=8, colour='red', aero=9, team='Redbull', horses=990, driver=driver)

    def test_model_creation(self):
        # Test that a model was created successfully
        obj = Car.objects.get(team='Redbull')
        self.assertEqual(obj.aero, 9)

    def test_model_deletion(self):
        # Test that a model can be deleted successfully
        obj = Car.objects.get(team='Redbull')
        obj.delete()
        self.assertRaises(Car.DoesNotExist,Car.objects.get, team='Redbull')


class DriverTestCase(TestCase):
    def setUp(self):
        # Set up any test data here
        Driver.objects.create(number=16, last_name='Leclerc', first_name='Charles', age=23)


    def test_model_creation(self):
        # Test that a model was created successfully
        obj = Driver.objects.get(last_name='Leclerc')
        self.assertEqual(obj.number, 16)

    def test_model_deletion(self):
        # Test that a model can be deleted successfully
        obj = Driver.objects.get(last_name='Leclerc')
        obj.delete()
        self.assertRaises(Driver.DoesNotExist, Driver.objects.get, last_name='Leclerc')
