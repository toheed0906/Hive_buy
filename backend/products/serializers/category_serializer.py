from rest_framework import serializers
from ..models import Category



class CategorySerializer(serializers.ModelSerializer):
    sub_category = serializers.StringRelatedField(many = True, read_only = True)
    class Meta:
        model = Category
        fields = ["id", "category_name", "sub_category"]
        