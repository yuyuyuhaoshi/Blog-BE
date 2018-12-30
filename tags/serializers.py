from rest_framework import serializers
from django.db.models import Count

from tags.models import Tag
from posts.models import Post

class TagListSerializer(serializers.HyperlinkedModelSerializer):
    """
    标签列表
    """
    class Meta:
        model = Tag
        fields = (
            'id',
            'url',
            'name',
        )


class TagDetailSerializer(serializers.ModelSerializer):
    post_count = serializers.SerializerMethodField()
    class Meta:
        model = Tag
        fields = (
            'id',
            'name',
            'post_count'
        )

    def get_post_count(self, obj):
        tag = obj
        tag_id = tag.id
        # count = Post.objects.annotate(tags_num=Count('tags')).filter()
        return 10