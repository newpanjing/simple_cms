import json
from ueditor import site
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from system.models import SystemConfig
from cms.models import *
import random


def index(request):
    # 4和图集
    atlas_size = 4
    atlas = []
    count = Article.objects.count()

    # 随机推荐4个
    for i in range(0, atlas_size):
        index = random.randint(0, count - 1)
        r = \
            Article.objects.values('cover', 'id', 'category__name', 'category__alias', 'title', 'summary',
                                   'create_date')[
                index]
        atlas.append(r)

    # 每个分类显示4篇文章
    category_newest = []

    categorys = Category.objects.filter(home_display=True)
    for c in categorys:
        category_newest.append({
            'category': c,
            'articles': Article.objects.filter(category_id=c.id).values('cover', 'id', 'category__name',
                                                                        'category__alias', 'title', 'summary',
                                                                        'create_date')[:4]
        })

    return render(request, 'index.html', {
        'latest': Article.objects.values('id', 'title', 'category__alias', 'create_date').last(),
        'tops': Article.objects.filter(top=True).order_by('-update_date').values('id', 'category__alias', 'title',
                                                                                 'cover')[:6],
        'news': Article.objects.order_by('-id').values('title', 'category__alias', 'id', 'summary')[:3],
        'articles': Article.objects.order_by('-id').values('title', 'id', 'category__alias', 'cover', 'summary',
                                                           'category__name', 'create_date', 'hits')[:16],
        'atlas': atlas,
        'category_newest': category_newest
    })


def settings(req):
    fields = ('key', 'value', 'label', 'type')
    return render(req, 'admin/settings.html', {
        'datas': json.dumps(list(SystemConfig.objects.values(*fields)))
    })


def settings_save(req):
    success = True

    try:
        post = req.POST

        # 删除所有的配置
        SystemConfig.objects.all().delete()
        props = json.loads(post.get('props'))
        for item in props:
            SystemConfig(
                key=item.get('key'),
                value=item.get('value'),
                label=item.get('label'),
                type=item.get('type')
            ).save()

    except Exception as e:
        print(e)
        success = False

    return HttpResponse(json.dumps({
        'success': success
    }), content_type="application/json")


def aritlce(req, category, id):
    a = Article.objects.get(id=id)
    a.hits += 1
    a.save()

    return render(req, 'article.html', {
        'article': a
    })


def category(req, category_alias, page=1):
    return render(req, 'category.html', {
        'alias': category_alias,
        'current_page': page
    })


@csrf_exempt
def ueditor_upload(request):
    return site.handler(request)
