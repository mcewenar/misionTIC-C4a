from rest_framework import serializers
from authApp.models.shipping import Shipping

class ShippingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipping
        fields = ['Shipping_id', 'conveyor', 'delivery_time', 'was_delivered']