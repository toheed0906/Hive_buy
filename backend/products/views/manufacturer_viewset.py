from rest_framework import viewsets 
from ..serializers import ManufacturerSerializer
from ..models import Manufacturer


class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all().order_by("-id")
    serializer_class = ManufacturerSerializer