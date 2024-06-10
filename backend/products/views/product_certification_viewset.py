from rest_framework import viewsets 
from ..serializers import ProductCertificationSerializer
from ..models import ProductCertification


class ProductCertificationViewSet(viewsets.ModelViewSet):
    queryset = ProductCertification.objects.all()
    serializer_class = ProductCertificationSerializer