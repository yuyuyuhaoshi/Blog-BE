from django.core.exceptions import ValidationError
from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _

LINK_SHOW_TYPE = (
    ('i', '首页'),
    ('l', '列表页'),
    ('p', '文章页面'),
    ('a', '全站'),
)


class Links(models.Model):
    """友情链接"""

    name = models.CharField('链接名称', max_length=30, unique=True)
    link = models.URLField('链接地址')
    sequence = models.IntegerField('排序', unique=True)
    is_enable = models.BooleanField('是否显示', default=True, blank=False, null=False)
    show_type = models.CharField('显示类型', max_length=1, choices=LINK_SHOW_TYPE, default='i')
    created_time = models.DateTimeField('创建时间', default=now)
    last_mod_time = models.DateTimeField('修改时间', default=now)

    class Meta:
        ordering = ['sequence']
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class SiteSettings(models.Model):
    sitename = models.CharField("网站名称", max_length=200, null=False, blank=False, default='')
    site_description = models.TextField("网站描述", max_length=1000, null=False, blank=False, default='')
    site_keywords = models.TextField("网站关键字", max_length=1000, null=False, blank=False, default='')
    case_number = models.CharField('备案号', max_length=2000, null=True, blank=True, default='')
    analyticscode = models.TextField("网站统计代码", max_length=1000, null=False, blank=False, default='')

    def clean(self):
        if SiteSettings.objects.exclude(id=self.id).count():
            raise ValidationError(_('只能有一个配置'))
