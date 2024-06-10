from rest_framework import viewsets 
from ..serializers import SupplierCertificationSerializer
from ..models import SupplierCertification

class SupplierCertificationViewSet(viewsets.ModelViewSet):
    queryset = SupplierCertification.objects.all()
    serializer_class = SupplierCertificationSerializer
