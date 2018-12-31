from rest_framework import serializers

from categories.models import Category


class CategoryListSerializer(serializers.HyperlinkedModelSerializer):
    """
    分类列表
    """
    class Meta:
        model = Category
        fields = (
            'id',
            'url',
            'name',
        )

class CategoryDetailSerializer(serializers.ModelSerializer):
    """
    分类详情
    """
    child_category = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'parent_category',
            'child_category'
        )

    def get_child_category(self, obj):
        return []
