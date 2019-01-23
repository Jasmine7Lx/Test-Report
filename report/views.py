from django.shortcuts import render,get_list_or_404,render_to_response, redirect
from django.http import JsonResponse
#from django.urls import reverse
from django.db import models
from .models import User,Demand,Developer,Compat,Report
#from django.template import RequestContext
from django import forms
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers,viewsets
from rest_framework.renderers import JSONRenderer
from django.core import serializers
import json
from .serializers import DemandAllSerializer,UserListSerializer,CompatListSerializer
from django.db.models import Q
from django.http import HttpResponse
#from django.urls import reverse
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

 #       else:
 #           from django.forms.utils import ErrorDict
 #       return render(request, 'login/login.html',{'obj1':objPost})

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
        serializer = UserListSerializer(tester,many=True)
        return JsonResponse({"result": 200, "msg": "执行成功", "data":serializer.data})

#获取开发人员列表
@csrf_exempt
def getDeveloperList(request):
    if request.method == 'GET':
        developer = Developer.objects.raw('select * from report_developer where role in ("web","app","background")')
        serializer = UserListSerializer(developer,many=True)
        return JsonResponse({"result": 200, "msg": "执行成功", "data":serializer.data})

#获取产品人员列表
@csrf_exempt
def getProductList(request):
    if request.method == 'GET':
        product = Developer.objects.filter(role='product')
        serializer = UserListSerializer(product,many=True)
        return JsonResponse({"result": 200, "msg": "执行成功", "data":serializer.data})

#获取电脑列表
def getComputerList(request):
    if request.method == 'GET':
        computer = Compat.objects.filter(compat_type='computer')
        serializer = CompatListSerializer(computer,many=True)
        return JsonResponse({"result":200, "msg":"执行成功", "data":serializer.data})

#获取浏览器列表
def getBrowserList(request):
    if request.method == 'GET':
        browser = Compat.objects.filter(compat_type='browser')
        serializer = CompatListSerializer(browser,many=True)
        return JsonResponse({"result":200, "msg":"执行成功", "data":serializer.data})

#获取手机列表
def getPhoneList(request):
    if request.method == 'GET':
        phone = Compat.objects.filter(compat_type='phone')
        serializer = CompatListSerializer(phone,many=True)
        return JsonResponse({"result":200, "msg":"执行成功", "data":serializer.data})

#报告
@csrf_exempt
def Report(request):
    if request.method == 'POST':
        received_json_data = json.loads(request.body)
        report_type = received_json_data.get("report_type")
        result = received_json_data.get("result")
        env = received_json_data.get("environment")
        time = received_json_data.get("time")
        start_time = time[0]
        end_time = time[1]
        demand_id = received_json_data.get("demand_id")
        report_dic = {"report_type":report_type, "result":result,'env':env,'start_time':start_time,'end_time':end_time,'demand_id':demand_id}
        print(report_dic)
        print('开始操作数据库')
        Report.objects.create(**report_dic)
        print('操作数据库完成')
        return JsonResponse({"result": 200, "msg": "执行成功"})