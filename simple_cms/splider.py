import os
import random
import time
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "simple_cms.settings")
django.setup()
from cms.models import *

import requests
from bs4 import BeautifulSoup

for i in range(1, 157):
    try:
        print('采集第：{}篇'.format(i))
        url = 'http://www.178bird.com/article-{}-1.html'.format(i)
        r = requests.get(url, timeout=(3, 7))
        if r.status_code != 200:
            print('状态码不正确，跳过:status_code={}'.format(r.status_code))
            continue
        html_doc = r.text

        soup = BeautifulSoup(html_doc, "lxml")
        content = ''
        # 图片替换后存到本地
        p = soup.find_all(id='article_content')
        if len(p) == 0:
            print('内容不对，跳过')
            continue
        cover = ''
        for img in p[0].find_all('img'):
            try:
                src = img.attrs.get('src')
                if src.find('http') == -1:
                    src_url = '{}/{}'.format('http://www.178bird.com', src)
                    r = requests.get(src_url, timeout=(3, 7))
                    if r.status_code == 200:
                        suffix = os.path.splitext(src)[1]
                        # 按照时间命名文件
                        filename = '{}{}{}'.format(int(time.time() * 1000000), random.randint(10, 99), suffix)
                        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                        filepath = os.path.join(BASE_DIR, 'static/upload', filename)

                        with open(filepath, "wb") as f:  # 开始写文件，wb代表写二进制文件
                            f.write(r.content)

                        print(src_url)
                        print(filepath)

                        img.attrs['src'] = '/static/upload/{}'.format(filename)
                        img.parent.attrs['href'] = img.attrs['src']

                        cover = img.attrs['src']
            except Exception as e:
                print(e)
        content = []

        for i in p[0].contents:
            content.append(str(i))

        data = {
            'title': soup.find_all(class_='deanacticletop')[0].get_text().replace('\n', ''),
            'summary': soup.find_all('meta', attrs={'name': 'description'})[0].attrs.get('content'),
            'content': ''.join(content),
            'cover': cover
        }
        dbr = Article(
            title=data.get('title'),
            summary=data.get('summary'),
            content=data.get('content'),
            cover=data.get('cover')
        ).save()
        print(data)
        print(dbr)
    except Exception as e:
        print(e)
