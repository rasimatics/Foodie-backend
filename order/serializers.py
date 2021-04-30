from rest_framework import serializers
from .models import Order, OrderItem
from product.serializers import ItemSerializer


class ListOrderItemSerializer(serializers.ModelSerializer):
    item = ItemSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'quantity', 'item']
        depth = 1


class ListOrderSerializer(serializers.ModelSerializer):
    items = ListOrderItemSerializer(read_only=True, many=True)

    class Meta:
        model = Order
        fields = ["id", "items", 'address', 'total_amount', 'delivery_method', 'payment_method']
