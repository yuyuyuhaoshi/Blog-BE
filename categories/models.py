from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.timezone import now
from django.contrib.auth.models import User

from utils.base_model import SoftDeletionModel


class Category(SoftDeletionModel):
    name = models.CharField('分类名', max_length=100, unique=True, blank=False, null=False)
    parent_category = models.ForeignKey('self', verbose_name="父级分类", blank=True, null=True, on_delete=models.CASCADE)
    created_time = models.DateTimeField('创建时间', default=now)

    class Meta:
        ordering = ['name']
        verbose_name = "分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

