
from authApp.models import Customer
from authApp.serializers.customerSerializer import CustomerSerializer
from rest_framework import generics

# List, Create
class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

# Read, Update, Delete
class CustomerRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

