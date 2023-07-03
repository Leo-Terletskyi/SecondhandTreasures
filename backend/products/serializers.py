from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer

from .models import Category, Product


class ProductSerializer(serializers.ModelSerializer):
    image = VersatileImageFieldSerializer(sizes='product_image')
    # image_full_size = serializers.SerializerMethodField()
    image_thumbnail = serializers.SerializerMethodField()
    """image_medium_square_crop = serializers.SerializerMethodField()
    image_small_square_crop = serializers.SerializerMethodField()"""
    category_name = serializers.CharField(source='category.name')

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'slug',
            'category_name',
            'description',
            'price',
            'get_absolute_url',
            'image',
            'image_thumbnail',
        ]

    def get_image_thumbnail(self, product):
        request = self.context.get('request')
        photo_url = product.image.thumbnail['100x100']
        return request.build_absolute_uri(photo_url)


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
