# Create your views here.
from myapp.models import *
from myapp.forms import Users, loginform
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django import forms
from django.contrib import messages


# create views
def index(request):
    username = request.COOKIES.get('cookie_username', '')
    return render_to_response('index.html', {'user_name': username})


def register(request):
    method = request.method
    if method == 'POST':
        # 如果是post提交的动作，就将post中的数据赋值给user_form，供该函数使用
        user_form = Users(request.POST)
        if user_form.is_valid():
            # 获取表单数据
            username = user_form.cleaned_data['user_name']
            useremail = user_form.cleaned_data['user_email']
            userpassword = user_form.cleaned_data['user_password']
            userpassword1 = user_form.cleaned_data['user_password1']
            if userpassword != userpassword1:
                return messages.error(request, '两次密码输入不匹配')
            # 注册合法性判断
            registerJudge = User.objects.filter(user_email=useremail)
            if not registerJudge:
                # 添加到数据库
                registerAdd = User.objects.create(user_name=username,
                                                  user_email=useremail,
                                                  user_password=userpassword)
                return render_to_response('register.html', {'registerAdd': registerAdd,
                                                            'user_name': username,
                                                            'user_email': useremail})
            else:
                return render("register.html", {'msg': '注册失败，邮箱已注册!'}, RequestContext(request))

    else:
        user_form = Users()
    return render_to_response('register.html', {'user_form': user_form, 'Method': method}, RequestContext(request))


def login(request):
    if request.method == 'POST':
        login_form = loginform(request.POST)
        if login_form.is_valid():
            useremail = login_form.cleaned_data['user_email']
            userpassword = login_form.cleaned_data['user_password']
            # 对比输入的用户名和密码是否和数据库中一致
            passwordJudge = User.objects.filter(user_email__exact=useremail,
                                                user_password__exact=userpassword)
            if passwordJudge:
                response = HttpResponseRedirect('/index/')
                response.set_cookie('cookie_useremail', useremail, 3600)
                return response
            else:
                return HttpResponse('密码错误')
    else:
        login_form = loginform()
    return render_to_response('login.html', {'login_form': login_form}, RequestContext(request))


def create_testcase(request):
    if request.method == 'POST':
        pass


def base(request):
    return render(request, 'base.html')

