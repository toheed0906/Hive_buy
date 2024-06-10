from rest_framework import serializers
from ..models import Image


class ProductImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = "__all__"