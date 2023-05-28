
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from show_product.models import product
from show_product.permission import IsAdminOrAuthorOrReadOnly
from show_product.serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly ,IsAdminOrAuthorOrReadOnly]










# class ShowViewSet(viewsets.ModelViewSet):
#     queryset = product.objects.all()
#     print(queryset)
#     serializer_class = product_serializer
#
# class CommentViewSet(viewsets.ModelViewSet):
#     serializer_class = CommentSerializer
#
#     def get_queryset(self):
#         return Comment.objects.filter(product_id=self.kwargs['product_pk'])
#
#     def perform_create(self, serializer):
#         serializer.save(product_id=self.kwargs['product_pk'])
