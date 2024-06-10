from django.db import models
from .product_model import Product


class Image(models.Model):

    image = models.CharField()
    product = models.ForeignKey(Product, on_delete= models.CASCADE, blank= True, null= True, related_name="product_image")
    def __str__(self):
        return  self.image

    