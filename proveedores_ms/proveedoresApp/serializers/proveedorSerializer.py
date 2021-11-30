from rest_framework import serializers
from proveedoresApp.models.proveedor import Proveedor
class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = ('idRegister','name_company','name_contact','cel','address','city','email')