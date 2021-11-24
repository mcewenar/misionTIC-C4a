from rest_framework import serializers
from authApp.models.order import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['Order_id', 'customer_id', 'shipping_id', 'payment_method', 'shipping_address', 'date']