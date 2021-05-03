from rest_framework import generics
from .serializers import OrderSerializer, CreateUpdateDestroyOrderSerializer
from .permissions import OrderOwnerPermission
from .models import Order


class ListOrders(generics.ListAPIView):
    """
        Get all orders
    """
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class CreateOrder(generics.CreateAPIView):
    """
        Create order
    """
    serializer_class = CreateUpdateDestroyOrderSerializer


class RetrieveUpdateDestroyOrder(generics.RetrieveUpdateDestroyAPIView):
    """
        Get, update and delete order
    """
    lookup_field = "id"
    serializer_class = CreateUpdateDestroyOrderSerializer
    permission_classes = [OrderOwnerPermission, ]
    queryset = Order.objects.all()
