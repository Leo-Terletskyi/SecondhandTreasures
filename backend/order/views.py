import stripe

from django.conf import settings


from rest_framework import permissions, status, authentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Order
from .serializers import OrderSerializer, MyOrderSerializer


@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def checkout(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        stripe.api_key = settings.STRIPE_SECRET_KEY

        original_products = []
        items = serializer.validated_data['items']
        for item in items:
            current_product = item.get('product')
            products_available = current_product.quantity
            products_required = item.get('quantity')
            original_products.append([current_product, products_available])
            if products_available >= products_required:
                current_product.quantity -= products_required
                current_product.save()
            else:
                current_product.quantity = 0
                item['quantity'] = products_available
                current_product.save()
        paid_amount = sum(item.get('quantity') * item.get('product').price for item in items)
        try:
            charge = stripe.Charge.create(
                amount=int(paid_amount * 100),
                currency='USD',
                description='Charge from SecondhandTreasures',
                source=serializer.validated_data['stripe_token']
            )
            
            serializer.save(user=request.user, paid_amount=paid_amount)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception:
            for product in original_products:
                product[0].quantity = product[1]
                product[0].save()
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MyOrderList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, format=None):
        orders = Order.objects.filter(user=request.user)
        serializer = MyOrderSerializer(orders, many=True)
        return Response(serializer.data)
