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
            'created_time',
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
            'child_category',
            'created_time',
        )

    def get_child_category(self, obj):
        all_category = Category.objects.filter(parent_category=obj.id)
        category_serializer = CategoryListSerializer(all_category, many=True,
                                                     context={'request': self.context['request']})
        return category_serializer.data
