from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.timezone import now
from django.contrib.auth.models import User

from utils.base_model import SoftDeletionModel


class Post(SoftDeletionModel):
    title = models.CharField('标题', max_length=100, blank=False, null=False)
    content = models.TextField('正文', blank=False, null=False)
    created_time = models.DateTimeField('创建时间', default=now)
    modified_time = models.DateTimeField('上一次修改时间', default=now)
    summary = models.TextField('摘要', max_length=200, blank=True)
    pinned = models.BooleanField('置顶', default=False)
    category = models.ForeignKey('categories.Category', verbose_name="分类", on_delete=models.CASCADE)
    tags = models.ManyToManyField('tags.Tag', verbose_name="标签", blank=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_time']
        verbose_name = "文章"
        verbose_name_plural = verbose_name

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])
