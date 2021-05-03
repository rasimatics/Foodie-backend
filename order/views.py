from rest_framework import generics
from .serializers import OrderSerializer, CreateUpdateDestroyOrderSerializer
from .models import Order


class ListOrders(generics.ListAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class CreateOrder(generics.CreateAPIView):
    serializer_class = CreateUpdateDestroyOrderSerializer


class RetrieveUpdateDestroyOrder(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = "id"
    serializer_class = CreateUpdateDestroyOrderSerializer
    queryset = Order.objects.all()

