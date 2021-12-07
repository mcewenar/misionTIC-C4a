from rest_framework import serializers
from products.models.products import Products

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Products
        fields = ['id_products', 'name_product', 'price', 'stock', 'type_product']