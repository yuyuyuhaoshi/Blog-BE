from rest_framework import serializers

from categories.serializers import CategoryDetailSerializer
from posts.models import Post
from tags.serializers import TagListSerializer, TagDetailSerializer
from utils.mixins import EagerLoaderMixin


class PostListSerializer(serializers.HyperlinkedModelSerializer, EagerLoaderMixin):
    """
    文章列表
    """
    author = serializers.SerializerMethodField()
    tags = TagDetailSerializer(many=True)
    category = CategoryDetailSerializer()
    url = serializers.HyperlinkedIdentityField(view_name='post-detail', lookup_field='id')

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
    tags = TagDetailSerializer(many=True)
    category = CategoryDetailSerializer()

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