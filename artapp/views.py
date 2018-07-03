from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


def index(requset):
    # 请求路径和请求方法
    print(requset.path,requset.method)
    # 请求头的元信息和GET请求参数(叫查询参数)
    # print(requset.META,requset.GET)
    print(requset.GET.get('page','没有数据'))
    # POST请求参数(表单参数)
    print(requset.POST)
    # return HttpResponse('<h1>您好<h1>')
    # 返回Json响应对象
    # return JsonResponse({'name':'disen','age':20})
    # 返回渲染模板
    return render(requset,'art/list.html',context={'name':'disen','age':20})