from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.response import Response

from utils.pagination import CustomPageNumberPagination
from tags.models import Tag
from tags.serializers import TagListSerializer, TagDetailSerializer


class TagPageNumberPagination(CustomPageNumberPagination):
    page_size = 120
    max_page_size = 120


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagListSerializer
    http_method_names = ['get',]
    pagination_class = TagPageNumberPagination

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = TagDetailSerializer(instance, context={'request': request})
        return Response(serializer.data)
