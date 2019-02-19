from django.shortcuts import render,get_list_or_404,render_to_response, redirect
from django.http import JsonResponse
import datetime
from django.db import models
from .models import User,Demand,Developer,Compat,Report,Remain,Config,Build,Bug,Compat
from django import forms
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers,viewsets
from rest_framework.renderers import JSONRenderer
from django.core import serializers
import json
from .serializers import DemandAllSerializer,DeveloperListSerializer,CompatListSerializer,ReportListSerializer,BugListSerializer
from django.http import HttpResponse
from django.template import RequestContext
from django import forms

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

@csrf_exempt
def getDemandAll(request):
    if request.method == 'GET':
        demands = Demand.objects.all()
        serializer = DemandAllSerializer(demands, many=True)
        return JsonResponse({"result": 200, "msg": "执行成功", "data":serializer.data})

#报告编辑页，选择需求后获取对应产研测人员列表
@csrf_exempt
def getDeveloperAll(request):
    if request.method == 'GET':
        demand_id = request.GET.get("id")
        developers = Demand.objects.get(id=demand_id).developer.values('id','name','role')
        developer = json.dumps(list(developers))
        return JsonResponse({"result": 200, "msg": "执行成功", "data":developer})

#获取测试人员列表
@csrf_exempt
def getTesterList(request):
    if request.method == 'GET':
        testers = Developer.objects.filter(role='tester')
        serializer = DeveloperListSerializer(testers,many=True)
        return JsonResponse({"result": 200, "msg": "执行成功", "data":serializer.data})

#获取开发人员列表
@csrf_exempt
def getDeveloperList(request):
    if request.method == 'GET':
        developers = Developer.objects.raw('select * from report_developer where role in ("web","app","background")')
        serializer = DeveloperListSerializer(developers,many=True)
        return JsonResponse({"result": 200, "msg": "执行成功", "data":serializer.data})

#获取产品人员列表
@csrf_exempt
def getProductList(request):
    if request.method == 'GET':
        products = Developer.objects.filter(role='product')
        serializer = DeveloperListSerializer(products,many=True)
        return JsonResponse({"result": 200, "msg": "执行成功", "data":serializer.data})

#获取电脑列表
@csrf_exempt
def getComputerList(request):
    if request.method == 'GET':
        computer = Compat.objects.filter(compat_type='computer')
        serializer = CompatListSerializer(computer,many=True)
        return JsonResponse({"result":200, "msg":"执行成功", "data":serializer.data})

#获取浏览器列表
@csrf_exempt
def getBrowserList(request):
    if request.method == 'GET':
        browser = Compat.objects.filter(compat_type='browser')
        serializer = CompatListSerializer(browser,many=True)
        return JsonResponse({"result":200, "msg":"执行成功", "data":serializer.data})

#获取手机列表
@csrf_exempt
def getPhoneList(request):
    if request.method == 'GET':
        phone = Compat.objects.filter(compat_type='phone')
        serializer = CompatListSerializer(phone,many=True)
        return JsonResponse({"result":200, "msg":"执行成功", "data":serializer.data})

#报告
@csrf_exempt
def PcReport(request):
    if request.method == 'POST':
        #获取前端传过来的表单数据
        received_post_data = json.loads(request.body)
        #获取report表需要的表单数据
        result = received_post_data.get("result")
        env = received_post_data.get("environment")
        time = received_post_data.get("time")
        start_time = time[0]
        end_time = time[1]
        demand_id = received_post_data.get("demand")
        developer_id = 1
        #数据存report表
        report_dic = {"report_type":"pc", "result":result,"env":env,"start_time":start_time,"end_time":end_time,"demand_id":demand_id, "developer_id":developer_id}
        report = Report.objects.create(**report_dic)
        #report = Report.objects.get(id='3')
        report_id = report.id
        # #获取遗留问题数据
        remains = received_post_data.get("remains")
        #遍历remains并存库
        if(remains != None):
            for remain in remains:
                if(remain['remain'] != ''):
                    remain = Remain.objects.create(content=remain['remain'], report_id=report_id)

        # #获取配置并存库
        configs = received_post_data.get("configs")
        if(configs != None):
            for config in configs:
                if(config['config'] != ''):
                    config = Config.objects.create(content=config['config'], report_id=report_id)

        # #获取测试版本/链接信息并存库
        builds = received_post_data.get("builds")
        if(builds != None):
            for build in builds:
                if(build['build'] != ''):
                    build = Build.objects.create(site=build['build'], report_id=report_id)
        
        # #获取前端bug并存库
        frontbugs = received_post_data.get("frontbugs")
        if(frontbugs != None):
            for frontbug in frontbugs:
                if(frontbug['frontbug'] != ''):
                    bug = Bug.objects.create(content=frontbug['frontbug'], status=frontbug['status'], demand_id=demand_id, bug_type="frontbug")
        # #获取后端bug并存库
        backbugs = received_post_data.get("backbugs")
        if(backbugs != None):
            for backbug in backbugs:
                if(backbug['backbug'] != ''):
                    bug = Bug.objects.create(content=backbug['backbug'], status=backbug['status'], demand_id=demand_id, bug_type="backbug")
        
        #获取移动端bug并存库
        appbugs = received_post_data.get("appbugs")
        if(appbugs != None):
            for appbug in appbugs:
                if(appbug['appbug'] != ''):
                    bug = Bug.objects.create(content=appbug['appbug'], status=backbug['status'], demand_id=demand_id, bug_type="appbug")
        
        #获取兼容性并存库
        computers = received_post_data.get("computer")
        browsers = received_post_data.get("browser")
        phones = received_post_data.get("phone")
        if(computers != None):
            if(computers != []):
                for x in computers:
                    compat_computer = Compat.objects.get(id=x)
                    compat_computer.report.add(report_id)
        if(browsers != None):
            if(browsers != []):
                for x in browsers:
                    compat_browser = Compat.objects.get(id=x)
                    compat_browser.report.add(report_id)
        if(phones != None):
            if(phones != []):
                for x in phones:
                    compat_phone = Compat.objects.get(id=x)
                    compat_phone.report.add(report_id)

        finish_time = report.create_time
        demand_finish_time = Demand.objects.filter(id=demand_id).update(finish_time=finish_time)
        return JsonResponse({"result": 200, "msg": "执行成功"})

    if request.method == 'GET':
        #获取对应的report_id
        report_id = request.GET.get("id")
        #取出report表的数据并序列化
        reports = Report.objects.select_related().filter(id=report_id)
        report = ReportListSerializer(reports, many=True)
        #取出remain表的数据并序列化
        remains = Report.objects.filter(id=report_id).values('remain__content')
        remain = json.dumps(list(remains))
        #取出config表的数据并序列化
        configs = Report.objects.filter(id=report_id).values('config__content')
        config = json.dumps(list(configs))
        #取出build表的数据并序列化
        builds = Report.objects.filter(id=report_id).values('build__site')
        build = json.dumps(list(builds))
        #获取demand_id，从而获取bug表数据并序列化
        demand_id = Report.objects.get(id=report_id).demand_id
        bugs = Demand.objects.filter(id=demand_id).values('bug__bug_type','bug__content','bug__status')
        bug = json.dumps(list(bugs))
        #获取compat_report表数据并序列化
        compats = Report.objects.get(id=report_id).compat.values('compat_type','system')
        compat = json.dumps(list(compats))
        # for compat in compats:
        #         print(compat.system)
        
        return JsonResponse({"result": 200, "msg": "执行成功", "report":report.data[0], "remain":remain, "bug":bug, "config":config, "build":build, "compat":compat})

#获取报告列表
@csrf_exempt
def getReportList(request):
    if request.method == 'GET':
        reports = Report.objects.select_related().all()
        reportlist = ReportListSerializer(reports, many=True)
        return JsonResponse({"result":200, "msg":"执行成功", "reportlist":reportlist.data})

#增加需求
@csrf_exempt
def getDemandList(request):
    if request.method == 'POST':
        #获取前端传过来的表单数据
        received_post_data = json.loads(request.body)
        #获取demand表需要的表单数据
        name = received_post_data.get("name")
        status = received_post_data.get("status")
        testers = received_post_data.get("tester")
        developers = received_post_data.get("developer")
        product = received_post_data.get("product")
        time = datetime.datetime.now()
        if(status == "no_summit"):
            demand_dict = {"name":name, "status":status}
            demand = Demand.objects.create(**demand_dict)
        elif(status == "summit"):
            demand_dict = {"name":name, "status":status, "summit_test_time":time}
            demand = Demand.objects.create(**demand_dict)
        elif(status == "completed"):
            demand_dict = {"name":name, "status":status, "finish_time":time}
            demand = Demand.objects.create(**demand_dict)
        if(testers != None):
            if(testers != []):
                for x in testers:
                    developer_tester = Developer.objects.get(id=x)
                    developer_tester.demand.add(demand.id)
        if(developers != None):
            if(developers != []):
                for x in developers:
                    developer_developer = Developer.objects.get(id=x)
                    developer_developer.demand.add(demand.id)
        if(product != None):
            if(product != ''):
                developer_product = Developer.objects.get(id=product)
                developer_product.demand.add(demand.id)
        return JsonResponse({"result":200, "msg":"执行成功"})

    if request.method == 'GET':
        demand_id = request.GET.get("id")
        # demand_id = 3
        demands = Demand.objects.filter(id=demand_id).all()
        serializer = DemandAllSerializer(demands, many=True)
        testers = Demand.objects.get(id=demand_id).developer.filter(role='tester').values('name')
        tester = json.dumps(list(testers))
        developers = Demand.objects.get(id=demand_id).developer.raw('select * from report_developer where role in ("web","app","background")')
        # developer = json.dumps(list(developers))
        developer = json.loads(serializers.serialize('json',developers))
        products = Demand.objects.get(id=demand_id).developer.filter(role='product').values('name')
        product = json.dumps(list(products))
        return JsonResponse({"result": 200, "msg": "执行成功", "data":serializer.data, "tester":tester, "developer":developer, "product":product})

    # if request.method == 'GET':
    #     demands = Demand.objects.all()
    #     serializer = DemandAllSerializer(demands, many=True)
    #     for x in demands:
    #         testers = Demand.objects.get(id=x.id).developer.filter(role='tester').values('name')
    #         tester = json.dumps(list(testers))
    #         developers = Demand.objects.get(id=x.id).developer.raw('select * from report_developer where role in ("web","app","background")')
    #         # developer = json.dumps(list(developers))
    #         developer = json.loads(serializers.serialize('json',developers))
    #         products = Demand.objects.get(id=x.id).developer.filter(role='product').values('name')
    #         product = json.dumps(list(products))
    #     return JsonResponse({"result": 200, "msg": "执行成功", "data":serializer.data, "tester":tester, "developer":developer, "product":product})


#bug列表
@csrf_exempt
def getBugList(request):
    if request.method == 'GET':
        bugs = Bug.objects.all()
        serializer = BugListSerializer(bugs, many=True)
        return JsonResponse({"result": 200, "msg": "执行成功", "data":serializer.data})