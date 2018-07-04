from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from artapp.models import  ArtTag,Art
# Create your views here.


def index(request):

    return render(request,'art/list.html',context = {'arts':Art.objects.all(),
                                                     'tags':ArtTag.objects.all()})



def add_tags(request):
    # 第一次跳转,编辑
    if request.method == 'GET':
        # 新增编辑(不带tag的id),修改编辑(带tag的id) ,
        # 判断是否为修改
        id = request.GET.get('id')
        # print(id)  # 1
        # print(type(id))  # str
        tag = None
        if id :
            # 存在id,即为修改
            tag = ArtTag.objects.get(id=id)
        return render(request,'art/edit_tags.html',{'tag':tag})

    # 第二次跳转,为表单的post提交,新增修改
    else:
        # post 请求
        # 新增 和 修改
        if request.POST.get('id'):
            tag = ArtTag.objects.get(id = request.POST.get('id'))
        else:
            tag = ArtTag()
        tag.title = request.POST.get('title')
        tag.save()  # 保存到数据库
        return redirect('/art/list_tags')  # 重定向


def delete_tag(request):
    id = request.GET.get('id')
    if id:
        result = ArtTag.objects.filter(id=id)
        # print(result)  # <QuerySet [<ArtTag: ArtTag object>]>
        # print(type(result))  # <class 'django.db.models.query.QuerySet'>
        # 判断查询集是否存在
        if result.exists():
            result.delete()
    # 重定向到列表页面
    return redirect('/art/list_tags')


def list_tags(request):
    return render(request,'art/tags_list.html',
                  context={'tags':ArtTag.objects.all()})


def edit_art(request):
    if request.method == 'GET':

        return render(request,'art/edit_art.html')


    else:
        art_tag = ArtTag()
        art = Art()
        art.title = request.POST.get('title')
        art.summary = request.POST.get('summary')
        art.author = request.POST.get('author')
        art.img = request.POST.get('img')
        tag = request.POST.get('tag')
        tag_id = ArtTag.objects.filter(title = tag).first()
        if tag_id:
            print(tag_id)
            art.tag_id = tag_id.id
            art.save()
            return redirect('/art')
        else:
            msg = '分类不正确,请重试'
            return render(request, 'art/edit_art.html',{'msg':msg})






