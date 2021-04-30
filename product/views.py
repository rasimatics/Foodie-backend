from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from .serializers import ItemSerializer, ItemDetailSerializer, CategorySerializer
from .models import Item, Category


class ItemList(generics.ListAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter, ]
    search_fields = ['title', 'description', 'brand__title']


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ItemDetailSerializer
    queryset = Item.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'


class CategoryList(generics.ListAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()



