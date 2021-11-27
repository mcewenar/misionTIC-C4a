from rest_framework import generics
from django.core.exceptions import ObjectDoesNotExist
from proveedoresApp.models.proveedor import Proveedor
from proveedoresApp.serializers.proveedorSerializer import ProveedorSerializer
#from rest_framework import views, status
#from rest_framework.response import Response

#List, Create
class ProveedorListCreateView(generics.ListCreateAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

#Read, Update, Delete
class ProveedorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer










#from django.shortcuts import render
#from django.views.decorators.csrf import csrf_exempt
#from rest_framework.parsers import JSONParser
#from django.http.response import JsonResponse
#
#from proveedoresApp.models import Proveedor
#from proveedoresApp.serializers import ProveedorSerializer
#
#
##Create your views here
#@csrf_exempt
#def proveedorApi(request,id=0): #Busca por un ID para hacer las operaciones
#    if request.method=='GET':
#        proveedores = Proveedor.objects.all()
#        proveedores_serializer = ProveedorSerializer(proveedores,many=True) #Convierte a JSON usando serializer
#        return JsonResponse(proveedores_serializer.data,safe=False)
#    elif request.method=='POST':
#        proveedor_data=JSONParser().parse(request)
#        proveedores_serializer=ProveedorSerializer(data=proveedor_data)
#        if proveedores_serializer.is_valid():
#            proveedores_serializer.save()
#            return JsonResponse("Provider added successfully",safe=False)
#        return JsonResponse("Operation failed",safe=False)
#    elif request.method=='PUT':
#        proveedor_data=JSONParser().parse(request)
#        proveedor= Proveedor.objects.get(idRegister=proveedor_data['idRegister'])
#        proveedores_serializer=ProveedorSerializer(proveedor,data=proveedor_data)
#        if proveedores_serializer.is_valid():
#            proveedores_serializer.save()
#            return JsonResponse("Update Successully")
#        return JsonResponse("Failed update")
#    elif request.method=='DELETE':
#        proveedor=Proveedor.objects.get(idRegister=id)
#        proveedor.delete()
#        return JsonResponse("Delete successfully",safe=False)
#        


















#from django.shortcuts import render
#
#from django.http.response import JsonResponse
#from proveedores_ms import proveedoresApp
#from rest_framework.parsers import JSONParser 
#from rest_framework import status
#
#from proveedoresApp.models import Proveedor
#from proveedoresApp.serializers import ProveedorSerializer
#from rest_framework.decorators import api_view
#
#
#@api_view(['GET', 'POST', 'DELETE'])
#def tutorial_list(request):
#    # GET list of tutorials, POST a new tutorial, DELETE all tutorials
#    if request.method == 'GET':
#        proveedor = Proveedor.objects.all()
#        
#        nameCompany = request.GET.get('name_company', None)
#        if nameCompany is not None:
#            tutorials = proveedor.filter(nameCompany__icontains=nameCompany)
#        proveedor_serializer = ProveedorSerializer(proveedor, many=True)
#        return JsonResponse(proveedor_serializer.data, safe=False)
#        # 'safe=False' for objects serialization
#    elif request.method == 'POST':
#        proveedor_data = JSONParser().parse(request)
#        proveedor_serializer = ProveedorSerializer(data=proveedor_data)
#        if proveedor_serializer.is_valid():
#            proveedor_serializer.save()
#            return JsonResponse(proveedor_serializer.data, status=status.HTTP_201_CREATED) 
#        return JsonResponse(proveedor_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
#@api_view(['GET', 'PUT', 'DELETE'])
#def tutorial_detail(request, pk):
#    # find tutorial by pk (id)
#    # ... tutorial = Tutorial.objects.get(pk=pk)
#
#    if request.method == 'GET': 
#        proveedor_serializer = ProveedorSerializer(tutorial) 
#        return JsonResponse(tutorial_serializer.data)
#    try: 
#        tutorial = Proveedor.objects.get(pk=pk) 
#    except Proveedor.DoesNotExist: 
#        return JsonResponse({'message': 'Provider does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 

# GET / PUT / DELETE tutorial
    
#@api_view(['GET'])
#def tutorial_list_published(request):
#    # GET all published tutorials



#    url(r'^admin/$', views.tutorial_list), #GET, POST, DELETE. GET list of tutorials, POST a new tutorial, DELETE all tutorials
#    url(r'^proveedor/(?P<pk>[0-9]+)$', views.tutorial_detail), #GET, PUT, DELETE. GET / PUT / DELETE tutorial by ‘id’
#    url(r'^proveedores/$', views.tutorial_list_published), #GET. GET all published tutorials
#    url(r'^', include('proveedoresApp.urls'))