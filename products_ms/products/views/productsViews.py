from rest_framework import generics, filters
from products.models import Products
from products.serializers import ProductsSerializer


# List, Create
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'
    ordering = 'id_products'

# Read, Update, Delete
class ProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer