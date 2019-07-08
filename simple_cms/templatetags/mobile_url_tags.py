from django import template

register = template.Library()  # 这一句必须这样写

ROOT = 'mobile'
STATIC_ROOT = '/static/mobile'


@register.simple_tag
def get_category_url(alias):
    return '/mobile/{}'.format(alias)


@register.simple_tag
def get_category_page(alias):
    if not alias:
        alias = 'topic'
    return '/mobile/{}/p/'.format(alias)


@register.simple_tag
def static(url):
    if url.find('no_image.png') != -1:
        return '/static/' + url
    rs = STATIC_ROOT
    if url.find('/') != 0:
        rs += '/'
    rs += url
    return rs


@register.simple_tag
def get_article_url(alias, id):
    return '/{}/{}/{}.html'.format(ROOT, alias, id)
