from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Building(models.Model):
    landlord = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.PROTECT)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)

    def __str__(self):
        return self.address


class Unit(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    tenant = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.PROTECT)
    number = models.CharField(max_length=5)
    rooms = models.IntegerField(default=1)
    bathrooms = models.IntegerField(default=1)
    description = models.TextField()

    def __str__(self):
        return self.number
