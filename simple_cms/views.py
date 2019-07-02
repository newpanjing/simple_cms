import json

from django.http import HttpResponse
from django.shortcuts import render

from system.models import SystemConfig


def index(request):
    return render(request, 'index.html', {

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
