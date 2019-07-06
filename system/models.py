from django.db import models

# Create your models here.
from django.utils.html import format_html


class SystemConfig(models.Model):
    label = models.CharField(max_length=128, verbose_name='配置项', null=True, blank=False)
    key = models.CharField(max_length=128, verbose_name='Key', db_index=True)
    value = models.CharField(max_length=2048, verbose_name='Value')

    update_date = models.DateTimeField(auto_now=True, verbose_name='更新时间', null=True, blank=True)

    type_choices = (
        (0, '单行文本框'),
        (1, '多行文本框'),
    )
    type = models.IntegerField(choices=type_choices, verbose_name='类型', default=0)

    def __str__(self):
        return format_html('{}={}', self.key, self.value)

    class Meta:
        verbose_name = '配置'
        verbose_name_plural = verbose_name + '管理'


class Navbar(models.Model):
    name = models.CharField(max_length=64, verbose_name='名称')
    url = models.CharField(max_length=512, verbose_name='链接地址', default='javascript:;')
    parent_id = models.IntegerField(null=True, blank=True, verbose_name='父id')
    sort = models.IntegerField(default=0, verbose_name='排序', help_text='值越小排越前')

    type = models.IntegerField(choices=(
        (0, '电脑'),
        (1, '手机')
    ), verbose_name='类型', default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '导航菜单'
        verbose_name_plural = verbose_name


class Links(models.Model):
    name = models.CharField(max_length=64, verbose_name='名称')

    url = models.URLField(max_length=256, verbose_name='链接')

    sort = models.IntegerField(default=0, verbose_name='排序', help_text='值越小排越前')

    type_choices = (
        (0, 'QQ'),
        (1, '微信'),
        (2, '邮箱'),
        (3, '手机'),
        (4, '其他'),
    )
    type = models.IntegerField(choices=type_choices, verbose_name='类型', default=0)
    contact = models.CharField(max_length=32, verbose_name='联系人', null=True)

    create_date = models.DateTimeField(auto_now_add=True, verbose_name='创建时间', null=True, blank=True)
    update_date = models.DateTimeField(auto_now=True, verbose_name='更新时间', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '友链'
        verbose_name_plural = verbose_name + '管理'
