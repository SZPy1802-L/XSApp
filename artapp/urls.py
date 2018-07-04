from django.conf.urls import url
from django.contrib import admin
from artapp.views import *


urlpatterns = [
    # 声明主页面的请求
    url(r'^tags$', add_tags,name='tags'),
    url(r'^list_tags', list_tags,name='list_tags'),
    url(r'^delete_tag', delete_tag,name='delete_tag'),
    url(r'^upload_file', upload_file,name='upload_file'),
    url(r'^$', index),

]
