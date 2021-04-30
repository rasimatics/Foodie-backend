from rest_framework import generics
from .serializers import ListOrderSerializer, CreateOrderSerializer
from .models import Order


class ListOrders(generics.ListAPIView):
    serializer_class = ListOrderSerializer
    queryset = Order.objects.all()


class CreateOrder(generics.CreateAPIView):
    serializer_class = CreateOrderSerializer



class RetrieveUpdateDestroyOrder(generics.RetrieveUpdateDestroyAPIView):
    pass

