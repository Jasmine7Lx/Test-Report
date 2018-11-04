from django.shortcuts import render,get_list_or_404,render_to_response, redirect
from django.http import HttpResponse
#from django.urls import reverse
from .models import User
from django.template import RequestContext
from django import forms
# Create your views here.

#表单
class LoginForm(forms.Form):
    username = forms.CharField(required=True, label="username", error_messages={'required':'用户名不能为空'})
    password = forms.CharField(required=True, label="password", widget=forms.PasswordInput(), min_length=6, max_length=10, error_messages={'required':'密码不能为空'})
    
#登录验证
def login(request):
    if request.POST:
        objPost = LoginForm(request.POST)
        if objPost.is_valid():
            #获取表单用户名密码
            username = objPost.cleaned_data['username']
            password = objPost.cleaned_data['password']
            #表单数据与数据库进行比较
            user = User.objects.filter(username__exact = username, password__exact = password)
            if user:
                #成功，跳转index页面
                response = redirect('report:index')
                #将username写入cookie，失效时间为3600
                response.set_cookie('username', username, 3600)
                return response
            else:
                #比较失败，仍在login页面
                from django.forms.utils import ErrorDict
                return render(request, 'login/login.html',{'obj1':objPost})
        else:
            from django.forms.utils import ErrorDict
            return render(request, 'login/login.html',{'obj1':objPost})
    else:
        objGet = LoginForm()
        return render(request, 'login/login.html', {'obj1':objGet })

def index(request):
    return render(request, 'report/index.html')
    
    
def w_report(request):
    pass

def bug_list(request):
    pass

def logout(request):
    pass
