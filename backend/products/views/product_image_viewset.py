from rest_framework import viewsets 
from ..serializers import ProductImageSerializer
from ..models import Image

class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ProductImageSerializer