from rest_framework.viewsets import ModelViewSet

from order.models.order import Order
from order.serializers.order_serializer import OrderSerializer

class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()