from django.shortcuts import render, redirect

from userapp.forms import UserForm
from userapp.models import UserProfile
from json import loads

# Create your views here.
def regist(request):
    if request.method == 'GET':
        return render(request, 'user/regist.html')
    else: # post
        # user = UserProfile()
        # user.username = request.POST.get('username')
        # user.password = request.POST.get('password')
        # user.phone = request.POST.get('phone')
        # user.photo = request.FILES.get('photo')

        # 创建UserForm的实例对象
        # 要求：表单中指定的字段名必须和model模型中字段名保持一致
        userForm = UserForm(request.POST,
                            request.FILES)

        # 保存之前要验证数据
        if userForm.is_valid():  # 验证通过
            userForm.save()
            return redirect('/art/')
        else:
            print('验证出错：', userForm.errors.as_json())

            # form.errors.as_json() 返回是 json字符串
            # 格式： {'字段名1':[{'message':'xx', code:'required'}],
            #        '字段名2':[{'message':'xx', code:'required'}]}
            return render(request, 'user/regist.html',
                          {'errors': loads(userForm.errors.as_json())})

