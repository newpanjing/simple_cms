import os
import random
import time
from django.conf import settings
from django.core.files.storage import Storage


class FileStorage(Storage):

    def __init__(self):
        self.root = os.environ.get('UPLOAD_ROOT', getattr(settings, 'UPLOAD_ROOT', None))
        self.prefix = os.environ.get('UPLOAD_PATH_PREFIX', getattr(settings, 'UPLOAD_PATH_PREFIX', None))
        if not os.path.exists(self.root):
            os.makedirs(self.root)

    def exists(self, name):
        return os.path.exists(os.path.join(self.root, name))

    def url(self, name):
        return name

    def _save(self, name, content):
        suffix = os.path.splitext(name)[1]

        # 按照时间命名文件

        filename = '{}{}{}'.format(int(time.time() * 1000000), random.randint(10, 99), suffix)

        # 获取配置
        filepath = os.path.join(self.root, filename)
        f = open(filepath, 'wb')

        content.open()
        for chunk in content.chunks():
            f.write(chunk)
        f.flush()
        f.close()
        content.close()

        return '{}{}'.format(self.prefix, filename)
