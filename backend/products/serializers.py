from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer

from .models import Category, Product


class ProductSerializer(serializers.ModelSerializer):
    image = VersatileImageFieldSerializer(sizes='product_image')
    category_name = serializers.CharField(source='category.name')

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'slug',
            'category_name',
            'description',
            'quantity',
            'price',
            'get_absolute_url',
            'image',
        ]


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    products_count = serializers.IntegerField(source='products.count')

    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'get_absolute_url',
            'products_count',
            'products',
        ]
