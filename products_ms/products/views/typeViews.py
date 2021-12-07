from rest_framework import views, status, generics, filters
from rest_framework.response import Response
from products.models import Type
from products.serializers import TypeSerializer


# List, Create
class TypeListCreateView(generics.ListCreateAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'
    ordering = 'name'

# Read, Update, Delete
class TypeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer