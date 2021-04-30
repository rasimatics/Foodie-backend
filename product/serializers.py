from rest_framework import serializers
from .models import Item, Image, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image']


class ItemSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = ['id', 'title', 'price', 'image']

    @staticmethod
    def get_image(obj):
        image = ImageSerializer(obj.images.first())
        return image.data


class ItemDetailSerializer(serializers.ModelSerializer):
    category = serializers.ReadOnlyField(source='category.title')
    brand = serializers.ReadOnlyField(source='brand.title')
    images = ImageSerializer(read_only=True, many=True)

    class Meta:
        model = Item
        fields = ['id', 'title', 'description', 'price', 'category', 'brand', 'images']

