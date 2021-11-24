from django.core.exceptions import ObjectDoesNotExist
from rest_framework import views, status
from rest_framework.response import Response
from rest_framework import generics


from authApp import serializers
# Model
from authApp.models import Provider
# Serializer
from authApp.serializers import ProviderSerializer


class TestView(views.APIView):
    def get(self, request):
        response = {"message": "Esto es una prueba"}
        return Response(data=response, status=status.HTTP_200_OK)
'''
class ProviderView(views.APIView):
    def get(self, request):
        queryset = Provider.objects.all()
        serializer = ProviderSerializer(data=queryset, many=True)
        serializer.is_valid()
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        print("Información obtenida", request.data)
        serializer = ProviderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {"message": "Se creó la cuenta"}
            return Response(data=data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

'''
#List, Create
class ProviderListCreateViews(generics.ListCreateAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

#Read, Update, Delete
class ProviderRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
