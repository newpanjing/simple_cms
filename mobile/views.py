# from django.shortcuts import render
from django import shortcuts

from cms.models import Page, Category, Article


def render(request, template_name, context=None, content_type=None, status=None, using=None):
    return shortcuts.render(request, 'mobile/{}'.format(template_name), context, content_type, status, using)


def index(request):
    return render(request, 'index.html')


def category(request, alias, page=1):
    # 先找自定义页面，如果没有才是分类

    p = Page.objects.filter(alias=alias).first()
    if p:
        template = 'page.html'

        return render(request, template, {
            'page': p
        })
    else:
        return render(request, 'category.html', {
            'alias': alias,
            'current_page': page,
            'category': Category.objects.filter(alias=alias).first()
        })


def aritlce(req, alias, id):
    a = Article.objects.get(id=id)
    a.hits += 1
    a.save()

    return render(req, 'article.html', {
        'article': a,
        'alias': alias
    })
