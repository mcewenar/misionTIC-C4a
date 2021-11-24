from rest_framework import serializers
from authApp.models.customer import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'user', 'name', 'email', 'address', 'phone', 'city']