from rest_framework import generics
from products.models import Photo
from products.serializers import PhotoSerializer
from django_filters.rest_framework import DjangoFilterBackend

# List, Create
class PhotoListCreateView(generics.ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['product', 'name']
    ordering_fields = '__all__'
    ordering = 'product'

# Read, Update, Delete
class PhotoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer