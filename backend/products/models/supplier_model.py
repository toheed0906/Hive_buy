from django.db import models
from .supplier_certification_model import SupplierCertification


class Supplier(models.Model):

    supplier_name = models.CharField( max_length = 50 , verbose_name = "name")
    rating = models.PositiveIntegerField( default = 0 )
    certifications = models.ManyToManyField( SupplierCertification , blank = True )

    def __str__(self):
        return self.supplier_name