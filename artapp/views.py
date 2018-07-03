from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.



def index(request):
    # 请求路径和请求方法
    print(request.path,request.method)
    # 请求头的源信息和GET请求参数(查询参数)
    # print(request.META,request.GET) # 字典类型
    print(request.GET)
    print(request.GET.get('page'),request.GET.get('tag'))
    # POST请求参数,表单参数
    print(request.POST) # 字典类型

    # 响应对象
    # return HttpResponse('<h1>您好</h1>')
    # return JsonResponse({'name':'Disen'})
    return render(request,'art/list.html',context = {'name':'Disen','age':20})