from rest_framework import serializers
from ..models import Product


class ProductSeralizer(serializers.ModelSerializer):
    product_image = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Product
        fields = (
            "id", "product_name", "short_description", "unit", 
            "minimum_order_qunatity", "stock_in_usa",  "price", 
            "supplier", "manufacturer", "category", "certifications", 
            'product_image' 
        )
        depth = 2
        
        