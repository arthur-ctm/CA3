from django import forms

from .models import Car
from .models import Driver


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = '__all__'
