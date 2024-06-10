from django.db import models
from .manufacturer_model import Manufacturer
from .product_certification_model import ProductCertification
from .supplier_model import Supplier
from .sub_category_model import SubCategory
from time import timezone
from django.contrib.postgres.fields import ArrayField


UNIT_TYPE_CHOICES=[
    ("Set", "Set"),
    ("Piece", "Piece"),
    ("Box", "Box"),
    ("Unit", "Unit"),
    ("Pair", "Pair")
]

class Product(models.Model):
    product_name = models.CharField( max_length= 50 , null= False, blank= False )
    short_description = models.CharField( max_length= 100)
    unit = models.CharField(choices = UNIT_TYPE_CHOICES, max_length = 10, default = "Piece")
    minimum_order_qunatity = models.PositiveIntegerField( default= 1 )
    price = models.FloatField()
    stock_in_usa = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null= True, blank = True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, null= True, blank= True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null= True, blank= True)
    category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null= True, blank= True)
    certifications = models.ManyToManyField(ProductCertification, blank= True)

    def __str__(self):
        return self.product_name


   