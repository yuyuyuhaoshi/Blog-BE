from rest_framework import serializers

from posts.models import Post
from tags.serializers import TagListSerializer
from utils.mixins import EagerLoaderMixin


class PostListSerializer(serializers.HyperlinkedModelSerializer, EagerLoaderMixin):
    """
    文章列表
    """
    author = serializers.SerializerMethodField()
    tags = TagListSerializer(many=True, read_only=True)

    SELECT_RELATED_FIELDS = ['author', ]
    PREFETCH_RELATED_FIELDS = ['category']

    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'summary',
            'created_time',
            'modified_time',
            'pinned',
            'category',
            'tags',
            'author',
            'views',
        )

    def get_author(self, obj):
        author = obj.author
        return {
            'id': author.id,
            'username': author.username
        }


class PostDetailSerializer(PostListSerializer):
    author = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'content',
            'created_time',
            'modified_time',
            'pinned',
            'category',
            'tags',
            'author',
            'views',
        )