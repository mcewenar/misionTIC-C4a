from rest_framework import generics
from products.models import Products
from products.serializers import ProductsSerializer
from django_filters.rest_framework import DjangoFilterBackend


# List, Create
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id_products', 'name_product','type_product']
    ordering_fields = '__all__'
    ordering = 'id_products'

# Read, Update, Delete
class ProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer