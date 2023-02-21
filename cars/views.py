# Import necessary models and forms
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import CarForm
from .models import Car
from .forms import DriverForm
from .models import Driver


# Define views for cars
def car_list(request):
    # Get all cars from the database
    cars = Car.objects.all()
    # Render the car list template with the cars retrieved from the database
    return render(request, 'car_list.html', {'cars': cars})


def car_detail(request, car_id):
    # Get the car with the given car_id or return a 404 error
    car = get_object_or_404(Car, pk=car_id)
    if request.method == 'POST':
        # If the request method is POST, create a form instance from the submitted data
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            # If the form is valid, save the car and redirect to the car detail page
            form.save()
            return HttpResponseRedirect(reverse('car_detail', args=[car.id]))
    else:
        # If the request method is GET, create a form instance from the car data
        form = CarForm(instance=car)
    # Render the car detail template with the car and form instances
    return render(request, 'car_detail.html', {'car': car, 'form': form})


def car_create(request):
    # Create a form instance from the submitted data or none
    form = CarForm(request.POST or None)
    if form.is_valid():
        # If the form is valid, save the car and redirect to the car list page
        form.save()
        return redirect('car_list')
    # Render the car form template with the form instance
    return render(request, 'car_form.html', {'form': form})


def car_update(request, car_id):
    # Get the car with the given car_id or return a 404 error
    car = get_object_or_404(Car, pk=car_id)
    if request.method == 'POST':
        # If the request method is POST, create a form instance from the submitted data
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            # If the form is valid, save the car and redirect to the car list page
            form.save()
            return redirect('car_list')
    else:
        # If the request method is GET, create a form instance from the car data
        form = CarForm(instance=car)
    # Render the car form template with the car and form instances
    return render(request, 'car_form.html', {'form': form, 'car': car})


def car_delete(request, car_id):
    # Get the car with the given car_id or return a 404 error
    car = get_object_or_404(Car, pk=car_id)
    if request.method == 'POST':
        # If the request method is POST, delete the car and redirect to the car list page
        car.delete()
        return redirect('car_list')
    # Render the car confirm delete template with the car instance
    return render(request, 'car_confirm_delete.html', {'car': car})


# Define views for drivers
def driver_list(request):
    # Get all drivers from the database
    drivers = Driver.objects.all()
    # Render the driver list template with the drivers retrieved from the database
    return render(request, 'driver_list.html', {'drivers': drivers})


def driver_detail(request, driver_id):
    # Get the Driver object with the given driver_id, or return a 404 page if it doesn't exist
    driver = get_object_or_404(Driver, id=driver_id)
    # Render the driver_detail.html template, passing in the driver object
    return render(request, 'driver_detail.html', {'driver': driver})


def driver_create(request):
    # Create a new DriverForm instance with the data in the POST request, or an empty form if there is no POST data
    form = DriverForm(request.POST or None)
    # If the form is valid, save the new driver object and redirect to the driver_list page
    if form.is_valid():
        form.save()
        return redirect('driver_list')
    # Render the driver_form.html template, passing in the form object
    return render(request, 'driver_form.html', {'form': form})


def driver_update(request, driver_id):
    # Get the Driver object with the given driver_id, or return a 404 page if it doesn't exist
    driver = get_object_or_404(Driver, id=driver_id)
    if request.method == 'POST':
        # Create a DriverForm instance with the data in the POST request and the existing driver object, or an empty form
        # with the driver data if there is no POST data
        form = DriverForm(request.POST or None, instance=driver)
        # If the form is valid, save the updated driver object and redirect to the driver_list page
        if form.is_valid():
            form.save()
            return redirect('driver_list')
    else:
        # If the request method is GET, create a form instance from the car data
        form = DriverForm(instance=driver)
    # Render the driver_form.html template, passing in the form and driver objects
    return render(request, 'driver_form.html', {'form': form, 'driver': driver})


def driver_delete(request, driver_id):
    # Get the Driver object with the given driver_id, or return a 404 page if it doesn't exist
    driver = get_object_or_404(Driver, id=driver_id)
    # Delete the driver object and redirect to the driver_list page
    driver.delete()
    return redirect('driver_list')
