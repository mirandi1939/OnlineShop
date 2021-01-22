from rest_framework.viewsets import ModelViewSet
from .models import Product
from .permissions import ProductPermission, IsProductAuthor
from .serializers import ProductDetailsSerializer, ProductSerializer
from .filters import ProductFilter




class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductDetailsSerializer
    filterset_class = ProductFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        params = self.request.query_params
        return queryset

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permissions = []
        else:
            permissions = [ProductPermission, IsProductAuthor, ]
        return [permission() for permission in permissions]

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductSerializer
        return ProductDetailsSerializer

    def get_serializer_context(self):
        return {'action': self.action, 'request': self.request}