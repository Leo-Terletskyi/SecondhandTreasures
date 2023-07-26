from django.db.models import Q
from django.http import Http404

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from .models import Category, Product
from .serializers import AllCategoriesSerializer, CategorySerializer, ProductSerializer


class AllProducts(APIView):
    def get(self, request):
        products = Product.objects.select_related('category').filter(quantity__gt=0)
        product_serializer = ProductSerializer(products, many=True, context={'request': request})
        return Response(product_serializer.data)


class CheckProducts(APIView):
    def get(self, request):
        products_list = request.data.get('productsList', '')
        if products_list:
            products = Product.objects.select_related('category').filter(slug__in=products_list, quantity__gt=0)
            product_serializer = ProductSerializer(products, many=True, context={'request': request})
            return Response(product_serializer.data)


@api_view(['POST'])
def check_products(request):
    products_list = request.data.get('productsList')
    if products_list:
        products = Product.objects.select_related('category').filter(slug__in=products_list)
        product_serializer = ProductSerializer(products, many=True, context={'request': request})
        return Response(product_serializer.data)
    return Response({'productsList': []})


class AllCategories(APIView):
    def get(self, request):
        categories = Category.objects.all()
        category_serializer = AllCategoriesSerializer(categories, many=True, context={'request': request})
        return Response(category_serializer.data)


class LatestProducts(APIView):
    def get(self, request):
        products = Product.objects.select_related('category').filter(quantity__gt=0)[:10]
        serializer = ProductSerializer(products, many=True, context={'request': request})
        return Response(serializer.data)


class ProductDetail(APIView):
    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.select_related('category').filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404
    
    def get(self, request, category_slug, product_slug):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(product, context={'request': request})
        return Response(serializer.data)


class CategoryDetail(APIView):
    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            raise Http404
    
    def get(self, request, category_slug):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category, context={'request': request})
        return Response(serializer.data)


@api_view(['POST'])
def search_products(request):
    query = request.data.get('query', '')
    if query:
        products = Product.objects.select_related('category').filter(quantity__gt=0).filter(
            Q(name__icontains=query) | Q(description__icontains=query))
        serializer = ProductSerializer(products, many=True, context={'request': request})
        return Response(serializer.data)
    return Response({'products': []})
