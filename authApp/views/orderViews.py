from rest_framework import generics
from rest_framework import views, status
from rest_framework.response import Response 
from authApp.models import Order
from authApp.serializers import OrderSerializer
# Vista Metodo Largo con get y post
class CRUD_Order(views.APIView):
    def get(self, request):
        querySet = Order.objects.all()
        serializer = OrderSerializer(data = querySet, many = True)
        serializer.is_valid()
        return Response(serializer.data, status = status.HTTP_200_OK)
    def post(self, request):
        print("Información obtenida", request.data)
        serializer = OrderSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            data = {"Message" : "Se creo la orden de compra"}
            return Response(data=data, status= status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status= status.HTTP_400_BAD_REQUEST)
# vista metodo corto con put y delete
class CRUD_Order2(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


