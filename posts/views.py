from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.response import Response

from posts.models import Post
from posts.serializers import PostListSerializer, PostDetailSerializer


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PostListSerializer.setup_eager_loading(
        Post.objects.order_by('-pinned', '-modified_time'),
        select_related=PostListSerializer.SELECT_RELATED_FIELDS,
        prefetch_related=PostListSerializer.PREFETCH_RELATED_FIELDS
    )
    serializer_class = PostListSerializer
    http_method_names = ['get',]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('tags', 'category',)
    lookup_field = 'id'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.increase_views()
        instance.refresh_from_db()
        serializer = PostDetailSerializer(instance, context={'request': request})
        return Response(serializer.data)
