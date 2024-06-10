from rest_framework import serializers
from ..models import SupplierCertification

class SupplierCertificationSerializer(serializers.ModelSerializer):


    class Meta:
       model = SupplierCertification
       fields = "__all__"