from django.contrib import admin
from .models import Product, Manufacturer, SupplierCertification, ProductCertification, Category, SubCategory, Supplier, Image


class ProductAdmin(admin.ModelAdmin):
    list_display = ("product_name", "short_description", "unit", "minimum_order_qunatity", "stock_in_usa","price",  "manufacturer", "supplier", "category")

class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ("manufacturer_name", "location")

class SupplierCertificationAdmin(admin.ModelAdmin):
    list_display = ("certification_name",)

class ProductCertificationAdmin(admin.ModelAdmin):
    list_display = ("certification_name",)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category_name",)

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ("sub_category_name",)

class SupplierAdmin(admin.ModelAdmin):
    list_display = ("supplier_name", "rating")

class ImageAdim(admin.ModelAdmin):
    list_display = ("product", "image")


admin.site.register(Image, ImageAdim )
admin.site.register(Product, ProductAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(SupplierCertification, SupplierCertificationAdmin)
admin.site.register(ProductCertification, ProductCertificationAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Supplier, SupplierAdmin)