from django.urls import include, path
from django.contrib import admin
from rest_framework import routers 
from .views import CategoryViewSet, SubCategoryViewSet, \
    SupplierViewSet, ManufacturerViewSet, \
    ProductCertificationViewSet, ProductImageViewSet, \
    SupplierCertificationViewSet, ProductViewSet

router = routers.DefaultRouter() 

router.register(r'categories', CategoryViewSet) 
router.register(r'subcategories', SubCategoryViewSet)
router.register(r'supplier', SupplierViewSet)
router.register(r'manufacturer',ManufacturerViewSet)
router.register(r'productcertification', ProductCertificationViewSet)
router.register(r'productimages', ProductImageViewSet)
router.register(r'suppliercertification', SupplierCertificationViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [ 
    path('admin/',admin.site.urls),
    path('', include(router.urls)), 
    path('api-auth/', include('rest_framework.urls')) 
] 