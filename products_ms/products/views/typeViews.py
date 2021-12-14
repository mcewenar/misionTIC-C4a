from rest_framework import generics
from products.models import Type
from products.serializers import TypeSerializer
from django_filters.rest_framework import DjangoFilterBackend



# List, Create
class TypeListCreateView(generics.ListCreateAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'name']
    ordering_fields = '__all__'
    ordering = 'name'

# Read, Update, Delete
class TypeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer