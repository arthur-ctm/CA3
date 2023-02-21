from django.db import models


class Driver(models.Model):
    number = models.IntegerField();
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name +" "+ self.last_name+" " + str(self.number)


class Car(models.Model):
    team = models.CharField(max_length=200)
    colour = models.CharField(max_length=200)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    horses = models.IntegerField()
    aero = models.IntegerField()
    safety = models.IntegerField()

    def __str__(self):
        return self.team

