from rest_framework import serializers
from products.models.photo import Photo

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['id', 'name', 'product', 'image']