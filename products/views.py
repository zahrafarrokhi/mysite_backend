from rest_framework import mixins, viewsets

from .models import Product
from .serializers import ProductSerializer


class ProductView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
