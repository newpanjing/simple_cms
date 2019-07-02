import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "simple_cms.settings")
django.setup()

from cms.models import Article

rs = Article.objects.all()
for a in rs:
    title = a.title

    if title.find('防治') != -1 or title.find('治疗') != -1 or title.find('症状') != -1:
        a.category_id = 2
    elif title.find('百科') != -1:
        a.category_id = 3
    else:
        a.category_id = 1

    a.save()
