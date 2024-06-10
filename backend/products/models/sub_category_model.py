from django.db import models
from .category_model import Category

class SubCategory(models.Model):

    sub_category_name = models.CharField( max_length= 50 , unique = True, verbose_name= "Name")
    category = models.ForeignKey(Category, on_delete= models.CASCADE, null= True, related_name="sub_category")


    def __str__(self):
        return self.sub_category_name