from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ListOrderSerializer
from .models import Order


class ListOrders(ListAPIView):
    serializer_class = ListOrderSerializer
    queryset = Order.objects.all()


class CreateOrder(CreateAPIView):
    pass


class RetrieveUpdateDestroyOrder(RetrieveUpdateDestroyAPIView):
    pass


