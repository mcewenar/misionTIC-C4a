from authApp.models import Shipping
from authApp.serializers.shippingSerializer import ShippingSerializer
from rest_framework import generics

# List, Create
class ShippingListCreateView(generics.ListCreateAPIView):
    queryset = Shipping.objects.all()
    serializer_class = ShippingSerializer

# Read, Update, Delete
class ShippingRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shipping.objects.all()
    serializer_class = ShippingSerializer
