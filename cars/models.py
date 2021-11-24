from django.db import models


class TirePosition(models.Model):
    class Type(models.IntegerChoices):
        FRONT = 1
        REAR = 2

    name = models.CharField(max_length=16)

    class Meta:
        db_table = "tire_positions"


class Tire(models.Model):
    tire_position = models.ForeignKey(TirePosition, on_delete=models.PROTECT)
    width = models.PositiveSmallIntegerField()
    aspect_ratio = models.PositiveSmallIntegerField()
    wheel_size = models.PositiveSmallIntegerField()

    class Meta:
        db_table = "tires"


class Car(models.Model):
    model_name = models.CharField(max_length=32)
    front_tire = models.ForeignKey("cars.Tire", on_delete=models.CASCADE, related_name="front_cars")
    rear_tire = models.ForeignKey("cars.Tire", on_delete=models.CASCADE, related_name="rear_cars")

    class Meta:
        db_table = "cars"
