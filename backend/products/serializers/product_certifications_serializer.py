from rest_framework import serializers
from ..models import ProductCertification

class ProductCertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCertification
        fields = "__all__"