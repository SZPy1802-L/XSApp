from django.conf.urls import url
from django.contrib import admin

from userapp import views


urlpatterns = [
    # 声明注册请求
    url(r'^regist', views.regist),


]
