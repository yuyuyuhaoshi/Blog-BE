from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.response import Response

from utils.pagination import CustomPageNumberPagination
from categories.models import Category
from categories.serializers import CategoryListSerializer, CategoryDetailSerializer


class CategoryPageNumberPagination(CustomPageNumberPagination):
    page_size = 120
    max_page_size = 120


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    http_method_names = ['get',]
    pagination_class = CategoryPageNumberPagination

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = CategoryDetailSerializer(instance, context={'request': request})
        return Response(serializer.data)
