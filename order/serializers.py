from rest_framework import serializers
from .models import Order, OrderItem
from product.serializers import ItemSerializer


class ListOrderItemSerializer(serializers.ModelSerializer):
    item = ItemSerializer()
    price = serializers.FloatField(source="get_price")

    class Meta:
        model = OrderItem
        fields = ['id', 'quantity', 'item', 'price']
        depth = 1


class OrderSerializer(serializers.ModelSerializer):
    items = ListOrderItemSerializer(many=True, read_only=True)
    total_amount = serializers.FloatField(source="get_total_amount")

    class Meta:
        model = Order
        fields = ["id", "items", 'address', 'total_amount', 'delivery_method', 'payment_method', 'user']


class CreateUpdateOrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'quantity', 'item']


class CreateUpdateDestroyOrderSerializer(serializers.ModelSerializer):
    items = CreateUpdateOrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ["id", 'address', 'items', 'delivery_method', 'payment_method', 'user']
        extra_kwargs = {
            'user': {'read_only': True}
        }

    def create(self, validated_data):
        items = validated_data.pop('items')
        order = Order(**validated_data)
        order.user = self.context['request'].user
        order.save()
        for data in items:
            OrderItem.objects.create(quantity=data['quantity'], item=data['item'], order=order)
        return order

    def update(self, instance, validated_data):
        items = validated_data.pop('items')
        for item_instance, item in zip(instance.items.all(), items):
            item_serializer = CreateUpdateOrderItemSerializer()
            super(CreateUpdateOrderItemSerializer, item_serializer).update(item_instance, item)

        super(CreateUpdateDestroyOrderSerializer, self).update(instance, validated_data)
        return instance




