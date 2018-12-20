# Generated by Django 2.1.4 on 2018-12-21 01:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='链接名称')),
                ('link', models.URLField(verbose_name='链接地址')),
                ('sequence', models.IntegerField(unique=True, verbose_name='排序')),
                ('is_enable', models.BooleanField(default=True, verbose_name='是否显示')),
                ('show_type', models.CharField(choices=[('i', '首页'), ('l', '列表页'), ('p', '文章页面'), ('a', '全站')], default='i', max_length=1, verbose_name='显示类型')),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('last_mod_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '友情链接',
                'verbose_name_plural': '友情链接',
                'ordering': ['sequence'],
            },
        ),
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sitename', models.CharField(default='', max_length=200, verbose_name='网站名称')),
                ('site_description', models.TextField(default='', max_length=1000, verbose_name='网站描述')),
                ('site_keywords', models.TextField(default='', max_length=1000, verbose_name='网站关键字')),
                ('case_number', models.CharField(blank=True, default='', max_length=2000, null=True, verbose_name='备案号')),
                ('analyticscode', models.TextField(default='', max_length=1000, verbose_name='网站统计代码')),
            ],
        ),
    ]