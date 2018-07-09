# 避免celery.py 和 celery的冲突问题
from __future__ import absolute_import
import os

from celery import Celery

from XSproject import settings

# 设置环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'XSproject.settings')


# 创建 celery 并指定 名称
app = Celery('XSProject')
app.config_from_object('django.conf:settings')


# 自动发现当前项目中所有app应用中的celery任务
app.autodiscover_tasks(lambda : settings.INSTALLED_APPS)



