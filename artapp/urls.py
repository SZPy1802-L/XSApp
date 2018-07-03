
from django.conf.urls import url
from django.contrib import admin
from artapp import views
urlpatterns = [
    # 声明主页面的请求
    url('', views.index),
]
