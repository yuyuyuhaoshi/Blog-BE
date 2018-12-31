from rest_framework import serializers

from tags.models import Tag
from posts.models import Post


class TagListSerializer(serializers.HyperlinkedModelSerializer):
    """
    标签列表
    """
    created_time = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Tag
        fields = (
            'id',
            'url',
            'name',
            'created_time',
        )


class TagDetailSerializer(serializers.ModelSerializer):
    post_count = serializers.SerializerMethodField()
    created_time = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Tag
        fields = (
            'id',
            'name',
            'post_count',
            'created_time',
        )

    def get_post_count(self, obj):
        tag_id = obj.id
        count = len(Post.objects.values("id").filter(tags=tag_id))
        return count
