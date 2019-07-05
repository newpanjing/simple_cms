import datetime
import math

from django import template
from django.core.paginator import Paginator
from django.template.loader import get_template

from system.models import *
from cms.models import *
import re
import json

register = template.Library()  # 这一句必须这样写


@register.simple_tag
def load_settings():
    # TODO 可以加缓存
    results = {}
    fields = ('key', 'value', 'label', 'type')
    data = list(SystemConfig.objects.values(*fields))
    for item in data:
        results[item.get('key')] = item.get('value')

    return results


@register.simple_tag
def load_links():
    return Links.objects.order_by('sort').values('url', 'name')


@register.simple_tag
def load_navbar():
    return Navbar.objects.values('name', 'url').order_by('sort')


@register.simple_tag
def get_year():
    return datetime.datetime.now().year


@register.filter
def filter_img(val):
    return val or '/static/image/no_image.png'


@register.simple_tag
def get_new_article(size=10):
    return Article.objects.order_by('-id').values('id', 'title', 'create_date',
                                                  'category__alias', 'category__name',
                                                  'cover', 'hits', 'summary')[:size]


@register.simple_tag
def get_hot_article(size=10):
    return Article.objects.order_by('-hits').values('id', 'title', 'create_date',
                                                    'category__alias', 'category__name',
                                                    'cover', 'hits', 'summary')[:size]


@register.filter
def get_opacity(val):
    return (11 - val) / 10


@register.simple_tag
def get_prev(id):
    """获取前一篇文章"""
    return Article.objects.filter(id__lt=id).order_by('-id').values('id', 'title', 'category__alias').first()


@register.simple_tag
def get_next(id):
    """获取前一篇文章"""
    return Article.objects.filter(id__gt=id).order_by('id').values('id', 'title', 'category__alias').first()


@register.simple_tag
def get_category(alias, page=1, size=10):
    params = {}
    if alias:
        params['category__alias'] = alias

    articles = Article.objects.filter(**params).order_by('-id').values('id', 'title', 'create_date',
                                                                       'category__alias', 'category__name',
                                                                       'cover', 'hits', 'summary')
    paginator = Paginator(articles, size)
    url = '/{}/p/'.format(alias)
    if not alias:
        url = '/topic'
    return {
        'count': paginator.count,
        'num_pages': paginator.num_pages,
        'list': paginator.page(page),
        'num_size': size,
        'current_page': page,
        'url': url
    }


def get_page_range(page_num, show_num, current_page):
    # 分偶数和奇数
    current_page = int(current_page)
    page_num = int(page_num)
    show_num = int(show_num)

    if show_num % 2 == 0:
        fore = int((show_num - 1) / 2)
        after = int(show_num / 2)
    else:
        fore = int(show_num / 2)
        after = math.ceil((show_num - 1) / 2)

    star = current_page - fore
    end = current_page + after
    if star < 1:
        end += int(math.fabs(star))
        star = 1

    if end > page_num:
        star -= end - page_num
        end = page_num

    if star < 1:
        star = 1
    if end > page_num:
        end = page_num
    return star, end


@register.simple_tag
def get_paginator(num_page_count, current_page, show_num, url):
    num_page_count = int(num_page_count)
    current_page = int(current_page)
    show_num = int(show_num)

    start, end = get_page_range(num_page_count, show_num, current_page)

    prev = current_page - 1
    next = current_page + 1

    page_list = []
    for i in range(start, end + 1):
        page_list.append(i)

    engine = get_template('paginator.html')
    html = engine.render({
        'url': url,
        'num_pages': num_page_count,
        'current_page': current_page,
        'show_num': show_num,
        'start': start,
        'end': end,
        'prev': prev,
        'next': next,
        'page_list': page_list
    })
    return format_html(html)


@register.simple_tag
def get_all_category():
    return Category.objects.order_by('sort').values('name', 'alias')

@register.filter
def test(val):
    print(val)