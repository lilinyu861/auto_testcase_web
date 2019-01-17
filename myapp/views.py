# Create your views here.
from myapp.models import *
from myapp.forms import *
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.contrib import messages
from myapp.interfacetest.interface_test import Test


# create views
# 主页
def index(request):
    username = request.COOKIES.get('cookie_username', '')
    return render_to_response('index.html', {'user_name': username})


# 注册
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
                return messages.error(request, '两次密码输入不一致')

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
                return render_to_response("register.html", {'user_form': user_form}, RequestContext(request))
        else:
            return render_to_response('register.html', {'user_form': user_form}, RequestContext(request))

    else:
        user_form = Users()
    return render_to_response('register.html', {'user_form': user_form, 'Method': method}, RequestContext(request))


# 登录
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
                return render_to_response('index.html', {'login_form': login_form}, RequestContext(request))
            # 登录密码不一致则报错
            else:
                return HttpResponse('密码错误')
    else:
        login_form = loginform()
    return render_to_response('login.html', {'login_form': login_form}, RequestContext(request))


# 工具
def tools(request):
    return render(request, 'tools.html')


# 工具/接口测试工具
def interfacetest(request):
    if request.method == 'POST':
        interface_form = interfaceform(request.POST)
        if interface_form.is_valid():
            request_method = interface_form.cleaned_data['request_method']
            interface_url = interface_form.cleaned_data['interface_url']
            header_name = interface_form.cleaned_data['header_name']
            header_value = interface_form.cleaned_data['header_value']
            para_name = interface_form.cleaned_data['para_name']
            para_value = interface_form.cleaned_data['para_value']
            if request_method == 'post':
                  resp = Test.test_interface_post(request_method, interface_url, header_name, header_value,
                                                 para_name, para_value)
            # if request_method == 'get':
            #     msg = Test.test_interface_get(request_method, interface_url, header_name, header_value, para_name, para_value)
            # if request_method == 'patch':
            #     msg = Test.test_interface_patch(request_method, interface_url, header_name, header_value, para_name, para_value)
            # if request_method == 'put':
            #     msg = Test.test_interface_put(request_method, interface_url, header_name, header_value, para_name, para_value)
            # if request_method == 'delete':
            #     msg = Test.test_interface_delete(request_method, interface_url, header_name, header_value, para_name, para_value)
            return render_to_response('InterfaceTest.html', {'response': resp}, RequestContext(request))
    else:
        interface_form = interfaceform()
        return render_to_response('InterfaceTest.html', {'interface_form': interface_form}, RequestContext(request))


def framework(request):
    return render(request, 'framework.html')


def blog(request):
    return render(request, 'blog.html')


def user(request):
    return render(request, 'user.html')


def actc(request):
    return render(request, 'ACTC.html')


def create_testcase(request):
    if request.method == 'POST':
        pass