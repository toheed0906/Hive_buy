from rest_framework import viewsets 
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from ..serializers import ProductSeralizer
from ..models import  Product
from django_filters import rest_framework as filters
from rest_framework.pagination import PageNumberPagination

class ProductPagination(PageNumberPagination):
    page_size = 9
    ordering = "id"
  


class ProductFilter(filters.FilterSet):
    min_price = filters.NumberFilter( field_name = "price", lookup_expr = 'gte', label = "Minimum Price")
    max_price = filters.NumberFilter( field_name = "price", lookup_expr = 'lte', label = "Maximum Price" )
    minimimum_order_quantity = filters.NumberFilter(field_name = "minimum_order_qunatity", lookup_expr = 'lt')
   
    class Meta:
        model = Product
        fields = {
            'stock_in_usa' : ["exact"],
            'product_name':  ["icontains"],
            'category__sub_category_name':  ["exact"],
            'category__category__category_name':  ["exact"],
            'manufacturer__location': ["in"],

        }

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSeralizer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_class = ProductFilter
    ordering_fields = ['price', "minimum_order_qunatity","created_at","supplier__rating"]
    pagination_class = ProductPagination

