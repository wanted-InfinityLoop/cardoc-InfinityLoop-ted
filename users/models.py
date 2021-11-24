from django.db import models


class User(models.Model):
    id = models.CharField(max_length=32, unique=True, primary_key=True)
    password = models.CharField(max_length=128)
    tires = models.ManyToManyField("cars.Tire", through="CarOwner")

    class Meta:
        db_table = "users"


class CarOwner(models.Model):
    model_name = models.CharField(max_length=32)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tire = models.ForeignKey("cars.Tire", on_delete=models.CASCADE)

    class Meta:
        db_table = "cars_owners"
