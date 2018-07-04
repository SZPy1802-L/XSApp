import os

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from XSproject import settings
from artapp.models import ArtTag, Art


def index(requset):

    # 返回渲染模板
    return render(requset,'art/list.html',
                  context={'arts': Art.objects.all(),
                           'tags': ArtTag.objects.all(),
                           })


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

# 上传文件
def upload_file(request):
    if request.method == 'GET':
        return render(request, 'art/upload.html',{'arttags':ArtTag.objects.all()})
    else:
        # post提交上传文章
        img = request.FILES.get('img')
        summary = request.POST.get('summary')
        author = request.POST.get('author')
        title = request.POST.get('title')
        tag = request.POST.get('tag')
        print(tag)
        arttag = ArtTag.objects.filter(title=tag).first()
        # 保存到数据库
        art = Art()
        art.title = title
        art.author = author
        art.summary = summary
        art.img = img
        art.tag_id = arttag.id
        art.save()
        return redirect('/art')

