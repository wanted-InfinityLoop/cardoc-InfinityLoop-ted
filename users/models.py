from django.db import models


class User(models.Model):
    id = models.CharField(max_length=32, unique=True, primary_key=True)
    password = models.CharField(max_length=128)
    cars = models.ManyToManyField("cars.Car", through="CarOwner")

    class Meta:
        db_table = "users"


class CarOwner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey("cars.Car", on_delete=models.CASCADE)

    class Meta:
        db_table = "cars_owners"
