from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from artapp.models import ArtTag

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


def add_tags(request):
    # 添加标签类型的处理函数
    if request.method == 'GET':
        # 新增, 修改
        # 判断是否为修改
        id = request.GET.get('id')
        tag = None
        if id:
            # 存在id,即为修改
            tag = ArtTag.objects.get(id=id)
        return render(request, 'art/edit_tags.html', {'tag': tag})
    else:
        # POST 请求
        # 新增, 修改
        if request.POST.get('id'):
            tag = ArtTag.objects.get(id=request.POST.get('id'))
        else:
            tag = ArtTag()
        tag.title = request.POST.get('title')
        tag.save()  # 保存到数据库

        return redirect('/art/list_tags')  # 重定向

def delete_tag(request):
    id = request.GET.get('id')
    if id:
        result = ArtTag.objects.filter(id=id)
        if result.exists():
            result.delete()

    # 重定向到列表页面
    return redirect('/art/list_tags')


def list_tags(request):
    return render(request,
                  'art/tags_list.html',
                  context={
                    'tags':   ArtTag.objects.all()
                  })