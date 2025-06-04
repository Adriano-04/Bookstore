from rest_framework.viewsets import ModelViewSet

from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import AllowAny  

from product.models import Product
from product.serializers.product_serializer import ProductSerializer

class ProductViewSet(ModelViewSet):
        authetication_classes = [BasicAuthentication, SessionAuthentication, TokenAuthentication]
        permission_classes = [AllowAny]

        serializer_class = ProductSerializer

        def get_queryset(self):
                return Product.objects.all().order_by('id')