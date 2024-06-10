from rest_framework import viewsets 
from ..serializers import SubCategorySerializer
from ..models import SubCategory

class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all() 
    serializer_class = SubCategorySerializer