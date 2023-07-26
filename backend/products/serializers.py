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
    products = serializers.SerializerMethodField()
    
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'get_absolute_url',
            'products',
        ]
    
    def get_products(self, obj):
        products = Product.objects.select_related('category').filter(category=obj)
        serializer = ProductSerializer(instance=products, many=True, context=self.context)
        return serializer.data


class AllCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'get_absolute_url',
        ]
