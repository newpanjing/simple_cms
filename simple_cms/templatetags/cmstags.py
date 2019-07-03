import datetime
from django import template
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
    return Article.objects.order_by('-id').values('id', 'title', 'create_date', 'category__alias', 'category__name',
                                                  'cover', 'hits', 'summary')[:size]
