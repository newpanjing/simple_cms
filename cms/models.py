from django.db import models

# Create your models here.
from django.utils.html import format_html
from simpleui.fields import FileField


class Category(models.Model):
    name = models.CharField(verbose_name='分类名', max_length=64)
    alias = models.CharField(verbose_name='别名', max_length=128, help_text='url连接名', db_index=True)

    sort = models.IntegerField(verbose_name='排序', default=0, help_text='越小排越前')

    create_date = models.DateTimeField(auto_now_add=True, verbose_name='创建时间', null=True, blank=True)
    update_date = models.DateTimeField(auto_now=True, verbose_name='更新时间', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = '分类管理'


class Article(models.Model):
    title = models.CharField(verbose_name='标题', max_length=256)
    summary = models.CharField(verbose_name='摘要', max_length=256, null=True, blank=True)
    cover = models.FileField(verbose_name='封面', max_length=512, null=True, blank=True)
    # cover = FileField(verbose_name='封面', max_length=512, null=True, blank=True, placeholder='封面')
    content = models.TextField(verbose_name='内容')

    tags = models.CharField(verbose_name='标签', max_length=128, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='分类')

    hits = models.IntegerField(verbose_name='点击量', default=0)

    create_date = models.DateTimeField(auto_now_add=True, verbose_name='创建时间', null=True, blank=True)
    update_date = models.DateTimeField(auto_now=True, verbose_name='更新时间', null=True, blank=True)

    def cover_display(self):
        return format_html('<img src="/static/upload/{}" width="50" height="50" loading="lazy" lazy="lazy">', self.cover)

    cover_display.short_description = '封面'

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章管理'


class Banner(models.Model):
    cover = models.CharField(verbose_name='封面', max_length=256)
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='文章')
    sort = models.IntegerField(verbose_name='排序', default=0, help_text='值越小排越前')

    def cover_display(self):
        return self.article.cover_display()

    def __str__(self):
        return self.article.title

    class Meta:
        verbose_name = '首页推荐'
        verbose_name_plural = '首页推荐'
