from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=32)
    name_eng = models.CharField(max_length=32, blank=True, default="")
    country = models.CharField(max_length=16, blank=True, default="")
    website_url = models.URLField()

    class Meta:
        db_table = "brands"


class Model(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        db_table = "models"


class Trim(models.Model):
    name = models.CharField(max_length=32)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)

    class Meta:
        db_table = "trims"


class SpecType(models.Model):
    class Type(models.IntegerChoices):
        FUEL = 1
        DIMENSION = 2
        ENGINE = 3
        DRIVING = 4

    name = models.CharField(max_length=32)

    class Meta:
        db_table = "spec_types"


class SpecInfo(models.Model):
    spec_type = models.ForeignKey(SpecType, on_delete=models.PROTECT)
    trim = models.ForeignKey(Trim, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    name_eng = models.CharField(max_length=32)
    value = models.CharField(max_length=32)
    unit = models.CharField(max_length=16, blank=True, default="")
    multi_values = models.CharField(max_length=32, blank=True, default="")

    class Meta:
        db_table = "spec_infos"
