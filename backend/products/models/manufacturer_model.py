from django.db import models


class Manufacturer(models.Model):

    manufacturer_name = models.CharField(max_length=50, unique=True, verbose_name="name")
    location = models.CharField(max_length=30)

    def __str__(self):
        return self.manufacturer_name

    