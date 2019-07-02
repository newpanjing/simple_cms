import datetime
from django import template
from system.models import *

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
def load_navbar():
    return Navbar.objects.values('name', 'url').order_by('sort')


@register.simple_tag
def get_year():
    return datetime.datetime.now().year
