from rest_framework import serializers

from categories.serializers import CategoryListSerializer
from posts.models import Post
from tags.serializers import TagListSerializer
from utils.mixins import EagerLoaderMixin


class PostListSerializer(serializers.HyperlinkedModelSerializer, EagerLoaderMixin):
    """
    文章列表
    """
    author = serializers.SerializerMethodField()
    tags = TagListSerializer(many=True)
    category = CategoryListSerializer()
    url = serializers.HyperlinkedIdentityField(view_name='post-detail', lookup_field='id')
    created_time = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M:%S")

    SELECT_RELATED_FIELDS = ['author', ]
    PREFETCH_RELATED_FIELDS = ['category', ]

    class Meta:
        model = Post
        fields = (
            'id',
            'url',
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
    tags = TagListSerializer(many=True)
    category = CategoryListSerializer()
    created_time = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M:%S")

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

    def get_author(self, obj):
        author = obj.author
        return {
            'id': author.id,
            'username': author.username
        }