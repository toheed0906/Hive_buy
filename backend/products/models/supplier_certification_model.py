from django.db import models


class SupplierCertification(models.Model):
    certification_name = models.CharField(max_length= 50, unique= True)

    def __str__(self):
        return self.certification_name

   