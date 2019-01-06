from django.shortcuts import render,get_list_or_404,render_to_response, redirect
from django.http import JsonResponse
#from django.urls import reverse
from .models import User,Demand,Developer
#from django.template import RequestContext
from django import forms
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers,viewsets
from rest_framework.renderers import JSONRenderer
from django.core import serializers
import json
from .serializers import DemandAllSerializer,TesterListSerializer,DeveloperListSerializer
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

# @csrf_exempt
# def getDemandAll(request):
#     if request.method == 'GET':
#     # demand1 = Demand1(name='123')
#     # demand1 = Demand.objects.get(id='1')
#         querySet = Demand.objects.all()
#         list = json.loads(serializers.serialize('json', querySet))
#     # serializer = DemandSerializer(demand1)
#     # print(serializer.data)
#     # json = serializer.data
#     # print(json)
#     # return JsonResponse({"result": 0, "msg": "执行成功"})
#         return JsonResponse({"result": 200, "msg": "执行成功", "data":list})

# # class DemandSerializer(serializers.Serializer):
# #     demand_name = serializers.CharField(max_length=200)
# #     demand_status =  serializers.CharField(max_length=200)
# #     print("===============================")
# #     print(demand_name)

# @csrf_exempt
# def getDemandAll(request):
#     if request.method == 'GET':
#         querySet = Demand.objects.all()
#         list = json.loads(serializers.serialize('json', querySet))
#         return JsonResponse({"result": 200, "msg": "执行成功", "data":list})
@csrf_exempt
def getDemandAll(request):
    if request.method == 'GET':
        demands = Demand.objects.all()
        serializer = DemandAllSerializer(demands, many=True)
        return JsonResponse({"result": 200, "msg": "执行成功", "data":serializer.data})

#获取测试人员列表
@csrf_exempt
def getTesterList(request):
    if request.method == 'GET':
        tester = Developer.objects.filter(role='tester')
        serializer = TesterListSerializer(tester,many=True)
        return JsonResponse({"result": 200, "msg": "执行成功", "data":serializer.data})

#获取开发人员列表
@csrf_exempt
def getDeveloperList(request):
    if request.method == 'GET':
        developer = Developer.objects.filter(role='web')
        serializer = DeveloperListSerializer(developer,many=True)
        return JsonResponse({"result": 200, "msg": "执行成功", "data":serializer.data})

def  getReportAll(request):
    querySet = Report.objects.all()
    pass