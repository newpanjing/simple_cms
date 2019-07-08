from django.db import models

# Create your models here.
from django.utils.html import format_html

from ueditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(verbose_name='分类名', max_length=64)
    alias = models.CharField(verbose_name='别名', max_length=128, help_text='url连接名', db_index=True)

    keywords = models.CharField(max_length=512, verbose_name='关键字', null=True, blank=True)
    description = models.CharField(max_length=512, verbose_name='描述', null=True, blank=True)

    sort = models.IntegerField(verbose_name='排序', default=0, help_text='越小排越前')
    home_display = models.BooleanField(verbose_name='首页显示', default=False, help_text='首页显示文章')

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
    content = RichTextField(verbose_name='内容')

    tags = models.CharField(verbose_name='标签', max_length=128, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='分类')

    hits = models.IntegerField(verbose_name='点击量', default=0)

    top = models.BooleanField(verbose_name='推荐', default=False)

    create_date = models.DateTimeField(auto_now_add=True, verbose_name='创建时间', null=True, blank=True)
    update_date = models.DateTimeField(auto_now=True, verbose_name='更新时间', null=True, blank=True)

    def cover_display(self):
        return format_html('<img src="{}" width="50" height="50" loading="lazy" lazy="lazy">', self.cover)

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


class Page(models.Model):
    alias = models.CharField(max_length=256, verbose_name='别名', db_index=True)
    title = models.CharField(max_length=256, verbose_name='标题')
    keywords = models.CharField(max_length=512, verbose_name='关键字', null=True, blank=True)
    description = models.CharField(max_length=512, verbose_name='描述', null=True, blank=True)
    content = RichTextField(verbose_name='内容', null=True, blank=False)
    createDate = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    update_date = models.DateTimeField(auto_now=True, verbose_name='更新时间', null=True, blank=True)

    display = models.BooleanField(verbose_name='是否显示', default=True, db_index=True)
    head = models.TextField(verbose_name='头部脚本', null=True, blank=True)
    footer = models.TextField(verbose_name='尾部脚本', null=True, blank=True)
    side = models.BooleanField(verbose_name='显示右侧边栏', default=True, help_text='该值在手机版无效')

    type = models.IntegerField(choices=(
        (0, '电脑'),
        (1, '手机')
    ), verbose_name='页面类型', default=0)

    class Meta:
        verbose_name = '页面'
        verbose_name_plural = '页面管理'

    def __str__(self):
        return self.title
