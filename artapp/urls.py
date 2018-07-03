
from django.conf.urls import url
from django.contrib import admin
from artapp.views import *

urlpatterns = [
    # 声明主页面的请求
    url('^$', index),
    url(r'^tags$',add_tags),
    url(r'^delete_tag$',delete_tag),
    url(r'^list_tags$',list_tags)
]
