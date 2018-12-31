from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

from utils.base_model import SoftDeletionModel


class Tag(SoftDeletionModel):
    name = models.CharField('标题名', max_length=100, unique=True, blank=False, null=False)
    created_time = models.DateTimeField('创建时间', default=now)

    class Meta:
        ordering = ['name']
        verbose_name = "标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
